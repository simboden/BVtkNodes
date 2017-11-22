from .core import *    

class VTKSphereSource(Node, VTKTreeNode):

    bl_idname = 'VTKSphereSourceType'
    bl_label  = 'vtkSphereSource'

    m_ThetaResolution = bpy.props.IntProperty        ( name = 'Theta Res.', default=10, min=1, max=500 )
    m_PhiResolution   = bpy.props.IntProperty        ( name = 'Phi   Res.', default=10, min=1, max=500 )
    m_Center          = bpy.props.FloatVectorProperty( name = 'Center',     default=(0.0, 0.0, 0.0), size=3 )
    m_Radius          = bpy.props.FloatProperty      ( name = 'Radius.',    default=1, min=0.001, max=500 )

    def properties( self ):
        return ['m_ThetaResolution','m_PhiResolution','m_Center','m_Radius']    

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )
    
CLASSES.append( VTKSphereSource )        
TYPENAMES.append( 'VTKSphereSourceType' )
