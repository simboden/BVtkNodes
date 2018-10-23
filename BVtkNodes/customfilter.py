from .core import *
TYPENAMES = []

# ----------------------------------------------------------------
# Custom filter
# ----------------------------------------------------------------


class VTKCustomFilter(Node, VTKNode):
    """# This file is used for vtk custom filter.
    # On update all of this file will be executed.
    # To the chosen function will be passed:
    # - A list of objects, if custom filter node has multiple links in input.
    # - A single object, if custom filter node has a single link in input.
    # Your function must return a variable which can be set as input of the
    # node following custom filter.
    """
    bl_idname = 'VTKCustomFilterType'
    bl_label = 'CustomFilter'

    def texts(self, context):
        t = []
        i = 0
        for text in bpy.data.texts:
            t.append((text.name, text.name, text.name, 'TEXT', i))
            i += 1
        if not t:
            t.append(('No texts found', 'No texts found', 'No texts found', 'TEXT', i))
        return t


    def functions(self, context=None):
        f = []
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            for func in t.split('def ')[1:]:
                if '(' in func:
                    name = func.split('(')[0].replace(' ','')
                    f.append((name, name, name))
        return f

    text = bpy.props.EnumProperty(items=texts, name='text')
    func = bpy.props.EnumProperty(items=functions, name='function')

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'], [], [], ['output'])

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)
        row.prop(self, 'text')
        op = row.operator('vtk.new_text', icon='ZOOMIN', text='')
        op.name = 'customfilter.py'
        op.body = self.__doc__.replace("    ","")
        if len(self.functions()):
            layout.prop(self, 'func')
        else:
            layout.label('No functions found in specified text')

    def apply_properties(self, vtkobj):
        pass

    def apply_inputs(self, vtkobj):
        pass

    def get_output(self, socketname):
        """ execute user defined function.
         If something goes wrong print the error and
        return the input object.
         """
        input_objects = [x[1] for x in self.get_input_nodes('input')]
        if len(input_objects) == 1:
            input_objects = input_objects[0]
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            try:
                exec(t, globals(), locals())
            except Exception as e:
                print('VTKCustomFilter - error while parsing user defined text:',
                      str(e).replace('<string>', self.text))
                return self.get_input_node('input')[1]
            if self.func not in locals():
                print('VTKCustomFilter - function not found')
            else:
                try:
                    user_output = eval(self.func+'(input_objects)')
                    return user_output
                except Exception as e:
                    print('VTKCustomFilter - error while executing user defined function:',str(e))
        return self.get_input_node('input')[1]

    def setup(self):
        self.inputs['input'].link_limit = 300

    def export_properties(self):
        """ called on export """
        dict = {}
        if self.text in bpy.data.texts:
            t = bpy.data.texts[self.text].as_string()
            dict['text_as_string'] = t
            dict['text_name'] = self.text
        return dict

    def import_properties(self, dict):
        """ called on import """
        bpy.ops.vtk.new_text(body=dict['text_as_string'], name=dict['text_name'])

add_class(VTKCustomFilter)
TYPENAMES.append('VTKCustomFilterType')

# ----------------------------------------------------------------
# New text operator
# ----------------------------------------------------------------


class VTKNewText(bpy.types.Operator):
    bl_idname = 'vtk.new_text'
    bl_label = 'Create a new text'

    name = bpy.props.StringProperty(default='New text')
    body = bpy.props.StringProperty()

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
            self.report({'INFO'}, "See '"+text.name+"' in the text editor")
        return {'FINISHED'}

add_ui_class(VTKNewText)
# ----------------------------------------------------------------
menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(VTKNodeCategory("custom", "custom", items=menu_items))
# ----------------------------------------------------------------