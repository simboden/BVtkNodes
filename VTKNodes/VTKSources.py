from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAMRCutPlane(Node, VTKTreeNode):

    bl_idname = 'VTKAMRCutPlaneType'
    bl_label  = 'vtkAMRCutPlane'
    
    m_UseNativeCutter   = bpy.props.BoolProperty( name='UseNativeCutter',   default=True )
    m_LevelOfResolution = bpy.props.IntProperty ( name='LevelOfResolution', default=0 )
    
    def m_properties( self ):
        return ['m_UseNativeCutter','m_LevelOfResolution',]
    
CLASSES.append  ( VTKAMRCutPlane )        
TYPENAMES.append('VTKAMRCutPlaneType' )

#--------------------------------------------------------------
class VTKAMRGaussianPulseSource(Node, VTKTreeNode):

    bl_idname = 'VTKAMRGaussianPulseSourceType'
    bl_label  = 'vtkAMRGaussianPulseSource'
    
    m_PulseAmplitude = bpy.props.FloatProperty      ( name='PulseAmplitude', default=0.0001 )
    m_PulseOrigin    = bpy.props.FloatVectorProperty( name='PulseOrigin',    default=(0.0, 0.0, 0.0), size=3 )
    m_PulseWidth     = bpy.props.FloatVectorProperty( name='PulseWidth',     default=(0.5, 0.5, 0.5), size=3 )
    
    def m_properties( self ):
        return ['m_PulseAmplitude','m_PulseOrigin','m_PulseWidth',]
    
CLASSES.append  ( VTKAMRGaussianPulseSource )        
TYPENAMES.append('VTKAMRGaussianPulseSourceType' )

#--------------------------------------------------------------
class VTKArcSource(Node, VTKTreeNode):

    bl_idname = 'VTKArcSourceType'
    bl_label  = 'vtkArcSource'
    
    m_Negative          = bpy.props.BoolProperty       ( name='Negative',          default=False )
    m_UseNormalAndAngle = bpy.props.BoolProperty       ( name='UseNormalAndAngle', default=False )
    m_Resolution        = bpy.props.IntProperty        ( name='Resolution',        default=1 )
    m_Angle             = bpy.props.FloatProperty      ( name='Angle',             default=90.0 )
    m_Center            = bpy.props.FloatVectorProperty( name='Center',            default=(0.0, 0.0, 0.0), size=3 )
    m_Normal            = bpy.props.FloatVectorProperty( name='Normal',            default=(0.0, 0.0, 1.0), size=3 )
    m_Point1            = bpy.props.FloatVectorProperty( name='Point1',            default=(0.0, 0.5, 0.0), size=3 )
    m_Point2            = bpy.props.FloatVectorProperty( name='Point2',            default=(0.5, 0.0, 0.0), size=3 )
    m_PolarVector       = bpy.props.FloatVectorProperty( name='PolarVector',       default=(1.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Negative','m_UseNormalAndAngle','m_Resolution','m_Angle','m_Center','m_Normal','m_Point1','m_Point2','m_PolarVector',]
    
CLASSES.append  ( VTKArcSource )        
TYPENAMES.append('VTKArcSourceType' )

#--------------------------------------------------------------
class VTKArrowSource(Node, VTKTreeNode):

    bl_idname = 'VTKArrowSourceType'
    bl_label  = 'vtkArrowSource'
    
    m_Invert          = bpy.props.BoolProperty ( name='Invert',          default=False )
    m_ShaftResolution = bpy.props.IntProperty  ( name='ShaftResolution', default=6 )
    m_TipResolution   = bpy.props.IntProperty  ( name='TipResolution',   default=6 )
    m_ShaftRadius     = bpy.props.FloatProperty( name='ShaftRadius',     default=0.03 )
    m_TipLength       = bpy.props.FloatProperty( name='TipLength',       default=0.35 )
    m_TipRadius       = bpy.props.FloatProperty( name='TipRadius',       default=0.1 )
    
    def m_properties( self ):
        return ['m_Invert','m_ShaftResolution','m_TipResolution','m_ShaftRadius','m_TipLength','m_TipRadius',]
    
CLASSES.append  ( VTKArrowSource )        
TYPENAMES.append('VTKArrowSourceType' )

#--------------------------------------------------------------
class VTKAxes(Node, VTKTreeNode):

    bl_idname = 'VTKAxesType'
    bl_label  = 'vtkAxes'
    
    m_ComputeNormals = bpy.props.BoolProperty       ( name='ComputeNormals', default=1 )
    m_Symmetric      = bpy.props.BoolProperty       ( name='Symmetric',      default=0 )
    m_ScaleFactor    = bpy.props.FloatProperty      ( name='ScaleFactor',    default=1.0 )
    m_Origin         = bpy.props.FloatVectorProperty( name='Origin',         default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_ComputeNormals','m_Symmetric','m_ScaleFactor','m_Origin',]
    
CLASSES.append  ( VTKAxes )        
TYPENAMES.append('VTKAxesType' )

#--------------------------------------------------------------
class VTKBooleanTexture(Node, VTKTreeNode):

    bl_idname = 'VTKBooleanTextureType'
    bl_label  = 'vtkBooleanTexture'
    
    m_Thickness = bpy.props.IntProperty      ( name='Thickness', default=0 )
    m_XSize     = bpy.props.IntProperty      ( name='XSize',     default=12 )
    m_YSize     = bpy.props.IntProperty      ( name='YSize',     default=12 )
    m_InIn      = bpy.props.IntVectorProperty( name='InIn',      default=[255, 255], size=2 )
    m_InOn      = bpy.props.IntVectorProperty( name='InOn',      default=[255, 255], size=2 )
    m_InOut     = bpy.props.IntVectorProperty( name='InOut',     default=[255, 255], size=2 )
    m_OnIn      = bpy.props.IntVectorProperty( name='OnIn',      default=[255, 255], size=2 )
    m_OnOn      = bpy.props.IntVectorProperty( name='OnOn',      default=[255, 255], size=2 )
    m_OnOut     = bpy.props.IntVectorProperty( name='OnOut',     default=[255, 255], size=2 )
    m_OutIn     = bpy.props.IntVectorProperty( name='OutIn',     default=[255, 255], size=2 )
    m_OutOn     = bpy.props.IntVectorProperty( name='OutOn',     default=[255, 255], size=2 )
    m_OutOut    = bpy.props.IntVectorProperty( name='OutOut',    default=[255, 255], size=2 )
    
    def m_properties( self ):
        return ['m_Thickness','m_XSize','m_YSize','m_InIn','m_InOn','m_InOut','m_OnIn','m_OnOn','m_OnOut','m_OutIn','m_OutOn','m_OutOut',]
    
CLASSES.append  ( VTKBooleanTexture )        
TYPENAMES.append('VTKBooleanTextureType' )

#--------------------------------------------------------------
class VTKBoundedPointSource(Node, VTKTreeNode):

    bl_idname = 'VTKBoundedPointSourceType'
    bl_label  = 'vtkBoundedPointSource'
    
    m_ProduceCellOutput    = bpy.props.BoolProperty       ( name='ProduceCellOutput',    default=False )
    m_ProduceRandomScalars = bpy.props.BoolProperty       ( name='ProduceRandomScalars', default=False )
    m_NumberOfPoints       = bpy.props.IntProperty        ( name='NumberOfPoints',       default=100 )
    m_Bounds               = bpy.props.FloatVectorProperty( name='Bounds',               default=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), size=6 )
    m_ScalarRange          = bpy.props.FloatVectorProperty( name='ScalarRange',          default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_ProduceCellOutput','m_ProduceRandomScalars','m_NumberOfPoints','m_Bounds','m_ScalarRange',]
    
CLASSES.append  ( VTKBoundedPointSource )        
TYPENAMES.append('VTKBoundedPointSourceType' )

#--------------------------------------------------------------
class VTKConeSource(Node, VTKTreeNode):

    bl_idname = 'VTKConeSourceType'
    bl_label  = 'vtkConeSource'
    
    m_Capping    = bpy.props.BoolProperty       ( name='Capping',    default=1 )
    m_Resolution = bpy.props.IntProperty        ( name='Resolution', default=6 )
    m_Angle      = bpy.props.FloatProperty      ( name='Angle',      default=26.56505117707799 )
    m_Height     = bpy.props.FloatProperty      ( name='Height',     default=1.0 )
    m_Radius     = bpy.props.FloatProperty      ( name='Radius',     default=0.5 )
    m_Center     = bpy.props.FloatVectorProperty( name='Center',     default=(0.0, 0.0, 0.0), size=3 )
    m_Direction  = bpy.props.FloatVectorProperty( name='Direction',  default=(1.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_Angle','m_Height','m_Radius','m_Center','m_Direction',]
    
CLASSES.append  ( VTKConeSource )        
TYPENAMES.append('VTKConeSourceType' )

#--------------------------------------------------------------
class VTKCubeSource(Node, VTKTreeNode):

    bl_idname = 'VTKCubeSourceType'
    bl_label  = 'vtkCubeSource'
    
    m_XLength = bpy.props.FloatProperty      ( name='XLength', default=1.0 )
    m_YLength = bpy.props.FloatProperty      ( name='YLength', default=1.0 )
    m_ZLength = bpy.props.FloatProperty      ( name='ZLength', default=1.0 )
    m_Center  = bpy.props.FloatVectorProperty( name='Center',  default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_XLength','m_YLength','m_ZLength','m_Center',]
    
CLASSES.append  ( VTKCubeSource )        
TYPENAMES.append('VTKCubeSourceType' )

#--------------------------------------------------------------
class VTKCylinderSource(Node, VTKTreeNode):

    bl_idname = 'VTKCylinderSourceType'
    bl_label  = 'vtkCylinderSource'
    
    m_Capping    = bpy.props.BoolProperty       ( name='Capping',    default=1 )
    m_Resolution = bpy.props.IntProperty        ( name='Resolution', default=6 )
    m_Height     = bpy.props.FloatProperty      ( name='Height',     default=1.0 )
    m_Radius     = bpy.props.FloatProperty      ( name='Radius',     default=0.5 )
    m_Center     = bpy.props.FloatVectorProperty( name='Center',     default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_Height','m_Radius','m_Center',]
    
CLASSES.append  ( VTKCylinderSource )        
TYPENAMES.append('VTKCylinderSourceType' )

#--------------------------------------------------------------
class VTKDataObjectGenerator(Node, VTKTreeNode):

    bl_idname = 'VTKDataObjectGeneratorType'
    bl_label  = 'vtkDataObjectGenerator'
    
    m_Program = bpy.props.StringProperty( name='Program', default="ID1" )
    
    def m_properties( self ):
        return ['m_Program',]
    
CLASSES.append  ( VTKDataObjectGenerator )        
TYPENAMES.append('VTKDataObjectGeneratorType' )

#--------------------------------------------------------------
class VTKDiagonalMatrixSource(Node, VTKTreeNode):

    bl_idname = 'VTKDiagonalMatrixSourceType'
    bl_label  = 'vtkDiagonalMatrixSource'
    
    m_ColumnLabel   = bpy.props.StringProperty( name='ColumnLabel',   default="columns" )
    m_RowLabel      = bpy.props.StringProperty( name='RowLabel',      default="rows" )
    m_ArrayType     = bpy.props.IntProperty   ( name='ArrayType',     default=0 )
    m_Extents       = bpy.props.IntProperty   ( name='Extents',       default=3 )
    m_Diagonal      = bpy.props.FloatProperty ( name='Diagonal',      default=1.0 )
    m_SubDiagonal   = bpy.props.FloatProperty ( name='SubDiagonal',   default=0.0 )
    m_SuperDiagonal = bpy.props.FloatProperty ( name='SuperDiagonal', default=0.0 )
    
    def m_properties( self ):
        return ['m_ColumnLabel','m_RowLabel','m_ArrayType','m_Extents','m_Diagonal','m_SubDiagonal','m_SuperDiagonal',]
    
CLASSES.append  ( VTKDiagonalMatrixSource )        
TYPENAMES.append('VTKDiagonalMatrixSourceType' )

#--------------------------------------------------------------
class VTKDiskSource(Node, VTKTreeNode):

    bl_idname = 'VTKDiskSourceType'
    bl_label  = 'vtkDiskSource'
    
    m_CircumferentialResolution = bpy.props.IntProperty  ( name='CircumferentialResolution', default=6 )
    m_RadialResolution          = bpy.props.IntProperty  ( name='RadialResolution',          default=1 )
    m_InnerRadius               = bpy.props.FloatProperty( name='InnerRadius',               default=0.25 )
    m_OuterRadius               = bpy.props.FloatProperty( name='OuterRadius',               default=0.5 )
    
    def m_properties( self ):
        return ['m_CircumferentialResolution','m_RadialResolution','m_InnerRadius','m_OuterRadius',]
    
CLASSES.append  ( VTKDiskSource )        
TYPENAMES.append('VTKDiskSourceType' )

#--------------------------------------------------------------
class VTKEarthSource(Node, VTKTreeNode):

    bl_idname = 'VTKEarthSourceType'
    bl_label  = 'vtkEarthSource'
    
    m_Outline = bpy.props.BoolProperty ( name='Outline', default=1 )
    m_OnRatio = bpy.props.IntProperty  ( name='OnRatio', default=10 )
    m_Radius  = bpy.props.FloatProperty( name='Radius',  default=1.0 )
    
    def m_properties( self ):
        return ['m_Outline','m_OnRatio','m_Radius',]
    
CLASSES.append  ( VTKEarthSource )        
TYPENAMES.append('VTKEarthSourceType' )

#--------------------------------------------------------------
class VTKEllipseArcSource(Node, VTKTreeNode):

    bl_idname = 'VTKEllipseArcSourceType'
    bl_label  = 'vtkEllipseArcSource'
    
    m_Resolution        = bpy.props.IntProperty        ( name='Resolution',        default=100 )
    m_Ratio             = bpy.props.FloatProperty      ( name='Ratio',             default=1.0 )
    m_SegmentAngle      = bpy.props.FloatProperty      ( name='SegmentAngle',      default=90.0 )
    m_StartAngle        = bpy.props.FloatProperty      ( name='StartAngle',        default=0.0 )
    m_Center            = bpy.props.FloatVectorProperty( name='Center',            default=(0.0, 0.0, 0.0), size=3 )
    m_MajorRadiusVector = bpy.props.FloatVectorProperty( name='MajorRadiusVector', default=(1.0, 0.0, 0.0), size=3 )
    m_Normal            = bpy.props.FloatVectorProperty( name='Normal',            default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Resolution','m_Ratio','m_SegmentAngle','m_StartAngle','m_Center','m_MajorRadiusVector','m_Normal',]
    
CLASSES.append  ( VTKEllipseArcSource )        
TYPENAMES.append('VTKEllipseArcSourceType' )

#--------------------------------------------------------------
class VTKEllipticalButtonSource(Node, VTKTreeNode):

    bl_idname = 'VTKEllipticalButtonSourceType'
    bl_label  = 'vtkEllipticalButtonSource'
    e_TextureStyle_items=[ (x,x,x) for x in ['FitImage', 'Proportional']]
    
    m_TwoSided                  = bpy.props.BoolProperty       ( name='TwoSided',                  default=0 )
    m_CircumferentialResolution = bpy.props.IntProperty        ( name='CircumferentialResolution', default=4 )
    m_ShoulderResolution        = bpy.props.IntProperty        ( name='ShoulderResolution',        default=2 )
    m_TextureResolution         = bpy.props.IntProperty        ( name='TextureResolution',         default=2 )
    m_Depth                     = bpy.props.FloatProperty      ( name='Depth',                     default=0.05 )
    m_Height                    = bpy.props.FloatProperty      ( name='Height',                    default=0.5 )
    m_RadialRatio               = bpy.props.FloatProperty      ( name='RadialRatio',               default=1.1 )
    m_Width                     = bpy.props.FloatProperty      ( name='Width',                     default=0.5 )
    e_TextureStyle              = bpy.props.EnumProperty       ( name='TextureStyle',              default="Proportional", items=e_TextureStyle_items )
    m_TextureDimensions         = bpy.props.IntVectorProperty  ( name='TextureDimensions',         default=[100, 100], size=2 )
    m_Center                    = bpy.props.FloatVectorProperty( name='Center',                    default=(0.0, 0.0, 0.0), size=3 )
    m_ShoulderTextureCoordinate = bpy.props.FloatVectorProperty( name='ShoulderTextureCoordinate', default=(0.0, 0.0), size=2 )
    
    def m_properties( self ):
        return ['m_TwoSided','m_CircumferentialResolution','m_ShoulderResolution','m_TextureResolution','m_Depth','m_Height','m_RadialRatio','m_Width','e_TextureStyle','m_TextureDimensions','m_Center','m_ShoulderTextureCoordinate',]
    
CLASSES.append  ( VTKEllipticalButtonSource )        
TYPENAMES.append('VTKEllipticalButtonSourceType' )

#--------------------------------------------------------------
class VTKEnsembleSource(Node, VTKTreeNode):

    bl_idname = 'VTKEnsembleSourceType'
    bl_label  = 'vtkEnsembleSource'
    
    m_CurrentMember = bpy.props.IntProperty( name='CurrentMember', default=0 )
    
    def m_properties( self ):
        return ['m_CurrentMember',]
    
CLASSES.append  ( VTKEnsembleSource )        
TYPENAMES.append('VTKEnsembleSourceType' )

#--------------------------------------------------------------
class VTKFrustumSource(Node, VTKTreeNode):

    bl_idname = 'VTKFrustumSourceType'
    bl_label  = 'vtkFrustumSource'
    
    m_ShowLines   = bpy.props.BoolProperty ( name='ShowLines',   default=True )
    m_LinesLength = bpy.props.FloatProperty( name='LinesLength', default=1.0 )
    
    def m_properties( self ):
        return ['m_ShowLines','m_LinesLength',]
    
CLASSES.append  ( VTKFrustumSource )        
TYPENAMES.append('VTKFrustumSourceType' )

#--------------------------------------------------------------
class VTKGeoGraticule(Node, VTKTreeNode):

    bl_idname = 'VTKGeoGraticuleType'
    bl_label  = 'vtkGeoGraticule'
    
    m_GeometryType    = bpy.props.IntProperty        ( name='GeometryType',    default=1 )
    m_LatitudeLevel   = bpy.props.IntProperty        ( name='LatitudeLevel',   default=2 )
    m_LongitudeLevel  = bpy.props.IntProperty        ( name='LongitudeLevel',  default=1 )
    m_LatitudeBounds  = bpy.props.FloatVectorProperty( name='LatitudeBounds',  default=(-90.0, 90.0), size=2 )
    m_LongitudeBounds = bpy.props.FloatVectorProperty( name='LongitudeBounds', default=(0.0, 180.0), size=2 )
    
    def m_properties( self ):
        return ['m_GeometryType','m_LatitudeLevel','m_LongitudeLevel','m_LatitudeBounds','m_LongitudeBounds',]
    
CLASSES.append  ( VTKGeoGraticule )        
TYPENAMES.append('VTKGeoGraticuleType' )

#--------------------------------------------------------------
class VTKGeoRandomGraphSource(Node, VTKTreeNode):

    bl_idname = 'VTKGeoRandomGraphSourceType'
    bl_label  = 'vtkGeoRandomGraphSource'
    
    m_AllowParallelEdges        = bpy.props.BoolProperty  ( name='AllowParallelEdges',        default=False )
    m_AllowSelfLoops            = bpy.props.BoolProperty  ( name='AllowSelfLoops',            default=False )
    m_Directed                  = bpy.props.BoolProperty  ( name='Directed',                  default=False )
    m_GeneratePedigreeIds       = bpy.props.BoolProperty  ( name='GeneratePedigreeIds',       default=True )
    m_IncludeEdgeWeights        = bpy.props.BoolProperty  ( name='IncludeEdgeWeights',        default=False )
    m_StartWithTree             = bpy.props.BoolProperty  ( name='StartWithTree',             default=False )
    m_UseEdgeProbability        = bpy.props.BoolProperty  ( name='UseEdgeProbability',        default=False )
    m_EdgePedigreeIdArrayName   = bpy.props.StringProperty( name='EdgePedigreeIdArrayName',   default="edge id" )
    m_EdgeWeightArrayName       = bpy.props.StringProperty( name='EdgeWeightArrayName',       default="edge weight" )
    m_VertexPedigreeIdArrayName = bpy.props.StringProperty( name='VertexPedigreeIdArrayName', default="vertex id" )
    m_NumberOfEdges             = bpy.props.IntProperty   ( name='NumberOfEdges',             default=10 )
    m_NumberOfVertices          = bpy.props.IntProperty   ( name='NumberOfVertices',          default=10 )
    m_Seed                      = bpy.props.IntProperty   ( name='Seed',                      default=1177 )
    m_EdgeProbability           = bpy.props.FloatProperty ( name='EdgeProbability',           default=0.5 )
    
    def m_properties( self ):
        return ['m_AllowParallelEdges','m_AllowSelfLoops','m_Directed','m_GeneratePedigreeIds','m_IncludeEdgeWeights','m_StartWithTree','m_UseEdgeProbability','m_EdgePedigreeIdArrayName','m_EdgeWeightArrayName','m_VertexPedigreeIdArrayName','m_NumberOfEdges','m_NumberOfVertices','m_Seed','m_EdgeProbability',]
    
CLASSES.append  ( VTKGeoRandomGraphSource )        
TYPENAMES.append('VTKGeoRandomGraphSourceType' )

#--------------------------------------------------------------
class VTKGlobeSource(Node, VTKTreeNode):

    bl_idname = 'VTKGlobeSourceType'
    bl_label  = 'vtkGlobeSource'
    
    m_AutoCalculateCurtainHeight = bpy.props.BoolProperty ( name='AutoCalculateCurtainHeight', default=True )
    m_QuadrilateralTessellation  = bpy.props.BoolProperty ( name='QuadrilateralTessellation',  default=0 )
    m_LatitudeResolution         = bpy.props.IntProperty  ( name='LatitudeResolution',         default=10 )
    m_LongitudeResolution        = bpy.props.IntProperty  ( name='LongitudeResolution',        default=10 )
    m_CurtainHeight              = bpy.props.FloatProperty( name='CurtainHeight',              default=1000.0 )
    m_Radius                     = bpy.props.FloatProperty( name='Radius',                     default=6356750.0 )
    
    def m_properties( self ):
        return ['m_AutoCalculateCurtainHeight','m_QuadrilateralTessellation','m_LatitudeResolution','m_LongitudeResolution','m_CurtainHeight','m_Radius',]
    
CLASSES.append  ( VTKGlobeSource )        
TYPENAMES.append('VTKGlobeSourceType' )

#--------------------------------------------------------------
class VTKGlyphSource2D(Node, VTKTreeNode):

    bl_idname = 'VTKGlyphSource2DType'
    bl_label  = 'vtkGlyphSource2D'
    e_GlyphType_items=[ (x,x,x) for x in ['None', 'Vertex', 'Dash', 'Cross', 'ThickCross', 'Triangle', 'Square', 'Circle', 'Diamond', 'Arrow', 'ThickArrow', 'HookedArrow', 'EdgeArrow']]
    
    m_Cross         = bpy.props.BoolProperty       ( name='Cross',         default=0 )
    m_Dash          = bpy.props.BoolProperty       ( name='Dash',          default=0 )
    m_Filled        = bpy.props.BoolProperty       ( name='Filled',        default=1 )
    m_Resolution    = bpy.props.IntProperty        ( name='Resolution',    default=8 )
    m_RotationAngle = bpy.props.FloatProperty      ( name='RotationAngle', default=0.0 )
    m_Scale         = bpy.props.FloatProperty      ( name='Scale',         default=1.0 )
    m_Scale2        = bpy.props.FloatProperty      ( name='Scale2',        default=1.5 )
    e_GlyphType     = bpy.props.EnumProperty       ( name='GlyphType',     default="Vertex", items=e_GlyphType_items )
    m_Center        = bpy.props.FloatVectorProperty( name='Center',        default=(0.0, 0.0, 0.0), size=3 )
    m_Color         = bpy.props.FloatVectorProperty( name='Color',         default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Cross','m_Dash','m_Filled','m_Resolution','m_RotationAngle','m_Scale','m_Scale2','e_GlyphType','m_Center','m_Color',]
    
CLASSES.append  ( VTKGlyphSource2D )        
TYPENAMES.append('VTKGlyphSource2DType' )

#--------------------------------------------------------------
class VTKHyperOctreeFractalSource(Node, VTKTreeNode):

    bl_idname = 'VTKHyperOctreeFractalSourceType'
    bl_label  = 'vtkHyperOctreeFractalSource'
    
    m_Dimension                 = bpy.props.IntProperty        ( name='Dimension',                 default=3 )
    m_MaximumLevel              = bpy.props.IntProperty        ( name='MaximumLevel',              default=5 )
    m_MaximumNumberOfIterations = bpy.props.IntProperty        ( name='MaximumNumberOfIterations', default=100 )
    m_MinimumLevel              = bpy.props.IntProperty        ( name='MinimumLevel',              default=3 )
    m_SpanThreshold             = bpy.props.FloatProperty      ( name='SpanThreshold',             default=2.0 )
    m_ProjectionAxes            = bpy.props.IntVectorProperty  ( name='ProjectionAxes',            default=[0, 1, 2], size=3 )
    m_OriginCX                  = bpy.props.FloatVectorProperty( name='OriginCX',                  default=(-1.75, -1.25, 0.0, 0.0), size=4 )
    m_SizeCX                    = bpy.props.FloatVectorProperty( name='SizeCX',                    default=(2.5, 2.5, 2.0, 1.5), size=4 )
    
    def m_properties( self ):
        return ['m_Dimension','m_MaximumLevel','m_MaximumNumberOfIterations','m_MinimumLevel','m_SpanThreshold','m_ProjectionAxes','m_OriginCX','m_SizeCX',]
    
CLASSES.append  ( VTKHyperOctreeFractalSource )        
TYPENAMES.append('VTKHyperOctreeFractalSourceType' )

#--------------------------------------------------------------
class VTKHyperOctreeSampleFunction(Node, VTKTreeNode):

    bl_idname = 'VTKHyperOctreeSampleFunctionType'
    bl_label  = 'vtkHyperOctreeSampleFunction'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_Dimension        = bpy.props.IntProperty        ( name='Dimension',        default=3 )
    m_Levels           = bpy.props.IntProperty        ( name='Levels',           default=5 )
    m_MinLevels        = bpy.props.IntProperty        ( name='MinLevels',        default=1 )
    m_Depth            = bpy.props.FloatProperty      ( name='Depth',            default=1.0 )
    m_Height           = bpy.props.FloatProperty      ( name='Height',           default=1.0 )
    m_Threshold        = bpy.props.FloatProperty      ( name='Threshold',        default=0.1 )
    m_Width            = bpy.props.FloatProperty      ( name='Width',            default=1.0 )
    e_OutputScalarType = bpy.props.EnumProperty       ( name='OutputScalarType', default="Double", items=e_OutputScalarType_items )
    m_Origin           = bpy.props.FloatVectorProperty( name='Origin',           default=(0.0, 0.0, 0.0), size=3 )
    m_Size             = bpy.props.FloatVectorProperty( name='Size',             default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Dimension','m_Levels','m_MinLevels','m_Depth','m_Height','m_Threshold','m_Width','e_OutputScalarType','m_Origin','m_Size',]
    
CLASSES.append  ( VTKHyperOctreeSampleFunction )        
TYPENAMES.append('VTKHyperOctreeSampleFunctionType' )

#--------------------------------------------------------------
class VTKImageCanvasSource2D(Node, VTKTreeNode):

    bl_idname = 'VTKImageCanvasSource2DType'
    bl_label  = 'vtkImageCanvasSource2D'
    e_ScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_DefaultZ                 = bpy.props.IntProperty        ( name='DefaultZ',                 default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_ScalarType               = bpy.props.EnumProperty       ( name='ScalarType',               default="Double", items=e_ScalarType_items )
    m_DrawColor                = bpy.props.FloatVectorProperty( name='DrawColor',                default=(0.0, 0.0, 0.0, 0.0), size=4 )
    m_Ratio                    = bpy.props.FloatVectorProperty( name='Ratio',                    default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_DefaultZ','m_NumberOfScalarComponents','e_ScalarType','m_DrawColor','m_Ratio',]
    
CLASSES.append  ( VTKImageCanvasSource2D )        
TYPENAMES.append('VTKImageCanvasSource2DType' )

#--------------------------------------------------------------
class VTKImageEllipsoidSource(Node, VTKTreeNode):

    bl_idname = 'VTKImageEllipsoidSourceType'
    bl_label  = 'vtkImageEllipsoidSource'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_InValue          = bpy.props.FloatProperty      ( name='InValue',          default=255.0 )
    m_OutValue         = bpy.props.FloatProperty      ( name='OutValue',         default=0.0 )
    e_OutputScalarType = bpy.props.EnumProperty       ( name='OutputScalarType', default="UnsignedChar", items=e_OutputScalarType_items )
    m_Center           = bpy.props.FloatVectorProperty( name='Center',           default=(128.0, 128.0, 0.0), size=3 )
    m_Radius           = bpy.props.FloatVectorProperty( name='Radius',           default=(70.0, 70.0, 70.0), size=3 )
    
    def m_properties( self ):
        return ['m_InValue','m_OutValue','e_OutputScalarType','m_Center','m_Radius',]
    
CLASSES.append  ( VTKImageEllipsoidSource )        
TYPENAMES.append('VTKImageEllipsoidSourceType' )

#--------------------------------------------------------------
class VTKImageGaussianSource(Node, VTKTreeNode):

    bl_idname = 'VTKImageGaussianSourceType'
    bl_label  = 'vtkImageGaussianSource'
    
    m_Maximum           = bpy.props.FloatProperty      ( name='Maximum',           default=1.0 )
    m_StandardDeviation = bpy.props.FloatProperty      ( name='StandardDeviation', default=100.0 )
    m_Center            = bpy.props.FloatVectorProperty( name='Center',            default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Maximum','m_StandardDeviation','m_Center',]
    
CLASSES.append  ( VTKImageGaussianSource )        
TYPENAMES.append('VTKImageGaussianSourceType' )

#--------------------------------------------------------------
class VTKImageGridSource(Node, VTKTreeNode):

    bl_idname = 'VTKImageGridSourceType'
    bl_label  = 'vtkImageGridSource'
    e_DataScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'Double']]
    
    m_FillValue      = bpy.props.FloatProperty      ( name='FillValue',      default=0.0 )
    m_LineValue      = bpy.props.FloatProperty      ( name='LineValue',      default=1.0 )
    e_DataScalarType = bpy.props.EnumProperty       ( name='DataScalarType', default="Double", items=e_DataScalarType_items )
    m_GridOrigin     = bpy.props.IntVectorProperty  ( name='GridOrigin',     default=[0, 0, 0], size=3 )
    m_GridSpacing    = bpy.props.IntVectorProperty  ( name='GridSpacing',    default=[10, 10, 0], size=3 )
    m_DataOrigin     = bpy.props.FloatVectorProperty( name='DataOrigin',     default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing    = bpy.props.FloatVectorProperty( name='DataSpacing',    default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FillValue','m_LineValue','e_DataScalarType','m_GridOrigin','m_GridSpacing','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKImageGridSource )        
TYPENAMES.append('VTKImageGridSourceType' )

#--------------------------------------------------------------
class VTKImageImport(Node, VTKTreeNode):

    bl_idname = 'VTKImageImportType'
    bl_label  = 'vtkImageImport'
    e_DataScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'Float', 'Double']]
    
    m_ScalarArrayName          = bpy.props.StringProperty     ( name='ScalarArrayName',          default="scalars" )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_ScalarArrayName','m_NumberOfScalarComponents','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKImageImport )        
TYPENAMES.append('VTKImageImportType' )

#--------------------------------------------------------------
class VTKImageMandelbrotSource(Node, VTKTreeNode):

    bl_idname = 'VTKImageMandelbrotSourceType'
    bl_label  = 'vtkImageMandelbrotSource'
    
    m_ConstantSize              = bpy.props.BoolProperty       ( name='ConstantSize',              default=1 )
    m_MaximumNumberOfIterations = bpy.props.IntProperty        ( name='MaximumNumberOfIterations', default=100 )
    m_SubsampleRate             = bpy.props.IntProperty        ( name='SubsampleRate',             default=1 )
    m_ProjectionAxes            = bpy.props.IntVectorProperty  ( name='ProjectionAxes',            default=[0, 1, 2], size=3 )
    m_OriginCX                  = bpy.props.FloatVectorProperty( name='OriginCX',                  default=(-1.75, -1.25, 0.0, 0.0), size=4 )
    m_SampleCX                  = bpy.props.FloatVectorProperty( name='SampleCX',                  default=(0.01, 0.01, 0.01, 0.01), size=4 )
    m_SizeCX                    = bpy.props.FloatVectorProperty( name='SizeCX',                    default=(2.5, 2.5, 2.0, 1.5), size=4 )
    
    def m_properties( self ):
        return ['m_ConstantSize','m_MaximumNumberOfIterations','m_SubsampleRate','m_ProjectionAxes','m_OriginCX','m_SampleCX','m_SizeCX',]
    
CLASSES.append  ( VTKImageMandelbrotSource )        
TYPENAMES.append('VTKImageMandelbrotSourceType' )

#--------------------------------------------------------------
class VTKImageNoiseSource(Node, VTKTreeNode):

    bl_idname = 'VTKImageNoiseSourceType'
    bl_label  = 'vtkImageNoiseSource'
    
    m_Maximum = bpy.props.FloatProperty( name='Maximum', default=10.0 )
    m_Minimum = bpy.props.FloatProperty( name='Minimum', default=0.0 )
    
    def m_properties( self ):
        return ['m_Maximum','m_Minimum',]
    
CLASSES.append  ( VTKImageNoiseSource )        
TYPENAMES.append('VTKImageNoiseSourceType' )

#--------------------------------------------------------------
class VTKImageSinusoidSource(Node, VTKTreeNode):

    bl_idname = 'VTKImageSinusoidSourceType'
    bl_label  = 'vtkImageSinusoidSource'
    
    m_Amplitude = bpy.props.FloatProperty      ( name='Amplitude', default=255.0 )
    m_Period    = bpy.props.FloatProperty      ( name='Period',    default=20.0 )
    m_Phase     = bpy.props.FloatProperty      ( name='Phase',     default=0.0 )
    m_Direction = bpy.props.FloatVectorProperty( name='Direction', default=(1.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Amplitude','m_Period','m_Phase','m_Direction',]
    
CLASSES.append  ( VTKImageSinusoidSource )        
TYPENAMES.append('VTKImageSinusoidSourceType' )

#--------------------------------------------------------------
class VTKImplicitFunctionToImageStencil(Node, VTKTreeNode):

    bl_idname = 'VTKImplicitFunctionToImageStencilType'
    bl_label  = 'vtkImplicitFunctionToImageStencil'
    
    m_Threshold         = bpy.props.FloatProperty      ( name='Threshold',         default=0.0 )
    m_OutputWholeExtent = bpy.props.IntVectorProperty  ( name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6 )
    m_OutputOrigin      = bpy.props.FloatVectorProperty( name='OutputOrigin',      default=(0.0, 0.0, 0.0), size=3 )
    m_OutputSpacing     = bpy.props.FloatVectorProperty( name='OutputSpacing',     default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Threshold','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    
CLASSES.append  ( VTKImplicitFunctionToImageStencil )        
TYPENAMES.append('VTKImplicitFunctionToImageStencilType' )

#--------------------------------------------------------------
class VTKLineSource(Node, VTKTreeNode):

    bl_idname = 'VTKLineSourceType'
    bl_label  = 'vtkLineSource'
    
    m_Resolution = bpy.props.IntProperty        ( name='Resolution', default=1 )
    m_Point1     = bpy.props.FloatVectorProperty( name='Point1',     default=(-0.5, 0.0, 0.0), size=3 )
    m_Point2     = bpy.props.FloatVectorProperty( name='Point2',     default=(0.5, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Resolution','m_Point1','m_Point2',]
    
CLASSES.append  ( VTKLineSource )        
TYPENAMES.append('VTKLineSourceType' )

#--------------------------------------------------------------
class VTKPSphereSource(Node, VTKTreeNode):

    bl_idname = 'VTKPSphereSourceType'
    bl_label  = 'vtkPSphereSource'
    
    m_LatLongTessellation = bpy.props.BoolProperty       ( name='LatLongTessellation', default=0 )
    m_PhiResolution       = bpy.props.IntProperty        ( name='PhiResolution',       default=8 )
    m_ThetaResolution     = bpy.props.IntProperty        ( name='ThetaResolution',     default=8 )
    m_EndPhi              = bpy.props.FloatProperty      ( name='EndPhi',              default=180.0 )
    m_EndTheta            = bpy.props.FloatProperty      ( name='EndTheta',            default=360.0 )
    m_Radius              = bpy.props.FloatProperty      ( name='Radius',              default=0.5 )
    m_StartPhi            = bpy.props.FloatProperty      ( name='StartPhi',            default=0.0 )
    m_StartTheta          = bpy.props.FloatProperty      ( name='StartTheta',          default=0.0 )
    m_Center              = bpy.props.FloatVectorProperty( name='Center',              default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_LatLongTessellation','m_PhiResolution','m_ThetaResolution','m_EndPhi','m_EndTheta','m_Radius','m_StartPhi','m_StartTheta','m_Center',]
    
CLASSES.append  ( VTKPSphereSource )        
TYPENAMES.append('VTKPSphereSourceType' )

#--------------------------------------------------------------
class VTKParametricFunctionSource(Node, VTKTreeNode):

    bl_idname = 'VTKParametricFunctionSourceType'
    bl_label  = 'vtkParametricFunctionSource'
    e_ScalarMode_items=[ (x,x,x) for x in ['None', 'U', 'V', 'U0', 'V0', 'U0V0', 'Modulus', 'Phase', 'Quadrant', 'X', 'Y', 'Z', 'Distance', 'FunctionDefined']]
    
    m_GenerateNormals            = bpy.props.BoolProperty( name='GenerateNormals',            default=1 )
    m_GenerateTextureCoordinates = bpy.props.BoolProperty( name='GenerateTextureCoordinates', default=0 )
    m_UResolution                = bpy.props.IntProperty ( name='UResolution',                default=50 )
    m_VResolution                = bpy.props.IntProperty ( name='VResolution',                default=50 )
    m_WResolution                = bpy.props.IntProperty ( name='WResolution',                default=50 )
    e_ScalarMode                 = bpy.props.EnumProperty( name='ScalarMode',                 default="None", items=e_ScalarMode_items )
    
    def m_properties( self ):
        return ['m_GenerateNormals','m_GenerateTextureCoordinates','m_UResolution','m_VResolution','m_WResolution','e_ScalarMode',]
    
CLASSES.append  ( VTKParametricFunctionSource )        
TYPENAMES.append('VTKParametricFunctionSourceType' )

#--------------------------------------------------------------
class VTKPipelineGraphSource(Node, VTKTreeNode):

    bl_idname = 'VTKPipelineGraphSourceType'
    bl_label  = 'vtkPipelineGraphSource'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPipelineGraphSource )        
TYPENAMES.append('VTKPipelineGraphSourceType' )

#--------------------------------------------------------------
class VTKPlatonicSolidSource(Node, VTKTreeNode):

    bl_idname = 'VTKPlatonicSolidSourceType'
    bl_label  = 'vtkPlatonicSolidSource'
    e_SolidType_items=[ (x,x,x) for x in ['Tetrahedron', 'Cube', 'Octahedron', 'Icosahedron', 'Dodecahedron']]
    
    e_SolidType = bpy.props.EnumProperty( name='SolidType', default="Tetrahedron", items=e_SolidType_items )
    
    def m_properties( self ):
        return ['e_SolidType',]
    
CLASSES.append  ( VTKPlatonicSolidSource )        
TYPENAMES.append('VTKPlatonicSolidSourceType' )

#--------------------------------------------------------------
class VTKPointLoad(Node, VTKTreeNode):

    bl_idname = 'VTKPointLoadType'
    bl_label  = 'vtkPointLoad'
    
    m_ComputeEffectiveStress = bpy.props.BoolProperty       ( name='ComputeEffectiveStress', default=1 )
    m_LoadValue              = bpy.props.FloatProperty      ( name='LoadValue',              default=1.0 )
    m_PoissonsRatio          = bpy.props.FloatProperty      ( name='PoissonsRatio',          default=0.3 )
    m_SampleDimensions       = bpy.props.IntVectorProperty  ( name='SampleDimensions',       default=[50, 50, 50], size=3 )
    m_ModelBounds            = bpy.props.FloatVectorProperty( name='ModelBounds',            default=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), size=6 )
    
    def m_properties( self ):
        return ['m_ComputeEffectiveStress','m_LoadValue','m_PoissonsRatio','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKPointLoad )        
TYPENAMES.append('VTKPointLoadType' )

#--------------------------------------------------------------
class VTKPointSource(Node, VTKTreeNode):

    bl_idname = 'VTKPointSourceType'
    bl_label  = 'vtkPointSource'
    e_Distribution_items=[ (x,x,x) for x in ['Shell', 'Uniform']]
    
    m_NumberOfPoints = bpy.props.IntProperty        ( name='NumberOfPoints', default=10 )
    m_Radius         = bpy.props.FloatProperty      ( name='Radius',         default=0.5 )
    e_Distribution   = bpy.props.EnumProperty       ( name='Distribution',   default="Uniform", items=e_Distribution_items )
    m_Center         = bpy.props.FloatVectorProperty( name='Center',         default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_NumberOfPoints','m_Radius','e_Distribution','m_Center',]
    
CLASSES.append  ( VTKPointSource )        
TYPENAMES.append('VTKPointSourceType' )

#--------------------------------------------------------------
class VTKPolyLineSource(Node, VTKTreeNode):

    bl_idname = 'VTKPolyLineSourceType'
    bl_label  = 'vtkPolyLineSource'
    
    m_Closed         = bpy.props.BoolProperty( name='Closed',         default=0 )
    m_NumberOfPoints = bpy.props.IntProperty ( name='NumberOfPoints', default=0 )
    
    def m_properties( self ):
        return ['m_Closed','m_NumberOfPoints',]
    
CLASSES.append  ( VTKPolyLineSource )        
TYPENAMES.append('VTKPolyLineSourceType' )

#--------------------------------------------------------------
class VTKProgrammableDataObjectSource(Node, VTKTreeNode):

    bl_idname = 'VTKProgrammableDataObjectSourceType'
    bl_label  = 'vtkProgrammableDataObjectSource'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKProgrammableDataObjectSource )        
TYPENAMES.append('VTKProgrammableDataObjectSourceType' )

#--------------------------------------------------------------
class VTKROIStencilSource(Node, VTKTreeNode):

    bl_idname = 'VTKROIStencilSourceType'
    bl_label  = 'vtkROIStencilSource'
    e_Shape_items=[ (x,x,x) for x in ['Box', 'Ellipsoid', 'CylinderX', 'CylinderY', 'CylinderZ']]
    
    e_Shape             = bpy.props.EnumProperty       ( name='Shape',             default="Box", items=e_Shape_items )
    m_OutputWholeExtent = bpy.props.IntVectorProperty  ( name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6 )
    m_Bounds            = bpy.props.FloatVectorProperty( name='Bounds',            default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    m_OutputOrigin      = bpy.props.FloatVectorProperty( name='OutputOrigin',      default=(0.0, 0.0, 0.0), size=3 )
    m_OutputSpacing     = bpy.props.FloatVectorProperty( name='OutputSpacing',     default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['e_Shape','m_OutputWholeExtent','m_Bounds','m_OutputOrigin','m_OutputSpacing',]
    
CLASSES.append  ( VTKROIStencilSource )        
TYPENAMES.append('VTKROIStencilSourceType' )

#--------------------------------------------------------------
class VTKRTAnalyticSource(Node, VTKTreeNode):

    bl_idname = 'VTKRTAnalyticSourceType'
    bl_label  = 'vtkRTAnalyticSource'
    
    m_SubsampleRate     = bpy.props.IntProperty        ( name='SubsampleRate',     default=1 )
    m_Maximum           = bpy.props.FloatProperty      ( name='Maximum',           default=255.0 )
    m_StandardDeviation = bpy.props.FloatProperty      ( name='StandardDeviation', default=0.5 )
    m_XFreq             = bpy.props.FloatProperty      ( name='XFreq',             default=60.0 )
    m_XMag              = bpy.props.FloatProperty      ( name='XMag',              default=10.0 )
    m_YFreq             = bpy.props.FloatProperty      ( name='YFreq',             default=30.0 )
    m_YMag              = bpy.props.FloatProperty      ( name='YMag',              default=18.0 )
    m_ZFreq             = bpy.props.FloatProperty      ( name='ZFreq',             default=40.0 )
    m_ZMag              = bpy.props.FloatProperty      ( name='ZMag',              default=5.0 )
    m_Center            = bpy.props.FloatVectorProperty( name='Center',            default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_SubsampleRate','m_Maximum','m_StandardDeviation','m_XFreq','m_XMag','m_YFreq','m_YMag','m_ZFreq','m_ZMag','m_Center',]
    
CLASSES.append  ( VTKRTAnalyticSource )        
TYPENAMES.append('VTKRTAnalyticSourceType' )

#--------------------------------------------------------------
class VTKRandomGraphSource(Node, VTKTreeNode):

    bl_idname = 'VTKRandomGraphSourceType'
    bl_label  = 'vtkRandomGraphSource'
    
    m_AllowParallelEdges        = bpy.props.BoolProperty  ( name='AllowParallelEdges',        default=False )
    m_AllowSelfLoops            = bpy.props.BoolProperty  ( name='AllowSelfLoops',            default=False )
    m_Directed                  = bpy.props.BoolProperty  ( name='Directed',                  default=False )
    m_GeneratePedigreeIds       = bpy.props.BoolProperty  ( name='GeneratePedigreeIds',       default=True )
    m_IncludeEdgeWeights        = bpy.props.BoolProperty  ( name='IncludeEdgeWeights',        default=False )
    m_StartWithTree             = bpy.props.BoolProperty  ( name='StartWithTree',             default=False )
    m_UseEdgeProbability        = bpy.props.BoolProperty  ( name='UseEdgeProbability',        default=False )
    m_EdgePedigreeIdArrayName   = bpy.props.StringProperty( name='EdgePedigreeIdArrayName',   default="edge id" )
    m_EdgeWeightArrayName       = bpy.props.StringProperty( name='EdgeWeightArrayName',       default="edge weight" )
    m_VertexPedigreeIdArrayName = bpy.props.StringProperty( name='VertexPedigreeIdArrayName', default="vertex id" )
    m_NumberOfEdges             = bpy.props.IntProperty   ( name='NumberOfEdges',             default=10 )
    m_NumberOfVertices          = bpy.props.IntProperty   ( name='NumberOfVertices',          default=10 )
    m_Seed                      = bpy.props.IntProperty   ( name='Seed',                      default=1177 )
    m_EdgeProbability           = bpy.props.FloatProperty ( name='EdgeProbability',           default=0.5 )
    
    def m_properties( self ):
        return ['m_AllowParallelEdges','m_AllowSelfLoops','m_Directed','m_GeneratePedigreeIds','m_IncludeEdgeWeights','m_StartWithTree','m_UseEdgeProbability','m_EdgePedigreeIdArrayName','m_EdgeWeightArrayName','m_VertexPedigreeIdArrayName','m_NumberOfEdges','m_NumberOfVertices','m_Seed','m_EdgeProbability',]
    
CLASSES.append  ( VTKRandomGraphSource )        
TYPENAMES.append('VTKRandomGraphSourceType' )

#--------------------------------------------------------------
class VTKRectangularButtonSource(Node, VTKTreeNode):

    bl_idname = 'VTKRectangularButtonSourceType'
    bl_label  = 'vtkRectangularButtonSource'
    e_TextureStyle_items=[ (x,x,x) for x in ['FitImage', 'Proportional']]
    
    m_TwoSided                  = bpy.props.BoolProperty       ( name='TwoSided',                  default=0 )
    m_BoxRatio                  = bpy.props.FloatProperty      ( name='BoxRatio',                  default=1.1 )
    m_Depth                     = bpy.props.FloatProperty      ( name='Depth',                     default=0.05 )
    m_Height                    = bpy.props.FloatProperty      ( name='Height',                    default=0.5 )
    m_TextureHeightRatio        = bpy.props.FloatProperty      ( name='TextureHeightRatio',        default=0.95 )
    m_TextureRatio              = bpy.props.FloatProperty      ( name='TextureRatio',              default=0.9 )
    m_Width                     = bpy.props.FloatProperty      ( name='Width',                     default=0.5 )
    e_TextureStyle              = bpy.props.EnumProperty       ( name='TextureStyle',              default="Proportional", items=e_TextureStyle_items )
    m_TextureDimensions         = bpy.props.IntVectorProperty  ( name='TextureDimensions',         default=[100, 100], size=2 )
    m_Center                    = bpy.props.FloatVectorProperty( name='Center',                    default=(0.0, 0.0, 0.0), size=3 )
    m_ShoulderTextureCoordinate = bpy.props.FloatVectorProperty( name='ShoulderTextureCoordinate', default=(0.0, 0.0), size=2 )
    
    def m_properties( self ):
        return ['m_TwoSided','m_BoxRatio','m_Depth','m_Height','m_TextureHeightRatio','m_TextureRatio','m_Width','e_TextureStyle','m_TextureDimensions','m_Center','m_ShoulderTextureCoordinate',]
    
CLASSES.append  ( VTKRectangularButtonSource )        
TYPENAMES.append('VTKRectangularButtonSourceType' )

#--------------------------------------------------------------
class VTKRegularPolygonSource(Node, VTKTreeNode):

    bl_idname = 'VTKRegularPolygonSourceType'
    bl_label  = 'vtkRegularPolygonSource'
    
    m_GeneratePolygon  = bpy.props.BoolProperty       ( name='GeneratePolygon',  default=1 )
    m_GeneratePolyline = bpy.props.BoolProperty       ( name='GeneratePolyline', default=1 )
    m_NumberOfSides    = bpy.props.IntProperty        ( name='NumberOfSides',    default=6 )
    m_Radius           = bpy.props.FloatProperty      ( name='Radius',           default=0.5 )
    m_Center           = bpy.props.FloatVectorProperty( name='Center',           default=(0.0, 0.0, 0.0), size=3 )
    m_Normal           = bpy.props.FloatVectorProperty( name='Normal',           default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_GeneratePolygon','m_GeneratePolyline','m_NumberOfSides','m_Radius','m_Center','m_Normal',]
    
CLASSES.append  ( VTKRegularPolygonSource )        
TYPENAMES.append('VTKRegularPolygonSourceType' )

#--------------------------------------------------------------
class VTKRenderLargeImage(Node, VTKTreeNode):

    bl_idname = 'VTKRenderLargeImageType'
    bl_label  = 'vtkRenderLargeImage'
    
    m_Magnification = bpy.props.IntProperty( name='Magnification', default=3 )
    
    def m_properties( self ):
        return ['m_Magnification',]
    
CLASSES.append  ( VTKRenderLargeImage )        
TYPENAMES.append('VTKRenderLargeImageType' )

#--------------------------------------------------------------
class VTKRendererSource(Node, VTKTreeNode):

    bl_idname = 'VTKRendererSourceType'
    bl_label  = 'vtkRendererSource'
    
    m_DepthValues          = bpy.props.BoolProperty( name='DepthValues',          default=0 )
    m_DepthValuesInScalars = bpy.props.BoolProperty( name='DepthValuesInScalars', default=0 )
    m_DepthValuesOnly      = bpy.props.BoolProperty( name='DepthValuesOnly',      default=0 )
    m_RenderFlag           = bpy.props.BoolProperty( name='RenderFlag',           default=0 )
    m_WholeWindow          = bpy.props.BoolProperty( name='WholeWindow',          default=0 )
    
    def m_properties( self ):
        return ['m_DepthValues','m_DepthValuesInScalars','m_DepthValuesOnly','m_RenderFlag','m_WholeWindow',]
    
CLASSES.append  ( VTKRendererSource )        
TYPENAMES.append('VTKRendererSourceType' )

#--------------------------------------------------------------
class VTKRowQueryToTable(Node, VTKTreeNode):

    bl_idname = 'VTKRowQueryToTableType'
    bl_label  = 'vtkRowQueryToTable'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKRowQueryToTable )        
TYPENAMES.append('VTKRowQueryToTableType' )

#--------------------------------------------------------------
class VTKSQLDatabaseTableSource(Node, VTKTreeNode):

    bl_idname = 'VTKSQLDatabaseTableSourceType'
    bl_label  = 'vtkSQLDatabaseTableSource'
    
    m_GeneratePedigreeIds = bpy.props.BoolProperty  ( name='GeneratePedigreeIds', default=True )
    m_PedigreeIdArrayName = bpy.props.StringProperty( name='PedigreeIdArrayName', default="id" )
    m_Query               = bpy.props.StringProperty( name='Query',               default="" )
    m_URL                 = bpy.props.StringProperty( name='URL',                 default="" )
    
    def m_properties( self ):
        return ['m_GeneratePedigreeIds','m_PedigreeIdArrayName','m_Query','m_URL',]
    
CLASSES.append  ( VTKSQLDatabaseTableSource )        
TYPENAMES.append('VTKSQLDatabaseTableSourceType' )

#--------------------------------------------------------------
class VTKSectorSource(Node, VTKTreeNode):

    bl_idname = 'VTKSectorSourceType'
    bl_label  = 'vtkSectorSource'
    
    m_CircumferentialResolution = bpy.props.IntProperty  ( name='CircumferentialResolution', default=6 )
    m_RadialResolution          = bpy.props.IntProperty  ( name='RadialResolution',          default=1 )
    m_EndAngle                  = bpy.props.FloatProperty( name='EndAngle',                  default=90.0 )
    m_InnerRadius               = bpy.props.FloatProperty( name='InnerRadius',               default=1.0 )
    m_OuterRadius               = bpy.props.FloatProperty( name='OuterRadius',               default=2.0 )
    m_StartAngle                = bpy.props.FloatProperty( name='StartAngle',                default=0.0 )
    m_ZCoord                    = bpy.props.FloatProperty( name='ZCoord',                    default=0.0 )
    
    def m_properties( self ):
        return ['m_CircumferentialResolution','m_RadialResolution','m_EndAngle','m_InnerRadius','m_OuterRadius','m_StartAngle','m_ZCoord',]
    
CLASSES.append  ( VTKSectorSource )        
TYPENAMES.append('VTKSectorSourceType' )

#--------------------------------------------------------------
class VTKSelectionSource(Node, VTKTreeNode):

    bl_idname = 'VTKSelectionSourceType'
    bl_label  = 'vtkSelectionSource'
    
    m_ArrayName         = bpy.props.StringProperty( name='ArrayName',         default="" )
    m_QueryString       = bpy.props.StringProperty( name='QueryString',       default="" )
    m_ArrayComponent    = bpy.props.IntProperty   ( name='ArrayComponent',    default=0 )
    m_CompositeIndex    = bpy.props.IntProperty   ( name='CompositeIndex',    default=-1 )
    m_ContainingCells   = bpy.props.IntProperty   ( name='ContainingCells',   default=1 )
    m_ContentType       = bpy.props.IntProperty   ( name='ContentType',       default=4 )
    m_FieldType         = bpy.props.IntProperty   ( name='FieldType',         default=0 )
    m_HierarchicalIndex = bpy.props.IntProperty   ( name='HierarchicalIndex', default=-1 )
    m_HierarchicalLevel = bpy.props.IntProperty   ( name='HierarchicalLevel', default=-1 )
    m_Inverse           = bpy.props.IntProperty   ( name='Inverse',           default=0 )
    
    def m_properties( self ):
        return ['m_ArrayName','m_QueryString','m_ArrayComponent','m_CompositeIndex','m_ContainingCells','m_ContentType','m_FieldType','m_HierarchicalIndex','m_HierarchicalLevel','m_Inverse',]
    
CLASSES.append  ( VTKSelectionSource )        
TYPENAMES.append('VTKSelectionSourceType' )

#--------------------------------------------------------------
class VTKSpherePuzzle(Node, VTKTreeNode):

    bl_idname = 'VTKSpherePuzzleType'
    bl_label  = 'vtkSpherePuzzle'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKSpherePuzzle )        
TYPENAMES.append('VTKSpherePuzzleType' )

#--------------------------------------------------------------
class VTKSphereSource(Node, VTKTreeNode):

    bl_idname = 'VTKSphereSourceType'
    bl_label  = 'vtkSphereSource'
    
    m_LatLongTessellation = bpy.props.BoolProperty       ( name='LatLongTessellation', default=0 )
    m_PhiResolution       = bpy.props.IntProperty        ( name='PhiResolution',       default=8 )
    m_ThetaResolution     = bpy.props.IntProperty        ( name='ThetaResolution',     default=8 )
    m_EndPhi              = bpy.props.FloatProperty      ( name='EndPhi',              default=180.0 )
    m_EndTheta            = bpy.props.FloatProperty      ( name='EndTheta',            default=360.0 )
    m_Radius              = bpy.props.FloatProperty      ( name='Radius',              default=0.5 )
    m_StartPhi            = bpy.props.FloatProperty      ( name='StartPhi',            default=0.0 )
    m_StartTheta          = bpy.props.FloatProperty      ( name='StartTheta',          default=0.0 )
    m_Center              = bpy.props.FloatVectorProperty( name='Center',              default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_LatLongTessellation','m_PhiResolution','m_ThetaResolution','m_EndPhi','m_EndTheta','m_Radius','m_StartPhi','m_StartTheta','m_Center',]
    
CLASSES.append  ( VTKSphereSource )        
TYPENAMES.append('VTKSphereSourceType' )

#--------------------------------------------------------------
class VTKSuperquadricSource(Node, VTKTreeNode):

    bl_idname = 'VTKSuperquadricSourceType'
    bl_label  = 'vtkSuperquadricSource'
    
    m_Toroidal        = bpy.props.BoolProperty       ( name='Toroidal',        default=0 )
    m_AxisOfSymmetry  = bpy.props.IntProperty        ( name='AxisOfSymmetry',  default=1 )
    m_PhiResolution   = bpy.props.IntProperty        ( name='PhiResolution',   default=16 )
    m_ThetaResolution = bpy.props.IntProperty        ( name='ThetaResolution', default=16 )
    m_PhiRoundness    = bpy.props.FloatProperty      ( name='PhiRoundness',    default=1.0 )
    m_Size            = bpy.props.FloatProperty      ( name='Size',            default=0.5 )
    m_ThetaRoundness  = bpy.props.FloatProperty      ( name='ThetaRoundness',  default=1.0 )
    m_Thickness       = bpy.props.FloatProperty      ( name='Thickness',       default=0.3333 )
    m_Center          = bpy.props.FloatVectorProperty( name='Center',          default=(0.0, 0.0, 0.0), size=3 )
    m_Scale           = bpy.props.FloatVectorProperty( name='Scale',           default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Toroidal','m_AxisOfSymmetry','m_PhiResolution','m_ThetaResolution','m_PhiRoundness','m_Size','m_ThetaRoundness','m_Thickness','m_Center','m_Scale',]
    
CLASSES.append  ( VTKSuperquadricSource )        
TYPENAMES.append('VTKSuperquadricSourceType' )

#--------------------------------------------------------------
class VTKTemporalFractal(Node, VTKTreeNode):

    bl_idname = 'VTKTemporalFractalType'
    bl_label  = 'vtkTemporalFractal'
    
    m_AdaptiveSubdivision      = bpy.props.BoolProperty ( name='AdaptiveSubdivision',      default=1 )
    m_DiscreteTimeSteps        = bpy.props.BoolProperty ( name='DiscreteTimeSteps',        default=0 )
    m_GenerateRectilinearGrids = bpy.props.BoolProperty ( name='GenerateRectilinearGrids', default=0 )
    m_GhostLevels              = bpy.props.BoolProperty ( name='GhostLevels',              default=0 )
    m_TwoDimensional           = bpy.props.BoolProperty ( name='TwoDimensional',           default=1 )
    m_Asymetric                = bpy.props.IntProperty  ( name='Asymetric',                default=1 )
    m_Dimensions               = bpy.props.IntProperty  ( name='Dimensions',               default=10 )
    m_MaximumLevel             = bpy.props.IntProperty  ( name='MaximumLevel',             default=6 )
    m_FractalValue             = bpy.props.FloatProperty( name='FractalValue',             default=9.5 )
    
    def m_properties( self ):
        return ['m_AdaptiveSubdivision','m_DiscreteTimeSteps','m_GenerateRectilinearGrids','m_GhostLevels','m_TwoDimensional','m_Asymetric','m_Dimensions','m_MaximumLevel','m_FractalValue',]
    
CLASSES.append  ( VTKTemporalFractal )        
TYPENAMES.append('VTKTemporalFractalType' )

#--------------------------------------------------------------
class VTKTessellatedBoxSource(Node, VTKTreeNode):

    bl_idname = 'VTKTessellatedBoxSourceType'
    bl_label  = 'vtkTessellatedBoxSource'
    
    m_DuplicateSharedPoints = bpy.props.BoolProperty       ( name='DuplicateSharedPoints', default=0 )
    m_Quads                 = bpy.props.BoolProperty       ( name='Quads',                 default=0 )
    m_Level                 = bpy.props.IntProperty        ( name='Level',                 default=0 )
    m_Bounds                = bpy.props.FloatVectorProperty( name='Bounds',                default=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), size=6 )
    
    def m_properties( self ):
        return ['m_DuplicateSharedPoints','m_Quads','m_Level','m_Bounds',]
    
CLASSES.append  ( VTKTessellatedBoxSource )        
TYPENAMES.append('VTKTessellatedBoxSourceType' )

#--------------------------------------------------------------
class VTKTextSource(Node, VTKTreeNode):

    bl_idname = 'VTKTextSourceType'
    bl_label  = 'vtkTextSource'
    
    m_Backing         = bpy.props.BoolProperty       ( name='Backing',         default=1 )
    m_Text            = bpy.props.StringProperty     ( name='Text',            default="" )
    m_BackgroundColor = bpy.props.FloatVectorProperty( name='BackgroundColor', default=(0.0, 0.0, 0.0), size=3 )
    m_ForegroundColor = bpy.props.FloatVectorProperty( name='ForegroundColor', default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Backing','m_Text','m_BackgroundColor','m_ForegroundColor',]
    
CLASSES.append  ( VTKTextSource )        
TYPENAMES.append('VTKTextSourceType' )

#--------------------------------------------------------------
class VTKTexturedSphereSource(Node, VTKTreeNode):

    bl_idname = 'VTKTexturedSphereSourceType'
    bl_label  = 'vtkTexturedSphereSource'
    
    m_PhiResolution   = bpy.props.IntProperty  ( name='PhiResolution',   default=8 )
    m_ThetaResolution = bpy.props.IntProperty  ( name='ThetaResolution', default=8 )
    m_Phi             = bpy.props.FloatProperty( name='Phi',             default=0.0 )
    m_Radius          = bpy.props.FloatProperty( name='Radius',          default=0.5 )
    m_Theta           = bpy.props.FloatProperty( name='Theta',           default=0.0 )
    
    def m_properties( self ):
        return ['m_PhiResolution','m_ThetaResolution','m_Phi','m_Radius','m_Theta',]
    
CLASSES.append  ( VTKTexturedSphereSource )        
TYPENAMES.append('VTKTexturedSphereSourceType' )

#--------------------------------------------------------------
class VTKTimeSourceExample(Node, VTKTreeNode):

    bl_idname = 'VTKTimeSourceExampleType'
    bl_label  = 'vtkTimeSourceExample'
    
    m_Analytic   = bpy.props.BoolProperty ( name='Analytic',   default=0 )
    m_Growing    = bpy.props.BoolProperty ( name='Growing',    default=0 )
    m_XAmplitude = bpy.props.FloatProperty( name='XAmplitude', default=0.0 )
    m_YAmplitude = bpy.props.FloatProperty( name='YAmplitude', default=0.0 )
    
    def m_properties( self ):
        return ['m_Analytic','m_Growing','m_XAmplitude','m_YAmplitude',]
    
CLASSES.append  ( VTKTimeSourceExample )        
TYPENAMES.append('VTKTimeSourceExampleType' )

#--------------------------------------------------------------
class VTKTransformToGrid(Node, VTKTreeNode):

    bl_idname = 'VTKTransformToGridType'
    bl_label  = 'vtkTransformToGrid'
    e_GridScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Float', 'Double']]
    
    e_GridScalarType = bpy.props.EnumProperty       ( name='GridScalarType', default="Float", items=e_GridScalarType_items )
    m_GridExtent     = bpy.props.IntVectorProperty  ( name='GridExtent',     default=[0, 0, 0, 0, 0, 0], size=6 )
    m_GridOrigin     = bpy.props.FloatVectorProperty( name='GridOrigin',     default=(0.0, 0.0, 0.0), size=3 )
    m_GridSpacing    = bpy.props.FloatVectorProperty( name='GridSpacing',    default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['e_GridScalarType','m_GridExtent','m_GridOrigin','m_GridSpacing',]
    
CLASSES.append  ( VTKTransformToGrid )        
TYPENAMES.append('VTKTransformToGridType' )

#--------------------------------------------------------------
class VTKTriangularTexture(Node, VTKTreeNode):

    bl_idname = 'VTKTriangularTextureType'
    bl_label  = 'vtkTriangularTexture'
    
    m_TexturePattern = bpy.props.IntProperty  ( name='TexturePattern', default=1 )
    m_XSize          = bpy.props.IntProperty  ( name='XSize',          default=64 )
    m_YSize          = bpy.props.IntProperty  ( name='YSize',          default=64 )
    m_ScaleFactor    = bpy.props.FloatProperty( name='ScaleFactor',    default=1.0 )
    
    def m_properties( self ):
        return ['m_TexturePattern','m_XSize','m_YSize','m_ScaleFactor',]
    
CLASSES.append  ( VTKTriangularTexture )        
TYPENAMES.append('VTKTriangularTextureType' )

#--------------------------------------------------------------
class VTKTrivialProducer(Node, VTKTreeNode):

    bl_idname = 'VTKTrivialProducerType'
    bl_label  = 'vtkTrivialProducer'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTrivialProducer )        
TYPENAMES.append('VTKTrivialProducerType' )

#--------------------------------------------------------------
class VTKVectorText(Node, VTKTreeNode):

    bl_idname = 'VTKVectorTextType'
    bl_label  = 'vtkVectorText'
    
    m_Text = bpy.props.StringProperty( name='Text', default="" )
    
    def m_properties( self ):
        return ['m_Text',]
    
CLASSES.append  ( VTKVectorText )        
TYPENAMES.append('VTKVectorTextType' )

#--------------------------------------------------------------
class VTKVolumeOutlineSource(Node, VTKTreeNode):

    bl_idname = 'VTKVolumeOutlineSourceType'
    bl_label  = 'vtkVolumeOutlineSource'
    
    m_GenerateFaces    = bpy.props.BoolProperty       ( name='GenerateFaces',    default=0 )
    m_GenerateOutline  = bpy.props.BoolProperty       ( name='GenerateOutline',  default=1 )
    m_GenerateScalars  = bpy.props.BoolProperty       ( name='GenerateScalars',  default=0 )
    m_ActivePlaneId    = bpy.props.IntProperty        ( name='ActivePlaneId',    default=-1 )
    m_ActivePlaneColor = bpy.props.FloatVectorProperty( name='ActivePlaneColor', default=(1.0, 1.0, 0.0), size=3 )
    m_Color            = bpy.props.FloatVectorProperty( name='Color',            default=(1.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_GenerateFaces','m_GenerateOutline','m_GenerateScalars','m_ActivePlaneId','m_ActivePlaneColor','m_Color',]
    
CLASSES.append  ( VTKVolumeOutlineSource )        
TYPENAMES.append('VTKVolumeOutlineSourceType' )

#--------------------------------------------------------------
class VTKWindowToImageFilter(Node, VTKTreeNode):

    bl_idname = 'VTKWindowToImageFilterType'
    bl_label  = 'vtkWindowToImageFilter'
    e_InputBufferType_items=[ (x,x,x) for x in ['RGB', 'RGBA', 'ZBuffer']]
    
    m_FixBoundary     = bpy.props.BoolProperty       ( name='FixBoundary',     default=False )
    m_ReadFrontBuffer = bpy.props.BoolProperty       ( name='ReadFrontBuffer', default=1 )
    m_ShouldRerender  = bpy.props.BoolProperty       ( name='ShouldRerender',  default=1 )
    m_Magnification   = bpy.props.IntProperty        ( name='Magnification',   default=1 )
    e_InputBufferType = bpy.props.EnumProperty       ( name='InputBufferType', default="RGB", items=e_InputBufferType_items )
    m_Viewport        = bpy.props.FloatVectorProperty( name='Viewport',        default=(0.0, 0.0, 1.0, 1.0), size=4 )
    
    def m_properties( self ):
        return ['m_FixBoundary','m_ReadFrontBuffer','m_ShouldRerender','m_Magnification','e_InputBufferType','m_Viewport',]
    
CLASSES.append  ( VTKWindowToImageFilter )        
TYPENAMES.append('VTKWindowToImageFilterType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( 'source', 'source', items=menu_items) )