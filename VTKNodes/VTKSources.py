from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKArcSource(Node, VTKTreeNode):

    bl_idname = 'VTKArcSourceType'
    bl_label  = 'vtkArcSource'

    
    m_Angle             = bpy.props.FloatProperty      ( name='Angle',             default=90.0 )
    m_Center            = bpy.props.FloatVectorProperty( name='Center',            default=(0.0, 0.0, 0.0), size=3 )
    m_Negative          = bpy.props.BoolProperty       ( name='Negative',          default=False )
    m_Normal            = bpy.props.FloatVectorProperty( name='Normal',            default=(0.0, 0.0, 1.0), size=3 )
    m_Point1            = bpy.props.FloatVectorProperty( name='Point1',            default=(0.0, 0.5, 0.0), size=3 )
    m_Point2            = bpy.props.FloatVectorProperty( name='Point2',            default=(0.5, 0.0, 0.0), size=3 )
    m_PolarVector       = bpy.props.FloatVectorProperty( name='PolarVector',       default=(1.0, 0.0, 0.0), size=3 )
    m_Resolution        = bpy.props.IntProperty        ( name='Resolution',        default=1 )
    m_UseNormalAndAngle = bpy.props.BoolProperty       ( name='UseNormalAndAngle', default=False )
    
    def m_properties( self ):
        return ['m_Angle','m_Center','m_Negative','m_Normal','m_Point1','m_Point2','m_PolarVector','m_Resolution','m_UseNormalAndAngle',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKArcSource )        
TYPENAMES.append('VTKArcSourceType' )

#--------------------------------------------------------------
class VTKArrowSource(Node, VTKTreeNode):

    bl_idname = 'VTKArrowSourceType'
    bl_label  = 'vtkArrowSource'

    
    m_Invert          = bpy.props.BoolProperty ( name='Invert',          default=False )
    m_ShaftRadius     = bpy.props.FloatProperty( name='ShaftRadius',     default=0.03 )
    m_ShaftResolution = bpy.props.IntProperty  ( name='ShaftResolution', default=6 )
    m_TipLength       = bpy.props.FloatProperty( name='TipLength',       default=0.35 )
    m_TipRadius       = bpy.props.FloatProperty( name='TipRadius',       default=0.1 )
    m_TipResolution   = bpy.props.IntProperty  ( name='TipResolution',   default=6 )
    
    def m_properties( self ):
        return ['m_Invert','m_ShaftRadius','m_ShaftResolution','m_TipLength','m_TipRadius','m_TipResolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKArrowSource )        
TYPENAMES.append('VTKArrowSourceType' )

#--------------------------------------------------------------
class VTKBoundedPointSource(Node, VTKTreeNode):

    bl_idname = 'VTKBoundedPointSourceType'
    bl_label  = 'vtkBoundedPointSource'

    
    m_Bounds               = bpy.props.FloatVectorProperty( name='Bounds',               default=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), size=6 )
    m_NumberOfPoints       = bpy.props.IntProperty        ( name='NumberOfPoints',       default=100 )
    m_ProduceCellOutput    = bpy.props.BoolProperty       ( name='ProduceCellOutput',    default=False )
    m_ProduceRandomScalars = bpy.props.BoolProperty       ( name='ProduceRandomScalars', default=False )
    m_ScalarRange          = bpy.props.FloatVectorProperty( name='ScalarRange',          default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_Bounds','m_NumberOfPoints','m_ProduceCellOutput','m_ProduceRandomScalars','m_ScalarRange',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKBoundedPointSource )        
TYPENAMES.append('VTKBoundedPointSourceType' )

#--------------------------------------------------------------
class VTKConeSource(Node, VTKTreeNode):

    bl_idname = 'VTKConeSourceType'
    bl_label  = 'vtkConeSource'

    
    m_Angle      = bpy.props.FloatProperty      ( name='Angle',      default=26.56505117707799 )
    m_Capping    = bpy.props.BoolProperty       ( name='Capping',    default=1 )
    m_Center     = bpy.props.FloatVectorProperty( name='Center',     default=(0.0, 0.0, 0.0), size=3 )
    m_Direction  = bpy.props.FloatVectorProperty( name='Direction',  default=(1.0, 0.0, 0.0), size=3 )
    m_Height     = bpy.props.FloatProperty      ( name='Height',     default=1.0 )
    m_Radius     = bpy.props.FloatProperty      ( name='Radius',     default=0.5 )
    m_Resolution = bpy.props.IntProperty        ( name='Resolution', default=6 )
    
    def m_properties( self ):
        return ['m_Angle','m_Capping','m_Center','m_Direction','m_Height','m_Radius','m_Resolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKConeSource )        
TYPENAMES.append('VTKConeSourceType' )

#--------------------------------------------------------------
class VTKCubeSource(Node, VTKTreeNode):

    bl_idname = 'VTKCubeSourceType'
    bl_label  = 'vtkCubeSource'

    
    m_Center  = bpy.props.FloatVectorProperty( name='Center',  default=(0.0, 0.0, 0.0), size=3 )
    m_XLength = bpy.props.FloatProperty      ( name='XLength', default=1.0 )
    m_YLength = bpy.props.FloatProperty      ( name='YLength', default=1.0 )
    m_ZLength = bpy.props.FloatProperty      ( name='ZLength', default=1.0 )
    
    def m_properties( self ):
        return ['m_Center','m_XLength','m_YLength','m_ZLength',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKCubeSource )        
TYPENAMES.append('VTKCubeSourceType' )

#--------------------------------------------------------------
class VTKCylinderSource(Node, VTKTreeNode):

    bl_idname = 'VTKCylinderSourceType'
    bl_label  = 'vtkCylinderSource'

    
    m_Capping    = bpy.props.BoolProperty       ( name='Capping',    default=1 )
    m_Center     = bpy.props.FloatVectorProperty( name='Center',     default=(0.0, 0.0, 0.0), size=3 )
    m_Height     = bpy.props.FloatProperty      ( name='Height',     default=1.0 )
    m_Radius     = bpy.props.FloatProperty      ( name='Radius',     default=0.5 )
    m_Resolution = bpy.props.IntProperty        ( name='Resolution', default=6 )
    
    def m_properties( self ):
        return ['m_Capping','m_Center','m_Height','m_Radius','m_Resolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKCylinderSource )        
TYPENAMES.append('VTKCylinderSourceType' )

#--------------------------------------------------------------
class VTKDiskSource(Node, VTKTreeNode):

    bl_idname = 'VTKDiskSourceType'
    bl_label  = 'vtkDiskSource'

    
    m_CircumferentialResolution = bpy.props.IntProperty  ( name='CircumferentialResolution', default=6 )
    m_InnerRadius               = bpy.props.FloatProperty( name='InnerRadius',               default=0.25 )
    m_OuterRadius               = bpy.props.FloatProperty( name='OuterRadius',               default=0.5 )
    m_RadialResolution          = bpy.props.IntProperty  ( name='RadialResolution',          default=1 )
    
    def m_properties( self ):
        return ['m_CircumferentialResolution','m_InnerRadius','m_OuterRadius','m_RadialResolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKDiskSource )        
TYPENAMES.append('VTKDiskSourceType' )

#--------------------------------------------------------------
class VTKEarthSource(Node, VTKTreeNode):

    bl_idname = 'VTKEarthSourceType'
    bl_label  = 'vtkEarthSource'

    
    m_OnRatio = bpy.props.IntProperty  ( name='OnRatio', default=10 )
    m_Outline = bpy.props.BoolProperty ( name='Outline', default=1 )
    m_Radius  = bpy.props.FloatProperty( name='Radius',  default=1.0 )
    
    def m_properties( self ):
        return ['m_OnRatio','m_Outline','m_Radius',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKEarthSource )        
TYPENAMES.append('VTKEarthSourceType' )

#--------------------------------------------------------------
class VTKEllipseArcSource(Node, VTKTreeNode):

    bl_idname = 'VTKEllipseArcSourceType'
    bl_label  = 'vtkEllipseArcSource'

    
    m_Center            = bpy.props.FloatVectorProperty( name='Center',            default=(0.0, 0.0, 0.0), size=3 )
    m_MajorRadiusVector = bpy.props.FloatVectorProperty( name='MajorRadiusVector', default=(1.0, 0.0, 0.0), size=3 )
    m_Normal            = bpy.props.FloatVectorProperty( name='Normal',            default=(0.0, 0.0, 1.0), size=3 )
    m_Ratio             = bpy.props.FloatProperty      ( name='Ratio',             default=1.0 )
    m_Resolution        = bpy.props.IntProperty        ( name='Resolution',        default=100 )
    m_SegmentAngle      = bpy.props.FloatProperty      ( name='SegmentAngle',      default=90.0 )
    m_StartAngle        = bpy.props.FloatProperty      ( name='StartAngle',        default=0.0 )
    
    def m_properties( self ):
        return ['m_Center','m_MajorRadiusVector','m_Normal','m_Ratio','m_Resolution','m_SegmentAngle','m_StartAngle',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKEllipseArcSource )        
TYPENAMES.append('VTKEllipseArcSourceType' )

#--------------------------------------------------------------
class VTKGlobeSource(Node, VTKTreeNode):

    bl_idname = 'VTKGlobeSourceType'
    bl_label  = 'vtkGlobeSource'

    
    m_AutoCalculateCurtainHeight = bpy.props.BoolProperty ( name='AutoCalculateCurtainHeight', default=True )
    m_CurtainHeight              = bpy.props.FloatProperty( name='CurtainHeight',              default=1000.0 )
    m_LatitudeResolution         = bpy.props.IntProperty  ( name='LatitudeResolution',         default=10 )
    m_LongitudeResolution        = bpy.props.IntProperty  ( name='LongitudeResolution',        default=10 )
    m_QuadrilateralTessellation  = bpy.props.BoolProperty ( name='QuadrilateralTessellation',  default=0 )
    m_Radius                     = bpy.props.FloatProperty( name='Radius',                     default=6356750.0 )
    
    def m_properties( self ):
        return ['m_AutoCalculateCurtainHeight','m_CurtainHeight','m_LatitudeResolution','m_LongitudeResolution','m_QuadrilateralTessellation','m_Radius',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKGlobeSource )        
TYPENAMES.append('VTKGlobeSourceType' )

#--------------------------------------------------------------
class VTKGlyphSource2D(Node, VTKTreeNode):

    bl_idname = 'VTKGlyphSource2DType'
    bl_label  = 'vtkGlyphSource2D'

    e_GlyphType_items=[ (x,x,x) for x in ['None', 'Vertex', 'Dash', 'Cross', 'ThickCross', 'Triangle', 'Square', 'Circle', 'Diamond', 'Arrow', 'ThickArrow', 'HookedArrow', 'EdgeArrow']]
    
    m_Center        = bpy.props.FloatVectorProperty( name='Center',        default=(0.0, 0.0, 0.0), size=3 )
    m_Color         = bpy.props.FloatVectorProperty( name='Color',         default=(1.0, 1.0, 1.0), size=3 )
    m_Cross         = bpy.props.BoolProperty       ( name='Cross',         default=0 )
    m_Dash          = bpy.props.BoolProperty       ( name='Dash',          default=0 )
    m_Filled        = bpy.props.BoolProperty       ( name='Filled',        default=1 )
    e_GlyphType     = bpy.props.EnumProperty       ( name='GlyphType',     default='Vertex', items=e_GlyphType_items )
    m_Resolution    = bpy.props.IntProperty        ( name='Resolution',    default=8 )
    m_RotationAngle = bpy.props.FloatProperty      ( name='RotationAngle', default=0.0 )
    m_Scale         = bpy.props.FloatProperty      ( name='Scale',         default=1.0 )
    m_Scale2        = bpy.props.FloatProperty      ( name='Scale2',        default=1.5 )
    
    def m_properties( self ):
        return ['m_Center','m_Color','m_Cross','m_Dash','m_Filled','e_GlyphType','m_Resolution','m_RotationAngle','m_Scale','m_Scale2',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKGlyphSource2D )        
TYPENAMES.append('VTKGlyphSource2DType' )

#--------------------------------------------------------------
class VTKLineSource(Node, VTKTreeNode):

    bl_idname = 'VTKLineSourceType'
    bl_label  = 'vtkLineSource'

    
    m_Point1     = bpy.props.FloatVectorProperty( name='Point1',     default=(-0.5, 0.0, 0.0), size=3 )
    m_Point2     = bpy.props.FloatVectorProperty( name='Point2',     default=(0.5, 0.0, 0.0), size=3 )
    m_Resolution = bpy.props.IntProperty        ( name='Resolution', default=1 )
    
    def m_properties( self ):
        return ['m_Point1','m_Point2','m_Resolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKLineSource )        
TYPENAMES.append('VTKLineSourceType' )

#--------------------------------------------------------------
class VTKPlaneSource(Node, VTKTreeNode):

    bl_idname = 'VTKPlaneSourceType'
    bl_label  = 'vtkPlaneSource'

    
    m_Center      = bpy.props.FloatVectorProperty( name='Center',      default=(0.0, 0.0, 0.0), size=3 )
    m_Normal      = bpy.props.FloatVectorProperty( name='Normal',      default=(0.0, 0.0, 1.0), size=3 )
    m_Origin      = bpy.props.FloatVectorProperty( name='Origin',      default=(-0.5, -0.5, 0.0), size=3 )
    m_Point1      = bpy.props.FloatVectorProperty( name='Point1',      default=(0.5, -0.5, 0.0), size=3 )
    m_Point2      = bpy.props.FloatVectorProperty( name='Point2',      default=(-0.5, 0.5, 0.0), size=3 )
    m_XResolution = bpy.props.IntProperty        ( name='XResolution', default=1 )
    m_YResolution = bpy.props.IntProperty        ( name='YResolution', default=1 )
    
    def m_properties( self ):
        return ['m_Center','m_Normal','m_Origin','m_Point1','m_Point2','m_XResolution','m_YResolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKPlaneSource )        
TYPENAMES.append('VTKPlaneSourceType' )

#--------------------------------------------------------------
class VTKPlatonicSolidSource(Node, VTKTreeNode):

    bl_idname = 'VTKPlatonicSolidSourceType'
    bl_label  = 'vtkPlatonicSolidSource'

    e_SolidType_items=[ (x,x,x) for x in ['Tetrahedron', 'Cube', 'Octahedron', 'Icosahedron', 'Dodecahedron']]
    
    e_SolidType = bpy.props.EnumProperty( name='SolidType', default='Tetrahedron', items=e_SolidType_items )
    
    def m_properties( self ):
        return ['e_SolidType',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKPlatonicSolidSource )        
TYPENAMES.append('VTKPlatonicSolidSourceType' )

#--------------------------------------------------------------
class VTKPointSource(Node, VTKTreeNode):

    bl_idname = 'VTKPointSourceType'
    bl_label  = 'vtkPointSource'

    e_Distribution_items=[ (x,x,x) for x in ['Shell', 'Uniform']]
    
    m_Center         = bpy.props.FloatVectorProperty( name='Center',         default=(0.0, 0.0, 0.0), size=3 )
    e_Distribution   = bpy.props.EnumProperty       ( name='Distribution',   default='Uniform', items=e_Distribution_items )
    m_NumberOfPoints = bpy.props.IntProperty        ( name='NumberOfPoints', default=10 )
    m_Radius         = bpy.props.FloatProperty      ( name='Radius',         default=0.5 )
    
    def m_properties( self ):
        return ['m_Center','e_Distribution','m_NumberOfPoints','m_Radius',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKPointSource )        
TYPENAMES.append('VTKPointSourceType' )

#--------------------------------------------------------------
class VTKRegularPolygonSource(Node, VTKTreeNode):

    bl_idname = 'VTKRegularPolygonSourceType'
    bl_label  = 'vtkRegularPolygonSource'

    
    m_Center           = bpy.props.FloatVectorProperty( name='Center',           default=(0.0, 0.0, 0.0), size=3 )
    m_GeneratePolygon  = bpy.props.BoolProperty       ( name='GeneratePolygon',  default=1 )
    m_GeneratePolyline = bpy.props.BoolProperty       ( name='GeneratePolyline', default=1 )
    m_Normal           = bpy.props.FloatVectorProperty( name='Normal',           default=(0.0, 0.0, 1.0), size=3 )
    m_NumberOfSides    = bpy.props.IntProperty        ( name='NumberOfSides',    default=6 )
    m_Radius           = bpy.props.FloatProperty      ( name='Radius',           default=0.5 )
    
    def m_properties( self ):
        return ['m_Center','m_GeneratePolygon','m_GeneratePolyline','m_Normal','m_NumberOfSides','m_Radius',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKRegularPolygonSource )        
TYPENAMES.append('VTKRegularPolygonSourceType' )

#--------------------------------------------------------------
class VTKSectorSource(Node, VTKTreeNode):

    bl_idname = 'VTKSectorSourceType'
    bl_label  = 'vtkSectorSource'

    
    m_CircumferentialResolution = bpy.props.IntProperty  ( name='CircumferentialResolution', default=6 )
    m_EndAngle                  = bpy.props.FloatProperty( name='EndAngle',                  default=90.0 )
    m_InnerRadius               = bpy.props.FloatProperty( name='InnerRadius',               default=1.0 )
    m_OuterRadius               = bpy.props.FloatProperty( name='OuterRadius',               default=2.0 )
    m_RadialResolution          = bpy.props.IntProperty  ( name='RadialResolution',          default=1 )
    m_StartAngle                = bpy.props.FloatProperty( name='StartAngle',                default=0.0 )
    m_ZCoord                    = bpy.props.FloatProperty( name='ZCoord',                    default=0.0 )
    
    def m_properties( self ):
        return ['m_CircumferentialResolution','m_EndAngle','m_InnerRadius','m_OuterRadius','m_RadialResolution','m_StartAngle','m_ZCoord',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKSectorSource )        
TYPENAMES.append('VTKSectorSourceType' )

#--------------------------------------------------------------
class VTKSphereSource(Node, VTKTreeNode):

    bl_idname = 'VTKSphereSourceType'
    bl_label  = 'vtkSphereSource'

    
    m_Center              = bpy.props.FloatVectorProperty( name='Center',              default=(0.0, 0.0, 0.0), size=3 )
    m_EndPhi              = bpy.props.FloatProperty      ( name='EndPhi',              default=180.0 )
    m_EndTheta            = bpy.props.FloatProperty      ( name='EndTheta',            default=360.0 )
    m_LatLongTessellation = bpy.props.BoolProperty       ( name='LatLongTessellation', default=0 )
    m_PhiResolution       = bpy.props.IntProperty        ( name='PhiResolution',       default=8 )
    m_Radius              = bpy.props.FloatProperty      ( name='Radius',              default=0.5 )
    m_StartPhi            = bpy.props.FloatProperty      ( name='StartPhi',            default=0.0 )
    m_StartTheta          = bpy.props.FloatProperty      ( name='StartTheta',          default=0.0 )
    m_ThetaResolution     = bpy.props.IntProperty        ( name='ThetaResolution',     default=8 )
    
    def m_properties( self ):
        return ['m_Center','m_EndPhi','m_EndTheta','m_LatLongTessellation','m_PhiResolution','m_Radius','m_StartPhi','m_StartTheta','m_ThetaResolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKSphereSource )        
TYPENAMES.append('VTKSphereSourceType' )

#--------------------------------------------------------------
class VTKSuperquadricSource(Node, VTKTreeNode):

    bl_idname = 'VTKSuperquadricSourceType'
    bl_label  = 'vtkSuperquadricSource'

    
    m_AxisOfSymmetry  = bpy.props.IntProperty        ( name='AxisOfSymmetry',  default=1 )
    m_Center          = bpy.props.FloatVectorProperty( name='Center',          default=(0.0, 0.0, 0.0), size=3 )
    m_PhiResolution   = bpy.props.IntProperty        ( name='PhiResolution',   default=16 )
    m_PhiRoundness    = bpy.props.FloatProperty      ( name='PhiRoundness',    default=1.0 )
    m_Scale           = bpy.props.FloatVectorProperty( name='Scale',           default=(1.0, 1.0, 1.0), size=3 )
    m_Size            = bpy.props.FloatProperty      ( name='Size',            default=0.5 )
    m_ThetaResolution = bpy.props.IntProperty        ( name='ThetaResolution', default=16 )
    m_ThetaRoundness  = bpy.props.FloatProperty      ( name='ThetaRoundness',  default=1.0 )
    m_Thickness       = bpy.props.FloatProperty      ( name='Thickness',       default=0.3333 )
    m_Toroidal        = bpy.props.BoolProperty       ( name='Toroidal',        default=0 )
    
    def m_properties( self ):
        return ['m_AxisOfSymmetry','m_Center','m_PhiResolution','m_PhiRoundness','m_Scale','m_Size','m_ThetaResolution','m_ThetaRoundness','m_Thickness','m_Toroidal',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKSuperquadricSource )        
TYPENAMES.append('VTKSuperquadricSourceType' )

#--------------------------------------------------------------
class VTKTessellatedBoxSource(Node, VTKTreeNode):

    bl_idname = 'VTKTessellatedBoxSourceType'
    bl_label  = 'vtkTessellatedBoxSource'

    
    m_Bounds                = bpy.props.FloatVectorProperty( name='Bounds',                default=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), size=6 )
    m_DuplicateSharedPoints = bpy.props.BoolProperty       ( name='DuplicateSharedPoints', default=0 )
    m_Level                 = bpy.props.IntProperty        ( name='Level',                 default=0 )
    m_Quads                 = bpy.props.BoolProperty       ( name='Quads',                 default=0 )
    
    def m_properties( self ):
        return ['m_Bounds','m_DuplicateSharedPoints','m_Level','m_Quads',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKTessellatedBoxSource )        
TYPENAMES.append('VTKTessellatedBoxSourceType' )

#--------------------------------------------------------------
class VTKTextSource(Node, VTKTreeNode):

    bl_idname = 'VTKTextSourceType'
    bl_label  = 'vtkTextSource'

    
    m_BackgroundColor = bpy.props.FloatVectorProperty( name='BackgroundColor', default=(0.0, 0.0, 0.0), size=3 )
    m_Backing         = bpy.props.BoolProperty       ( name='Backing',         default=1 )
    m_ForegroundColor = bpy.props.FloatVectorProperty( name='ForegroundColor', default=(1.0, 1.0, 1.0), size=3 )
    m_Text            = bpy.props.StringProperty     ( name='Text',            default='' )
    
    def m_properties( self ):
        return ['m_BackgroundColor','m_Backing','m_ForegroundColor','m_Text',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKTextSource )        
TYPENAMES.append('VTKTextSourceType' )

#--------------------------------------------------------------
class VTKTexturedSphereSource(Node, VTKTreeNode):

    bl_idname = 'VTKTexturedSphereSourceType'
    bl_label  = 'vtkTexturedSphereSource'

    
    m_Phi             = bpy.props.FloatProperty( name='Phi',             default=0.0 )
    m_PhiResolution   = bpy.props.IntProperty  ( name='PhiResolution',   default=8 )
    m_Radius          = bpy.props.FloatProperty( name='Radius',          default=0.5 )
    m_Theta           = bpy.props.FloatProperty( name='Theta',           default=0.0 )
    m_ThetaResolution = bpy.props.IntProperty  ( name='ThetaResolution', default=8 )
    
    def m_properties( self ):
        return ['m_Phi','m_PhiResolution','m_Radius','m_Theta','m_ThetaResolution',]
        
    def m_outputs(self):
        return [ 'VTKPolyDataSocketType',]
    
CLASSES.append  ( VTKTexturedSphereSource )        
TYPENAMES.append('VTKTexturedSphereSourceType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( 'sources', 'sources', items=menu_items) )