from .core import *    

class VTKCubeSource(Node, VTKTreeNode):

    bl_idname = 'VTKCubeSourceType'
    bl_label  = 'vtkCubeSource'

    m_XLength    = bpy.props.FloatProperty      ( name = 'x size',    default=1,  min=0.001, max=500 )
    m_YLength    = bpy.props.FloatProperty      ( name = 'y size',    default=1,  min=0.001, max=500 )
    m_ZLength    = bpy.props.FloatProperty      ( name = 'z size',    default=1,  min=0.001, max=500 )
    m_Center     = bpy.props.FloatVectorProperty( name = 'Center',    default=(0.0, 0.0, 0.0), size=3 )

    def properties( self ):
        return ['m_XLength','m_YLength','m_ZLength', 'm_Center']    

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )
    
CLASSES.append( VTKCubeSource )        
TYPENAMES.append( 'VTKCubeSourceType' )
