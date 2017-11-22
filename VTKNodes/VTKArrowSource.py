from .core import *    

class VTKArrowSource(Node, VTKTreeNode):

    bl_idname = 'VTKArrowSourceType'
    bl_label  = 'vtkArrowSource'

    m_TipResolution   = bpy.props.IntProperty     ( name = 'Tip Res.',     default=20,  min=1,     max=500 )
    m_TipRadius       = bpy.props.FloatProperty   ( name = 'Tip Radius',   default=0.2, min=0.001, max=500 )
    m_TipLength       = bpy.props.FloatProperty   ( name = 'Tip Lenght',   default=0.6, min=0.001, max=500 )
    m_ShaftResolution = bpy.props.IntProperty     ( name = 'Shaft Res.',   default=20,  min=1,     max=500 )
    m_ShaftRadius     = bpy.props.FloatProperty   ( name = 'Shaft Radius', default=0.1, min=0.001, max=500 )

    def properties( self ):
        return ['m_TipResolution','m_TipRadius','m_TipLength','m_ShaftResolution','m_ShaftRadius']    

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )
    
CLASSES.append( VTKArrowSource )        
TYPENAMES.append( 'VTKArrowSourceType' )

