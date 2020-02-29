from .core import l # Import logging
from .core import *

# -----------------------------------------------------------------------------
# Custom filter
# -----------------------------------------------------------------------------


class BVTK_Node_CustomFilter(Node, BVTK_Node):
    '''VTK Custom Filter, defined in Blender text data block. Supports one
    or multiple inputs. Custom function must return a variable which
    is set as input of the node following custom filter.
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
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, 'text')
        op = row.operator('node.bvtk_new_text', icon='ZOOM_IN', text='')
        op.name = 'customfilter.py'
        op.body = self.__doc__.replace("    ","")
        if len(self.functions()):
            layout.prop(self, 'func')
        else:
            layout.label(text='No functions found in specified text')

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        '''Execute user defined function. If something goes wrong,
        print the error and return the input object.
        '''
        input_objects = [x[1] for x in self.get_input_nodes('input')]
        if len(input_objects) == 1:
            input_objects = input_objects[0]
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            try:
                exec(t, globals(), locals())
            except Exception as e:
                l.error('error while parsing user defined text: ' + \
                      str(e).replace('<string>', self.text))
                return self.get_input_node('input')[1]
            if self.func not in locals():
                l.error('function not found')
            else:
                try:
                    user_output = eval(self.func+'(input_objects)')
                    return user_output
                except Exception as e:
                    l.error('error while executing user defined function:' + str(e))
        return self.get_input_node('input')[1]

    def setup(self):
        self.inputs['input'].link_limit = 300

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

    def blocks(self, context):
        '''Returns a list for a dynamic enum. Once verified that
        the input vtk object is decomposable in blocks, the list
        will contain an element for every block, with the following
        information:
        - Block index
        - Block data type (ex. structured grid)
        - Block custom name (if it's defined, in most cases it's not)
        '''
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            return []
        elif not vtkobj:
            return []
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return []
            if not hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                return []
            items = []
            meta_flag = True if hasattr(vtkobj, "GetMetaData") else False
            for i in range(vtkobj.GetNumberOfBlocks()):
                block = vtkobj.GetBlock(i)
                meta_data = vtkobj.GetMetaData(i) if meta_flag else None
                if meta_data:
                    custom_name = meta_data.Get(vtk.vtkCompositeDataSet.NAME())
                    if not custom_name:
                        custom_name = ""
                else:
                    custom_name = ""
                name = "[" + str(i) + "]: " + custom_name + " (" + \
                       (block.__class__.__name__ if block else "Empty Block") + ")"
                items.append((str(i), name, ""))
            return items

    block: bpy.props.EnumProperty(items=blocks, name="Output Block")

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label(text='Connect a node')
        elif not vtkobj:
            layout.label(text='Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return
            class_name = vtkobj.__class__.__name__
            layout.label(text="Input: "+class_name)
            if not hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                layout.label(text="Error: Input Object has no")
                layout.label(text="          MultiBlock Data")
                return
            layout.prop(self, "block")

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        '''The function checks if the specified block can be retrieved from
        the input vtk object, in case it's possible the said block is returned.
        '''
        in_node, vtkobj = self.get_input_node('input')
        if in_node:
            if vtkobj:
                vtkobj = resolve_algorithm_output(vtkobj)
                if vtkobj:
                    # TODO: remove "not" in front of hasattr(vtkobj, "GetBlock")?
                    if hasattr(vtkobj, "GetNumberOfBlocks") or not hasattr(vtkobj, "GetBlock"):
                        if self.block:
                            return vtkobj.GetBlock(int(self.block))
        return None


def update_timestep_in_filename(filename, time_step):
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
        replacement = defstr % time_step
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

    def check_range(self, context):
        in_node, out_port = self.get_input_node('input')
        if in_node:
            if out_port:
                if out_port.IsA('vtkAlgorithmOutput'):
                    prod = out_port.GetProducer()
                    executive = prod.GetExecutive()
                    out_info = prod.GetOutputInformation(out_port.GetIndex())
                    if hasattr(executive, "TIME_STEPS"):
                        time_steps = out_info.Get(executive.TIME_STEPS())

                        # If reader is aware of time, update time step
                        if time_steps:
                            size = len(time_steps)
                            #if self.time_step < -size:
                            #    self.time_step = -size
                            #elif self.time_step >= size:
                            #    self.time_step = size-1
                            # Make data loop outside normal time range.
                            # Value test is needed to avoid infinite property
                            # update loop calling check_range().
                            time_val = self.time_step % size
                            if self.time_step != time_val:
                                self.time_step = time_val

                        # Hack for time unaware readers: If file name of reader
                        # node contains number string at end, update it
                        else:
                            filename = in_node.m_FileName
                            newname = update_timestep_in_filename(filename, self.time_step)
                            in_node.m_FileName = newname

    time_step: bpy.props.IntProperty(update=check_range)

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        in_node, out_port = self.get_input_node('input')
        if not in_node:
            layout.label(text='Connect a node')
            return
        if not out_port:
            layout.label(text='Input has not vtkobj (try updating)')
            return
        if not out_port.IsA('vtkAlgorithmOutput'):
            layout.label(text='Input is not a vtkAlgorithm')
            return

        prod = out_port.GetProducer()
        executive = prod.GetExecutive()
        out_info = prod.GetOutputInformation(out_port.GetIndex())
        if hasattr(executive, "TIME_STEPS"):
            time_steps = out_info.Get(executive.TIME_STEPS())
            if time_steps:
                row = layout.row()
                row.prop(self, 'time_step', text="Time Step")
                row = layout.row()
                size = len(time_steps)
                row.label(text="Max Steps: "+str(size-1))
                if -size <= self.time_step < size:
                    layout.label(text="Time Value: "+str(time_steps[self.time_step]))
                else:
                    layout.label(text='Index error', icon='ERROR')
            else:
                layout.label(text='No time data on input')
        else:
            layout.label(text='Input contains no time steps')
        return

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        '''Check if the input is valid and if the time step can be set.
        If tests pass the time step is updated and the input object is returned,
        otherwise None is returned.
        '''
        in_node, out_port = self.get_input_node('input')
        if not in_node or not out_port:
            return None
        if not out_port.IsA('vtkAlgorithmOutput'):
            return None

        prod = out_port.GetProducer()
        executive = prod.GetExecutive()
        out_info = prod.GetOutputInformation(out_port.GetIndex())
        if hasattr(executive, "TIME_STEPS"):
            time_steps = out_info.Get(executive.TIME_STEPS())
            if time_steps:
                size = len(time_steps)
                if -size <= self.time_step < size:
                    if hasattr(prod, "UpdateTimeStep"):
                        prod.UpdateTimeStep(time_steps[self.time_step])
                    else:
                        l.error(prod.__class__.__name__+" does not have 'UpdateTimeStep' method.")
                        l.error("If you can, please document this case and report it to the developers.")
                else:
                    l.error('Index out of time steps range')
        return resolve_algorithm_output(out_port)


# Add classes and menu items
TYPENAMES = []
add_class(BVTK_Node_CustomFilter)
TYPENAMES.append('BVTK_Node_CustomFilterType')
add_ui_class(BVTK_OT_NewText)
add_class(BVTK_Node_MultiBlockLeaf)
TYPENAMES.append('BVTK_Node_MultiBlockLeafType')
add_class(BVTK_Node_TimeSelector)
TYPENAMES.append('BVTK_Node_TimeSelectorType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Custom", "Custom", items=menu_items))
