from .core import * 
TYPENAMES = []

#----------------------------------------------------------------   
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
    
CLASSES.append( VTKArrowSource      )        
TYPENAMES.append  ('VTKArrowSourceType' )

#----------------------------------------------------------------   
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

#----------------------------------------------------------------   
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

#----------------------------------------------------------------   
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

#----------------------------------------------------------------   
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

#----------------------------------------------------------------   
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory("sources", "sources", items=menu_items) )