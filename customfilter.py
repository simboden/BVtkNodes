from .core import l # Import logging
from .core import *
from .animation_helper import AnimationHelper
from .cache import PersistentStorageUser, persistent_storage
from .__init__ import converters_list
from .tree import node_tree_name
from .update import Update, no_queue_update

# -----------------------------------------------------------------------------
# Custom filter
# -----------------------------------------------------------------------------


class BVTK_Node_CustomFilter(Node, BVTK_Node):
    '''VTK Custom Filter, defined in a Blender text data block. Supports one
    input. Custom function must return a VTK output object.
    '''
    bl_idname = 'BVTK_Node_CustomFilterType'
    bl_label = 'Custom Filter'

    def texts(self, context):
        '''Generate list of text objects to choose'''
        t = []
        i = 0
        for text in bpy.data.texts:
            t.append((text.name, text.name, text.name, 'TEXT', i))
            i += 1
        if not t:
            t.append(('No texts found', 'No texts found', 'No texts found', 'TEXT', i))
        return t

    text: bpy.props.EnumProperty(items=texts, name='text')

    def functions(self, context=None):
        '''Generate list of functions to choose'''
        f = []
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            for func in t.split('def ')[1:]:
                if '(' in func:
                    name = func.split('(')[0].replace(' ','')
                    f.append((name, name, name))
        return f

    func: bpy.props.EnumProperty(items=functions, name='function')

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'], ['output'], [], [])

    def draw_buttons_special(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, 'text')
        op = row.operator('node.bvtk_new_text', icon='ZOOM_IN', text='')
        op.name = 'customfilter.py'
        op.body = self.__doc__.replace("    ","")
        if len(self.functions()):
            layout.prop(self, 'func')
        else:
            layout.label(text='No functions found in specified text')

    def apply_properties_special(self):
        return 'up-to-date'

    def get_vtk_output_object_special(self, socketname='output'):
        '''Execute user defined function. If something goes wrong,
        print the error and return the input object.
        '''
        input_node, vtk_output_obj, vtk_connection = self.get_input_node_and_output_vtk_objects()
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            try:
                exec(t, globals(), locals())
            except Exception as e:
                l.error('error while parsing user defined text: ' + \
                      str(e).replace('<string>', self.text))
                return vtk_output_obj
            if self.func not in locals():
                l.error('function not found')
            else:
                try:
                    user_output = eval(self.func+'(vtk_output_obj)')
                    return user_output
                except Exception as e:
                    l.error('error while executing user defined function:' + str(e))
        return vtk_output_obj

    # Currently core does not support multiple inputs
    #def init_special(self):
    #    self.inputs['input'].link_limit = 300

    def export_properties(self):
        '''Export node properties'''
        dict = {}
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            dict['text_as_string'] = t
            dict['text_name'] = self.text
        return dict

    def import_properties(self, dict):
        '''Import node properties'''
        bpy.ops.node.bvtk_new_text(body=dict['text_as_string'], name=dict['text_name'])

    def init_vtk(self):
        self.set_vtk_status('out-of-date')
        return None

class BVTK_OT_NewText(bpy.types.Operator):
    '''New text operator'''
    bl_idname = 'node.bvtk_new_text'
    bl_label = 'Create a new text'

    name: bpy.props.StringProperty(default='New text')
    body: bpy.props.StringProperty()

    def execute(self, context):
        text = bpy.data.texts.new(self.name)
        text.from_string(self.body)
        flag = True
        areas = context.screen.areas
        for area in areas:
            if area.type == 'TEXT_EDITOR':
                for space in area.spaces:
                    if space.type == 'TEXT_EDITOR':
                        if flag:
                            space.text = text
                            space.top = 0
                            flag = False
        if flag:
            self.report({'INFO'}, "See '" + text.name + "' in the text editor")
        return {'FINISHED'}


# ----------------------------------------------------------------
# MultiBlockLeaf
# ----------------------------------------------------------------

class BVTK_Node_MultiBlockLeaf(Node, BVTK_Node):
    '''This node breaks down vtkMultiBlock data and outputs one
    user selected block.
    '''
    bl_idname = 'BVTK_Node_MultiBlockLeafType'
    bl_label = 'Multi Block Leaf'
    bl_description = 'Node to extract one block from vtkMultiBlockDataSet'

    block: bpy.props.StringProperty(default="", name="Block Name", update=BVTK_Node.outdate_vtk_status)

    def block_enum_generator(self, context=None):
        '''Returns an enum list of block names'''

        items = [('None', 'Empty (clear value)', 'Empty (clear value)', ENUM_ICON, 0)]

        input_node, vtk_output_obj, vtk_connection = self.get_input_node_and_output_vtk_objects()
        if not hasattr(vtk_output_obj, "GetNumberOfBlocks") or \
           not hasattr(vtk_output_obj, "GetBlock"):
            return items

        for i in range(vtk_output_obj.GetNumberOfBlocks()):
            block = vtk_output_obj.GetBlock(i)
            if hasattr(vtk_output_obj, "GetMetaData"):
                meta_data = vtk_output_obj.GetMetaData(i)
                name = meta_data.Get(vtk.vtkCompositeDataSet.NAME())
            else:
                name = str(i)
            items.append((name, name, name, ENUM_ICON, i+1))
        return items

    def block_set_value(self, context=None):
        '''Set value of StringProprety using value from EnumProperty'''
        if self.block_enum == 'None':
            self.block = ""
        else:
            self.block = str(self.block_enum)

    block_enum: bpy.props.EnumProperty(items=block_enum_generator, update=block_set_value, name="Choices")

    def validate_and_update_values(self):
        '''Check that value in block property exists.
        '''
        if len(self.block) < 1:
            return "Error: Need a Block Name"
        block_enum_list = first_elements(self.block_enum_generator())
        if not self.block in block_enum_list:
            return "Block named %r was not found in input" % self.block

    def m_properties(self):
        return ['block']

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def draw_buttons_special(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, 'block')
        row.prop(self, 'block_enum', icon_only=True)

    def apply_properties_special(self):
        val = self.validate_and_update_values()
        if val:
            self.ui_message = val
            return 'error'
        return 'up-to-date'

    def get_vtk_output_object_special(self, socketname='output'):
        '''The function checks if the specified block can be retrieved from
        the input vtk object, in case it's possible the said block is returned.
        '''
        input_node, vtk_output_obj, vtk_connection = self.get_input_node_and_output_vtk_objects()
        if not vtk_output_obj:
            return None

        # Find index number from element list
        block_enum_list = first_elements(self.block_enum_generator())
        if not self.block in block_enum_list:
            return None
        i = block_enum_list.index(self.block) - 1
        if hasattr(vtk_output_obj, "GetBlock"):
            return vtk_output_obj.GetBlock(i)

    def init_vtk(self):
        self.set_vtk_status('out-of-date')
        return None

# ----------------------------------------------------------------
# Time Selector
# ----------------------------------------------------------------

def update_timestep_in_filename(filename, time_index):
    '''Return file name, where time definition integer string (assumed to
    be located just before dot at end of file name) has been replaced
    to argument time step number
    '''
    import re
    rec1 = re.compile(r'(\d+)\.\w+$', re.M)
    regex1 = rec1.search(filename)
    if regex1:
        numbers = regex1.group(1)
        n = len(numbers)
        defstr = "%0" + str(n) + "d"
        replacement = defstr % time_index
        # Replace with dot at end to increase odds for correct substitution
        newname = filename.replace(numbers + ".", replacement + ".")
        return newname
    return filename


class BVTK_Node_TimeSelector(Node, BVTK_Node):
    '''VTK time management node for time variant data. Display time sets,
    time values and set time.
    '''
    bl_idname = 'BVTK_Node_TimeSelectorType'
    bl_label = 'Time Selector'

    def get_time_values(self, context=None):
        '''Return list of time step values from VTK Executive or None if no
        time values are found.
        '''
        input_node, vtk_output_obj, vtk_connection = self.get_input_node_and_output_vtk_objects('input')
        if not vtk_connection or not vtk_connection.IsA('vtkAlgorithmOutput'):
            return None
        prod = vtk_connection.GetProducer()
        executive = prod.GetExecutive()
        out_info = prod.GetOutputInformation(vtk_connection.GetIndex())
        if not hasattr(executive, "TIME_STEPS"):
            return None
        time_values = out_info.Get(executive.TIME_STEPS())

        # If reader is aware of time, it provides list of time step values.
        # Added requirement len(time_values) > 1 because VTK 9.0.1
        # vtkPolyDataReader started to return TIME_STEPS=0.0
        # always (reader is not really time aware?).
        if time_values and len(time_values) > 1:
            return time_values

    def update_time_unaware_reader_node(self):
        '''Hack to update time unaware readers: If file name of input node
        contains number string at end, update it.
        '''
        input_node, _ = self.get_input_node_and_socketname('input')
        if not input_node:
            return None
        try:
            filename = input_node.m_FileName
            newname = update_timestep_in_filename(filename, self.time_index)
            input_node.m_FileName = newname
        except Exception as ex:
            pass

    def get_time_value(self):
        '''Return time value of current time index as a text string'''
        time_values = self.get_time_values()
        if not time_values:
            return 'Unknown'
        size = len(time_values)
        time_index = self.time_index % size
        return str(time_values[time_index])

    def activate_scene_time(self, context):
        if self.use_scene_time:
            self.time_index = context.scene.frame_current
        self.outdate_vtk_status(context)

    def time_index_update(self, context=None):
        '''Custom time_index out-of-date routine'''
        time_values = self.get_time_values()
        l.debug("time_values " + str(time_values))
        if not time_values:
            self.update_time_unaware_reader_node()
        self.outdate_vtk_status(context)

    time_index: bpy.props.IntProperty(name="Time Index", default=1, update=time_index_update)
    use_scene_time: bpy.props.BoolProperty(name="Use Scene Time", default=True, update=activate_scene_time)
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['time_index', 'use_scene_time']

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def apply_properties_special(self):
        '''Set time to VTK Executive'''
        self.ui_message = "Time: " + self.get_time_value()
        time_values = self.get_time_values()
        if time_values:
            input_node, vtk_output_obj, vtk_connection = self.get_input_node_and_output_vtk_objects('input')
            if not vtk_connection or not vtk_connection.IsA('vtkAlgorithmOutput'):
                self.ui_message = "No VTK connection or VTK Algorithm Output"
                return 'error'
            prod = vtk_connection.GetProducer()
            size = len(time_values)
            if -size <= self.time_index < size:
                if hasattr(prod, "UpdateTimeStep"):
                    prod.UpdateTimeStep(time_values[self.time_index])
                else:
                    self.ui_message = "Error: " + prod.__class__.__name__ + " does not have 'UpdateTimeStep' method."
                    return 'error'
            else:
                self.ui_message = "Error: time index " + str(self.time_index) + " is out of index range (%d)" % (size - 1)
                return 'error'
        return 'up-to-date'

    def get_vtk_output_object_special(self, socketname='output'):
        '''Pass on VTK output from input as output'''
        input_node, vtk_output_obj, vtk_connection = self.get_input_node_and_output_vtk_objects()
        return vtk_output_obj

    def init_vtk(self):
        self.set_vtk_status('out-of-date')
        return None

# ----------------------------------------------------------------
# Image Data Object Source
# ----------------------------------------------------------------

class BVTK_Node_ImageDataObjectSource(Node, BVTK_Node):
    '''BVTK node to generate a new vtkImageData object'''
    bl_idname = 'BVTK_Node_ImageDataObjectSourceType'
    bl_label = 'VTKImageData Object Source'

    origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3)
    dimensions: bpy.props.IntVectorProperty(name='Dimensions', default=[10, 10, 10], size=3)
    spacing: bpy.props.FloatVectorProperty(name='Spacing', default=[0.1, 0.1, 0.1], size=3)
    multiplier: bpy.props.FloatProperty(name='Multiplier', default=1.0)

    def m_properties(self):
        return ['origin', 'dimensions', 'spacing', 'multiplier']

    def m_connections(self):
        return ([], [], [], ['output'])

    def draw_buttons(self, context, layout):
        layout.prop(self, 'origin')
        layout.prop(self, 'dimensions')
        layout.prop(self, 'spacing')
        layout.prop(self, 'multiplier')

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        '''Generate a new vtkImageData object'''
        from mathutils import Vector
        img = vtk.vtkImageData()
        img.SetOrigin(self.origin)
        c = self.multiplier
        img.SetDimensions([round(c * dim) for dim in self.dimensions])
        img.SetSpacing(Vector(self.spacing) / c)
        return img

# ----------------------------------------------------------------
# Global Time Keeper
# ----------------------------------------------------------------
class BVTK_Node_GlobalTimeKeeper(PersistentStorageUser, AnimationHelper, Node, BVTK_Node):
    '''Global VTK time management node for time variant data. This is used to change
    the speed of the global VTK simulation, updating all Time selectors across the node
    tree according to the currently displayed global time. The VTK time is currently linearly linked
    to the scene time.
    '''
    bl_idname = 'BVTK_Node_GlobalTimeKeeperType'
    bl_label = 'Global Time Keeper'

    def update_time(self, context):
        self.get_persistent_storage()["updated_nodes"] = self.update_animated_properties(context.scene)
        self.get_persistent_storage()["animated_properties"] = self.animated_properties
        self.get_persistent_storage()["interpolation_modes"] = self.interpolation_modes
        self.get_persistent_storage()["animated_values"] = self.animated_values

    global_time: bpy.props.IntProperty(update=update_time, name="Global Time")
    invalid: bpy.props.BoolProperty(name="Is Node Valid")

    def m_connections(self):
        return ([], [], [], [])

    def draw_buttons(self, context, layout):
        if self.invalid:
            row = layout.row()
            row.label(text="You already have a global time keeper")
            return

        row = layout.row()
        row.label(text="Global Time: {}".format(self.global_time))
        storage = self.get_persistent_storage()
        if "animated_properties" in storage:
            animated_properties = storage["animated_properties"]

            if animated_properties is not None and len(animated_properties) > 0:
                row = layout.row()
                row.label(text="Animated properties: ")
                row = layout.row()
                row.label(text="Node")
                row.label(text="Attr.")
                row.label(text="Keyframes")
                row.label(text="Keyframe Vals")
                row.label(text="Current Val")
                row.label(text="Interpol. Mode")
                modes = storage["interpolation_modes"]
                animated_values = storage["animated_values"]

                for elem in animated_properties.values():
                    row = layout.row()
                    [row.label(text=str(val)) for val in elem[:3]]
                    row.label(text="(%s)" % [",".join(("%.2f" % (single_val)) for single_val in val) for val in elem[3]])
                    row.label(text="(%s)" % ",".join(["%.2f" % (val) for val in elem[4]]))
                    row.label(text=elem[-1])

        row = layout.row()
        row.separator()
        row.separator()
        row.separator()
        row.separator()
        row.operator("node.bvtk_node_update", text="update").node_path = node_path(self)
        return

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def update_cb(self):
        self.update_time(bpy.context)

    def set_new_time(self, frame):
        self.global_time = frame
        return self.get_persistent_storage()["updated_nodes"]

    def setup(self):
        if self.name != self.bl_label:
            self.invalid = True
            raise RuntimeError("A Global Time Keeper already exists. There can be only one Global Time Keeper per scene")

        #Cleanup procedure if the old Global Time Keeper tree was not properly deleted
        elif self.name in persistent_storage["nodes"]:
            del persistent_storage["nodes"][self.name]

        AnimationHelper.setup(self)
        assert(self.name == self.bl_label)
        self.bl_label
        persistent_storage["nodes"][self.bl_label] = {} #pass
        self.invalid = False

    def copy(self, node):
        self.setup()

# ----------------------------------------------------------------
# Update All Node
# ----------------------------------------------------------------
class BVTK_Node_UpdateAll(Node, BVTK_Node):
    '''This nodes provides an easy functionality to call all update on all convertes and/or writer nodes
    '''
    bl_idname = 'BVTK_Node_UpdateAllType'
    bl_label = 'Update All'

    update_all_converters: bpy.props.BoolProperty(name="Update All Converters", default=True)
    update_all_writers: bpy.props.BoolProperty(name="Update All Writers", default=True)
    error_count: bpy.props.IntProperty(name="Error Count", default=0)

    def m_connections(self):
        return ([], [], [], [])

    def m_properties(self):
        return ['update_all_converters', 'update_all_writers', 'error_count']

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, 'update_all_converters')
        row = layout.row()
        row.prop(self, 'update_all_writers')
        row = layout.row()
        row.separator()
        row.separator()
        row.separator()
        row.operator("node.bvtk_node_update", text="Update").node_path = node_path(self)
        return

    def update_cb(self):
        self.error_count = 0
        for node_group in bpy.data.node_groups.values():
            if node_group.name == node_tree_name:
                for node in node_group.nodes:

                    try:
                        #Converter nodes
                        if self.update_all_converters and node.bl_idname in converters_list:
                            no_queue_update(node, node.update_cb)

                            object_name = node.m_Name
                            if object_name not in bpy.data.objects:
                                l.error("Node " + node.name + " succeeded, but produced no output object (%s)" % (object_name))
                                self.error_count += 1

                        #Writer nodes
                        elif self.update_all_writers and node.bl_label.endswith("Writer"):
                            no_queue_update(node, lambda x: x, False)
                            node.get_vtkobj().Write()

                            if hasattr(node, "m_FileName"):
                                output_file = node.m_FileName.replace("//", bpy.path.abspath("//"))
                                if not os.path.exists(output_file):
                                    l.error("Node " + node.name + " succeeded, but produced no output file (%s)" % (output_file))
                                    self.error_count += 1
                                    
                    except Exception as ex:
                        l.error("Update of node " + node.name + " failed with " + str(ex))




# Add classes and menu items
TYPENAMES = []
add_class(BVTK_Node_CustomFilter)
TYPENAMES.append('BVTK_Node_CustomFilterType')
add_ui_class(BVTK_OT_NewText)
add_class(BVTK_Node_MultiBlockLeaf)
TYPENAMES.append('BVTK_Node_MultiBlockLeafType')
add_class(BVTK_Node_TimeSelector)
TYPENAMES.append('BVTK_Node_TimeSelectorType')
add_class(BVTK_Node_GlobalTimeKeeper)
TYPENAMES.append('BVTK_Node_GlobalTimeKeeperType')
add_class(BVTK_Node_UpdateAll)
TYPENAMES.append('BVTK_Node_UpdateAllType')
add_class(BVTK_Node_ImageDataObjectSource)
TYPENAMES.append('BVTK_Node_ImageDataObjectSourceType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Custom", "Custom", items=menu_items))
