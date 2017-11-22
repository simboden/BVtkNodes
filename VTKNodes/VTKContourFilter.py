from .core import *    

class VTKContourFilter(Node, VTKTreeNode):

    bl_idname = 'VTKContourFilterType'
    bl_label  = 'vtkContourFilter'
    m_Value = bpy.props.FloatProperty( name="IsoValue", default=0)

    def properties():
        return ['m_Value']

    def init(self, context):
        self.width = 200
        self.inputs.new ('VTKPolyDataSocketType', "in")
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )

    def apply_properties(self,vtkobj):
        vtkobj.SetValue(0, self.m_Value ) # non standard syntax

CLASSES.append( VTKContourFilter )  
TYPENAMES.append( 'VTKContourFilterType' )     