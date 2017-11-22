from .core import *    

class VTKConeSource(Node, VTKTreeNode):

    bl_idname = 'VTKConeSourceType'
    bl_label  = 'vtkConeSource'

    m_Capping    = bpy.props.BoolProperty       ( name = 'Capping',   default=True )
    m_Resolution = bpy.props.IntProperty        ( name = 'Resolution',default=10, min=1,     max=500 )
    m_Height     = bpy.props.FloatProperty      ( name = 'Height',    default=1,  min=0.001, max=500 )
    m_Radius     = bpy.props.FloatProperty      ( name = 'Radius',    default=1,  min=0.001, max=500 )
    m_Center     = bpy.props.FloatVectorProperty( name = 'Center',    default=(0.0, 0.0, 0.0), size=3 )
    m_Direction  = bpy.props.FloatVectorProperty( name = 'Direction', default=(0.0, 0.0, 1.0), size=3 )

    def properties( self ):
        return ['m_Capping','m_Resolution','m_Height','m_Radius','m_Center','m_Direction']    

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )
    
CLASSES.append( VTKConeSource )        
TYPENAMES.append( 'VTKConeSourceType' )
