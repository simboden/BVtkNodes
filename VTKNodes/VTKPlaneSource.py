from .core import *    

class VTKPlaneSource(Node, VTKTreeNode):

    bl_idname = 'VTKPlaneSourceType'
    bl_label  = 'vtkPlaneSource'

    m_XResolution = bpy.props.IntProperty        ( name = 'x resolution', default=1, min=1,     max=500 )
    m_YResolution = bpy.props.IntProperty        ( name = 'y resolution', default=1, min=1,     max=500 )
    m_Center      = bpy.props.FloatVectorProperty( name = 'Center',       default=(0.0, 0.0, 0.0), size=3 )
    m_Normal      = bpy.props.FloatVectorProperty( name = 'Normal',       default=(0.0, 0.0, 1.0), size=3 )

    def properties( self ):
        return ['m_XResolution','m_YResolution','m_Center','m_Normal']    

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )
    
CLASSES.append( VTKPlaneSource )        
TYPENAMES.append( 'VTKPlaneSourceType' )
