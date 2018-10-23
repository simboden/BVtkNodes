from .gen_VTKFilters1 import *
from .gen_VTKFilters2 import *
from .gen_VTKFilters  import *

# ---------------------------------------------------------------------------------
# Contour classes
# ---------------------------------------------------------------------------------


class ValueSettings(bpy.types.PropertyGroup):
    """ Actually a float array of variable size """
    value = bpy.props.FloatProperty(default = 0)


add_ui_class(ValueSettings)


class VTKContourHelper:
    """ Base class for filters similar to vtkCountourFilter  """
    m_ContourValues = bpy.props.CollectionProperty(type=ValueSettings)

    def draw_buttons(self, context, layout):
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                prop = m_properties[i]
                if prop == 'm_ContourValues':
                    prop = getattr(self, prop)
                    prop_path = node_prop_path(self, 'm_ContourValues')
                    row = layout.row()
                    op = row.operator('vtk.update_collection', text='', icon='ZOOMIN')
                    op.prop_path = prop_path
                    op.add = True
                    row.label('Contour values')
                    for i, item in enumerate(self.m_ContourValues):
                        row = layout.row(align=True)
                        op = row.operator('vtk.update_collection', text='', icon='ZOOMOUT')
                        op.prop_path = prop_path
                        op.add = False
                        op.index = i
                        row.prop(item, 'value')
                else:
                    layout.prop(self, prop)

    def apply_properties(self, vtkobj):
        m_properties = self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            if x == 'm_ContourValues':
                vtkobj.SetNumberOfContours(0)
                i = 0
                for item in self.m_ContourValues:
                    vtkobj.SetValue(i, item.value)
                    i += 1
            else:
                cmd = 'vtkobj.Set' + x[2:] + '(self.' + x + ')'
                exec(cmd, globals(), locals())

    def special_properties(self):
        return [x.value for x in self.m_ContourValues]

    def export_properties(self):
        """ called by export operator """
        return {'m_ContourValues':[x.value for x in self.m_ContourValues]}

    def import_properties(self, dict):
        """ called by import operator """
        values = dict['m_ContourValues']
        for i, val in enumerate(values):
            if i < len(self.m_ContourValues):
                self.m_ContourValues[i].value = val
            else:
                item = self.m_ContourValues.add()
                item.value = val

# --------------------------------------------------------------


class VTKContourFilter(VTKContourHelper, Node, VTKNode):
    bl_idname = 'VTKContourFilterType'
    bl_label = 'vtkContourFilter'

    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', default=True)
    m_GenerateTriangles = bpy.props.BoolProperty(name='GenerateTriangles', default=True)
    m_ArrayComponent = bpy.props.IntProperty(name='ArrayComponent', default=0)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', default=1)

    b_properties = bpy.props.BoolVectorProperty(name="", size=7, get=VTKNode.get_b, set=VTKNode.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars', 'm_GenerateTriangles', 'm_ArrayComponent',
                'm_NumberOfContours', 'm_ContourValues']

    def m_connections(self):
        return (['input'], ['output'], [], [])


add_class(VTKContourFilter)
# --------------------------------------------------------------


class VTKMarchingCubes(VTKContourHelper, Node, VTKNode):
    bl_idname = 'VTKMarchingCubesType'
    bl_label = 'vtkMarchingCubes'

    m_ComputeGradients = bpy.props.BoolProperty(name='ComputeGradients', default=True)
    m_ComputeNormals = bpy.props.BoolProperty(name='ComputeNormals', default=True)
    m_ComputeScalars = bpy.props.BoolProperty(name='ComputeScalars', default=True)
    m_NumberOfContours = bpy.props.IntProperty(name='NumberOfContours', default=1)

    b_properties = bpy.props.BoolVectorProperty(name="", size=5, get=VTKNode.get_b, set=VTKNode.set_b)

    def m_properties(self):
        return ['m_ComputeGradients', 'm_ComputeNormals', 'm_ComputeScalars',
                'm_NumberOfContours', 'm_ContourValues']

    def m_connections(self):
        return (['input'], ['output'], [], [])


add_class(VTKMarchingCubes)
# --------------------------------------------------------------


class UpdateCollection(bpy.types.Operator):
    bl_idname = "vtk.update_collection"
    bl_label = "update"
    index = bpy.props.IntProperty(default = 0)
    value = bpy.props.FloatProperty()
    prop_path = bpy.props.StringProperty()
    add = bpy.props.BoolProperty(default=True)

    def execute(self, context):
        prop = eval(self.prop_path)
        if self.add:
            item = prop.add()
            item.value = self.value
        else:
            prop.remove(self.index)
        return {'FINISHED'}

add_ui_class(UpdateCollection)
# --------------------------------------------------------------


class VTKAppendFilter(Node, VTKNode):
    bl_idname = 'VTKAppendFilterType'
    bl_label = 'vtkAppendFilter'

    m_MergePoints = bpy.props.BoolProperty(name='MergePoints', default=True)

    b_properties = bpy.props.BoolVectorProperty(name="", size=1, get=VTKNode.get_b, set=VTKNode.set_b)

    def m_properties(self):
        return ['m_MergePoints', ]

    def m_connections(self):
        return (['input'], ['output'], [], [])

    def setup(self):
        self.inputs['input'].link_limit = 300  # added

    def apply_inputs(self, vtkobj):
        added = [vtkobj.GetInputConnection(0, i) for i in range(vtkobj.GetNumberOfInputConnections(0))]
        toadd = []
        for node, in_obj in self.get_input_nodes('input'):
            toadd.append(in_obj)
            if in_obj not in added:
                vtkobj.AddInputConnection(in_obj)

        for obj in added:
            if obj not in toadd:
                vtkobj.RemoveInputConnection(0, obj)


add_class(VTKAppendFilter)
TYPENAMES.append('VTKAppendFilterType')
# --------------------------------------------------------------


