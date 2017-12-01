from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAMRResampleFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAMRResampleFilterType'
    bl_label  = 'vtkAMRResampleFilter'
    
    m_UseBiasVector      = bpy.props.BoolProperty       ( name='UseBiasVector',      default=False )
    m_DemandDrivenMode   = bpy.props.IntProperty        ( name='DemandDrivenMode',   default=0 )
    m_NumberOfPartitions = bpy.props.IntProperty        ( name='NumberOfPartitions', default=1 )
    m_TransferToNodes    = bpy.props.IntProperty        ( name='TransferToNodes',    default=1 )
    m_NumberOfSamples    = bpy.props.IntVectorProperty  ( name='NumberOfSamples',    default=[10, 10, 10], size=3 )
    m_BiasVector         = bpy.props.FloatVectorProperty( name='BiasVector',         default=(0.0, 0.0, 0.0), size=3 )
    m_Max                = bpy.props.FloatVectorProperty( name='Max',                default=(1.0, 1.0, 1.0), size=3 )
    m_Min                = bpy.props.FloatVectorProperty( name='Min',                default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_UseBiasVector','m_DemandDrivenMode','m_NumberOfPartitions','m_TransferToNodes','m_NumberOfSamples','m_BiasVector','m_Max','m_Min',]
    
CLASSES.append  ( VTKAMRResampleFilter )        
TYPENAMES.append('VTKAMRResampleFilterType' )

#--------------------------------------------------------------
class VTKAMRSliceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAMRSliceFilterType'
    bl_label  = 'vtkAMRSliceFilter'
    
    m_EnablePrefetching = bpy.props.BoolProperty ( name='EnablePrefetching', default=1 )
    m_ForwardUpstream   = bpy.props.BoolProperty ( name='ForwardUpstream',   default=1 )
    m_MaxResolution     = bpy.props.IntProperty  ( name='MaxResolution',     default=1 )
    m_Normal            = bpy.props.IntProperty  ( name='Normal',            default=1 )
    m_OffSetFromOrigin  = bpy.props.FloatProperty( name='OffSetFromOrigin',  default=0.0 )
    
    def m_properties( self ):
        return ['m_EnablePrefetching','m_ForwardUpstream','m_MaxResolution','m_Normal','m_OffSetFromOrigin',]
    
CLASSES.append  ( VTKAMRSliceFilter )        
TYPENAMES.append('VTKAMRSliceFilterType' )

#--------------------------------------------------------------
class VTKAMRToMultiBlockFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAMRToMultiBlockFilterType'
    bl_label  = 'vtkAMRToMultiBlockFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKAMRToMultiBlockFilter )        
TYPENAMES.append('VTKAMRToMultiBlockFilterType' )

#--------------------------------------------------------------
class VTKAdaptiveSubdivisionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAdaptiveSubdivisionFilterType'
    bl_label  = 'vtkAdaptiveSubdivisionFilter'
    
    m_MaximumNumberOfPasses    = bpy.props.IntProperty  ( name='MaximumNumberOfPasses',    default=0 )
    m_MaximumNumberOfTriangles = bpy.props.IntProperty  ( name='MaximumNumberOfTriangles', default=0 )
    m_MaximumEdgeLength        = bpy.props.FloatProperty( name='MaximumEdgeLength',        default=1.0 )
    m_MaximumTriangleArea      = bpy.props.FloatProperty( name='MaximumTriangleArea',      default=1.0 )
    
    def m_properties( self ):
        return ['m_MaximumNumberOfPasses','m_MaximumNumberOfTriangles','m_MaximumEdgeLength','m_MaximumTriangleArea',]
    
CLASSES.append  ( VTKAdaptiveSubdivisionFilter )        
TYPENAMES.append('VTKAdaptiveSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKAdjacencyMatrixToEdgeTable(Node, VTKFilter1Node):

    bl_idname = 'VTKAdjacencyMatrixToEdgeTableType'
    bl_label  = 'vtkAdjacencyMatrixToEdgeTable'
    
    m_ValueArrayName   = bpy.props.StringProperty( name='ValueArrayName',   default="value" )
    m_MinimumCount     = bpy.props.IntProperty   ( name='MinimumCount',     default=0 )
    m_SourceDimension  = bpy.props.IntProperty   ( name='SourceDimension',  default=0 )
    m_MinimumThreshold = bpy.props.FloatProperty ( name='MinimumThreshold', default=0.5 )
    
    def m_properties( self ):
        return ['m_ValueArrayName','m_MinimumCount','m_SourceDimension','m_MinimumThreshold',]
    
CLASSES.append  ( VTKAdjacencyMatrixToEdgeTable )        
TYPENAMES.append('VTKAdjacencyMatrixToEdgeTableType' )

#--------------------------------------------------------------
class VTKAggregateDataSetFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAggregateDataSetFilterType'
    bl_label  = 'vtkAggregateDataSetFilter'
    
    m_NumberOfTargetProcesses = bpy.props.IntProperty( name='NumberOfTargetProcesses', default=1 )
    
    def m_properties( self ):
        return ['m_NumberOfTargetProcesses',]
    
CLASSES.append  ( VTKAggregateDataSetFilter )        
TYPENAMES.append('VTKAggregateDataSetFilterType' )

#--------------------------------------------------------------
class VTKAngularPeriodicFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAngularPeriodicFilterType'
    bl_label  = 'vtkAngularPeriodicFilter'
    e_IterationMode_items=[ (x,x,x) for x in ['DirectNb', 'Max']]
    e_RotationAxis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    e_RotationMode_items=[ (x,x,x) for x in ['DirectAngle', 'ArrayValue']]
    
    m_ComputeRotationsOnTheFly = bpy.props.BoolProperty       ( name='ComputeRotationsOnTheFly', default=True )
    m_RotationArrayName        = bpy.props.StringProperty     ( name='RotationArrayName',        default="" )
    m_NumberOfPeriods          = bpy.props.IntProperty        ( name='NumberOfPeriods',          default=1 )
    m_RotationAngle            = bpy.props.FloatProperty      ( name='RotationAngle',            default=180.0 )
    e_IterationMode            = bpy.props.EnumProperty       ( name='IterationMode',            default="Max", items=e_IterationMode_items )
    e_RotationAxis             = bpy.props.EnumProperty       ( name='RotationAxis',             default="X", items=e_RotationAxis_items )
    e_RotationMode             = bpy.props.EnumProperty       ( name='RotationMode',             default="DirectAngle", items=e_RotationMode_items )
    m_Center                   = bpy.props.FloatVectorProperty( name='Center',                   default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_ComputeRotationsOnTheFly','m_RotationArrayName','m_NumberOfPeriods','m_RotationAngle','e_IterationMode','e_RotationAxis','e_RotationMode','m_Center',]
    
CLASSES.append  ( VTKAngularPeriodicFilter )        
TYPENAMES.append('VTKAngularPeriodicFilterType' )

#--------------------------------------------------------------
class VTKAnnotationLayersAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKAnnotationLayersAlgorithmType'
    bl_label  = 'vtkAnnotationLayersAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKAnnotationLayersAlgorithm )        
TYPENAMES.append('VTKAnnotationLayersAlgorithmType' )

#--------------------------------------------------------------
class VTKAppendArcLength(Node, VTKFilter1Node):

    bl_idname = 'VTKAppendArcLengthType'
    bl_label  = 'vtkAppendArcLength'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKAppendArcLength )        
TYPENAMES.append('VTKAppendArcLengthType' )

#--------------------------------------------------------------
class VTKAppendCompositeDataLeaves(Node, VTKFilter1Node):

    bl_idname = 'VTKAppendCompositeDataLeavesType'
    bl_label  = 'vtkAppendCompositeDataLeaves'
    
    m_AppendFieldData = bpy.props.BoolProperty( name='AppendFieldData', default=0 )
    
    def m_properties( self ):
        return ['m_AppendFieldData',]
    
CLASSES.append  ( VTKAppendCompositeDataLeaves )        
TYPENAMES.append('VTKAppendCompositeDataLeavesType' )

#--------------------------------------------------------------
class VTKAppendFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAppendFilterType'
    bl_label  = 'vtkAppendFilter'
    
    m_MergePoints = bpy.props.BoolProperty( name='MergePoints', default=0 )
    
    def m_properties( self ):
        return ['m_MergePoints',]
    
CLASSES.append  ( VTKAppendFilter )        
TYPENAMES.append('VTKAppendFilterType' )

#--------------------------------------------------------------
class VTKAppendPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKAppendPointsType'
    bl_label  = 'vtkAppendPoints'
    
    m_InputIdArrayName = bpy.props.StringProperty( name='InputIdArrayName', default="" )
    
    def m_properties( self ):
        return ['m_InputIdArrayName',]
    
CLASSES.append  ( VTKAppendPoints )        
TYPENAMES.append('VTKAppendPointsType' )

#--------------------------------------------------------------
class VTKAppendPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKAppendPolyDataType'
    bl_label  = 'vtkAppendPolyData'
    
    m_ParallelStreaming = bpy.props.BoolProperty( name='ParallelStreaming', default=0 )
    m_UserManagedInputs = bpy.props.BoolProperty( name='UserManagedInputs', default=0 )
    
    def m_properties( self ):
        return ['m_ParallelStreaming','m_UserManagedInputs',]
    
CLASSES.append  ( VTKAppendPolyData )        
TYPENAMES.append('VTKAppendPolyDataType' )

#--------------------------------------------------------------
class VTKAppendSelection(Node, VTKFilter1Node):

    bl_idname = 'VTKAppendSelectionType'
    bl_label  = 'vtkAppendSelection'
    
    m_AppendByUnion     = bpy.props.BoolProperty( name='AppendByUnion',     default=1 )
    m_UserManagedInputs = bpy.props.BoolProperty( name='UserManagedInputs', default=0 )
    
    def m_properties( self ):
        return ['m_AppendByUnion','m_UserManagedInputs',]
    
CLASSES.append  ( VTKAppendSelection )        
TYPENAMES.append('VTKAppendSelectionType' )

#--------------------------------------------------------------
class VTKArcPlotter(Node, VTKFilter1Node):

    bl_idname = 'VTKArcPlotterType'
    bl_label  = 'vtkArcPlotter'
    e_PlotMode_items=[ (x,x,x) for x in ['PlotScalars', 'PlotVectors', 'PlotNormals', 'PlotTCoords', 'PlotTensors', 'PlotFieldData']]
    
    m_UseDefaultNormal = bpy.props.BoolProperty       ( name='UseDefaultNormal', default=0 )
    m_FieldDataArray   = bpy.props.IntProperty        ( name='FieldDataArray',   default=0 )
    m_PlotComponent    = bpy.props.IntProperty        ( name='PlotComponent',    default=-1 )
    m_Height           = bpy.props.FloatProperty      ( name='Height',           default=0.5 )
    m_Offset           = bpy.props.FloatProperty      ( name='Offset',           default=0.0 )
    m_Radius           = bpy.props.FloatProperty      ( name='Radius',           default=0.5 )
    e_PlotMode         = bpy.props.EnumProperty       ( name='PlotMode',         default="PlotScalars", items=e_PlotMode_items )
    m_DefaultNormal    = bpy.props.FloatVectorProperty( name='DefaultNormal',    default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_UseDefaultNormal','m_FieldDataArray','m_PlotComponent','m_Height','m_Offset','m_Radius','e_PlotMode','m_DefaultNormal',]
    
CLASSES.append  ( VTKArcPlotter )        
TYPENAMES.append('VTKArcPlotterType' )

#--------------------------------------------------------------
class VTKArrayCalculator(Node, VTKFilter1Node):

    bl_idname = 'VTKArrayCalculatorType'
    bl_label  = 'vtkArrayCalculator'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData', 'UseVertexData', 'UseEdgeData']]
    
    m_CoordinateResults    = bpy.props.BoolProperty  ( name='CoordinateResults',    default=0 )
    m_ReplaceInvalidValues = bpy.props.BoolProperty  ( name='ReplaceInvalidValues', default=0 )
    m_ResultNormals        = bpy.props.BoolProperty  ( name='ResultNormals',        default=False )
    m_ResultTCoords        = bpy.props.BoolProperty  ( name='ResultTCoords',        default=False )
    m_Function             = bpy.props.StringProperty( name='Function',             default="" )
    m_ResultArrayName      = bpy.props.StringProperty( name='ResultArrayName',      default="resultArray" )
    m_ResultArrayType      = bpy.props.IntProperty   ( name='ResultArrayType',      default=11 )
    m_ReplacementValue     = bpy.props.FloatProperty ( name='ReplacementValue',     default=0.0 )
    e_AttributeMode        = bpy.props.EnumProperty  ( name='AttributeMode',        default="Default", items=e_AttributeMode_items )
    
    def m_properties( self ):
        return ['m_CoordinateResults','m_ReplaceInvalidValues','m_ResultNormals','m_ResultTCoords','m_Function','m_ResultArrayName','m_ResultArrayType','m_ReplacementValue','e_AttributeMode',]
    
CLASSES.append  ( VTKArrayCalculator )        
TYPENAMES.append('VTKArrayCalculatorType' )

#--------------------------------------------------------------
class VTKArrayDataAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKArrayDataAlgorithmType'
    bl_label  = 'vtkArrayDataAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKArrayDataAlgorithm )        
TYPENAMES.append('VTKArrayDataAlgorithmType' )

#--------------------------------------------------------------
class VTKArrayNorm(Node, VTKFilter1Node):

    bl_idname = 'VTKArrayNormType'
    bl_label  = 'vtkArrayNorm'
    
    m_Dimension = bpy.props.IntProperty( name='Dimension', default=0 )
    m_Invert    = bpy.props.IntProperty( name='Invert',    default=0 )
    m_L         = bpy.props.IntProperty( name='L',         default=2 )
    
    def m_properties( self ):
        return ['m_Dimension','m_Invert','m_L',]
    
CLASSES.append  ( VTKArrayNorm )        
TYPENAMES.append('VTKArrayNormType' )

#--------------------------------------------------------------
class VTKArrayToTable(Node, VTKFilter1Node):

    bl_idname = 'VTKArrayToTableType'
    bl_label  = 'vtkArrayToTable'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKArrayToTable )        
TYPENAMES.append('VTKArrayToTableType' )

#--------------------------------------------------------------
class VTKAssignAttribute(Node, VTKFilter1Node):

    bl_idname = 'VTKAssignAttributeType'
    bl_label  = 'vtkAssignAttribute'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKAssignAttribute )        
TYPENAMES.append('VTKAssignAttributeType' )

#--------------------------------------------------------------
class VTKAssignCoordinates(Node, VTKFilter1Node):

    bl_idname = 'VTKAssignCoordinatesType'
    bl_label  = 'vtkAssignCoordinates'
    
    m_XCoordArrayName = bpy.props.StringProperty( name='XCoordArrayName', default="" )
    m_YCoordArrayName = bpy.props.StringProperty( name='YCoordArrayName', default="" )
    m_ZCoordArrayName = bpy.props.StringProperty( name='ZCoordArrayName', default="" )
    
    def m_properties( self ):
        return ['m_XCoordArrayName','m_YCoordArrayName','m_ZCoordArrayName',]
    
CLASSES.append  ( VTKAssignCoordinates )        
TYPENAMES.append('VTKAssignCoordinatesType' )

#--------------------------------------------------------------
class VTKAttributeDataToFieldDataFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKAttributeDataToFieldDataFilterType'
    bl_label  = 'vtkAttributeDataToFieldDataFilter'
    
    m_PassAttributeData = bpy.props.BoolProperty( name='PassAttributeData', default=1 )
    
    def m_properties( self ):
        return ['m_PassAttributeData',]
    
CLASSES.append  ( VTKAttributeDataToFieldDataFilter )        
TYPENAMES.append('VTKAttributeDataToFieldDataFilterType' )

#--------------------------------------------------------------
class VTKBlankStructuredGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKBlankStructuredGridType'
    bl_label  = 'vtkBlankStructuredGrid'
    
    m_ArrayName        = bpy.props.StringProperty( name='ArrayName',        default="" )
    m_ArrayId          = bpy.props.IntProperty   ( name='ArrayId',          default=-1 )
    m_Component        = bpy.props.IntProperty   ( name='Component',        default=0 )
    m_MaxBlankingValue = bpy.props.FloatProperty ( name='MaxBlankingValue', default=9.999999680285692e+37 )
    m_MinBlankingValue = bpy.props.FloatProperty ( name='MinBlankingValue', default=9.999999680285692e+37 )
    
    def m_properties( self ):
        return ['m_ArrayName','m_ArrayId','m_Component','m_MaxBlankingValue','m_MinBlankingValue',]
    
CLASSES.append  ( VTKBlankStructuredGrid )        
TYPENAMES.append('VTKBlankStructuredGridType' )

#--------------------------------------------------------------
class VTKBlockIdScalars(Node, VTKFilter1Node):

    bl_idname = 'VTKBlockIdScalarsType'
    bl_label  = 'vtkBlockIdScalars'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKBlockIdScalars )        
TYPENAMES.append('VTKBlockIdScalarsType' )

#--------------------------------------------------------------
class VTKBrownianPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKBrownianPointsType'
    bl_label  = 'vtkBrownianPoints'
    
    m_MaximumSpeed = bpy.props.FloatProperty( name='MaximumSpeed', default=1.0 )
    m_MinimumSpeed = bpy.props.FloatProperty( name='MinimumSpeed', default=0.0 )
    
    def m_properties( self ):
        return ['m_MaximumSpeed','m_MinimumSpeed',]
    
CLASSES.append  ( VTKBrownianPoints )        
TYPENAMES.append('VTKBrownianPointsType' )

#--------------------------------------------------------------
class VTKButterflySubdivisionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKButterflySubdivisionFilterType'
    bl_label  = 'vtkButterflySubdivisionFilter'
    
    m_CheckForTriangles    = bpy.props.BoolProperty( name='CheckForTriangles',    default=1 )
    m_NumberOfSubdivisions = bpy.props.IntProperty ( name='NumberOfSubdivisions', default=1 )
    
    def m_properties( self ):
        return ['m_CheckForTriangles','m_NumberOfSubdivisions',]
    
CLASSES.append  ( VTKButterflySubdivisionFilter )        
TYPENAMES.append('VTKButterflySubdivisionFilterType' )

#--------------------------------------------------------------
class VTKCastToConcrete(Node, VTKFilter1Node):

    bl_idname = 'VTKCastToConcreteType'
    bl_label  = 'vtkCastToConcrete'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKCastToConcrete )        
TYPENAMES.append('VTKCastToConcreteType' )

#--------------------------------------------------------------
class VTKCellCenters(Node, VTKFilter1Node):

    bl_idname = 'VTKCellCentersType'
    bl_label  = 'vtkCellCenters'
    
    m_VertexCells = bpy.props.BoolProperty( name='VertexCells', default=0 )
    
    def m_properties( self ):
        return ['m_VertexCells',]
    
CLASSES.append  ( VTKCellCenters )        
TYPENAMES.append('VTKCellCentersType' )

#--------------------------------------------------------------
class VTKCellDataToPointData(Node, VTKFilter1Node):

    bl_idname = 'VTKCellDataToPointDataType'
    bl_label  = 'vtkCellDataToPointData'
    
    m_PassCellData = bpy.props.BoolProperty( name='PassCellData', default=0 )
    
    def m_properties( self ):
        return ['m_PassCellData',]
    
CLASSES.append  ( VTKCellDataToPointData )        
TYPENAMES.append('VTKCellDataToPointDataType' )

#--------------------------------------------------------------
class VTKCellDerivatives(Node, VTKFilter1Node):

    bl_idname = 'VTKCellDerivativesType'
    bl_label  = 'vtkCellDerivatives'
    e_TensorMode_items=[ (x,x,x) for x in ['PassTensors', 'ComputeGradient', 'ComputeStrain', 'ComputeGreenLagrangeStrain']]
    e_VectorMode_items=[ (x,x,x) for x in ['PassVectors', 'ComputeGradient', 'ComputeVorticity']]
    
    e_TensorMode = bpy.props.EnumProperty( name='TensorMode', default="ComputeGradient", items=e_TensorMode_items )
    e_VectorMode = bpy.props.EnumProperty( name='VectorMode', default="ComputeGradient", items=e_VectorMode_items )
    
    def m_properties( self ):
        return ['e_TensorMode','e_VectorMode',]
    
CLASSES.append  ( VTKCellDerivatives )        
TYPENAMES.append('VTKCellDerivativesType' )

#--------------------------------------------------------------
class VTKCellQuality(Node, VTKFilter1Node):

    bl_idname = 'VTKCellQualityType'
    bl_label  = 'vtkCellQuality'
    e_QualityMeasure_items=[ (x,x,x) for x in ['Area', 'AspectBeta', 'AspectFrobenius', 'AspectGamma', 'AspectRatio', 'CollapseRatio', 'Condition', 'Diagonal', 'Dimension', 'Distortion', 'Jacobian', 'MaxAngle', 'MaxAspectFrobenius', 'MaxEdgeRatio', 'MedAspectFrobenius', 'MinAngle', 'Oddy', 'RadiusRatio', 'RelativeSizeSquared', 'ScaledJacobian', 'Shape', 'ShapeAndSize', 'Shear', 'ShearAndSize', 'Skew', 'Stretch', 'Taper', 'Volume', 'Warpage']]
    
    m_UndefinedQuality    = bpy.props.FloatProperty( name='UndefinedQuality',    default=-1.0 )
    m_UnsupportedGeometry = bpy.props.FloatProperty( name='UnsupportedGeometry', default=-1.0 )
    e_QualityMeasure      = bpy.props.EnumProperty ( name='QualityMeasure',      default="Area", items=e_QualityMeasure_items )
    
    def m_properties( self ):
        return ['m_UndefinedQuality','m_UnsupportedGeometry','e_QualityMeasure',]
    
CLASSES.append  ( VTKCellQuality )        
TYPENAMES.append('VTKCellQualityType' )

#--------------------------------------------------------------
class VTKCellSizeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKCellSizeFilterType'
    bl_label  = 'vtkCellSizeFilter'
    
    m_ComputeArea   = bpy.props.BoolProperty  ( name='ComputeArea',   default=True )
    m_ComputeLength = bpy.props.BoolProperty  ( name='ComputeLength', default=True )
    m_ComputePoint  = bpy.props.BoolProperty  ( name='ComputePoint',  default=True )
    m_ComputeVolume = bpy.props.BoolProperty  ( name='ComputeVolume', default=True )
    m_ArrayName     = bpy.props.StringProperty( name='ArrayName',     default="size" )
    
    def m_properties( self ):
        return ['m_ComputeArea','m_ComputeLength','m_ComputePoint','m_ComputeVolume','m_ArrayName',]
    
CLASSES.append  ( VTKCellSizeFilter )        
TYPENAMES.append('VTKCellSizeFilterType' )

#--------------------------------------------------------------
class VTKCheckerboardSplatter(Node, VTKFilter1Node):

    bl_idname = 'VTKCheckerboardSplatterType'
    bl_label  = 'vtkCheckerboardSplatter'
    e_AccumulationMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Sum']]
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_Capping                = bpy.props.BoolProperty       ( name='Capping',                default=1 )
    m_NormalWarping          = bpy.props.BoolProperty       ( name='NormalWarping',          default=1 )
    m_ScalarWarping          = bpy.props.BoolProperty       ( name='ScalarWarping',          default=1 )
    m_Footprint              = bpy.props.IntProperty        ( name='Footprint',              default=2 )
    m_MaximumDimension       = bpy.props.IntProperty        ( name='MaximumDimension',       default=50 )
    m_ParallelSplatCrossover = bpy.props.IntProperty        ( name='ParallelSplatCrossover', default=2 )
    m_CapValue               = bpy.props.FloatProperty      ( name='CapValue',               default=0.0 )
    m_Eccentricity           = bpy.props.FloatProperty      ( name='Eccentricity',           default=2.5 )
    m_ExponentFactor         = bpy.props.FloatProperty      ( name='ExponentFactor',         default=-5.0 )
    m_NullValue              = bpy.props.FloatProperty      ( name='NullValue',              default=0.0 )
    m_Radius                 = bpy.props.FloatProperty      ( name='Radius',                 default=0.0 )
    m_ScaleFactor            = bpy.props.FloatProperty      ( name='ScaleFactor',            default=1.0 )
    e_AccumulationMode       = bpy.props.EnumProperty       ( name='AccumulationMode',       default="Max", items=e_AccumulationMode_items )
    e_OutputScalarType       = bpy.props.EnumProperty       ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    m_SampleDimensions       = bpy.props.IntVectorProperty  ( name='SampleDimensions',       default=[50, 50, 50], size=3 )
    m_ModelBounds            = bpy.props.FloatVectorProperty( name='ModelBounds',            default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_Capping','m_NormalWarping','m_ScalarWarping','m_Footprint','m_MaximumDimension','m_ParallelSplatCrossover','m_CapValue','m_Eccentricity','m_ExponentFactor','m_NullValue','m_Radius','m_ScaleFactor','e_AccumulationMode','e_OutputScalarType','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKCheckerboardSplatter )        
TYPENAMES.append('VTKCheckerboardSplatterType' )

#--------------------------------------------------------------
class VTKCirclePackLayout(Node, VTKFilter1Node):

    bl_idname = 'VTKCirclePackLayoutType'
    bl_label  = 'vtkCirclePackLayout'
    
    m_CirclesFieldName = bpy.props.StringProperty( name='CirclesFieldName', default="circles" )
    
    def m_properties( self ):
        return ['m_CirclesFieldName',]
    
CLASSES.append  ( VTKCirclePackLayout )        
TYPENAMES.append('VTKCirclePackLayoutType' )

#--------------------------------------------------------------
class VTKCirclePackToPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKCirclePackToPolyDataType'
    bl_label  = 'vtkCirclePackToPolyData'
    
    m_Resolution = bpy.props.IntProperty( name='Resolution', default=100 )
    
    def m_properties( self ):
        return ['m_Resolution',]
    
CLASSES.append  ( VTKCirclePackToPolyData )        
TYPENAMES.append('VTKCirclePackToPolyDataType' )

#--------------------------------------------------------------
class VTKCleanPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKCleanPolyDataType'
    bl_label  = 'vtkCleanPolyData'
    
    m_ConvertLinesToPoints = bpy.props.BoolProperty ( name='ConvertLinesToPoints', default=1 )
    m_ConvertPolysToLines  = bpy.props.BoolProperty ( name='ConvertPolysToLines',  default=1 )
    m_ConvertStripsToPolys = bpy.props.BoolProperty ( name='ConvertStripsToPolys', default=1 )
    m_PieceInvariant       = bpy.props.BoolProperty ( name='PieceInvariant',       default=1 )
    m_PointMerging         = bpy.props.BoolProperty ( name='PointMerging',         default=1 )
    m_ToleranceIsAbsolute  = bpy.props.BoolProperty ( name='ToleranceIsAbsolute',  default=0 )
    m_AbsoluteTolerance    = bpy.props.FloatProperty( name='AbsoluteTolerance',    default=1.0 )
    m_Tolerance            = bpy.props.FloatProperty( name='Tolerance',            default=0.0 )
    
    def m_properties( self ):
        return ['m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_PointMerging','m_ToleranceIsAbsolute','m_AbsoluteTolerance','m_Tolerance',]
    
CLASSES.append  ( VTKCleanPolyData )        
TYPENAMES.append('VTKCleanPolyDataType' )

#--------------------------------------------------------------
class VTKClipClosedSurface(Node, VTKFilter1Node):

    bl_idname = 'VTKClipClosedSurfaceType'
    bl_label  = 'vtkClipClosedSurface'
    e_ScalarMode_items=[ (x,x,x) for x in ['None', 'Colors', 'Labels']]
    
    m_GenerateFaces             = bpy.props.BoolProperty       ( name='GenerateFaces',             default=1 )
    m_GenerateOutline           = bpy.props.BoolProperty       ( name='GenerateOutline',           default=0 )
    m_PassPointData             = bpy.props.BoolProperty       ( name='PassPointData',             default=0 )
    m_TriangulationErrorDisplay = bpy.props.BoolProperty       ( name='TriangulationErrorDisplay', default=0 )
    m_ActivePlaneId             = bpy.props.IntProperty        ( name='ActivePlaneId',             default=-1 )
    m_Tolerance                 = bpy.props.FloatProperty      ( name='Tolerance',                 default=1e-06 )
    e_ScalarMode                = bpy.props.EnumProperty       ( name='ScalarMode',                default="None", items=e_ScalarMode_items )
    m_ActivePlaneColor          = bpy.props.FloatVectorProperty( name='ActivePlaneColor',          default=(1.0, 1.0, 0.0), size=3 )
    m_BaseColor                 = bpy.props.FloatVectorProperty( name='BaseColor',                 default=(1.0, 0.0, 0.0), size=3 )
    m_ClipColor                 = bpy.props.FloatVectorProperty( name='ClipColor',                 default=(1.0, 0.5, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_GenerateFaces','m_GenerateOutline','m_PassPointData','m_TriangulationErrorDisplay','m_ActivePlaneId','m_Tolerance','e_ScalarMode','m_ActivePlaneColor','m_BaseColor','m_ClipColor',]
    
CLASSES.append  ( VTKClipClosedSurface )        
TYPENAMES.append('VTKClipClosedSurfaceType' )

#--------------------------------------------------------------
class VTKClipConvexPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKClipConvexPolyDataType'
    bl_label  = 'vtkClipConvexPolyData'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKClipConvexPolyData )        
TYPENAMES.append('VTKClipConvexPolyDataType' )

#--------------------------------------------------------------
class VTKCollapseVerticesByArray(Node, VTKFilter1Node):

    bl_idname = 'VTKCollapseVerticesByArrayType'
    bl_label  = 'vtkCollapseVerticesByArray'
    
    m_AllowSelfLoops         = bpy.props.BoolProperty  ( name='AllowSelfLoops',         default=False )
    m_CountEdgesCollapsed    = bpy.props.BoolProperty  ( name='CountEdgesCollapsed',    default=False )
    m_CountVerticesCollapsed = bpy.props.BoolProperty  ( name='CountVerticesCollapsed', default=False )
    m_EdgesCollapsedArray    = bpy.props.StringProperty( name='EdgesCollapsedArray',    default="EdgesCollapsedCountArray" )
    m_VertexArray            = bpy.props.StringProperty( name='VertexArray',            default="" )
    m_VerticesCollapsedArray = bpy.props.StringProperty( name='VerticesCollapsedArray', default="VerticesCollapsedCountArray" )
    
    def m_properties( self ):
        return ['m_AllowSelfLoops','m_CountEdgesCollapsed','m_CountVerticesCollapsed','m_EdgesCollapsedArray','m_VertexArray','m_VerticesCollapsedArray',]
    
CLASSES.append  ( VTKCollapseVerticesByArray )        
TYPENAMES.append('VTKCollapseVerticesByArrayType' )

#--------------------------------------------------------------
class VTKCollectGraph(Node, VTKFilter1Node):

    bl_idname = 'VTKCollectGraphType'
    bl_label  = 'vtkCollectGraph'
    
    m_PassThrough = bpy.props.BoolProperty( name='PassThrough', default=0 )
    m_OutputType  = bpy.props.IntProperty ( name='OutputType',  default=2 )
    
    def m_properties( self ):
        return ['m_PassThrough','m_OutputType',]
    
CLASSES.append  ( VTKCollectGraph )        
TYPENAMES.append('VTKCollectGraphType' )

#--------------------------------------------------------------
class VTKCollectPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKCollectPolyDataType'
    bl_label  = 'vtkCollectPolyData'
    
    m_PassThrough = bpy.props.BoolProperty( name='PassThrough', default=0 )
    
    def m_properties( self ):
        return ['m_PassThrough',]
    
CLASSES.append  ( VTKCollectPolyData )        
TYPENAMES.append('VTKCollectPolyDataType' )

#--------------------------------------------------------------
class VTKCollectTable(Node, VTKFilter1Node):

    bl_idname = 'VTKCollectTableType'
    bl_label  = 'vtkCollectTable'
    
    m_PassThrough = bpy.props.BoolProperty( name='PassThrough', default=0 )
    
    def m_properties( self ):
        return ['m_PassThrough',]
    
CLASSES.append  ( VTKCollectTable )        
TYPENAMES.append('VTKCollectTableType' )

#--------------------------------------------------------------
class VTKCompositeDataGeometryFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKCompositeDataGeometryFilterType'
    bl_label  = 'vtkCompositeDataGeometryFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKCompositeDataGeometryFilter )        
TYPENAMES.append('VTKCompositeDataGeometryFilterType' )

#--------------------------------------------------------------
class VTKCompositeDataSetAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKCompositeDataSetAlgorithmType'
    bl_label  = 'vtkCompositeDataSetAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKCompositeDataSetAlgorithm )        
TYPENAMES.append('VTKCompositeDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKComputeQuartiles(Node, VTKFilter1Node):

    bl_idname = 'VTKComputeQuartilesType'
    bl_label  = 'vtkComputeQuartiles'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKComputeQuartiles )        
TYPENAMES.append('VTKComputeQuartilesType' )

#--------------------------------------------------------------
class VTKConnectivityFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKConnectivityFilterType'
    bl_label  = 'vtkConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_ColorRegions       = bpy.props.BoolProperty       ( name='ColorRegions',       default=0 )
    m_ScalarConnectivity = bpy.props.BoolProperty       ( name='ScalarConnectivity', default=0 )
    e_ExtractionMode     = bpy.props.EnumProperty       ( name='ExtractionMode',     default="LargestRegion", items=e_ExtractionMode_items )
    m_ClosestPoint       = bpy.props.FloatVectorProperty( name='ClosestPoint',       default=(0.0, 0.0, 0.0), size=3 )
    m_ScalarRange        = bpy.props.FloatVectorProperty( name='ScalarRange',        default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_ColorRegions','m_ScalarConnectivity','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    
CLASSES.append  ( VTKConnectivityFilter )        
TYPENAMES.append('VTKConnectivityFilterType' )

#--------------------------------------------------------------
class VTKContinuousScatterplot(Node, VTKFilter1Node):

    bl_idname = 'VTKContinuousScatterplotType'
    bl_label  = 'vtkContinuousScatterplot'
    
    m_Epsilon = bpy.props.FloatProperty( name='Epsilon', default=1e-06 )
    
    def m_properties( self ):
        return ['m_Epsilon',]
    
CLASSES.append  ( VTKContinuousScatterplot )        
TYPENAMES.append('VTKContinuousScatterplotType' )

#--------------------------------------------------------------
class VTKContourLoopExtraction(Node, VTKFilter1Node):

    bl_idname = 'VTKContourLoopExtractionType'
    bl_label  = 'vtkContourLoopExtraction'
    e_LoopClosure_items=[ (x,x,x) for x in ['Off', 'Boundary', 'All']]
    
    m_ScalarThresholding = bpy.props.BoolProperty       ( name='ScalarThresholding', default=False )
    e_LoopClosure        = bpy.props.EnumProperty       ( name='LoopClosure',        default="Boundary", items=e_LoopClosure_items )
    m_Normal             = bpy.props.FloatVectorProperty( name='Normal',             default=(0.0, 0.0, 1.0), size=3 )
    m_ScalarRange        = bpy.props.FloatVectorProperty( name='ScalarRange',        default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_ScalarThresholding','e_LoopClosure','m_Normal','m_ScalarRange',]
    
CLASSES.append  ( VTKContourLoopExtraction )        
TYPENAMES.append('VTKContourLoopExtractionType' )

#--------------------------------------------------------------
class VTKContourTriangulator(Node, VTKFilter1Node):

    bl_idname = 'VTKContourTriangulatorType'
    bl_label  = 'vtkContourTriangulator'
    
    m_TriangulationErrorDisplay = bpy.props.BoolProperty( name='TriangulationErrorDisplay', default=0 )
    
    def m_properties( self ):
        return ['m_TriangulationErrorDisplay',]
    
CLASSES.append  ( VTKContourTriangulator )        
TYPENAMES.append('VTKContourTriangulatorType' )

#--------------------------------------------------------------
class VTKCountFaces(Node, VTKFilter1Node):

    bl_idname = 'VTKCountFacesType'
    bl_label  = 'vtkCountFaces'
    
    m_OutputArrayName = bpy.props.StringProperty( name='OutputArrayName', default="Face Count" )
    
    def m_properties( self ):
        return ['m_OutputArrayName',]
    
CLASSES.append  ( VTKCountFaces )        
TYPENAMES.append('VTKCountFacesType' )

#--------------------------------------------------------------
class VTKCountVertices(Node, VTKFilter1Node):

    bl_idname = 'VTKCountVerticesType'
    bl_label  = 'vtkCountVertices'
    
    m_OutputArrayName = bpy.props.StringProperty( name='OutputArrayName', default="Vertex Count" )
    
    def m_properties( self ):
        return ['m_OutputArrayName',]
    
CLASSES.append  ( VTKCountVertices )        
TYPENAMES.append('VTKCountVerticesType' )

#--------------------------------------------------------------
class VTKCurvatures(Node, VTKFilter1Node):

    bl_idname = 'VTKCurvaturesType'
    bl_label  = 'vtkCurvatures'
    e_CurvatureType_items=[ (x,x,x) for x in ['Gaussian', 'Mean', 'Maximum', 'Minimum']]
    
    m_InvertMeanCurvature = bpy.props.BoolProperty( name='InvertMeanCurvature', default=0 )
    e_CurvatureType       = bpy.props.EnumProperty( name='CurvatureType',       default="Gaussian", items=e_CurvatureType_items )
    
    def m_properties( self ):
        return ['m_InvertMeanCurvature','e_CurvatureType',]
    
CLASSES.append  ( VTKCurvatures )        
TYPENAMES.append('VTKCurvaturesType' )

#--------------------------------------------------------------
class VTKCutMaterial(Node, VTKFilter1Node):

    bl_idname = 'VTKCutMaterialType'
    bl_label  = 'vtkCutMaterial'
    
    m_ArrayName         = bpy.props.StringProperty     ( name='ArrayName',         default="" )
    m_MaterialArrayName = bpy.props.StringProperty     ( name='MaterialArrayName', default="material" )
    m_Material          = bpy.props.IntProperty        ( name='Material',          default=0 )
    m_UpVector          = bpy.props.FloatVectorProperty( name='UpVector',          default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_ArrayName','m_MaterialArrayName','m_Material','m_UpVector',]
    
CLASSES.append  ( VTKCutMaterial )        
TYPENAMES.append('VTKCutMaterialType' )

#--------------------------------------------------------------
class VTKDICOMAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKDICOMAlgorithmType'
    bl_label  = 'vtkDICOMAlgorithm'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKDICOMAlgorithm )        
TYPENAMES.append('VTKDICOMAlgorithmType' )

#--------------------------------------------------------------
class VTKDICOMApplyPalette(Node, VTKFilter1Node):

    bl_idname = 'VTKDICOMApplyPaletteType'
    bl_label  = 'vtkDICOMApplyPalette'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKDICOMApplyPalette )        
TYPENAMES.append('VTKDICOMApplyPaletteType' )

#--------------------------------------------------------------
class VTKDICOMApplyRescale(Node, VTKFilter1Node):

    bl_idname = 'VTKDICOMApplyRescaleType'
    bl_label  = 'vtkDICOMApplyRescale'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputScalarType       = bpy.props.EnumProperty     ( name='OutputScalarType',       default="Double", items=e_OutputScalarType_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKDICOMApplyRescale )        
TYPENAMES.append('VTKDICOMApplyRescaleType' )

#--------------------------------------------------------------
class VTKDICOMCTRectifier(Node, VTKFilter1Node):

    bl_idname = 'VTKDICOMCTRectifierType'
    bl_label  = 'vtkDICOMCTRectifier'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_Reverse                = bpy.props.BoolProperty     ( name='Reverse',                default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_Reverse','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKDICOMCTRectifier )        
TYPENAMES.append('VTKDICOMCTRectifierType' )

#--------------------------------------------------------------
class VTKDICOMToRAS(Node, VTKFilter1Node):

    bl_idname = 'VTKDICOMToRASType'
    bl_label  = 'vtkDICOMToRAS'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AllowColumnReordering  = bpy.props.BoolProperty     ( name='AllowColumnReordering',  default=1 )
    m_AllowRowReordering     = bpy.props.BoolProperty     ( name='AllowRowReordering',     default=1 )
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_RASMatrixHasPosition   = bpy.props.BoolProperty     ( name='RASMatrixHasPosition',   default=1 )
    m_RASToDICOM             = bpy.props.BoolProperty     ( name='RASToDICOM',             default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_AllowColumnReordering','m_AllowRowReordering','m_EnableSMP','m_GlobalDefaultEnableSMP','m_RASMatrixHasPosition','m_RASToDICOM','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKDICOMToRAS )        
TYPENAMES.append('VTKDICOMToRASType' )

#--------------------------------------------------------------
class VTKDataObjectAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKDataObjectAlgorithmType'
    bl_label  = 'vtkDataObjectAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKDataObjectAlgorithm )        
TYPENAMES.append('VTKDataObjectAlgorithmType' )

#--------------------------------------------------------------
class VTKDataObjectToDataSetFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDataObjectToDataSetFilterType'
    bl_label  = 'vtkDataObjectToDataSetFilter'
    e_DataSetType_items=[ (x,x,x) for x in ['PolyData', 'StructuredPoints', 'StructuredGrid', 'RectilinearGrid', 'UnstructuredGrid']]
    
    m_DefaultNormalize = bpy.props.BoolProperty       ( name='DefaultNormalize', default=0 )
    e_DataSetType      = bpy.props.EnumProperty       ( name='DataSetType',      default="PolyData", items=e_DataSetType_items )
    m_Dimensions       = bpy.props.IntVectorProperty  ( name='Dimensions',       default=[0, 0, 0], size=3 )
    m_Origin           = bpy.props.FloatVectorProperty( name='Origin',           default=(0.0, 0.0, 0.0), size=3 )
    m_Spacing          = bpy.props.FloatVectorProperty( name='Spacing',          default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_DefaultNormalize','e_DataSetType','m_Dimensions','m_Origin','m_Spacing',]
    
CLASSES.append  ( VTKDataObjectToDataSetFilter )        
TYPENAMES.append('VTKDataObjectToDataSetFilterType' )

#--------------------------------------------------------------
class VTKDataObjectToTable(Node, VTKFilter1Node):

    bl_idname = 'VTKDataObjectToTableType'
    bl_label  = 'vtkDataObjectToTable'
    
    m_FieldType = bpy.props.IntProperty( name='FieldType', default=1 )
    
    def m_properties( self ):
        return ['m_FieldType',]
    
CLASSES.append  ( VTKDataObjectToTable )        
TYPENAMES.append('VTKDataObjectToTableType' )

#--------------------------------------------------------------
class VTKDataSetAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetAlgorithmType'
    bl_label  = 'vtkDataSetAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKDataSetAlgorithm )        
TYPENAMES.append('VTKDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKDataSetGradient(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetGradientType'
    bl_label  = 'vtkDataSetGradient'
    
    m_ResultArrayName = bpy.props.StringProperty( name='ResultArrayName', default="gradient" )
    
    def m_properties( self ):
        return ['m_ResultArrayName',]
    
CLASSES.append  ( VTKDataSetGradient )        
TYPENAMES.append('VTKDataSetGradientType' )

#--------------------------------------------------------------
class VTKDataSetGradientPrecompute(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetGradientPrecomputeType'
    bl_label  = 'vtkDataSetGradientPrecompute'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKDataSetGradientPrecompute )        
TYPENAMES.append('VTKDataSetGradientPrecomputeType' )

#--------------------------------------------------------------
class VTKDataSetRegionSurfaceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetRegionSurfaceFilterType'
    bl_label  = 'vtkDataSetRegionSurfaceFilter'
    
    m_PassThroughCellIds        = bpy.props.BoolProperty  ( name='PassThroughCellIds',        default=0 )
    m_PassThroughPointIds       = bpy.props.BoolProperty  ( name='PassThroughPointIds',       default=0 )
    m_SingleSided               = bpy.props.BoolProperty  ( name='SingleSided',               default=True )
    m_UseStrips                 = bpy.props.BoolProperty  ( name='UseStrips',                 default=0 )
    m_InterfaceIDsName          = bpy.props.StringProperty( name='InterfaceIDsName',          default="interface_ids" )
    m_MaterialIDsName           = bpy.props.StringProperty( name='MaterialIDsName',           default="material_ids" )
    m_MaterialPIDsName          = bpy.props.StringProperty( name='MaterialPIDsName',          default="material_ancestors" )
    m_MaterialPropertiesName    = bpy.props.StringProperty( name='MaterialPropertiesName',    default="material_properties" )
    m_OriginalCellIdsName       = bpy.props.StringProperty( name='OriginalCellIdsName',       default="vtkOriginalCellIds" )
    m_OriginalPointIdsName      = bpy.props.StringProperty( name='OriginalPointIdsName',      default="vtkOriginalPointIds" )
    m_RegionArrayName           = bpy.props.StringProperty( name='RegionArrayName',           default="material" )
    m_NonlinearSubdivisionLevel = bpy.props.IntProperty   ( name='NonlinearSubdivisionLevel', default=1 )
    m_PieceInvariant            = bpy.props.IntProperty   ( name='PieceInvariant',            default=0 )
    
    def m_properties( self ):
        return ['m_PassThroughCellIds','m_PassThroughPointIds','m_SingleSided','m_UseStrips','m_InterfaceIDsName','m_MaterialIDsName','m_MaterialPIDsName','m_MaterialPropertiesName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_RegionArrayName','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    
CLASSES.append  ( VTKDataSetRegionSurfaceFilter )        
TYPENAMES.append('VTKDataSetRegionSurfaceFilterType' )

#--------------------------------------------------------------
class VTKDataSetSurfaceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetSurfaceFilterType'
    bl_label  = 'vtkDataSetSurfaceFilter'
    
    m_PassThroughCellIds        = bpy.props.BoolProperty  ( name='PassThroughCellIds',        default=0 )
    m_PassThroughPointIds       = bpy.props.BoolProperty  ( name='PassThroughPointIds',       default=0 )
    m_UseStrips                 = bpy.props.BoolProperty  ( name='UseStrips',                 default=0 )
    m_OriginalCellIdsName       = bpy.props.StringProperty( name='OriginalCellIdsName',       default="vtkOriginalCellIds" )
    m_OriginalPointIdsName      = bpy.props.StringProperty( name='OriginalPointIdsName',      default="vtkOriginalPointIds" )
    m_NonlinearSubdivisionLevel = bpy.props.IntProperty   ( name='NonlinearSubdivisionLevel', default=1 )
    m_PieceInvariant            = bpy.props.IntProperty   ( name='PieceInvariant',            default=0 )
    
    def m_properties( self ):
        return ['m_PassThroughCellIds','m_PassThroughPointIds','m_UseStrips','m_OriginalCellIdsName','m_OriginalPointIdsName','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    
CLASSES.append  ( VTKDataSetSurfaceFilter )        
TYPENAMES.append('VTKDataSetSurfaceFilterType' )

#--------------------------------------------------------------
class VTKDataSetToDataObjectFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetToDataObjectFilterType'
    bl_label  = 'vtkDataSetToDataObjectFilter'
    
    m_CellData  = bpy.props.BoolProperty( name='CellData',  default=1 )
    m_FieldData = bpy.props.BoolProperty( name='FieldData', default=1 )
    m_Geometry  = bpy.props.BoolProperty( name='Geometry',  default=1 )
    m_PointData = bpy.props.BoolProperty( name='PointData', default=1 )
    m_Topology  = bpy.props.BoolProperty( name='Topology',  default=1 )
    
    def m_properties( self ):
        return ['m_CellData','m_FieldData','m_Geometry','m_PointData','m_Topology',]
    
CLASSES.append  ( VTKDataSetToDataObjectFilter )        
TYPENAMES.append('VTKDataSetToDataObjectFilterType' )

#--------------------------------------------------------------
class VTKDataSetTriangleFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDataSetTriangleFilterType'
    bl_label  = 'vtkDataSetTriangleFilter'
    
    m_TetrahedraOnly = bpy.props.BoolProperty( name='TetrahedraOnly', default=0 )
    
    def m_properties( self ):
        return ['m_TetrahedraOnly',]
    
CLASSES.append  ( VTKDataSetTriangleFilter )        
TYPENAMES.append('VTKDataSetTriangleFilterType' )

#--------------------------------------------------------------
class VTKDecimatePolylineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDecimatePolylineFilterType'
    bl_label  = 'vtkDecimatePolylineFilter'
    
    m_TargetReduction = bpy.props.FloatProperty( name='TargetReduction', default=0.9 )
    
    def m_properties( self ):
        return ['m_TargetReduction',]
    
CLASSES.append  ( VTKDecimatePolylineFilter )        
TYPENAMES.append('VTKDecimatePolylineFilterType' )

#--------------------------------------------------------------
class VTKDecimatePro(Node, VTKFilter1Node):

    bl_idname = 'VTKDecimateProType'
    bl_label  = 'vtkDecimatePro'
    
    m_AccumulateError        = bpy.props.BoolProperty ( name='AccumulateError',        default=0 )
    m_BoundaryVertexDeletion = bpy.props.BoolProperty ( name='BoundaryVertexDeletion', default=1 )
    m_PreSplitMesh           = bpy.props.BoolProperty ( name='PreSplitMesh',           default=0 )
    m_PreserveTopology       = bpy.props.BoolProperty ( name='PreserveTopology',       default=0 )
    m_Splitting              = bpy.props.BoolProperty ( name='Splitting',              default=1 )
    m_Degree                 = bpy.props.IntProperty  ( name='Degree',                 default=25 )
    m_ErrorIsAbsolute        = bpy.props.IntProperty  ( name='ErrorIsAbsolute',        default=0 )
    m_AbsoluteError          = bpy.props.FloatProperty( name='AbsoluteError',          default=1e+299 )
    m_FeatureAngle           = bpy.props.FloatProperty( name='FeatureAngle',           default=15.0 )
    m_InflectionPointRatio   = bpy.props.FloatProperty( name='InflectionPointRatio',   default=10.0 )
    m_MaximumError           = bpy.props.FloatProperty( name='MaximumError',           default=1e+299 )
    m_SplitAngle             = bpy.props.FloatProperty( name='SplitAngle',             default=75.0 )
    m_TargetReduction        = bpy.props.FloatProperty( name='TargetReduction',        default=0.9 )
    
    def m_properties( self ):
        return ['m_AccumulateError','m_BoundaryVertexDeletion','m_PreSplitMesh','m_PreserveTopology','m_Splitting','m_Degree','m_ErrorIsAbsolute','m_AbsoluteError','m_FeatureAngle','m_InflectionPointRatio','m_MaximumError','m_SplitAngle','m_TargetReduction',]
    
CLASSES.append  ( VTKDecimatePro )        
TYPENAMES.append('VTKDecimateProType' )

#--------------------------------------------------------------
class VTKDelaunay3D(Node, VTKFilter1Node):

    bl_idname = 'VTKDelaunay3DType'
    bl_label  = 'vtkDelaunay3D'
    
    m_AlphaLines            = bpy.props.BoolProperty ( name='AlphaLines',            default=1 )
    m_AlphaTets             = bpy.props.BoolProperty ( name='AlphaTets',             default=1 )
    m_AlphaTris             = bpy.props.BoolProperty ( name='AlphaTris',             default=1 )
    m_AlphaVerts            = bpy.props.BoolProperty ( name='AlphaVerts',            default=1 )
    m_BoundingTriangulation = bpy.props.BoolProperty ( name='BoundingTriangulation', default=0 )
    m_Alpha                 = bpy.props.FloatProperty( name='Alpha',                 default=0.0 )
    m_Offset                = bpy.props.FloatProperty( name='Offset',                default=2.5 )
    m_Tolerance             = bpy.props.FloatProperty( name='Tolerance',             default=0.001 )
    
    def m_properties( self ):
        return ['m_AlphaLines','m_AlphaTets','m_AlphaTris','m_AlphaVerts','m_BoundingTriangulation','m_Alpha','m_Offset','m_Tolerance',]
    
CLASSES.append  ( VTKDelaunay3D )        
TYPENAMES.append('VTKDelaunay3DType' )

#--------------------------------------------------------------
class VTKDensifyPointCloudFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKDensifyPointCloudFilterType'
    bl_label  = 'vtkDensifyPointCloudFilter'
    e_NeighborhoodType_items=[ (x,x,x) for x in ['Radius', 'NClosest']]
    
    m_InterpolateAttributeData  = bpy.props.BoolProperty ( name='InterpolateAttributeData',  default=True )
    m_MaximumNumberOfIterations = bpy.props.IntProperty  ( name='MaximumNumberOfIterations', default=3 )
    m_MaximumNumberOfPoints     = bpy.props.IntProperty  ( name='MaximumNumberOfPoints',     default=0 )
    m_NumberOfClosestPoints     = bpy.props.IntProperty  ( name='NumberOfClosestPoints',     default=6 )
    m_Radius                    = bpy.props.FloatProperty( name='Radius',                    default=1.0 )
    m_TargetDistance            = bpy.props.FloatProperty( name='TargetDistance',            default=0.5 )
    e_NeighborhoodType          = bpy.props.EnumProperty ( name='NeighborhoodType',          default="NClosest", items=e_NeighborhoodType_items )
    
    def m_properties( self ):
        return ['m_InterpolateAttributeData','m_MaximumNumberOfIterations','m_MaximumNumberOfPoints','m_NumberOfClosestPoints','m_Radius','m_TargetDistance','e_NeighborhoodType',]
    
CLASSES.append  ( VTKDensifyPointCloudFilter )        
TYPENAMES.append('VTKDensifyPointCloudFilterType' )

#--------------------------------------------------------------
class VTKDensifyPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKDensifyPolyDataType'
    bl_label  = 'vtkDensifyPolyData'
    
    m_NumberOfSubdivisions = bpy.props.IntProperty( name='NumberOfSubdivisions', default=1 )
    
    def m_properties( self ):
        return ['m_NumberOfSubdivisions',]
    
CLASSES.append  ( VTKDensifyPolyData )        
TYPENAMES.append('VTKDensifyPolyDataType' )

#--------------------------------------------------------------
class VTKDepthSortPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKDepthSortPolyDataType'
    bl_label  = 'vtkDepthSortPolyData'
    e_DepthSortMode_items=[ (x,x,x) for x in ['FirstPoint', 'BoundsCenter', 'ParametricCenter']]
    e_Direction_items=[ (x,x,x) for x in ['BackToFront', 'FrontToBack', 'SpecifiedVector']]
    
    m_SortScalars   = bpy.props.BoolProperty       ( name='SortScalars',   default=0 )
    e_DepthSortMode = bpy.props.EnumProperty       ( name='DepthSortMode', default="FirstPoint", items=e_DepthSortMode_items )
    e_Direction     = bpy.props.EnumProperty       ( name='Direction',     default="BackToFront", items=e_Direction_items )
    m_Origin        = bpy.props.FloatVectorProperty( name='Origin',        default=(0.0, 0.0, 0.0), size=3 )
    m_Vector        = bpy.props.FloatVectorProperty( name='Vector',        default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_SortScalars','e_DepthSortMode','e_Direction','m_Origin','m_Vector',]
    
CLASSES.append  ( VTKDepthSortPolyData )        
TYPENAMES.append('VTKDepthSortPolyDataType' )

#--------------------------------------------------------------
class VTKDijkstraGraphGeodesicPath(Node, VTKFilter1Node):

    bl_idname = 'VTKDijkstraGraphGeodesicPathType'
    bl_label  = 'vtkDijkstraGraphGeodesicPath'
    
    m_RepelPathFromVertices = bpy.props.BoolProperty( name='RepelPathFromVertices', default=0 )
    m_StopWhenEndReached    = bpy.props.BoolProperty( name='StopWhenEndReached',    default=0 )
    m_UseScalarWeights      = bpy.props.BoolProperty( name='UseScalarWeights',      default=0 )
    m_EndVertex             = bpy.props.IntProperty ( name='EndVertex',             default=0 )
    m_StartVertex           = bpy.props.IntProperty ( name='StartVertex',           default=0 )
    
    def m_properties( self ):
        return ['m_RepelPathFromVertices','m_StopWhenEndReached','m_UseScalarWeights','m_EndVertex','m_StartVertex',]
    
CLASSES.append  ( VTKDijkstraGraphGeodesicPath )        
TYPENAMES.append('VTKDijkstraGraphGeodesicPathType' )

#--------------------------------------------------------------
class VTKDijkstraImageGeodesicPath(Node, VTKFilter1Node):

    bl_idname = 'VTKDijkstraImageGeodesicPathType'
    bl_label  = 'vtkDijkstraImageGeodesicPath'
    
    m_RepelPathFromVertices = bpy.props.BoolProperty ( name='RepelPathFromVertices', default=0 )
    m_StopWhenEndReached    = bpy.props.BoolProperty ( name='StopWhenEndReached',    default=0 )
    m_UseScalarWeights      = bpy.props.BoolProperty ( name='UseScalarWeights',      default=0 )
    m_EndVertex             = bpy.props.IntProperty  ( name='EndVertex',             default=0 )
    m_StartVertex           = bpy.props.IntProperty  ( name='StartVertex',           default=0 )
    m_CurvatureWeight       = bpy.props.FloatProperty( name='CurvatureWeight',       default=0.0 )
    m_EdgeLengthWeight      = bpy.props.FloatProperty( name='EdgeLengthWeight',      default=0.0 )
    m_ImageWeight           = bpy.props.FloatProperty( name='ImageWeight',           default=1.0 )
    
    def m_properties( self ):
        return ['m_RepelPathFromVertices','m_StopWhenEndReached','m_UseScalarWeights','m_EndVertex','m_StartVertex','m_CurvatureWeight','m_EdgeLengthWeight','m_ImageWeight',]
    
CLASSES.append  ( VTKDijkstraImageGeodesicPath )        
TYPENAMES.append('VTKDijkstraImageGeodesicPathType' )

#--------------------------------------------------------------
class VTKDirectedGraphAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKDirectedGraphAlgorithmType'
    bl_label  = 'vtkDirectedGraphAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKDirectedGraphAlgorithm )        
TYPENAMES.append('VTKDirectedGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKDistanceToCamera(Node, VTKFilter1Node):

    bl_idname = 'VTKDistanceToCameraType'
    bl_label  = 'vtkDistanceToCamera'
    
    m_Scaling           = bpy.props.BoolProperty  ( name='Scaling',           default=False )
    m_DistanceArrayName = bpy.props.StringProperty( name='DistanceArrayName', default="DistanceToCamera" )
    m_ScreenSize        = bpy.props.FloatProperty ( name='ScreenSize',        default=5.0 )
    
    def m_properties( self ):
        return ['m_Scaling','m_DistanceArrayName','m_ScreenSize',]
    
CLASSES.append  ( VTKDistanceToCamera )        
TYPENAMES.append('VTKDistanceToCameraType' )

#--------------------------------------------------------------
class VTKDuplicatePolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKDuplicatePolyDataType'
    bl_label  = 'vtkDuplicatePolyData'
    
    m_Synchronous = bpy.props.BoolProperty( name='Synchronous', default=1 )
    m_ClientFlag  = bpy.props.IntProperty ( name='ClientFlag',  default=0 )
    
    def m_properties( self ):
        return ['m_Synchronous','m_ClientFlag',]
    
CLASSES.append  ( VTKDuplicatePolyData )        
TYPENAMES.append('VTKDuplicatePolyDataType' )

#--------------------------------------------------------------
class VTKEdgeCenters(Node, VTKFilter1Node):

    bl_idname = 'VTKEdgeCentersType'
    bl_label  = 'vtkEdgeCenters'
    
    m_VertexCells = bpy.props.BoolProperty( name='VertexCells', default=0 )
    
    def m_properties( self ):
        return ['m_VertexCells',]
    
CLASSES.append  ( VTKEdgeCenters )        
TYPENAMES.append('VTKEdgeCentersType' )

#--------------------------------------------------------------
class VTKEdgeLayout(Node, VTKFilter1Node):

    bl_idname = 'VTKEdgeLayoutType'
    bl_label  = 'vtkEdgeLayout'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKEdgeLayout )        
TYPENAMES.append('VTKEdgeLayoutType' )

#--------------------------------------------------------------
class VTKEdgePoints(Node, VTKFilter1Node):

    bl_idname = 'VTKEdgePointsType'
    bl_label  = 'vtkEdgePoints'
    
    m_Value = bpy.props.FloatProperty( name='Value', default=0.0 )
    
    def m_properties( self ):
        return ['m_Value',]
    
CLASSES.append  ( VTKEdgePoints )        
TYPENAMES.append('VTKEdgePointsType' )

#--------------------------------------------------------------
class VTKElevationFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKElevationFilterType'
    bl_label  = 'vtkElevationFilter'
    
    m_HighPoint   = bpy.props.FloatVectorProperty( name='HighPoint',   default=(0.0, 0.0, 1.0), size=3 )
    m_LowPoint    = bpy.props.FloatVectorProperty( name='LowPoint',    default=(0.0, 0.0, 0.0), size=3 )
    m_ScalarRange = bpy.props.FloatVectorProperty( name='ScalarRange', default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_HighPoint','m_LowPoint','m_ScalarRange',]
    
CLASSES.append  ( VTKElevationFilter )        
TYPENAMES.append('VTKElevationFilterType' )

#--------------------------------------------------------------
class VTKEuclideanClusterExtraction(Node, VTKFilter1Node):

    bl_idname = 'VTKEuclideanClusterExtractionType'
    bl_label  = 'vtkEuclideanClusterExtraction'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededClusters', 'SpecifiedClusters', 'LargestCluster', 'AllClusters', 'ClosestPointCluster']]
    
    m_ColorClusters      = bpy.props.BoolProperty       ( name='ColorClusters',      default=False )
    m_ScalarConnectivity = bpy.props.BoolProperty       ( name='ScalarConnectivity', default=False )
    m_Radius             = bpy.props.FloatProperty      ( name='Radius',             default=6.9049499344715e-310 )
    e_ExtractionMode     = bpy.props.EnumProperty       ( name='ExtractionMode',     default="LargestCluster", items=e_ExtractionMode_items )
    m_ClosestPoint       = bpy.props.FloatVectorProperty( name='ClosestPoint',       default=(0.0, 0.0, 0.0), size=3 )
    m_ScalarRange        = bpy.props.FloatVectorProperty( name='ScalarRange',        default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_ColorClusters','m_ScalarConnectivity','m_Radius','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    
CLASSES.append  ( VTKEuclideanClusterExtraction )        
TYPENAMES.append('VTKEuclideanClusterExtractionType' )

#--------------------------------------------------------------
class VTKExtractArray(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractArrayType'
    bl_label  = 'vtkExtractArray'
    
    m_Index = bpy.props.IntProperty( name='Index', default=0 )
    
    def m_properties( self ):
        return ['m_Index',]
    
CLASSES.append  ( VTKExtractArray )        
TYPENAMES.append('VTKExtractArrayType' )

#--------------------------------------------------------------
class VTKExtractBlock(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractBlockType'
    bl_label  = 'vtkExtractBlock'
    
    m_MaintainStructure = bpy.props.BoolProperty( name='MaintainStructure', default=0 )
    m_PruneOutput       = bpy.props.BoolProperty( name='PruneOutput',       default=1 )
    
    def m_properties( self ):
        return ['m_MaintainStructure','m_PruneOutput',]
    
CLASSES.append  ( VTKExtractBlock )        
TYPENAMES.append('VTKExtractBlockType' )

#--------------------------------------------------------------
class VTKExtractCTHPart(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractCTHPartType'
    bl_label  = 'vtkExtractCTHPart'
    
    m_Capping                    = bpy.props.BoolProperty ( name='Capping',                    default=True )
    m_GenerateTriangles          = bpy.props.BoolProperty ( name='GenerateTriangles',          default=True )
    m_RemoveGhostCells           = bpy.props.BoolProperty ( name='RemoveGhostCells',           default=True )
    m_VolumeFractionSurfaceValue = bpy.props.FloatProperty( name='VolumeFractionSurfaceValue', default=0.499 )
    
    def m_properties( self ):
        return ['m_Capping','m_GenerateTriangles','m_RemoveGhostCells','m_VolumeFractionSurfaceValue',]
    
CLASSES.append  ( VTKExtractCTHPart )        
TYPENAMES.append('VTKExtractCTHPartType' )

#--------------------------------------------------------------
class VTKExtractCells(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractCellsType'
    bl_label  = 'vtkExtractCells'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKExtractCells )        
TYPENAMES.append('VTKExtractCellsType' )

#--------------------------------------------------------------
class VTKExtractDataOverTime(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractDataOverTimeType'
    bl_label  = 'vtkExtractDataOverTime'
    
    m_PointIndex = bpy.props.IntProperty( name='PointIndex', default=0 )
    
    def m_properties( self ):
        return ['m_PointIndex',]
    
CLASSES.append  ( VTKExtractDataOverTime )        
TYPENAMES.append('VTKExtractDataOverTimeType' )

#--------------------------------------------------------------
class VTKExtractDataSets(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractDataSetsType'
    bl_label  = 'vtkExtractDataSets'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKExtractDataSets )        
TYPENAMES.append('VTKExtractDataSetsType' )

#--------------------------------------------------------------
class VTKExtractEdges(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractEdgesType'
    bl_label  = 'vtkExtractEdges'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKExtractEdges )        
TYPENAMES.append('VTKExtractEdgesType' )

#--------------------------------------------------------------
class VTKExtractGeometry(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractGeometryType'
    bl_label  = 'vtkExtractGeometry'
    
    m_ExtractBoundaryCells     = bpy.props.BoolProperty( name='ExtractBoundaryCells',     default=0 )
    m_ExtractInside            = bpy.props.BoolProperty( name='ExtractInside',            default=1 )
    m_ExtractOnlyBoundaryCells = bpy.props.BoolProperty( name='ExtractOnlyBoundaryCells', default=0 )
    
    def m_properties( self ):
        return ['m_ExtractBoundaryCells','m_ExtractInside','m_ExtractOnlyBoundaryCells',]
    
CLASSES.append  ( VTKExtractGeometry )        
TYPENAMES.append('VTKExtractGeometryType' )

#--------------------------------------------------------------
class VTKExtractGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractGridType'
    bl_label  = 'vtkExtractGrid'
    
    m_IncludeBoundary = bpy.props.BoolProperty     ( name='IncludeBoundary', default=0 )
    m_SampleRate      = bpy.props.IntVectorProperty( name='SampleRate',      default=[1, 1, 1], size=3 )
    m_VOI             = bpy.props.IntVectorProperty( name='VOI',             default=[0, 0, 0, 0, 0, 0], size=6 )
    
    def m_properties( self ):
        return ['m_IncludeBoundary','m_SampleRate','m_VOI',]
    
CLASSES.append  ( VTKExtractGrid )        
TYPENAMES.append('VTKExtractGridType' )

#--------------------------------------------------------------
class VTKExtractLevel(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractLevelType'
    bl_label  = 'vtkExtractLevel'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKExtractLevel )        
TYPENAMES.append('VTKExtractLevelType' )

#--------------------------------------------------------------
class VTKExtractPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractPieceType'
    bl_label  = 'vtkExtractPiece'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKExtractPiece )        
TYPENAMES.append('VTKExtractPieceType' )

#--------------------------------------------------------------
class VTKExtractPointCloudPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractPointCloudPieceType'
    bl_label  = 'vtkExtractPointCloudPiece'
    
    m_ModuloOrdering = bpy.props.BoolProperty( name='ModuloOrdering', default=True )
    
    def m_properties( self ):
        return ['m_ModuloOrdering',]
    
CLASSES.append  ( VTKExtractPointCloudPiece )        
TYPENAMES.append('VTKExtractPointCloudPieceType' )

#--------------------------------------------------------------
class VTKExtractPolyDataGeometry(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractPolyDataGeometryType'
    bl_label  = 'vtkExtractPolyDataGeometry'
    
    m_ExtractBoundaryCells = bpy.props.BoolProperty( name='ExtractBoundaryCells', default=0 )
    m_ExtractInside        = bpy.props.BoolProperty( name='ExtractInside',        default=1 )
    m_PassPoints           = bpy.props.BoolProperty( name='PassPoints',           default=0 )
    
    def m_properties( self ):
        return ['m_ExtractBoundaryCells','m_ExtractInside','m_PassPoints',]
    
CLASSES.append  ( VTKExtractPolyDataGeometry )        
TYPENAMES.append('VTKExtractPolyDataGeometryType' )

#--------------------------------------------------------------
class VTKExtractPolyDataPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractPolyDataPieceType'
    bl_label  = 'vtkExtractPolyDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKExtractPolyDataPiece )        
TYPENAMES.append('VTKExtractPolyDataPieceType' )

#--------------------------------------------------------------
class VTKExtractRectilinearGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractRectilinearGridType'
    bl_label  = 'vtkExtractRectilinearGrid'
    
    m_IncludeBoundary = bpy.props.BoolProperty     ( name='IncludeBoundary', default=0 )
    m_SampleRate      = bpy.props.IntVectorProperty( name='SampleRate',      default=[1, 1, 1], size=3 )
    m_VOI             = bpy.props.IntVectorProperty( name='VOI',             default=[0, 0, 0, 0, 0, 0], size=6 )
    
    def m_properties( self ):
        return ['m_IncludeBoundary','m_SampleRate','m_VOI',]
    
CLASSES.append  ( VTKExtractRectilinearGrid )        
TYPENAMES.append('VTKExtractRectilinearGridType' )

#--------------------------------------------------------------
class VTKExtractSurface(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractSurfaceType'
    bl_label  = 'vtkExtractSurface'
    
    m_ComputeGradients = bpy.props.BoolProperty ( name='ComputeGradients', default=0 )
    m_ComputeNormals   = bpy.props.BoolProperty ( name='ComputeNormals',   default=1 )
    m_HoleFilling      = bpy.props.BoolProperty ( name='HoleFilling',      default=False )
    m_Radius           = bpy.props.FloatProperty( name='Radius',           default=0.1 )
    
    def m_properties( self ):
        return ['m_ComputeGradients','m_ComputeNormals','m_HoleFilling','m_Radius',]
    
CLASSES.append  ( VTKExtractSurface )        
TYPENAMES.append('VTKExtractSurfaceType' )

#--------------------------------------------------------------
class VTKExtractTemporalFieldData(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractTemporalFieldDataType'
    bl_label  = 'vtkExtractTemporalFieldData'
    
    m_HandleCompositeDataBlocksIndividually = bpy.props.BoolProperty( name='HandleCompositeDataBlocksIndividually', default=True )
    
    def m_properties( self ):
        return ['m_HandleCompositeDataBlocksIndividually',]
    
CLASSES.append  ( VTKExtractTemporalFieldData )        
TYPENAMES.append('VTKExtractTemporalFieldDataType' )

#--------------------------------------------------------------
class VTKExtractTensorComponents(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractTensorComponentsType'
    bl_label  = 'vtkExtractTensorComponents'
    e_ScalarMode_items=[ (x,x,x) for x in ['Component', 'EffectiveStress', 'Determinant']]
    
    m_ExtractNormals      = bpy.props.BoolProperty     ( name='ExtractNormals',      default=0 )
    m_ExtractScalars      = bpy.props.BoolProperty     ( name='ExtractScalars',      default=0 )
    m_ExtractTCoords      = bpy.props.BoolProperty     ( name='ExtractTCoords',      default=0 )
    m_ExtractVectors      = bpy.props.BoolProperty     ( name='ExtractVectors',      default=0 )
    m_NormalizeNormals    = bpy.props.BoolProperty     ( name='NormalizeNormals',    default=1 )
    m_PassTensorsToOutput = bpy.props.BoolProperty     ( name='PassTensorsToOutput', default=0 )
    m_NumberOfTCoords     = bpy.props.IntProperty      ( name='NumberOfTCoords',     default=2 )
    e_ScalarMode          = bpy.props.EnumProperty     ( name='ScalarMode',          default="Component", items=e_ScalarMode_items )
    m_NormalComponents    = bpy.props.IntVectorProperty( name='NormalComponents',    default=[0, 1, 1, 1, 2, 1], size=6 )
    m_ScalarComponents    = bpy.props.IntVectorProperty( name='ScalarComponents',    default=[0, 0], size=2 )
    m_TCoordComponents    = bpy.props.IntVectorProperty( name='TCoordComponents',    default=[0, 2, 1, 2, 2, 2], size=6 )
    m_VectorComponents    = bpy.props.IntVectorProperty( name='VectorComponents',    default=[0, 0, 1, 0, 2, 0], size=6 )
    
    def m_properties( self ):
        return ['m_ExtractNormals','m_ExtractScalars','m_ExtractTCoords','m_ExtractVectors','m_NormalizeNormals','m_PassTensorsToOutput','m_NumberOfTCoords','e_ScalarMode','m_NormalComponents','m_ScalarComponents','m_TCoordComponents','m_VectorComponents',]
    
CLASSES.append  ( VTKExtractTensorComponents )        
TYPENAMES.append('VTKExtractTensorComponentsType' )

#--------------------------------------------------------------
class VTKExtractUnstructuredGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractUnstructuredGridType'
    bl_label  = 'vtkExtractUnstructuredGrid'
    
    m_CellClipping   = bpy.props.BoolProperty       ( name='CellClipping',   default=0 )
    m_ExtentClipping = bpy.props.BoolProperty       ( name='ExtentClipping', default=0 )
    m_Merging        = bpy.props.BoolProperty       ( name='Merging',        default=0 )
    m_PointClipping  = bpy.props.BoolProperty       ( name='PointClipping',  default=0 )
    m_CellMaximum    = bpy.props.IntProperty        ( name='CellMaximum',    default=0 )
    m_CellMinimum    = bpy.props.IntProperty        ( name='CellMinimum',    default=0 )
    m_PointMaximum   = bpy.props.IntProperty        ( name='PointMaximum',   default=0 )
    m_PointMinimum   = bpy.props.IntProperty        ( name='PointMinimum',   default=0 )
    m_Extent         = bpy.props.FloatVectorProperty( name='Extent',         default=(-1e+299, 1e+299, -1e+299, 1e+299, -1e+299, 1e+299), size=6 )
    
    def m_properties( self ):
        return ['m_CellClipping','m_ExtentClipping','m_Merging','m_PointClipping','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum','m_Extent',]
    
CLASSES.append  ( VTKExtractUnstructuredGrid )        
TYPENAMES.append('VTKExtractUnstructuredGridType' )

#--------------------------------------------------------------
class VTKExtractUnstructuredGridPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractUnstructuredGridPieceType'
    bl_label  = 'vtkExtractUnstructuredGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKExtractUnstructuredGridPiece )        
TYPENAMES.append('VTKExtractUnstructuredGridPieceType' )

#--------------------------------------------------------------
class VTKExtractUserDefinedPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractUserDefinedPieceType'
    bl_label  = 'vtkExtractUserDefinedPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKExtractUserDefinedPiece )        
TYPENAMES.append('VTKExtractUserDefinedPieceType' )

#--------------------------------------------------------------
class VTKExtractVOI(Node, VTKFilter1Node):

    bl_idname = 'VTKExtractVOIType'
    bl_label  = 'vtkExtractVOI'
    
    m_IncludeBoundary = bpy.props.BoolProperty     ( name='IncludeBoundary', default=0 )
    m_SampleRate      = bpy.props.IntVectorProperty( name='SampleRate',      default=[1, 1, 1], size=3 )
    m_VOI             = bpy.props.IntVectorProperty( name='VOI',             default=[0, 0, 0, 0, 0, 0], size=6 )
    
    def m_properties( self ):
        return ['m_IncludeBoundary','m_SampleRate','m_VOI',]
    
CLASSES.append  ( VTKExtractVOI )        
TYPENAMES.append('VTKExtractVOIType' )

#--------------------------------------------------------------
class VTKFeatureEdges(Node, VTKFilter1Node):

    bl_idname = 'VTKFeatureEdgesType'
    bl_label  = 'vtkFeatureEdges'
    
    m_BoundaryEdges    = bpy.props.BoolProperty ( name='BoundaryEdges',    default=1 )
    m_Coloring         = bpy.props.BoolProperty ( name='Coloring',         default=1 )
    m_FeatureEdges     = bpy.props.BoolProperty ( name='FeatureEdges',     default=1 )
    m_ManifoldEdges    = bpy.props.BoolProperty ( name='ManifoldEdges',    default=0 )
    m_NonManifoldEdges = bpy.props.BoolProperty ( name='NonManifoldEdges', default=1 )
    m_FeatureAngle     = bpy.props.FloatProperty( name='FeatureAngle',     default=30.0 )
    
    def m_properties( self ):
        return ['m_BoundaryEdges','m_Coloring','m_FeatureEdges','m_ManifoldEdges','m_NonManifoldEdges','m_FeatureAngle',]
    
CLASSES.append  ( VTKFeatureEdges )        
TYPENAMES.append('VTKFeatureEdgesType' )

#--------------------------------------------------------------
class VTKFieldDataToAttributeDataFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKFieldDataToAttributeDataFilterType'
    bl_label  = 'vtkFieldDataToAttributeDataFilter'
    e_InputField_items=[ (x,x,x) for x in ['DataObjectField', 'PointDataField', 'CellDataField']]
    e_OutputAttributeData_items=[ (x,x,x) for x in ['CellData', 'PointData']]
    
    m_DefaultNormalize    = bpy.props.BoolProperty( name='DefaultNormalize',    default=0 )
    e_InputField          = bpy.props.EnumProperty( name='InputField',          default="DataObjectField", items=e_InputField_items )
    e_OutputAttributeData = bpy.props.EnumProperty( name='OutputAttributeData', default="PointData", items=e_OutputAttributeData_items )
    
    def m_properties( self ):
        return ['m_DefaultNormalize','e_InputField','e_OutputAttributeData',]
    
CLASSES.append  ( VTKFieldDataToAttributeDataFilter )        
TYPENAMES.append('VTKFieldDataToAttributeDataFilterType' )

#--------------------------------------------------------------
class VTKFillHolesFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKFillHolesFilterType'
    bl_label  = 'vtkFillHolesFilter'
    
    m_HoleSize = bpy.props.FloatProperty( name='HoleSize', default=1.0 )
    
    def m_properties( self ):
        return ['m_HoleSize',]
    
CLASSES.append  ( VTKFillHolesFilter )        
TYPENAMES.append('VTKFillHolesFilterType' )

#--------------------------------------------------------------
class VTKFlyingEdgesPlaneCutter(Node, VTKFilter1Node):

    bl_idname = 'VTKFlyingEdgesPlaneCutterType'
    bl_label  = 'vtkFlyingEdgesPlaneCutter'
    
    m_ComputeNormals        = bpy.props.BoolProperty( name='ComputeNormals',        default=0 )
    m_InterpolateAttributes = bpy.props.BoolProperty( name='InterpolateAttributes', default=0 )
    m_ArrayComponent        = bpy.props.IntProperty ( name='ArrayComponent',        default=0 )
    
    def m_properties( self ):
        return ['m_ComputeNormals','m_InterpolateAttributes','m_ArrayComponent',]
    
CLASSES.append  ( VTKFlyingEdgesPlaneCutter )        
TYPENAMES.append('VTKFlyingEdgesPlaneCutterType' )

#--------------------------------------------------------------
class VTKForceTime(Node, VTKFilter1Node):

    bl_idname = 'VTKForceTimeType'
    bl_label  = 'vtkForceTime'
    
    m_IgnorePipelineTime = bpy.props.BoolProperty ( name='IgnorePipelineTime', default=True )
    m_ForcedTime         = bpy.props.FloatProperty( name='ForcedTime',         default=0.0 )
    
    def m_properties( self ):
        return ['m_IgnorePipelineTime','m_ForcedTime',]
    
CLASSES.append  ( VTKForceTime )        
TYPENAMES.append('VTKForceTimeType' )

#--------------------------------------------------------------
class VTKGaussianSplatter(Node, VTKFilter1Node):

    bl_idname = 'VTKGaussianSplatterType'
    bl_label  = 'vtkGaussianSplatter'
    e_AccumulationMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Sum']]
    
    m_Capping          = bpy.props.BoolProperty       ( name='Capping',          default=1 )
    m_NormalWarping    = bpy.props.BoolProperty       ( name='NormalWarping',    default=1 )
    m_ScalarWarping    = bpy.props.BoolProperty       ( name='ScalarWarping',    default=1 )
    m_CapValue         = bpy.props.FloatProperty      ( name='CapValue',         default=0.0 )
    m_Eccentricity     = bpy.props.FloatProperty      ( name='Eccentricity',     default=2.5 )
    m_ExponentFactor   = bpy.props.FloatProperty      ( name='ExponentFactor',   default=-5.0 )
    m_NullValue        = bpy.props.FloatProperty      ( name='NullValue',        default=0.0 )
    m_Radius           = bpy.props.FloatProperty      ( name='Radius',           default=0.1 )
    m_ScaleFactor      = bpy.props.FloatProperty      ( name='ScaleFactor',      default=1.0 )
    e_AccumulationMode = bpy.props.EnumProperty       ( name='AccumulationMode', default="Max", items=e_AccumulationMode_items )
    m_SampleDimensions = bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[50, 50, 50], size=3 )
    m_ModelBounds      = bpy.props.FloatVectorProperty( name='ModelBounds',      default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_Capping','m_NormalWarping','m_ScalarWarping','m_CapValue','m_Eccentricity','m_ExponentFactor','m_NullValue','m_Radius','m_ScaleFactor','e_AccumulationMode','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKGaussianSplatter )        
TYPENAMES.append('VTKGaussianSplatterType' )

#--------------------------------------------------------------
class VTKGenerateIndexArray(Node, VTKFilter1Node):

    bl_idname = 'VTKGenerateIndexArrayType'
    bl_label  = 'vtkGenerateIndexArray'
    
    m_ArrayName          = bpy.props.StringProperty( name='ArrayName',          default="index" )
    m_ReferenceArrayName = bpy.props.StringProperty( name='ReferenceArrayName', default="" )
    m_FieldType          = bpy.props.IntProperty   ( name='FieldType',          default=0 )
    m_PedigreeID         = bpy.props.IntProperty   ( name='PedigreeID',         default=0 )
    
    def m_properties( self ):
        return ['m_ArrayName','m_ReferenceArrayName','m_FieldType','m_PedigreeID',]
    
CLASSES.append  ( VTKGenerateIndexArray )        
TYPENAMES.append('VTKGenerateIndexArrayType' )

#--------------------------------------------------------------
class VTKGenericDataSetTessellator(Node, VTKFilter1Node):

    bl_idname = 'VTKGenericDataSetTessellatorType'
    bl_label  = 'vtkGenericDataSetTessellator'
    
    m_KeepCellIds = bpy.props.BoolProperty( name='KeepCellIds', default=1 )
    m_Merging     = bpy.props.BoolProperty( name='Merging',     default=1 )
    
    def m_properties( self ):
        return ['m_KeepCellIds','m_Merging',]
    
CLASSES.append  ( VTKGenericDataSetTessellator )        
TYPENAMES.append('VTKGenericDataSetTessellatorType' )

#--------------------------------------------------------------
class VTKGenericOutlineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKGenericOutlineFilterType'
    bl_label  = 'vtkGenericOutlineFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKGenericOutlineFilter )        
TYPENAMES.append('VTKGenericOutlineFilterType' )

#--------------------------------------------------------------
class VTKGeoAdaptiveArcs(Node, VTKFilter1Node):

    bl_idname = 'VTKGeoAdaptiveArcsType'
    bl_label  = 'vtkGeoAdaptiveArcs'
    
    m_GlobeRadius            = bpy.props.FloatProperty( name='GlobeRadius',            default=6356750.0 )
    m_MaximumPixelSeparation = bpy.props.FloatProperty( name='MaximumPixelSeparation', default=10.0 )
    m_MinimumPixelSeparation = bpy.props.FloatProperty( name='MinimumPixelSeparation', default=1.0 )
    
    def m_properties( self ):
        return ['m_GlobeRadius','m_MaximumPixelSeparation','m_MinimumPixelSeparation',]
    
CLASSES.append  ( VTKGeoAdaptiveArcs )        
TYPENAMES.append('VTKGeoAdaptiveArcsType' )

#--------------------------------------------------------------
class VTKGeoArcs(Node, VTKFilter1Node):

    bl_idname = 'VTKGeoArcsType'
    bl_label  = 'vtkGeoArcs'
    
    m_NumberOfSubdivisions = bpy.props.IntProperty  ( name='NumberOfSubdivisions', default=20 )
    m_ExplodeFactor        = bpy.props.FloatProperty( name='ExplodeFactor',        default=0.2 )
    m_GlobeRadius          = bpy.props.FloatProperty( name='GlobeRadius',          default=6356750.0 )
    
    def m_properties( self ):
        return ['m_NumberOfSubdivisions','m_ExplodeFactor','m_GlobeRadius',]
    
CLASSES.append  ( VTKGeoArcs )        
TYPENAMES.append('VTKGeoArcsType' )

#--------------------------------------------------------------
class VTKGeoAssignCoordinates(Node, VTKFilter1Node):

    bl_idname = 'VTKGeoAssignCoordinatesType'
    bl_label  = 'vtkGeoAssignCoordinates'
    
    m_CoordinatesInArrays = bpy.props.BoolProperty  ( name='CoordinatesInArrays', default=True )
    m_LatitudeArrayName   = bpy.props.StringProperty( name='LatitudeArrayName',   default="" )
    m_LongitudeArrayName  = bpy.props.StringProperty( name='LongitudeArrayName',  default="" )
    m_GlobeRadius         = bpy.props.FloatProperty ( name='GlobeRadius',         default=6356750.0 )
    
    def m_properties( self ):
        return ['m_CoordinatesInArrays','m_LatitudeArrayName','m_LongitudeArrayName','m_GlobeRadius',]
    
CLASSES.append  ( VTKGeoAssignCoordinates )        
TYPENAMES.append('VTKGeoAssignCoordinatesType' )

#--------------------------------------------------------------
class VTKGeoSampleArcs(Node, VTKFilter1Node):

    bl_idname = 'VTKGeoSampleArcsType'
    bl_label  = 'vtkGeoSampleArcs'
    e_InputCoordinateSystem_items=[ (x,x,x) for x in ['Rectangular', 'Spherical']]
    e_OutputCoordinateSystem_items=[ (x,x,x) for x in ['Rectangular', 'Spherical']]
    
    m_GlobeRadius            = bpy.props.FloatProperty( name='GlobeRadius',            default=6356750.0 )
    m_MaximumDistanceMeters  = bpy.props.FloatProperty( name='MaximumDistanceMeters',  default=100000.0 )
    e_InputCoordinateSystem  = bpy.props.EnumProperty ( name='InputCoordinateSystem',  default="Rectangular", items=e_InputCoordinateSystem_items )
    e_OutputCoordinateSystem = bpy.props.EnumProperty ( name='OutputCoordinateSystem', default="Rectangular", items=e_OutputCoordinateSystem_items )
    
    def m_properties( self ):
        return ['m_GlobeRadius','m_MaximumDistanceMeters','e_InputCoordinateSystem','e_OutputCoordinateSystem',]
    
CLASSES.append  ( VTKGeoSampleArcs )        
TYPENAMES.append('VTKGeoSampleArcsType' )

#--------------------------------------------------------------
class VTKGeometryFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKGeometryFilterType'
    bl_label  = 'vtkGeometryFilter'
    
    m_CellClipping   = bpy.props.BoolProperty       ( name='CellClipping',   default=0 )
    m_ExtentClipping = bpy.props.BoolProperty       ( name='ExtentClipping', default=0 )
    m_Merging        = bpy.props.BoolProperty       ( name='Merging',        default=1 )
    m_PointClipping  = bpy.props.BoolProperty       ( name='PointClipping',  default=0 )
    m_CellMaximum    = bpy.props.IntProperty        ( name='CellMaximum',    default=0 )
    m_CellMinimum    = bpy.props.IntProperty        ( name='CellMinimum',    default=0 )
    m_PointMaximum   = bpy.props.IntProperty        ( name='PointMaximum',   default=0 )
    m_PointMinimum   = bpy.props.IntProperty        ( name='PointMinimum',   default=0 )
    m_Extent         = bpy.props.FloatVectorProperty( name='Extent',         default=(-1e+299, 1e+299, -1e+299, 1e+299, -1e+299, 1e+299), size=6 )
    
    def m_properties( self ):
        return ['m_CellClipping','m_ExtentClipping','m_Merging','m_PointClipping','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum','m_Extent',]
    
CLASSES.append  ( VTKGeometryFilter )        
TYPENAMES.append('VTKGeometryFilterType' )

#--------------------------------------------------------------
class VTKGradientFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKGradientFilterType'
    bl_label  = 'vtkGradientFilter'
    
    m_ComputeDivergence   = bpy.props.BoolProperty  ( name='ComputeDivergence',   default=0 )
    m_ComputeGradient     = bpy.props.BoolProperty  ( name='ComputeGradient',     default=1 )
    m_ComputeQCriterion   = bpy.props.BoolProperty  ( name='ComputeQCriterion',   default=0 )
    m_ComputeVorticity    = bpy.props.BoolProperty  ( name='ComputeVorticity',    default=0 )
    m_FasterApproximation = bpy.props.BoolProperty  ( name='FasterApproximation', default=0 )
    m_DivergenceArrayName = bpy.props.StringProperty( name='DivergenceArrayName', default="" )
    m_QCriterionArrayName = bpy.props.StringProperty( name='QCriterionArrayName', default="" )
    m_ResultArrayName     = bpy.props.StringProperty( name='ResultArrayName',     default="" )
    m_VorticityArrayName  = bpy.props.StringProperty( name='VorticityArrayName',  default="" )
    
    def m_properties( self ):
        return ['m_ComputeDivergence','m_ComputeGradient','m_ComputeQCriterion','m_ComputeVorticity','m_FasterApproximation','m_DivergenceArrayName','m_QCriterionArrayName','m_ResultArrayName','m_VorticityArrayName',]
    
CLASSES.append  ( VTKGradientFilter )        
TYPENAMES.append('VTKGradientFilterType' )

#--------------------------------------------------------------
class VTKGraphAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKGraphAlgorithmType'
    bl_label  = 'vtkGraphAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKGraphAlgorithm )        
TYPENAMES.append('VTKGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKGraphLayout(Node, VTKFilter1Node):

    bl_idname = 'VTKGraphLayoutType'
    bl_label  = 'vtkGraphLayout'
    
    m_UseTransform = bpy.props.BoolProperty ( name='UseTransform', default=False )
    m_ZRange       = bpy.props.FloatProperty( name='ZRange',       default=0.0 )
    
    def m_properties( self ):
        return ['m_UseTransform','m_ZRange',]
    
CLASSES.append  ( VTKGraphLayout )        
TYPENAMES.append('VTKGraphLayoutType' )

#--------------------------------------------------------------
class VTKGraphLayoutFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKGraphLayoutFilterType'
    bl_label  = 'vtkGraphLayoutFilter'
    
    m_AutomaticBoundsComputation = bpy.props.BoolProperty       ( name='AutomaticBoundsComputation', default=1 )
    m_ThreeDimensionalLayout     = bpy.props.BoolProperty       ( name='ThreeDimensionalLayout',     default=1 )
    m_MaxNumberOfIterations      = bpy.props.IntProperty        ( name='MaxNumberOfIterations',      default=50 )
    m_CoolDownRate               = bpy.props.FloatProperty      ( name='CoolDownRate',               default=10.0 )
    m_GraphBounds                = bpy.props.FloatVectorProperty( name='GraphBounds',                default=(-0.5, 0.5, -0.5, 0.5, -0.5, 0.5), size=6 )
    
    def m_properties( self ):
        return ['m_AutomaticBoundsComputation','m_ThreeDimensionalLayout','m_MaxNumberOfIterations','m_CoolDownRate','m_GraphBounds',]
    
CLASSES.append  ( VTKGraphLayoutFilter )        
TYPENAMES.append('VTKGraphLayoutFilterType' )

#--------------------------------------------------------------
class VTKGraphToGlyphs(Node, VTKFilter1Node):

    bl_idname = 'VTKGraphToGlyphsType'
    bl_label  = 'vtkGraphToGlyphs'
    
    m_Filled     = bpy.props.BoolProperty ( name='Filled',     default=True )
    m_Scaling    = bpy.props.BoolProperty ( name='Scaling',    default=False )
    m_GlyphType  = bpy.props.IntProperty  ( name='GlyphType',  default=7 )
    m_ScreenSize = bpy.props.FloatProperty( name='ScreenSize', default=10.0 )
    
    def m_properties( self ):
        return ['m_Filled','m_Scaling','m_GlyphType','m_ScreenSize',]
    
CLASSES.append  ( VTKGraphToGlyphs )        
TYPENAMES.append('VTKGraphToGlyphsType' )

#--------------------------------------------------------------
class VTKGraphToPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKGraphToPointsType'
    bl_label  = 'vtkGraphToPoints'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKGraphToPoints )        
TYPENAMES.append('VTKGraphToPointsType' )

#--------------------------------------------------------------
class VTKGraphWeightEuclideanDistanceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKGraphWeightEuclideanDistanceFilterType'
    bl_label  = 'vtkGraphWeightEuclideanDistanceFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKGraphWeightEuclideanDistanceFilter )        
TYPENAMES.append('VTKGraphWeightEuclideanDistanceFilterType' )

#--------------------------------------------------------------
class VTKGreedyTerrainDecimation(Node, VTKFilter1Node):

    bl_idname = 'VTKGreedyTerrainDecimationType'
    bl_label  = 'vtkGreedyTerrainDecimation'
    e_ErrorMeasure_items=[ (x,x,x) for x in ['NumberOfTriangles', 'SpecifiedReduction', 'AbsoluteError', 'RelativeError']]
    
    m_BoundaryVertexDeletion = bpy.props.BoolProperty ( name='BoundaryVertexDeletion', default=1 )
    m_ComputeNormals         = bpy.props.BoolProperty ( name='ComputeNormals',         default=0 )
    m_NumberOfTriangles      = bpy.props.IntProperty  ( name='NumberOfTriangles',      default=1000 )
    m_AbsoluteError          = bpy.props.FloatProperty( name='AbsoluteError',          default=1.0 )
    m_Reduction              = bpy.props.FloatProperty( name='Reduction',              default=0.9 )
    m_RelativeError          = bpy.props.FloatProperty( name='RelativeError',          default=0.01 )
    e_ErrorMeasure           = bpy.props.EnumProperty ( name='ErrorMeasure',           default="SpecifiedReduction", items=e_ErrorMeasure_items )
    
    def m_properties( self ):
        return ['m_BoundaryVertexDeletion','m_ComputeNormals','m_NumberOfTriangles','m_AbsoluteError','m_Reduction','m_RelativeError','e_ErrorMeasure',]
    
CLASSES.append  ( VTKGreedyTerrainDecimation )        
TYPENAMES.append('VTKGreedyTerrainDecimationType' )

#--------------------------------------------------------------
class VTKGroupLeafVertices(Node, VTKFilter1Node):

    bl_idname = 'VTKGroupLeafVerticesType'
    bl_label  = 'vtkGroupLeafVertices'
    
    m_GroupDomain = bpy.props.StringProperty( name='GroupDomain', default="group_vertex" )
    
    def m_properties( self ):
        return ['m_GroupDomain',]
    
CLASSES.append  ( VTKGroupLeafVertices )        
TYPENAMES.append('VTKGroupLeafVerticesType' )

#--------------------------------------------------------------
class VTKHedgeHog(Node, VTKFilter1Node):

    bl_idname = 'VTKHedgeHogType'
    bl_label  = 'vtkHedgeHog'
    e_VectorMode_items=[ (x,x,x) for x in ['UseVector', 'UseNormal']]
    
    m_ScaleFactor = bpy.props.FloatProperty( name='ScaleFactor', default=1.0 )
    e_VectorMode  = bpy.props.EnumProperty ( name='VectorMode',  default="UseVector", items=e_VectorMode_items )
    
    def m_properties( self ):
        return ['m_ScaleFactor','e_VectorMode',]
    
CLASSES.append  ( VTKHedgeHog )        
TYPENAMES.append('VTKHedgeHogType' )

#--------------------------------------------------------------
class VTKHierarchicalBinningFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKHierarchicalBinningFilterType'
    bl_label  = 'vtkHierarchicalBinningFilter'
    
    m_Automatic      = bpy.props.BoolProperty       ( name='Automatic',      default=True )
    m_NumberOfLevels = bpy.props.IntProperty        ( name='NumberOfLevels', default=3 )
    m_Divisions      = bpy.props.IntVectorProperty  ( name='Divisions',      default=[2, 2, 2], size=3 )
    m_Bounds         = bpy.props.FloatVectorProperty( name='Bounds',         default=(0.0, 1.0, 0.0, 1.0, 0.0, 1.0), size=6 )
    
    def m_properties( self ):
        return ['m_Automatic','m_NumberOfLevels','m_Divisions','m_Bounds',]
    
CLASSES.append  ( VTKHierarchicalBinningFilter )        
TYPENAMES.append('VTKHierarchicalBinningFilterType' )

#--------------------------------------------------------------
class VTKHierarchicalBoxDataSetAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKHierarchicalBoxDataSetAlgorithmType'
    bl_label  = 'vtkHierarchicalBoxDataSetAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHierarchicalBoxDataSetAlgorithm )        
TYPENAMES.append('VTKHierarchicalBoxDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKHierarchicalDataExtractDataSets(Node, VTKFilter1Node):

    bl_idname = 'VTKHierarchicalDataExtractDataSetsType'
    bl_label  = 'vtkHierarchicalDataExtractDataSets'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHierarchicalDataExtractDataSets )        
TYPENAMES.append('VTKHierarchicalDataExtractDataSetsType' )

#--------------------------------------------------------------
class VTKHierarchicalDataExtractLevel(Node, VTKFilter1Node):

    bl_idname = 'VTKHierarchicalDataExtractLevelType'
    bl_label  = 'vtkHierarchicalDataExtractLevel'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHierarchicalDataExtractLevel )        
TYPENAMES.append('VTKHierarchicalDataExtractLevelType' )

#--------------------------------------------------------------
class VTKHierarchicalDataLevelFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKHierarchicalDataLevelFilterType'
    bl_label  = 'vtkHierarchicalDataLevelFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHierarchicalDataLevelFilter )        
TYPENAMES.append('VTKHierarchicalDataLevelFilterType' )

#--------------------------------------------------------------
class VTKHierarchicalDataSetGeometryFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKHierarchicalDataSetGeometryFilterType'
    bl_label  = 'vtkHierarchicalDataSetGeometryFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHierarchicalDataSetGeometryFilter )        
TYPENAMES.append('VTKHierarchicalDataSetGeometryFilterType' )

#--------------------------------------------------------------
class VTKHull(Node, VTKFilter1Node):

    bl_idname = 'VTKHullType'
    bl_label  = 'vtkHull'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHull )        
TYPENAMES.append('VTKHullType' )

#--------------------------------------------------------------
class VTKHyperOctreeDepth(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperOctreeDepthType'
    bl_label  = 'vtkHyperOctreeDepth'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHyperOctreeDepth )        
TYPENAMES.append('VTKHyperOctreeDepthType' )

#--------------------------------------------------------------
class VTKHyperOctreeLimiter(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperOctreeLimiterType'
    bl_label  = 'vtkHyperOctreeLimiter'
    
    m_MaximumLevel = bpy.props.IntProperty( name='MaximumLevel', default=5 )
    
    def m_properties( self ):
        return ['m_MaximumLevel',]
    
CLASSES.append  ( VTKHyperOctreeLimiter )        
TYPENAMES.append('VTKHyperOctreeLimiterType' )

#--------------------------------------------------------------
class VTKHyperOctreeSurfaceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperOctreeSurfaceFilterType'
    bl_label  = 'vtkHyperOctreeSurfaceFilter'
    
    m_Merging            = bpy.props.BoolProperty( name='Merging',            default=0 )
    m_PassThroughCellIds = bpy.props.BoolProperty( name='PassThroughCellIds', default=0 )
    
    def m_properties( self ):
        return ['m_Merging','m_PassThroughCellIds',]
    
CLASSES.append  ( VTKHyperOctreeSurfaceFilter )        
TYPENAMES.append('VTKHyperOctreeSurfaceFilterType' )

#--------------------------------------------------------------
class VTKHyperOctreeToUniformGridFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperOctreeToUniformGridFilterType'
    bl_label  = 'vtkHyperOctreeToUniformGridFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHyperOctreeToUniformGridFilter )        
TYPENAMES.append('VTKHyperOctreeToUniformGridFilterType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisCut(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperTreeGridAxisCutType'
    bl_label  = 'vtkHyperTreeGridAxisCut'
    
    m_PlaneNormalAxis = bpy.props.IntProperty  ( name='PlaneNormalAxis', default=0 )
    m_PlanePosition   = bpy.props.FloatProperty( name='PlanePosition',   default=0.0 )
    
    def m_properties( self ):
        return ['m_PlaneNormalAxis','m_PlanePosition',]
    
CLASSES.append  ( VTKHyperTreeGridAxisCut )        
TYPENAMES.append('VTKHyperTreeGridAxisCutType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGeometry(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperTreeGridGeometryType'
    bl_label  = 'vtkHyperTreeGridGeometry'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHyperTreeGridGeometry )        
TYPENAMES.append('VTKHyperTreeGridGeometryType' )

#--------------------------------------------------------------
class VTKHyperTreeGridToUnstructuredGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKHyperTreeGridToUnstructuredGridType'
    bl_label  = 'vtkHyperTreeGridToUnstructuredGrid'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKHyperTreeGridToUnstructuredGrid )        
TYPENAMES.append('VTKHyperTreeGridToUnstructuredGridType' )

#--------------------------------------------------------------
class VTKIconGlyphFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKIconGlyphFilterType'
    bl_label  = 'vtkIconGlyphFilter'
    e_Gravity_items=[ (x,x,x) for x in ['TopRight', 'TopCenter', 'TopLeft', 'CenterRight', 'CenterCenter', 'CenterLeft', 'BottomRight', 'BottomCenter', 'BottomLeft']]
    e_IconScaling_items=[ (x,x,x) for x in ['ScalingOff', 'ScalingArray']]
    
    m_PassScalars   = bpy.props.BoolProperty     ( name='PassScalars',   default=False )
    m_UseIconSize   = bpy.props.BoolProperty     ( name='UseIconSize',   default=True )
    e_Gravity       = bpy.props.EnumProperty     ( name='Gravity',       default="CenterCenter", items=e_Gravity_items )
    e_IconScaling   = bpy.props.EnumProperty     ( name='IconScaling',   default="ScalingOff", items=e_IconScaling_items )
    m_DisplaySize   = bpy.props.IntVectorProperty( name='DisplaySize',   default=[25, 25], size=2 )
    m_IconSheetSize = bpy.props.IntVectorProperty( name='IconSheetSize', default=[1, 1], size=2 )
    m_IconSize      = bpy.props.IntVectorProperty( name='IconSize',      default=[1, 1], size=2 )
    m_Offset        = bpy.props.IntVectorProperty( name='Offset',        default=[0, 0], size=2 )
    
    def m_properties( self ):
        return ['m_PassScalars','m_UseIconSize','e_Gravity','e_IconScaling','m_DisplaySize','m_IconSheetSize','m_IconSize','m_Offset',]
    
CLASSES.append  ( VTKIconGlyphFilter )        
TYPENAMES.append('VTKIconGlyphFilterType' )

#--------------------------------------------------------------
class VTKIdFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKIdFilterType'
    bl_label  = 'vtkIdFilter'
    
    m_CellIds      = bpy.props.BoolProperty  ( name='CellIds',      default=1 )
    m_FieldData    = bpy.props.BoolProperty  ( name='FieldData',    default=0 )
    m_PointIds     = bpy.props.BoolProperty  ( name='PointIds',     default=1 )
    m_IdsArrayName = bpy.props.StringProperty( name='IdsArrayName', default="vtkIdFilter_Ids" )
    
    def m_properties( self ):
        return ['m_CellIds','m_FieldData','m_PointIds','m_IdsArrayName',]
    
CLASSES.append  ( VTKIdFilter )        
TYPENAMES.append('VTKIdFilterType' )

#--------------------------------------------------------------
class VTKImageAnisotropicDiffusion2D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageAnisotropicDiffusion2DType'
    bl_label  = 'vtkImageAnisotropicDiffusion2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Corners                    = bpy.props.BoolProperty     ( name='Corners',                    default=1 )
    m_Edges                      = bpy.props.BoolProperty     ( name='Edges',                      default=1 )
    m_EnableSMP                  = bpy.props.BoolProperty     ( name='EnableSMP',                  default=False )
    m_Faces                      = bpy.props.BoolProperty     ( name='Faces',                      default=1 )
    m_GlobalDefaultEnableSMP     = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',     default=False )
    m_GradientMagnitudeThreshold = bpy.props.BoolProperty     ( name='GradientMagnitudeThreshold', default=0 )
    m_DesiredBytesPerPiece       = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',       default=65536 )
    m_NumberOfIterations         = bpy.props.IntProperty      ( name='NumberOfIterations',         default=4 )
    m_NumberOfThreads            = bpy.props.IntProperty      ( name='NumberOfThreads',            default=8 )
    m_DiffusionFactor            = bpy.props.FloatProperty    ( name='DiffusionFactor',            default=1.0 )
    m_DiffusionThreshold         = bpy.props.FloatProperty    ( name='DiffusionThreshold',         default=5.0 )
    e_SplitMode                  = bpy.props.EnumProperty     ( name='SplitMode',                  default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize           = bpy.props.IntVectorProperty( name='MinimumPieceSize',           default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_Corners','m_Edges','m_EnableSMP','m_Faces','m_GlobalDefaultEnableSMP','m_GradientMagnitudeThreshold','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','m_DiffusionFactor','m_DiffusionThreshold','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageAnisotropicDiffusion2D )        
TYPENAMES.append('VTKImageAnisotropicDiffusion2DType' )

#--------------------------------------------------------------
class VTKImageAnisotropicDiffusion3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageAnisotropicDiffusion3DType'
    bl_label  = 'vtkImageAnisotropicDiffusion3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Corners                    = bpy.props.BoolProperty     ( name='Corners',                    default=1 )
    m_Edges                      = bpy.props.BoolProperty     ( name='Edges',                      default=1 )
    m_EnableSMP                  = bpy.props.BoolProperty     ( name='EnableSMP',                  default=False )
    m_Faces                      = bpy.props.BoolProperty     ( name='Faces',                      default=1 )
    m_GlobalDefaultEnableSMP     = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP',     default=False )
    m_GradientMagnitudeThreshold = bpy.props.BoolProperty     ( name='GradientMagnitudeThreshold', default=0 )
    m_DesiredBytesPerPiece       = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',       default=65536 )
    m_NumberOfIterations         = bpy.props.IntProperty      ( name='NumberOfIterations',         default=4 )
    m_NumberOfThreads            = bpy.props.IntProperty      ( name='NumberOfThreads',            default=8 )
    m_DiffusionFactor            = bpy.props.FloatProperty    ( name='DiffusionFactor',            default=1.0 )
    m_DiffusionThreshold         = bpy.props.FloatProperty    ( name='DiffusionThreshold',         default=5.0 )
    e_SplitMode                  = bpy.props.EnumProperty     ( name='SplitMode',                  default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize           = bpy.props.IntVectorProperty( name='MinimumPieceSize',           default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_Corners','m_Edges','m_EnableSMP','m_Faces','m_GlobalDefaultEnableSMP','m_GradientMagnitudeThreshold','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','m_DiffusionFactor','m_DiffusionThreshold','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageAnisotropicDiffusion3D )        
TYPENAMES.append('VTKImageAnisotropicDiffusion3DType' )

#--------------------------------------------------------------
class VTKImageAppend(Node, VTKFilter1Node):

    bl_idname = 'VTKImageAppendType'
    bl_label  = 'vtkImageAppend'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_PreserveExtents        = bpy.props.BoolProperty     ( name='PreserveExtents',        default=0 )
    m_AppendAxis             = bpy.props.IntProperty      ( name='AppendAxis',             default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PreserveExtents','m_AppendAxis','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageAppend )        
TYPENAMES.append('VTKImageAppendType' )

#--------------------------------------------------------------
class VTKImageAppendComponents(Node, VTKFilter1Node):

    bl_idname = 'VTKImageAppendComponentsType'
    bl_label  = 'vtkImageAppendComponents'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageAppendComponents )        
TYPENAMES.append('VTKImageAppendComponentsType' )

#--------------------------------------------------------------
class VTKImageBSplineCoefficients(Node, VTKFilter1Node):

    bl_idname = 'VTKImageBSplineCoefficientsType'
    bl_label  = 'vtkImageBSplineCoefficients'
    e_BorderMode_items=[ (x,x,x) for x in ['Clamp', 'Repeat', 'Mirror']]
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Bypass                 = bpy.props.BoolProperty     ( name='Bypass',                 default=0 )
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_SplineDegree           = bpy.props.IntProperty      ( name='SplineDegree',           default=3 )
    e_BorderMode             = bpy.props.EnumProperty     ( name='BorderMode',             default="Clamp", items=e_BorderMode_items )
    e_OutputScalarType       = bpy.props.EnumProperty     ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_Bypass','m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_SplineDegree','e_BorderMode','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageBSplineCoefficients )        
TYPENAMES.append('VTKImageBSplineCoefficientsType' )

#--------------------------------------------------------------
class VTKImageButterworthHighPass(Node, VTKFilter1Node):

    bl_idname = 'VTKImageButterworthHighPassType'
    bl_label  = 'vtkImageButterworthHighPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty       ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_Order                  = bpy.props.IntProperty        ( name='Order',                  default=1 )
    m_XCutOff                = bpy.props.FloatProperty      ( name='XCutOff',                default=1e+299 )
    m_YCutOff                = bpy.props.FloatProperty      ( name='YCutOff',                default=1e+299 )
    m_ZCutOff                = bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+299 )
    e_SplitMode              = bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                 = bpy.props.FloatVectorProperty( name='CutOff',                 default=(1e+299, 1e+299, 1e+299), size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Order','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    
CLASSES.append  ( VTKImageButterworthHighPass )        
TYPENAMES.append('VTKImageButterworthHighPassType' )

#--------------------------------------------------------------
class VTKImageButterworthLowPass(Node, VTKFilter1Node):

    bl_idname = 'VTKImageButterworthLowPassType'
    bl_label  = 'vtkImageButterworthLowPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty       ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_Order                  = bpy.props.IntProperty        ( name='Order',                  default=1 )
    m_XCutOff                = bpy.props.FloatProperty      ( name='XCutOff',                default=1e+299 )
    m_YCutOff                = bpy.props.FloatProperty      ( name='YCutOff',                default=1e+299 )
    m_ZCutOff                = bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+299 )
    e_SplitMode              = bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                 = bpy.props.FloatVectorProperty( name='CutOff',                 default=(1e+299, 1e+299, 1e+299), size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Order','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    
CLASSES.append  ( VTKImageButterworthLowPass )        
TYPENAMES.append('VTKImageButterworthLowPassType' )

#--------------------------------------------------------------
class VTKImageCacheFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKImageCacheFilterType'
    bl_label  = 'vtkImageCacheFilter'
    
    m_CacheSize = bpy.props.IntProperty( name='CacheSize', default=10 )
    
    def m_properties( self ):
        return ['m_CacheSize',]
    
CLASSES.append  ( VTKImageCacheFilter )        
TYPENAMES.append('VTKImageCacheFilterType' )

#--------------------------------------------------------------
class VTKImageCast(Node, VTKFilter1Node):

    bl_idname = 'VTKImageCastType'
    bl_label  = 'vtkImageCast'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ClampOverflow          = bpy.props.BoolProperty     ( name='ClampOverflow',          default=0 )
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputScalarType       = bpy.props.EnumProperty     ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_ClampOverflow','m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageCast )        
TYPENAMES.append('VTKImageCastType' )

#--------------------------------------------------------------
class VTKImageCityBlockDistance(Node, VTKFilter1Node):

    bl_idname = 'VTKImageCityBlockDistanceType'
    bl_label  = 'vtkImageCityBlockDistance'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageCityBlockDistance )        
TYPENAMES.append('VTKImageCityBlockDistanceType' )

#--------------------------------------------------------------
class VTKImageContinuousDilate3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageContinuousDilate3DType'
    bl_label  = 'vtkImageContinuousDilate3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize             = bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageContinuousDilate3D )        
TYPENAMES.append('VTKImageContinuousDilate3DType' )

#--------------------------------------------------------------
class VTKImageContinuousErode3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageContinuousErode3DType'
    bl_label  = 'vtkImageContinuousErode3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize             = bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageContinuousErode3D )        
TYPENAMES.append('VTKImageContinuousErode3DType' )

#--------------------------------------------------------------
class VTKImageCursor3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageCursor3DType'
    bl_label  = 'vtkImageCursor3D'
    
    m_CursorRadius   = bpy.props.IntProperty        ( name='CursorRadius',   default=5 )
    m_CursorValue    = bpy.props.FloatProperty      ( name='CursorValue',    default=255.0 )
    m_CursorPosition = bpy.props.FloatVectorProperty( name='CursorPosition', default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_CursorRadius','m_CursorValue','m_CursorPosition',]
    
CLASSES.append  ( VTKImageCursor3D )        
TYPENAMES.append('VTKImageCursor3DType' )

#--------------------------------------------------------------
class VTKImageDataStreamer(Node, VTKFilter1Node):

    bl_idname = 'VTKImageDataStreamerType'
    bl_label  = 'vtkImageDataStreamer'
    
    m_NumberOfStreamDivisions = bpy.props.IntProperty( name='NumberOfStreamDivisions', default=10 )
    
    def m_properties( self ):
        return ['m_NumberOfStreamDivisions',]
    
CLASSES.append  ( VTKImageDataStreamer )        
TYPENAMES.append('VTKImageDataStreamerType' )

#--------------------------------------------------------------
class VTKImageDataToPointSet(Node, VTKFilter1Node):

    bl_idname = 'VTKImageDataToPointSetType'
    bl_label  = 'vtkImageDataToPointSet'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKImageDataToPointSet )        
TYPENAMES.append('VTKImageDataToPointSetType' )

#--------------------------------------------------------------
class VTKImageDataToUniformGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKImageDataToUniformGridType'
    bl_label  = 'vtkImageDataToUniformGrid'
    
    m_Reverse = bpy.props.BoolProperty( name='Reverse', default=0 )
    
    def m_properties( self ):
        return ['m_Reverse',]
    
CLASSES.append  ( VTKImageDataToUniformGrid )        
TYPENAMES.append('VTKImageDataToUniformGridType' )

#--------------------------------------------------------------
class VTKImageDilateErode3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageDilateErode3DType'
    bl_label  = 'vtkImageDilateErode3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_DilateValue            = bpy.props.FloatProperty    ( name='DilateValue',            default=0.0 )
    m_ErodeValue             = bpy.props.FloatProperty    ( name='ErodeValue',             default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize             = bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_DilateValue','m_ErodeValue','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageDilateErode3D )        
TYPENAMES.append('VTKImageDilateErode3DType' )

#--------------------------------------------------------------
class VTKImageDivergence(Node, VTKFilter1Node):

    bl_idname = 'VTKImageDivergenceType'
    bl_label  = 'vtkImageDivergence'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageDivergence )        
TYPENAMES.append('VTKImageDivergenceType' )

#--------------------------------------------------------------
class VTKImageEuclideanDistance(Node, VTKFilter1Node):

    bl_idname = 'VTKImageEuclideanDistanceType'
    bl_label  = 'vtkImageEuclideanDistance'
    e_Algorithm_items=[ (x,x,x) for x in ['SaitoCached', 'Saito']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ConsiderAnisotropy     = bpy.props.BoolProperty     ( name='ConsiderAnisotropy',     default=1 )
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_Initialize             = bpy.props.BoolProperty     ( name='Initialize',             default=1 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_MaximumDistance        = bpy.props.FloatProperty    ( name='MaximumDistance',        default=2147483647.0 )
    e_Algorithm              = bpy.props.EnumProperty     ( name='Algorithm',              default="Saito", items=e_Algorithm_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_ConsiderAnisotropy','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Initialize','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','m_MaximumDistance','e_Algorithm','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageEuclideanDistance )        
TYPENAMES.append('VTKImageEuclideanDistanceType' )

#--------------------------------------------------------------
class VTKImageEuclideanToPolar(Node, VTKFilter1Node):

    bl_idname = 'VTKImageEuclideanToPolarType'
    bl_label  = 'vtkImageEuclideanToPolar'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_ThetaMaximum           = bpy.props.FloatProperty    ( name='ThetaMaximum',           default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_ThetaMaximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageEuclideanToPolar )        
TYPENAMES.append('VTKImageEuclideanToPolarType' )

#--------------------------------------------------------------
class VTKImageFFT(Node, VTKFilter1Node):

    bl_idname = 'VTKImageFFTType'
    bl_label  = 'vtkImageFFT'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageFFT )        
TYPENAMES.append('VTKImageFFTType' )

#--------------------------------------------------------------
class VTKImageFourierCenter(Node, VTKFilter1Node):

    bl_idname = 'VTKImageFourierCenterType'
    bl_label  = 'vtkImageFourierCenter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageFourierCenter )        
TYPENAMES.append('VTKImageFourierCenterType' )

#--------------------------------------------------------------
class VTKImageGaussianSmooth(Node, VTKFilter1Node):

    bl_idname = 'VTKImageGaussianSmoothType'
    bl_label  = 'vtkImageGaussianSmooth'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty       ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty        ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_RadiusFactors          = bpy.props.FloatVectorProperty( name='RadiusFactors',          default=(1.5, 1.5, 1.5), size=3 )
    m_StandardDeviations     = bpy.props.FloatVectorProperty( name='StandardDeviations',     default=(2.0, 2.0, 2.0), size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_RadiusFactors','m_StandardDeviations',]
    
CLASSES.append  ( VTKImageGaussianSmooth )        
TYPENAMES.append('VTKImageGaussianSmoothType' )

#--------------------------------------------------------------
class VTKImageGradient(Node, VTKFilter1Node):

    bl_idname = 'VTKImageGradientType'
    bl_label  = 'vtkImageGradient'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_HandleBoundaries       = bpy.props.BoolProperty     ( name='HandleBoundaries',       default=1 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageGradient )        
TYPENAMES.append('VTKImageGradientType' )

#--------------------------------------------------------------
class VTKImageGradientMagnitude(Node, VTKFilter1Node):

    bl_idname = 'VTKImageGradientMagnitudeType'
    bl_label  = 'vtkImageGradientMagnitude'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_HandleBoundaries       = bpy.props.BoolProperty     ( name='HandleBoundaries',       default=1 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageGradientMagnitude )        
TYPENAMES.append('VTKImageGradientMagnitudeType' )

#--------------------------------------------------------------
class VTKImageHSIToRGB(Node, VTKFilter1Node):

    bl_idname = 'VTKImageHSIToRGBType'
    bl_label  = 'vtkImageHSIToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum                = bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageHSIToRGB )        
TYPENAMES.append('VTKImageHSIToRGBType' )

#--------------------------------------------------------------
class VTKImageHSVToRGB(Node, VTKFilter1Node):

    bl_idname = 'VTKImageHSVToRGBType'
    bl_label  = 'vtkImageHSVToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum                = bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageHSVToRGB )        
TYPENAMES.append('VTKImageHSVToRGBType' )

#--------------------------------------------------------------
class VTKImageHybridMedian2D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageHybridMedian2DType'
    bl_label  = 'vtkImageHybridMedian2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageHybridMedian2D )        
TYPENAMES.append('VTKImageHybridMedian2DType' )

#--------------------------------------------------------------
class VTKImageIdealHighPass(Node, VTKFilter1Node):

    bl_idname = 'VTKImageIdealHighPassType'
    bl_label  = 'vtkImageIdealHighPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty       ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_XCutOff                = bpy.props.FloatProperty      ( name='XCutOff',                default=1e+299 )
    m_YCutOff                = bpy.props.FloatProperty      ( name='YCutOff',                default=1e+299 )
    m_ZCutOff                = bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+299 )
    e_SplitMode              = bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                 = bpy.props.FloatVectorProperty( name='CutOff',                 default=(1e+299, 1e+299, 1e+299), size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    
CLASSES.append  ( VTKImageIdealHighPass )        
TYPENAMES.append('VTKImageIdealHighPassType' )

#--------------------------------------------------------------
class VTKImageIdealLowPass(Node, VTKFilter1Node):

    bl_idname = 'VTKImageIdealLowPassType'
    bl_label  = 'vtkImageIdealLowPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty       ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty        ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_XCutOff                = bpy.props.FloatProperty      ( name='XCutOff',                default=1e+299 )
    m_YCutOff                = bpy.props.FloatProperty      ( name='YCutOff',                default=1e+299 )
    m_ZCutOff                = bpy.props.FloatProperty      ( name='ZCutOff',                default=1e+299 )
    e_SplitMode              = bpy.props.EnumProperty       ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty  ( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_CutOff                 = bpy.props.FloatVectorProperty( name='CutOff',                 default=(1e+299, 1e+299, 1e+299), size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    
CLASSES.append  ( VTKImageIdealLowPass )        
TYPENAMES.append('VTKImageIdealLowPassType' )

#--------------------------------------------------------------
class VTKImageIslandRemoval2D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageIslandRemoval2DType'
    bl_label  = 'vtkImageIslandRemoval2D'
    
    m_SquareNeighborhood = bpy.props.BoolProperty ( name='SquareNeighborhood', default=0 )
    m_AreaThreshold      = bpy.props.IntProperty  ( name='AreaThreshold',      default=4 )
    m_IslandValue        = bpy.props.FloatProperty( name='IslandValue',        default=0.0 )
    m_ReplaceValue       = bpy.props.FloatProperty( name='ReplaceValue',       default=255.0 )
    
    def m_properties( self ):
        return ['m_SquareNeighborhood','m_AreaThreshold','m_IslandValue','m_ReplaceValue',]
    
CLASSES.append  ( VTKImageIslandRemoval2D )        
TYPENAMES.append('VTKImageIslandRemoval2DType' )

#--------------------------------------------------------------
class VTKImageLaplacian(Node, VTKFilter1Node):

    bl_idname = 'VTKImageLaplacianType'
    bl_label  = 'vtkImageLaplacian'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageLaplacian )        
TYPENAMES.append('VTKImageLaplacianType' )

#--------------------------------------------------------------
class VTKImageLogarithmicScale(Node, VTKFilter1Node):

    bl_idname = 'VTKImageLogarithmicScaleType'
    bl_label  = 'vtkImageLogarithmicScale'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Constant               = bpy.props.FloatProperty    ( name='Constant',               default=10.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Constant','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageLogarithmicScale )        
TYPENAMES.append('VTKImageLogarithmicScaleType' )

#--------------------------------------------------------------
class VTKImageLuminance(Node, VTKFilter1Node):

    bl_idname = 'VTKImageLuminanceType'
    bl_label  = 'vtkImageLuminance'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageLuminance )        
TYPENAMES.append('VTKImageLuminanceType' )

#--------------------------------------------------------------
class VTKImageMagnify(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMagnifyType'
    bl_label  = 'vtkImageMagnify'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_Interpolate            = bpy.props.BoolProperty     ( name='Interpolate',            default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MagnificationFactors   = bpy.props.IntVectorProperty( name='MagnificationFactors',   default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_Interpolate','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MagnificationFactors','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageMagnify )        
TYPENAMES.append('VTKImageMagnifyType' )

#--------------------------------------------------------------
class VTKImageMagnitude(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMagnitudeType'
    bl_label  = 'vtkImageMagnitude'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageMagnitude )        
TYPENAMES.append('VTKImageMagnitudeType' )

#--------------------------------------------------------------
class VTKImageMapToColors(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMapToColorsType'
    bl_label  = 'vtkImageMapToColors'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_PassAlphaToOutput      = bpy.props.BoolProperty     ( name='PassAlphaToOutput',      default=0 )
    m_ActiveComponent        = bpy.props.IntProperty      ( name='ActiveComponent',        default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputFormat           = bpy.props.EnumProperty     ( name='OutputFormat',           default="RGBA", items=e_OutputFormat_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_NaNColor               = bpy.props.IntVectorProperty( name='NaNColor',               default=[0, 0, 0, 0], size=4 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    
CLASSES.append  ( VTKImageMapToColors )        
TYPENAMES.append('VTKImageMapToColorsType' )

#--------------------------------------------------------------
class VTKImageMapToRGBA(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMapToRGBAType'
    bl_label  = 'vtkImageMapToRGBA'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_PassAlphaToOutput      = bpy.props.BoolProperty     ( name='PassAlphaToOutput',      default=0 )
    m_ActiveComponent        = bpy.props.IntProperty      ( name='ActiveComponent',        default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_OutputFormat           = bpy.props.EnumProperty     ( name='OutputFormat',           default="RGBA", items=e_OutputFormat_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_NaNColor               = bpy.props.IntVectorProperty( name='NaNColor',               default=[0, 0, 0, 0], size=4 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    
CLASSES.append  ( VTKImageMapToRGBA )        
TYPENAMES.append('VTKImageMapToRGBAType' )

#--------------------------------------------------------------
class VTKImageMapToWindowLevelColors(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMapToWindowLevelColorsType'
    bl_label  = 'vtkImageMapToWindowLevelColors'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_PassAlphaToOutput      = bpy.props.BoolProperty     ( name='PassAlphaToOutput',      default=0 )
    m_ActiveComponent        = bpy.props.IntProperty      ( name='ActiveComponent',        default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Level                  = bpy.props.FloatProperty    ( name='Level',                  default=127.5 )
    m_Window                 = bpy.props.FloatProperty    ( name='Window',                 default=255.0 )
    e_OutputFormat           = bpy.props.EnumProperty     ( name='OutputFormat',           default="RGBA", items=e_OutputFormat_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_NaNColor               = bpy.props.IntVectorProperty( name='NaNColor',               default=[0, 0, 0, 0], size=4 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Level','m_Window','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    
CLASSES.append  ( VTKImageMapToWindowLevelColors )        
TYPENAMES.append('VTKImageMapToWindowLevelColorsType' )

#--------------------------------------------------------------
class VTKImageMaskBits(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMaskBitsType'
    bl_label  = 'vtkImageMaskBits'
    e_Operation_items=[ (x,x,x) for x in ['And', 'Or', 'Xor', 'Nand', 'Nor']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_Operation              = bpy.props.EnumProperty     ( name='Operation',              default="And", items=e_Operation_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_Masks                  = bpy.props.IntVectorProperty( name='Masks',                  default=[0, 0, 0, 0], size=4 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_Operation','e_SplitMode','m_Masks','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageMaskBits )        
TYPENAMES.append('VTKImageMaskBitsType' )

#--------------------------------------------------------------
class VTKImageMedian3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageMedian3DType'
    bl_label  = 'vtkImageMedian3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize             = bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageMedian3D )        
TYPENAMES.append('VTKImageMedian3DType' )

#--------------------------------------------------------------
class VTKImageNormalize(Node, VTKFilter1Node):

    bl_idname = 'VTKImageNormalizeType'
    bl_label  = 'vtkImageNormalize'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageNormalize )        
TYPENAMES.append('VTKImageNormalizeType' )

#--------------------------------------------------------------
class VTKImageOpenClose3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageOpenClose3DType'
    bl_label  = 'vtkImageOpenClose3D'
    
    m_CloseValue = bpy.props.FloatProperty( name='CloseValue', default=255.0 )
    m_OpenValue  = bpy.props.FloatProperty( name='OpenValue',  default=0.0 )
    
    def m_properties( self ):
        return ['m_CloseValue','m_OpenValue',]
    
CLASSES.append  ( VTKImageOpenClose3D )        
TYPENAMES.append('VTKImageOpenClose3DType' )

#--------------------------------------------------------------
class VTKImageQuantizeRGBToIndex(Node, VTKFilter1Node):

    bl_idname = 'VTKImageQuantizeRGBToIndexType'
    bl_label  = 'vtkImageQuantizeRGBToIndex'
    
    m_NumberOfColors         = bpy.props.IntProperty  ( name='NumberOfColors',         default=256 )
    m_BuildTreeExecuteTime   = bpy.props.FloatProperty( name='BuildTreeExecuteTime',   default=0.0 )
    m_InitializeExecuteTime  = bpy.props.FloatProperty( name='InitializeExecuteTime',  default=0.0 )
    m_LookupIndexExecuteTime = bpy.props.FloatProperty( name='LookupIndexExecuteTime', default=0.0 )
    
    def m_properties( self ):
        return ['m_NumberOfColors','m_BuildTreeExecuteTime','m_InitializeExecuteTime','m_LookupIndexExecuteTime',]
    
CLASSES.append  ( VTKImageQuantizeRGBToIndex )        
TYPENAMES.append('VTKImageQuantizeRGBToIndexType' )

#--------------------------------------------------------------
class VTKImageRFFT(Node, VTKFilter1Node):

    bl_idname = 'VTKImageRFFTType'
    bl_label  = 'vtkImageRFFT'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageRFFT )        
TYPENAMES.append('VTKImageRFFTType' )

#--------------------------------------------------------------
class VTKImageRGBToHSI(Node, VTKFilter1Node):

    bl_idname = 'VTKImageRGBToHSIType'
    bl_label  = 'vtkImageRGBToHSI'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum                = bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageRGBToHSI )        
TYPENAMES.append('VTKImageRGBToHSIType' )

#--------------------------------------------------------------
class VTKImageRGBToHSV(Node, VTKFilter1Node):

    bl_idname = 'VTKImageRGBToHSVType'
    bl_label  = 'vtkImageRGBToHSV'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum                = bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageRGBToHSV )        
TYPENAMES.append('VTKImageRGBToHSVType' )

#--------------------------------------------------------------
class VTKImageRGBToYIQ(Node, VTKFilter1Node):

    bl_idname = 'VTKImageRGBToYIQType'
    bl_label  = 'vtkImageRGBToYIQ'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum                = bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageRGBToYIQ )        
TYPENAMES.append('VTKImageRGBToYIQType' )

#--------------------------------------------------------------
class VTKImageRange3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageRange3DType'
    bl_label  = 'vtkImageRange3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize             = bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageRange3D )        
TYPENAMES.append('VTKImageRange3DType' )

#--------------------------------------------------------------
class VTKImageSeedConnectivity(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSeedConnectivityType'
    bl_label  = 'vtkImageSeedConnectivity'
    
    m_Dimensionality         = bpy.props.IntProperty( name='Dimensionality',         default=3 )
    m_InputConnectValue      = bpy.props.IntProperty( name='InputConnectValue',      default=255 )
    m_OutputConnectedValue   = bpy.props.IntProperty( name='OutputConnectedValue',   default=255 )
    m_OutputUnconnectedValue = bpy.props.IntProperty( name='OutputUnconnectedValue', default=0 )
    
    def m_properties( self ):
        return ['m_Dimensionality','m_InputConnectValue','m_OutputConnectedValue','m_OutputUnconnectedValue',]
    
CLASSES.append  ( VTKImageSeedConnectivity )        
TYPENAMES.append('VTKImageSeedConnectivityType' )

#--------------------------------------------------------------
class VTKImageSeparableConvolution(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSeparableConvolutionType'
    bl_label  = 'vtkImageSeparableConvolution'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=3 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageSeparableConvolution )        
TYPENAMES.append('VTKImageSeparableConvolutionType' )

#--------------------------------------------------------------
class VTKImageShiftScale(Node, VTKFilter1Node):

    bl_idname = 'VTKImageShiftScaleType'
    bl_label  = 'vtkImageShiftScale'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ClampOverflow          = bpy.props.BoolProperty     ( name='ClampOverflow',          default=0 )
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Scale                  = bpy.props.FloatProperty    ( name='Scale',                  default=1.0 )
    m_Shift                  = bpy.props.FloatProperty    ( name='Shift',                  default=0.0 )
    e_OutputScalarType       = bpy.props.EnumProperty     ( name='OutputScalarType',       default="Char", items=e_OutputScalarType_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_ClampOverflow','m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Scale','m_Shift','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageShiftScale )        
TYPENAMES.append('VTKImageShiftScaleType' )

#--------------------------------------------------------------
class VTKImageShrink3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageShrink3DType'
    bl_label  = 'vtkImageShrink3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_Averaging              = bpy.props.BoolProperty     ( name='Averaging',              default=1 )
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_Maximum                = bpy.props.BoolProperty     ( name='Maximum',                default=0 )
    m_Mean                   = bpy.props.BoolProperty     ( name='Mean',                   default=1 )
    m_Median                 = bpy.props.BoolProperty     ( name='Median',                 default=0 )
    m_Minimum                = bpy.props.BoolProperty     ( name='Minimum',                default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_Shift                  = bpy.props.IntVectorProperty( name='Shift',                  default=[0, 0, 0], size=3 )
    m_ShrinkFactors          = bpy.props.IntVectorProperty( name='ShrinkFactors',          default=[1, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_Averaging','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Maximum','m_Mean','m_Median','m_Minimum','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_Shift','m_ShrinkFactors',]
    
CLASSES.append  ( VTKImageShrink3D )        
TYPENAMES.append('VTKImageShrink3DType' )

#--------------------------------------------------------------
class VTKImageSkeleton2D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSkeleton2DType'
    bl_label  = 'vtkImageSkeleton2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_Prune                  = bpy.props.BoolProperty     ( name='Prune',                  default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfIterations     = bpy.props.IntProperty      ( name='NumberOfIterations',     default=1 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_Prune','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageSkeleton2D )        
TYPENAMES.append('VTKImageSkeleton2DType' )

#--------------------------------------------------------------
class VTKImageSlab(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSlabType'
    bl_label  = 'vtkImageSlab'
    e_Operation_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_Orientation_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_MultiSliceOutput       = bpy.props.BoolProperty     ( name='MultiSliceOutput',       default=0 )
    m_TrapezoidIntegration   = bpy.props.BoolProperty     ( name='TrapezoidIntegration',   default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_Operation              = bpy.props.EnumProperty     ( name='Operation',              default="Mean", items=e_Operation_items )
    e_Orientation            = bpy.props.EnumProperty     ( name='Orientation',            default="Z", items=e_Orientation_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    m_SliceRange             = bpy.props.IntVectorProperty( name='SliceRange',             default=[-2147483648, 0], size=2 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_MultiSliceOutput','m_TrapezoidIntegration','m_DesiredBytesPerPiece','m_NumberOfThreads','e_Operation','e_Orientation','e_SplitMode','m_MinimumPieceSize','m_SliceRange',]
    
CLASSES.append  ( VTKImageSlab )        
TYPENAMES.append('VTKImageSlabType' )

#--------------------------------------------------------------
class VTKImageSobel2D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSobel2DType'
    bl_label  = 'vtkImageSobel2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageSobel2D )        
TYPENAMES.append('VTKImageSobel2DType' )

#--------------------------------------------------------------
class VTKImageSobel3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSobel3DType'
    bl_label  = 'vtkImageSobel3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageSobel3D )        
TYPENAMES.append('VTKImageSobel3DType' )

#--------------------------------------------------------------
class VTKImageSpatialAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKImageSpatialAlgorithmType'
    bl_label  = 'vtkImageSpatialAlgorithm'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageSpatialAlgorithm )        
TYPENAMES.append('VTKImageSpatialAlgorithmType' )

#--------------------------------------------------------------
class VTKImageStencilAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKImageStencilAlgorithmType'
    bl_label  = 'vtkImageStencilAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKImageStencilAlgorithm )        
TYPENAMES.append('VTKImageStencilAlgorithmType' )

#--------------------------------------------------------------
class VTKImageStencilSource(Node, VTKFilter1Node):

    bl_idname = 'VTKImageStencilSourceType'
    bl_label  = 'vtkImageStencilSource'
    
    m_OutputWholeExtent = bpy.props.IntVectorProperty  ( name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6 )
    m_OutputOrigin      = bpy.props.FloatVectorProperty( name='OutputOrigin',      default=(0.0, 0.0, 0.0), size=3 )
    m_OutputSpacing     = bpy.props.FloatVectorProperty( name='OutputSpacing',     default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    
CLASSES.append  ( VTKImageStencilSource )        
TYPENAMES.append('VTKImageStencilSourceType' )

#--------------------------------------------------------------
class VTKImageStencilToImage(Node, VTKFilter1Node):

    bl_idname = 'VTKImageStencilToImageType'
    bl_label  = 'vtkImageStencilToImage'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_InsideValue      = bpy.props.FloatProperty( name='InsideValue',      default=1.0 )
    m_OutsideValue     = bpy.props.FloatProperty( name='OutsideValue',     default=0.0 )
    e_OutputScalarType = bpy.props.EnumProperty ( name='OutputScalarType', default="UnsignedChar", items=e_OutputScalarType_items )
    
    def m_properties( self ):
        return ['m_InsideValue','m_OutsideValue','e_OutputScalarType',]
    
CLASSES.append  ( VTKImageStencilToImage )        
TYPENAMES.append('VTKImageStencilToImageType' )

#--------------------------------------------------------------
class VTKImageThreshold(Node, VTKFilter1Node):

    bl_idname = 'VTKImageThresholdType'
    bl_label  = 'vtkImageThreshold'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double', 'SignedChar']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_ReplaceIn              = bpy.props.BoolProperty     ( name='ReplaceIn',              default=0 )
    m_ReplaceOut             = bpy.props.BoolProperty     ( name='ReplaceOut',             default=0 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_InValue                = bpy.props.FloatProperty    ( name='InValue',                default=0.0 )
    m_OutValue               = bpy.props.FloatProperty    ( name='OutValue',               default=0.0 )
    e_OutputScalarType       = bpy.props.EnumProperty     ( name='OutputScalarType',       default="Char", items=e_OutputScalarType_items )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ReplaceIn','m_ReplaceOut','m_DesiredBytesPerPiece','m_NumberOfThreads','m_InValue','m_OutValue','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageThreshold )        
TYPENAMES.append('VTKImageThresholdType' )

#--------------------------------------------------------------
class VTKImageToAMR(Node, VTKFilter1Node):

    bl_idname = 'VTKImageToAMRType'
    bl_label  = 'vtkImageToAMR'
    
    m_MaximumNumberOfBlocks = bpy.props.IntProperty( name='MaximumNumberOfBlocks', default=100 )
    m_NumberOfLevels        = bpy.props.IntProperty( name='NumberOfLevels',        default=2 )
    m_RefinementRatio       = bpy.props.IntProperty( name='RefinementRatio',       default=2 )
    
    def m_properties( self ):
        return ['m_MaximumNumberOfBlocks','m_NumberOfLevels','m_RefinementRatio',]
    
CLASSES.append  ( VTKImageToAMR )        
TYPENAMES.append('VTKImageToAMRType' )

#--------------------------------------------------------------
class VTKImageToImageStencil(Node, VTKFilter1Node):

    bl_idname = 'VTKImageToImageStencilType'
    bl_label  = 'vtkImageToImageStencil'
    
    m_LowerThreshold = bpy.props.FloatProperty( name='LowerThreshold', default=-9.999999680285692e+37 )
    m_UpperThreshold = bpy.props.FloatProperty( name='UpperThreshold', default=9.999999680285692e+37 )
    
    def m_properties( self ):
        return ['m_LowerThreshold','m_UpperThreshold',]
    
CLASSES.append  ( VTKImageToImageStencil )        
TYPENAMES.append('VTKImageToImageStencilType' )

#--------------------------------------------------------------
class VTKImageToPolyDataFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKImageToPolyDataFilterType'
    bl_label  = 'vtkImageToPolyDataFilter'
    e_ColorMode_items=[ (x,x,x) for x in ['LUT', 'Linear256']]
    e_OutputStyle_items=[ (x,x,x) for x in ['Pixelize', 'Polygonalize', 'RunLength']]
    
    m_Decimation                  = bpy.props.BoolProperty ( name='Decimation',                  default=1 )
    m_Smoothing                   = bpy.props.BoolProperty ( name='Smoothing',                   default=1 )
    m_Error                       = bpy.props.IntProperty  ( name='Error',                       default=100 )
    m_NumberOfSmoothingIterations = bpy.props.IntProperty  ( name='NumberOfSmoothingIterations', default=40 )
    m_SubImageSize                = bpy.props.IntProperty  ( name='SubImageSize',                default=250 )
    m_DecimationError             = bpy.props.FloatProperty( name='DecimationError',             default=1.5 )
    e_ColorMode                   = bpy.props.EnumProperty ( name='ColorMode',                   default="Linear256", items=e_ColorMode_items )
    e_OutputStyle                 = bpy.props.EnumProperty ( name='OutputStyle',                 default="Polygonalize", items=e_OutputStyle_items )
    
    def m_properties( self ):
        return ['m_Decimation','m_Smoothing','m_Error','m_NumberOfSmoothingIterations','m_SubImageSize','m_DecimationError','e_ColorMode','e_OutputStyle',]
    
CLASSES.append  ( VTKImageToPolyDataFilter )        
TYPENAMES.append('VTKImageToPolyDataFilterType' )

#--------------------------------------------------------------
class VTKImageToStructuredGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKImageToStructuredGridType'
    bl_label  = 'vtkImageToStructuredGrid'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKImageToStructuredGrid )        
TYPENAMES.append('VTKImageToStructuredGridType' )

#--------------------------------------------------------------
class VTKImageTranslateExtent(Node, VTKFilter1Node):

    bl_idname = 'VTKImageTranslateExtentType'
    bl_label  = 'vtkImageTranslateExtent'
    
    m_Translation = bpy.props.IntVectorProperty( name='Translation', default=[0, 0, 0], size=3 )
    
    def m_properties( self ):
        return ['m_Translation',]
    
CLASSES.append  ( VTKImageTranslateExtent )        
TYPENAMES.append('VTKImageTranslateExtentType' )

#--------------------------------------------------------------
class VTKImageVariance3D(Node, VTKFilter1Node):

    bl_idname = 'VTKImageVariance3DType'
    bl_label  = 'vtkImageVariance3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_KernelSize             = bpy.props.IntVectorProperty( name='KernelSize',             default=[1, 1, 1], size=3 )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageVariance3D )        
TYPENAMES.append('VTKImageVariance3DType' )

#--------------------------------------------------------------
class VTKImageWeightedSum(Node, VTKFilter1Node):

    bl_idname = 'VTKImageWeightedSumType'
    bl_label  = 'vtkImageWeightedSum'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_NormalizeByWeight      = bpy.props.BoolProperty     ( name='NormalizeByWeight',      default=1 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_NormalizeByWeight','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageWeightedSum )        
TYPENAMES.append('VTKImageWeightedSumType' )

#--------------------------------------------------------------
class VTKImageYIQToRGB(Node, VTKFilter1Node):

    bl_idname = 'VTKImageYIQToRGBType'
    bl_label  = 'vtkImageYIQToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=8 )
    m_Maximum                = bpy.props.FloatProperty    ( name='Maximum',                default=255.0 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKImageYIQToRGB )        
TYPENAMES.append('VTKImageYIQToRGBType' )

#--------------------------------------------------------------
class VTKImplicitModeller(Node, VTKFilter1Node):

    bl_idname = 'VTKImplicitModellerType'
    bl_label  = 'vtkImplicitModeller'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_ProcessMode_items=[ (x,x,x) for x in ['PerVoxel', 'PerCell']]
    
    m_AdjustBounds           = bpy.props.BoolProperty       ( name='AdjustBounds',           default=1 )
    m_Capping                = bpy.props.BoolProperty       ( name='Capping',                default=1 )
    m_ScaleToMaximumDistance = bpy.props.BoolProperty       ( name='ScaleToMaximumDistance', default=0 )
    m_LocatorMaxLevel        = bpy.props.IntProperty        ( name='LocatorMaxLevel',        default=5 )
    m_NumberOfThreads        = bpy.props.IntProperty        ( name='NumberOfThreads',        default=8 )
    m_AdjustDistance         = bpy.props.FloatProperty      ( name='AdjustDistance',         default=0.0125 )
    m_CapValue               = bpy.props.FloatProperty      ( name='CapValue',               default=9.999999680285692e+37 )
    m_MaximumDistance        = bpy.props.FloatProperty      ( name='MaximumDistance',        default=0.1 )
    e_OutputScalarType       = bpy.props.EnumProperty       ( name='OutputScalarType',       default="Float", items=e_OutputScalarType_items )
    e_ProcessMode            = bpy.props.EnumProperty       ( name='ProcessMode',            default="PerCell", items=e_ProcessMode_items )
    m_SampleDimensions       = bpy.props.IntVectorProperty  ( name='SampleDimensions',       default=[50, 50, 50], size=3 )
    m_ModelBounds            = bpy.props.FloatVectorProperty( name='ModelBounds',            default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_AdjustBounds','m_Capping','m_ScaleToMaximumDistance','m_LocatorMaxLevel','m_NumberOfThreads','m_AdjustDistance','m_CapValue','m_MaximumDistance','e_OutputScalarType','e_ProcessMode','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKImplicitModeller )        
TYPENAMES.append('VTKImplicitModellerType' )

#--------------------------------------------------------------
class VTKImplicitTextureCoords(Node, VTKFilter1Node):

    bl_idname = 'VTKImplicitTextureCoordsType'
    bl_label  = 'vtkImplicitTextureCoords'
    
    m_FlipTexture = bpy.props.BoolProperty( name='FlipTexture', default=0 )
    
    def m_properties( self ):
        return ['m_FlipTexture',]
    
CLASSES.append  ( VTKImplicitTextureCoords )        
TYPENAMES.append('VTKImplicitTextureCoordsType' )

#--------------------------------------------------------------
class VTKInterpolateDataSetAttributes(Node, VTKFilter1Node):

    bl_idname = 'VTKInterpolateDataSetAttributesType'
    bl_label  = 'vtkInterpolateDataSetAttributes'
    
    m_T = bpy.props.FloatProperty( name='T', default=0.0 )
    
    def m_properties( self ):
        return ['m_T',]
    
CLASSES.append  ( VTKInterpolateDataSetAttributes )        
TYPENAMES.append('VTKInterpolateDataSetAttributesType' )

#--------------------------------------------------------------
class VTKKCoreDecomposition(Node, VTKFilter1Node):

    bl_idname = 'VTKKCoreDecompositionType'
    bl_label  = 'vtkKCoreDecomposition'
    
    m_CheckInputGraph       = bpy.props.BoolProperty( name='CheckInputGraph',       default=True )
    m_UseInDegreeNeighbors  = bpy.props.BoolProperty( name='UseInDegreeNeighbors',  default=True )
    m_UseOutDegreeNeighbors = bpy.props.BoolProperty( name='UseOutDegreeNeighbors', default=True )
    
    def m_properties( self ):
        return ['m_CheckInputGraph','m_UseInDegreeNeighbors','m_UseOutDegreeNeighbors',]
    
CLASSES.append  ( VTKKCoreDecomposition )        
TYPENAMES.append('VTKKCoreDecompositionType' )

#--------------------------------------------------------------
class VTKKCoreLayout(Node, VTKFilter1Node):

    bl_idname = 'VTKKCoreLayoutType'
    bl_label  = 'vtkKCoreLayout'
    
    m_Cartesian                  = bpy.props.BoolProperty  ( name='Cartesian',                  default=True )
    m_Polar                      = bpy.props.BoolProperty  ( name='Polar',                      default=False )
    m_CartesianCoordsXArrayName  = bpy.props.StringProperty( name='CartesianCoordsXArrayName',  default="" )
    m_CartesianCoordsYArrayName  = bpy.props.StringProperty( name='CartesianCoordsYArrayName',  default="" )
    m_PolarCoordsAngleArrayName  = bpy.props.StringProperty( name='PolarCoordsAngleArrayName',  default="" )
    m_PolarCoordsRadiusArrayName = bpy.props.StringProperty( name='PolarCoordsRadiusArrayName', default="" )
    m_Epsilon                    = bpy.props.FloatProperty ( name='Epsilon',                    default=0.20000000298023224 )
    m_UnitRadius                 = bpy.props.FloatProperty ( name='UnitRadius',                 default=1.0 )
    
    def m_properties( self ):
        return ['m_Cartesian','m_Polar','m_CartesianCoordsXArrayName','m_CartesianCoordsYArrayName','m_PolarCoordsAngleArrayName','m_PolarCoordsRadiusArrayName','m_Epsilon','m_UnitRadius',]
    
CLASSES.append  ( VTKKCoreLayout )        
TYPENAMES.append('VTKKCoreLayoutType' )

#--------------------------------------------------------------
class VTKLabelHierarchyAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKLabelHierarchyAlgorithmType'
    bl_label  = 'vtkLabelHierarchyAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKLabelHierarchyAlgorithm )        
TYPENAMES.append('VTKLabelHierarchyAlgorithmType' )

#--------------------------------------------------------------
class VTKLevelIdScalars(Node, VTKFilter1Node):

    bl_idname = 'VTKLevelIdScalarsType'
    bl_label  = 'vtkLevelIdScalars'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKLevelIdScalars )        
TYPENAMES.append('VTKLevelIdScalarsType' )

#--------------------------------------------------------------
class VTKLinearExtrusionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKLinearExtrusionFilterType'
    bl_label  = 'vtkLinearExtrusionFilter'
    e_ExtrusionType_items=[ (x,x,x) for x in ['VectorExtrusion', 'NormalExtrusion', 'PointExtrusion']]
    
    m_Capping        = bpy.props.BoolProperty       ( name='Capping',        default=1 )
    m_ScaleFactor    = bpy.props.FloatProperty      ( name='ScaleFactor',    default=1.0 )
    e_ExtrusionType  = bpy.props.EnumProperty       ( name='ExtrusionType',  default="NormalExtrusion", items=e_ExtrusionType_items )
    m_ExtrusionPoint = bpy.props.FloatVectorProperty( name='ExtrusionPoint', default=(0.0, 0.0, 0.0), size=3 )
    m_Vector         = bpy.props.FloatVectorProperty( name='Vector',         default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Capping','m_ScaleFactor','e_ExtrusionType','m_ExtrusionPoint','m_Vector',]
    
CLASSES.append  ( VTKLinearExtrusionFilter )        
TYPENAMES.append('VTKLinearExtrusionFilterType' )

#--------------------------------------------------------------
class VTKLinearSelector(Node, VTKFilter1Node):

    bl_idname = 'VTKLinearSelectorType'
    bl_label  = 'vtkLinearSelector'
    
    m_IncludeVertices            = bpy.props.BoolProperty       ( name='IncludeVertices',            default=True )
    m_Tolerance                  = bpy.props.FloatProperty      ( name='Tolerance',                  default=0.0 )
    m_VertexEliminationTolerance = bpy.props.FloatProperty      ( name='VertexEliminationTolerance', default=1e-06 )
    m_EndPoint                   = bpy.props.FloatVectorProperty( name='EndPoint',                   default=(1.0, 1.0, 1.0), size=3 )
    m_StartPoint                 = bpy.props.FloatVectorProperty( name='StartPoint',                 default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_IncludeVertices','m_Tolerance','m_VertexEliminationTolerance','m_EndPoint','m_StartPoint',]
    
CLASSES.append  ( VTKLinearSelector )        
TYPENAMES.append('VTKLinearSelectorType' )

#--------------------------------------------------------------
class VTKLinearSubdivisionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKLinearSubdivisionFilterType'
    bl_label  = 'vtkLinearSubdivisionFilter'
    
    m_CheckForTriangles    = bpy.props.BoolProperty( name='CheckForTriangles',    default=1 )
    m_NumberOfSubdivisions = bpy.props.IntProperty ( name='NumberOfSubdivisions', default=1 )
    
    def m_properties( self ):
        return ['m_CheckForTriangles','m_NumberOfSubdivisions',]
    
CLASSES.append  ( VTKLinearSubdivisionFilter )        
TYPENAMES.append('VTKLinearSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKLinearToQuadraticCellsFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKLinearToQuadraticCellsFilterType'
    bl_label  = 'vtkLinearToQuadraticCellsFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKLinearToQuadraticCellsFilter )        
TYPENAMES.append('VTKLinearToQuadraticCellsFilterType' )

#--------------------------------------------------------------
class VTKLinkEdgels(Node, VTKFilter1Node):

    bl_idname = 'VTKLinkEdgelsType'
    bl_label  = 'vtkLinkEdgels'
    
    m_GradientThreshold = bpy.props.FloatProperty( name='GradientThreshold', default=0.1 )
    m_LinkThreshold     = bpy.props.FloatProperty( name='LinkThreshold',     default=90.0 )
    m_PhiThreshold      = bpy.props.FloatProperty( name='PhiThreshold',      default=90.0 )
    
    def m_properties( self ):
        return ['m_GradientThreshold','m_LinkThreshold','m_PhiThreshold',]
    
CLASSES.append  ( VTKLinkEdgels )        
TYPENAMES.append('VTKLinkEdgelsType' )

#--------------------------------------------------------------
class VTKLoopSubdivisionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKLoopSubdivisionFilterType'
    bl_label  = 'vtkLoopSubdivisionFilter'
    
    m_CheckForTriangles    = bpy.props.BoolProperty( name='CheckForTriangles',    default=1 )
    m_NumberOfSubdivisions = bpy.props.IntProperty ( name='NumberOfSubdivisions', default=1 )
    
    def m_properties( self ):
        return ['m_CheckForTriangles','m_NumberOfSubdivisions',]
    
CLASSES.append  ( VTKLoopSubdivisionFilter )        
TYPENAMES.append('VTKLoopSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKMapArrayValues(Node, VTKFilter1Node):

    bl_idname = 'VTKMapArrayValuesType'
    bl_label  = 'vtkMapArrayValues'
    
    m_PassArray       = bpy.props.BoolProperty  ( name='PassArray',       default=0 )
    m_InputArrayName  = bpy.props.StringProperty( name='InputArrayName',  default="" )
    m_OutputArrayName = bpy.props.StringProperty( name='OutputArrayName', default="ArrayMap" )
    m_FieldType       = bpy.props.IntProperty   ( name='FieldType',       default=0 )
    m_OutputArrayType = bpy.props.IntProperty   ( name='OutputArrayType', default=6 )
    m_FillValue       = bpy.props.FloatProperty ( name='FillValue',       default=-1.0 )
    
    def m_properties( self ):
        return ['m_PassArray','m_InputArrayName','m_OutputArrayName','m_FieldType','m_OutputArrayType','m_FillValue',]
    
CLASSES.append  ( VTKMapArrayValues )        
TYPENAMES.append('VTKMapArrayValuesType' )

#--------------------------------------------------------------
class VTKMaskFields(Node, VTKFilter1Node):

    bl_idname = 'VTKMaskFieldsType'
    bl_label  = 'vtkMaskFields'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMaskFields )        
TYPENAMES.append('VTKMaskFieldsType' )

#--------------------------------------------------------------
class VTKMaskPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKMaskPointsType'
    bl_label  = 'vtkMaskPoints'
    
    m_GenerateVertices                  = bpy.props.BoolProperty( name='GenerateVertices',                  default=0 )
    m_ProportionalMaximumNumberOfPoints = bpy.props.BoolProperty( name='ProportionalMaximumNumberOfPoints', default=0 )
    m_RandomMode                        = bpy.props.BoolProperty( name='RandomMode',                        default=0 )
    m_SingleVertexPerCell               = bpy.props.BoolProperty( name='SingleVertexPerCell',               default=0 )
    m_MaximumNumberOfPoints             = bpy.props.IntProperty ( name='MaximumNumberOfPoints',             default=0 )
    m_Offset                            = bpy.props.IntProperty ( name='Offset',                            default=0 )
    m_OnRatio                           = bpy.props.IntProperty ( name='OnRatio',                           default=2 )
    m_RandomModeType                    = bpy.props.IntProperty ( name='RandomModeType',                    default=0 )
    
    def m_properties( self ):
        return ['m_GenerateVertices','m_ProportionalMaximumNumberOfPoints','m_RandomMode','m_SingleVertexPerCell','m_MaximumNumberOfPoints','m_Offset','m_OnRatio','m_RandomModeType',]
    
CLASSES.append  ( VTKMaskPoints )        
TYPENAMES.append('VTKMaskPointsType' )

#--------------------------------------------------------------
class VTKMaskPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKMaskPolyDataType'
    bl_label  = 'vtkMaskPolyData'
    
    m_Offset  = bpy.props.IntProperty( name='Offset',  default=0 )
    m_OnRatio = bpy.props.IntProperty( name='OnRatio', default=11 )
    
    def m_properties( self ):
        return ['m_Offset','m_OnRatio',]
    
CLASSES.append  ( VTKMaskPolyData )        
TYPENAMES.append('VTKMaskPolyDataType' )

#--------------------------------------------------------------
class VTKMatricizeArray(Node, VTKFilter1Node):

    bl_idname = 'VTKMatricizeArrayType'
    bl_label  = 'vtkMatricizeArray'
    
    m_SliceDimension = bpy.props.IntProperty( name='SliceDimension', default=0 )
    
    def m_properties( self ):
        return ['m_SliceDimension',]
    
CLASSES.append  ( VTKMatricizeArray )        
TYPENAMES.append('VTKMatricizeArrayType' )

#--------------------------------------------------------------
class VTKMatrixMathFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKMatrixMathFilterType'
    bl_label  = 'vtkMatrixMathFilter'
    e_Operation_items=[ (x,x,x) for x in ['Determinant', 'Eigenvalue', 'Eigenvector', 'Inverse']]
    
    e_Operation = bpy.props.EnumProperty( name='Operation', default="Determinant", items=e_Operation_items )
    
    def m_properties( self ):
        return ['e_Operation',]
    
CLASSES.append  ( VTKMatrixMathFilter )        
TYPENAMES.append('VTKMatrixMathFilterType' )

#--------------------------------------------------------------
class VTKMemoryLimitImageDataStreamer(Node, VTKFilter1Node):

    bl_idname = 'VTKMemoryLimitImageDataStreamerType'
    bl_label  = 'vtkMemoryLimitImageDataStreamer'
    
    m_MemoryLimit             = bpy.props.IntProperty( name='MemoryLimit',             default=51200 )
    m_NumberOfStreamDivisions = bpy.props.IntProperty( name='NumberOfStreamDivisions', default=10 )
    
    def m_properties( self ):
        return ['m_MemoryLimit','m_NumberOfStreamDivisions',]
    
CLASSES.append  ( VTKMemoryLimitImageDataStreamer )        
TYPENAMES.append('VTKMemoryLimitImageDataStreamerType' )

#--------------------------------------------------------------
class VTKMergeColumns(Node, VTKFilter1Node):

    bl_idname = 'VTKMergeColumnsType'
    bl_label  = 'vtkMergeColumns'
    
    m_MergedColumnName = bpy.props.StringProperty( name='MergedColumnName', default="" )
    
    def m_properties( self ):
        return ['m_MergedColumnName',]
    
CLASSES.append  ( VTKMergeColumns )        
TYPENAMES.append('VTKMergeColumnsType' )

#--------------------------------------------------------------
class VTKMergeFields(Node, VTKFilter1Node):

    bl_idname = 'VTKMergeFieldsType'
    bl_label  = 'vtkMergeFields'
    
    m_NumberOfComponents = bpy.props.IntProperty( name='NumberOfComponents', default=0 )
    
    def m_properties( self ):
        return ['m_NumberOfComponents',]
    
CLASSES.append  ( VTKMergeFields )        
TYPENAMES.append('VTKMergeFieldsType' )

#--------------------------------------------------------------
class VTKMeshQuality(Node, VTKFilter1Node):

    bl_idname = 'VTKMeshQualityType'
    bl_label  = 'vtkMeshQuality'
    e_HexQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'MedAspectFrobenius', 'MaxAspectFrobenius', 'Condition', 'ScaledJacobian', 'Shear', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'MaxEdgeRatios', 'Skew', 'Taper', 'Volume', 'Stretch', 'Diagonal', 'Dimension', 'Oddy', 'ShearAndSize', 'Jacobian']]
    e_QuadQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'AspectRatio', 'RadiusRatio', 'MedAspectFrobenius', 'MaxAspectFrobenius', 'MinAngle', 'MaxAngle', 'Condition', 'ScaledJacobian', 'Shear', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'MaxEdgeRatios', 'Skew', 'Taper', 'Stretch', 'Oddy', 'ShearAndSize', 'Jacobian', 'Warpage', 'Area']]
    e_TetQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'AspectRatio', 'RadiusRatio', 'AspectFrobenius', 'MinAngle', 'CollapseRatio', 'Condition', 'ScaledJacobian', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'Volume', 'Jacobian', 'AspectGamma', 'AspectBeta']]
    e_TriangleQualityMeasure_items=[ (x,x,x) for x in ['EdgeRatio', 'AspectRatio', 'RadiusRatio', 'AspectFrobenius', 'MinAngle', 'MaxAngle', 'Condition', 'ScaledJacobian', 'RelativeSizeSquared', 'Shape', 'ShapeAndSize', 'Distortion', 'Area']]
    
    m_CompatibilityMode      = bpy.props.BoolProperty( name='CompatibilityMode',      default=0 )
    m_Ratio                  = bpy.props.BoolProperty( name='Ratio',                  default=1 )
    m_SaveCellQuality        = bpy.props.BoolProperty( name='SaveCellQuality',        default=1 )
    m_Volume                 = bpy.props.BoolProperty( name='Volume',                 default=0 )
    e_HexQualityMeasure      = bpy.props.EnumProperty( name='HexQualityMeasure',      default="MaxAspectFrobenius", items=e_HexQualityMeasure_items )
    e_QuadQualityMeasure     = bpy.props.EnumProperty( name='QuadQualityMeasure',     default="EdgeRatio", items=e_QuadQualityMeasure_items )
    e_TetQualityMeasure      = bpy.props.EnumProperty( name='TetQualityMeasure',      default="AspectRatio", items=e_TetQualityMeasure_items )
    e_TriangleQualityMeasure = bpy.props.EnumProperty( name='TriangleQualityMeasure', default="AspectRatio", items=e_TriangleQualityMeasure_items )
    
    def m_properties( self ):
        return ['m_CompatibilityMode','m_Ratio','m_SaveCellQuality','m_Volume','e_HexQualityMeasure','e_QuadQualityMeasure','e_TetQualityMeasure','e_TriangleQualityMeasure',]
    
CLASSES.append  ( VTKMeshQuality )        
TYPENAMES.append('VTKMeshQualityType' )

#--------------------------------------------------------------
class VTKMoleculeAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKMoleculeAlgorithmType'
    bl_label  = 'vtkMoleculeAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMoleculeAlgorithm )        
TYPENAMES.append('VTKMoleculeAlgorithmType' )

#--------------------------------------------------------------
class VTKMoleculeToAtomBallFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKMoleculeToAtomBallFilterType'
    bl_label  = 'vtkMoleculeToAtomBallFilter'
    
    m_RadiusSource = bpy.props.IntProperty  ( name='RadiusSource', default=0 )
    m_Resolution   = bpy.props.IntProperty  ( name='Resolution',   default=50 )
    m_RadiusScale  = bpy.props.FloatProperty( name='RadiusScale',  default=0.8 )
    
    def m_properties( self ):
        return ['m_RadiusSource','m_Resolution','m_RadiusScale',]
    
CLASSES.append  ( VTKMoleculeToAtomBallFilter )        
TYPENAMES.append('VTKMoleculeToAtomBallFilterType' )

#--------------------------------------------------------------
class VTKMoleculeToBondStickFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKMoleculeToBondStickFilterType'
    bl_label  = 'vtkMoleculeToBondStickFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMoleculeToBondStickFilter )        
TYPENAMES.append('VTKMoleculeToBondStickFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockDataGroupFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKMultiBlockDataGroupFilterType'
    bl_label  = 'vtkMultiBlockDataGroupFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMultiBlockDataGroupFilter )        
TYPENAMES.append('VTKMultiBlockDataGroupFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockDataSetAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKMultiBlockDataSetAlgorithmType'
    bl_label  = 'vtkMultiBlockDataSetAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMultiBlockDataSetAlgorithm )        
TYPENAMES.append('VTKMultiBlockDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKMultiBlockFromTimeSeriesFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKMultiBlockFromTimeSeriesFilterType'
    bl_label  = 'vtkMultiBlockFromTimeSeriesFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMultiBlockFromTimeSeriesFilter )        
TYPENAMES.append('VTKMultiBlockFromTimeSeriesFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockMergeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKMultiBlockMergeFilterType'
    bl_label  = 'vtkMultiBlockMergeFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMultiBlockMergeFilter )        
TYPENAMES.append('VTKMultiBlockMergeFilterType' )

#--------------------------------------------------------------
class VTKMultiThreshold(Node, VTKFilter1Node):

    bl_idname = 'VTKMultiThresholdType'
    bl_label  = 'vtkMultiThreshold'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKMultiThreshold )        
TYPENAMES.append('VTKMultiThresholdType' )

#--------------------------------------------------------------
class VTKNetworkHierarchy(Node, VTKFilter1Node):

    bl_idname = 'VTKNetworkHierarchyType'
    bl_label  = 'vtkNetworkHierarchy'
    
    m_IPArrayName = bpy.props.StringProperty( name='IPArrayName', default="ip" )
    
    def m_properties( self ):
        return ['m_IPArrayName',]
    
CLASSES.append  ( VTKNetworkHierarchy )        
TYPENAMES.append('VTKNetworkHierarchyType' )

#--------------------------------------------------------------
class VTKNonOverlappingAMRAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKNonOverlappingAMRAlgorithmType'
    bl_label  = 'vtkNonOverlappingAMRAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKNonOverlappingAMRAlgorithm )        
TYPENAMES.append('VTKNonOverlappingAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKNormalizeMatrixVectors(Node, VTKFilter1Node):

    bl_idname = 'VTKNormalizeMatrixVectorsType'
    bl_label  = 'vtkNormalizeMatrixVectors'
    
    m_VectorDimension = bpy.props.IntProperty  ( name='VectorDimension', default=1 )
    m_PValue          = bpy.props.FloatProperty( name='PValue',          default=2.0 )
    
    def m_properties( self ):
        return ['m_VectorDimension','m_PValue',]
    
CLASSES.append  ( VTKNormalizeMatrixVectors )        
TYPENAMES.append('VTKNormalizeMatrixVectorsType' )

#--------------------------------------------------------------
class VTKOBBDicer(Node, VTKFilter1Node):

    bl_idname = 'VTKOBBDicerType'
    bl_label  = 'vtkOBBDicer'
    e_DiceMode_items=[ (x,x,x) for x in ['NumberOfPointsPerPiece', 'SpecifiedNumberOfPieces', 'MemoryLimitPerPiece']]
    
    m_FieldData              = bpy.props.BoolProperty( name='FieldData',              default=0 )
    m_MemoryLimit            = bpy.props.IntProperty ( name='MemoryLimit',            default=51200 )
    m_NumberOfPieces         = bpy.props.IntProperty ( name='NumberOfPieces',         default=10 )
    m_NumberOfPointsPerPiece = bpy.props.IntProperty ( name='NumberOfPointsPerPiece', default=5000 )
    e_DiceMode               = bpy.props.EnumProperty( name='DiceMode',               default="NumberOfPointsPerPiece", items=e_DiceMode_items )
    
    def m_properties( self ):
        return ['m_FieldData','m_MemoryLimit','m_NumberOfPieces','m_NumberOfPointsPerPiece','e_DiceMode',]
    
CLASSES.append  ( VTKOBBDicer )        
TYPENAMES.append('VTKOBBDicerType' )

#--------------------------------------------------------------
class VTKOpenGLImageGradient(Node, VTKFilter1Node):

    bl_idname = 'VTKOpenGLImageGradientType'
    bl_label  = 'vtkOpenGLImageGradient'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP              = bpy.props.BoolProperty     ( name='EnableSMP',              default=False )
    m_GlobalDefaultEnableSMP = bpy.props.BoolProperty     ( name='GlobalDefaultEnableSMP', default=False )
    m_HandleBoundaries       = bpy.props.BoolProperty     ( name='HandleBoundaries',       default=1 )
    m_DesiredBytesPerPiece   = bpy.props.IntProperty      ( name='DesiredBytesPerPiece',   default=65536 )
    m_Dimensionality         = bpy.props.IntProperty      ( name='Dimensionality',         default=2 )
    m_NumberOfThreads        = bpy.props.IntProperty      ( name='NumberOfThreads',        default=1 )
    e_SplitMode              = bpy.props.EnumProperty     ( name='SplitMode',              default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize       = bpy.props.IntVectorProperty( name='MinimumPieceSize',       default=[16, 1, 1], size=3 )
    
    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    
CLASSES.append  ( VTKOpenGLImageGradient )        
TYPENAMES.append('VTKOpenGLImageGradientType' )

#--------------------------------------------------------------
class VTKOutlineCornerFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKOutlineCornerFilterType'
    bl_label  = 'vtkOutlineCornerFilter'
    
    m_CornerFactor = bpy.props.FloatProperty( name='CornerFactor', default=0.2 )
    
    def m_properties( self ):
        return ['m_CornerFactor',]
    
CLASSES.append  ( VTKOutlineCornerFilter )        
TYPENAMES.append('VTKOutlineCornerFilterType' )

#--------------------------------------------------------------
class VTKOutlineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKOutlineFilterType'
    bl_label  = 'vtkOutlineFilter'
    
    m_GenerateFaces = bpy.props.BoolProperty( name='GenerateFaces', default=0 )
    
    def m_properties( self ):
        return ['m_GenerateFaces',]
    
CLASSES.append  ( VTKOutlineFilter )        
TYPENAMES.append('VTKOutlineFilterType' )

#--------------------------------------------------------------
class VTKOverlappingAMRAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKOverlappingAMRAlgorithmType'
    bl_label  = 'vtkOverlappingAMRAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKOverlappingAMRAlgorithm )        
TYPENAMES.append('VTKOverlappingAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKOverlappingAMRLevelIdScalars(Node, VTKFilter1Node):

    bl_idname = 'VTKOverlappingAMRLevelIdScalarsType'
    bl_label  = 'vtkOverlappingAMRLevelIdScalars'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKOverlappingAMRLevelIdScalars )        
TYPENAMES.append('VTKOverlappingAMRLevelIdScalarsType' )

#--------------------------------------------------------------
class VTKPCAAnalysisFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPCAAnalysisFilterType'
    bl_label  = 'vtkPCAAnalysisFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPCAAnalysisFilter )        
TYPENAMES.append('VTKPCAAnalysisFilterType' )

#--------------------------------------------------------------
class VTKPCACurvatureEstimation(Node, VTKFilter1Node):

    bl_idname = 'VTKPCACurvatureEstimationType'
    bl_label  = 'vtkPCACurvatureEstimation'
    
    m_SampleSize = bpy.props.IntProperty( name='SampleSize', default=25 )
    
    def m_properties( self ):
        return ['m_SampleSize',]
    
CLASSES.append  ( VTKPCACurvatureEstimation )        
TYPENAMES.append('VTKPCACurvatureEstimationType' )

#--------------------------------------------------------------
class VTKPCANormalEstimation(Node, VTKFilter1Node):

    bl_idname = 'VTKPCANormalEstimationType'
    bl_label  = 'vtkPCANormalEstimation'
    e_NormalOrientation_items=[ (x,x,x) for x in ['AsComputed', 'Point', 'GraphTraversal']]
    
    m_FlipNormals       = bpy.props.BoolProperty       ( name='FlipNormals',       default=False )
    m_SampleSize        = bpy.props.IntProperty        ( name='SampleSize',        default=25 )
    e_NormalOrientation = bpy.props.EnumProperty       ( name='NormalOrientation', default="Point", items=e_NormalOrientation_items )
    m_OrientationPoint  = bpy.props.FloatVectorProperty( name='OrientationPoint',  default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_FlipNormals','m_SampleSize','e_NormalOrientation','m_OrientationPoint',]
    
CLASSES.append  ( VTKPCANormalEstimation )        
TYPENAMES.append('VTKPCANormalEstimationType' )

#--------------------------------------------------------------
class VTKPCellDataToPointData(Node, VTKFilter1Node):

    bl_idname = 'VTKPCellDataToPointDataType'
    bl_label  = 'vtkPCellDataToPointData'
    
    m_PassCellData   = bpy.props.BoolProperty( name='PassCellData',   default=0 )
    m_PieceInvariant = bpy.props.BoolProperty( name='PieceInvariant', default=1 )
    
    def m_properties( self ):
        return ['m_PassCellData','m_PieceInvariant',]
    
CLASSES.append  ( VTKPCellDataToPointData )        
TYPENAMES.append('VTKPCellDataToPointDataType' )

#--------------------------------------------------------------
class VTKPLinearExtrusionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPLinearExtrusionFilterType'
    bl_label  = 'vtkPLinearExtrusionFilter'
    e_ExtrusionType_items=[ (x,x,x) for x in ['VectorExtrusion', 'NormalExtrusion', 'PointExtrusion']]
    
    m_Capping        = bpy.props.BoolProperty       ( name='Capping',        default=1 )
    m_PieceInvariant = bpy.props.BoolProperty       ( name='PieceInvariant', default=0 )
    m_ScaleFactor    = bpy.props.FloatProperty      ( name='ScaleFactor',    default=1.0 )
    e_ExtrusionType  = bpy.props.EnumProperty       ( name='ExtrusionType',  default="NormalExtrusion", items=e_ExtrusionType_items )
    m_ExtrusionPoint = bpy.props.FloatVectorProperty( name='ExtrusionPoint', default=(0.0, 0.0, 0.0), size=3 )
    m_Vector         = bpy.props.FloatVectorProperty( name='Vector',         default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Capping','m_PieceInvariant','m_ScaleFactor','e_ExtrusionType','m_ExtrusionPoint','m_Vector',]
    
CLASSES.append  ( VTKPLinearExtrusionFilter )        
TYPENAMES.append('VTKPLinearExtrusionFilterType' )

#--------------------------------------------------------------
class VTKPMaskPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKPMaskPointsType'
    bl_label  = 'vtkPMaskPoints'
    
    m_GenerateVertices                  = bpy.props.BoolProperty( name='GenerateVertices',                  default=0 )
    m_ProportionalMaximumNumberOfPoints = bpy.props.BoolProperty( name='ProportionalMaximumNumberOfPoints', default=0 )
    m_RandomMode                        = bpy.props.BoolProperty( name='RandomMode',                        default=0 )
    m_SingleVertexPerCell               = bpy.props.BoolProperty( name='SingleVertexPerCell',               default=0 )
    m_MaximumNumberOfPoints             = bpy.props.IntProperty ( name='MaximumNumberOfPoints',             default=0 )
    m_Offset                            = bpy.props.IntProperty ( name='Offset',                            default=0 )
    m_OnRatio                           = bpy.props.IntProperty ( name='OnRatio',                           default=2 )
    m_RandomModeType                    = bpy.props.IntProperty ( name='RandomModeType',                    default=0 )
    
    def m_properties( self ):
        return ['m_GenerateVertices','m_ProportionalMaximumNumberOfPoints','m_RandomMode','m_SingleVertexPerCell','m_MaximumNumberOfPoints','m_Offset','m_OnRatio','m_RandomModeType',]
    
CLASSES.append  ( VTKPMaskPoints )        
TYPENAMES.append('VTKPMaskPointsType' )

#--------------------------------------------------------------
class VTKPOutlineCornerFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPOutlineCornerFilterType'
    bl_label  = 'vtkPOutlineCornerFilter'
    
    m_CornerFactor = bpy.props.FloatProperty( name='CornerFactor', default=0.2 )
    
    def m_properties( self ):
        return ['m_CornerFactor',]
    
CLASSES.append  ( VTKPOutlineCornerFilter )        
TYPENAMES.append('VTKPOutlineCornerFilterType' )

#--------------------------------------------------------------
class VTKPOutlineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPOutlineFilterType'
    bl_label  = 'vtkPOutlineFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPOutlineFilter )        
TYPENAMES.append('VTKPOutlineFilterType' )

#--------------------------------------------------------------
class VTKPPolyDataNormals(Node, VTKFilter1Node):

    bl_idname = 'VTKPPolyDataNormalsType'
    bl_label  = 'vtkPPolyDataNormals'
    
    m_AutoOrientNormals    = bpy.props.BoolProperty ( name='AutoOrientNormals',    default=0 )
    m_ComputeCellNormals   = bpy.props.BoolProperty ( name='ComputeCellNormals',   default=0 )
    m_ComputePointNormals  = bpy.props.BoolProperty ( name='ComputePointNormals',  default=1 )
    m_Consistency          = bpy.props.BoolProperty ( name='Consistency',          default=1 )
    m_FlipNormals          = bpy.props.BoolProperty ( name='FlipNormals',          default=0 )
    m_NonManifoldTraversal = bpy.props.BoolProperty ( name='NonManifoldTraversal', default=1 )
    m_PieceInvariant       = bpy.props.BoolProperty ( name='PieceInvariant',       default=1 )
    m_Splitting            = bpy.props.BoolProperty ( name='Splitting',            default=1 )
    m_FeatureAngle         = bpy.props.FloatProperty( name='FeatureAngle',         default=30.0 )
    
    def m_properties( self ):
        return ['m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_PieceInvariant','m_Splitting','m_FeatureAngle',]
    
CLASSES.append  ( VTKPPolyDataNormals )        
TYPENAMES.append('VTKPPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKPProjectSphereFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPProjectSphereFilterType'
    bl_label  = 'vtkPProjectSphereFilter'
    
    m_KeepPolePoints = bpy.props.BoolProperty       ( name='KeepPolePoints', default=False )
    m_TranslateZ     = bpy.props.BoolProperty       ( name='TranslateZ',     default=False )
    m_Center         = bpy.props.FloatVectorProperty( name='Center',         default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_KeepPolePoints','m_TranslateZ','m_Center',]
    
CLASSES.append  ( VTKPProjectSphereFilter )        
TYPENAMES.append('VTKPProjectSphereFilterType' )

#--------------------------------------------------------------
class VTKPReflectionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPReflectionFilterType'
    bl_label  = 'vtkPReflectionFilter'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_CopyInput = bpy.props.BoolProperty ( name='CopyInput', default=1 )
    m_Center    = bpy.props.FloatProperty( name='Center',    default=0.0 )
    e_Plane     = bpy.props.EnumProperty ( name='Plane',     default="XMin", items=e_Plane_items )
    
    def m_properties( self ):
        return ['m_CopyInput','m_Center','e_Plane',]
    
CLASSES.append  ( VTKPReflectionFilter )        
TYPENAMES.append('VTKPReflectionFilterType' )

#--------------------------------------------------------------
class VTKPResampleFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPResampleFilterType'
    bl_label  = 'vtkPResampleFilter'
    
    m_UseInputBounds    = bpy.props.BoolProperty     ( name='UseInputBounds',    default=1 )
    m_SamplingDimension = bpy.props.IntVectorProperty( name='SamplingDimension', default=[10, 10, 10], size=3 )
    
    def m_properties( self ):
        return ['m_UseInputBounds','m_SamplingDimension',]
    
CLASSES.append  ( VTKPResampleFilter )        
TYPENAMES.append('VTKPResampleFilterType' )

#--------------------------------------------------------------
class VTKPYoungsMaterialInterface(Node, VTKFilter1Node):

    bl_idname = 'VTKPYoungsMaterialInterfaceType'
    bl_label  = 'vtkPYoungsMaterialInterface'
    
    m_AxisSymetric          = bpy.props.BoolProperty       ( name='AxisSymetric',          default=0 )
    m_FillMaterial          = bpy.props.BoolProperty       ( name='FillMaterial',          default=0 )
    m_InverseNormal         = bpy.props.BoolProperty       ( name='InverseNormal',         default=0 )
    m_OnionPeel             = bpy.props.BoolProperty       ( name='OnionPeel',             default=0 )
    m_ReverseMaterialOrder  = bpy.props.BoolProperty       ( name='ReverseMaterialOrder',  default=0 )
    m_UseAllBlocks          = bpy.props.BoolProperty       ( name='UseAllBlocks',          default=True )
    m_UseFractionAsDistance = bpy.props.BoolProperty       ( name='UseFractionAsDistance', default=0 )
    m_NumberOfMaterials     = bpy.props.IntProperty        ( name='NumberOfMaterials',     default=0 )
    m_VolumeFractionRange   = bpy.props.FloatVectorProperty( name='VolumeFractionRange',   default=(0.01, 0.99), size=2 )
    
    def m_properties( self ):
        return ['m_AxisSymetric','m_FillMaterial','m_InverseNormal','m_OnionPeel','m_ReverseMaterialOrder','m_UseAllBlocks','m_UseFractionAsDistance','m_NumberOfMaterials','m_VolumeFractionRange',]
    
CLASSES.append  ( VTKPYoungsMaterialInterface )        
TYPENAMES.append('VTKPYoungsMaterialInterfaceType' )

#--------------------------------------------------------------
class VTKPassArrays(Node, VTKFilter1Node):

    bl_idname = 'VTKPassArraysType'
    bl_label  = 'vtkPassArrays'
    
    m_RemoveArrays  = bpy.props.BoolProperty( name='RemoveArrays',  default=False )
    m_UseFieldTypes = bpy.props.BoolProperty( name='UseFieldTypes', default=False )
    
    def m_properties( self ):
        return ['m_RemoveArrays','m_UseFieldTypes',]
    
CLASSES.append  ( VTKPassArrays )        
TYPENAMES.append('VTKPassArraysType' )

#--------------------------------------------------------------
class VTKPassInputTypeAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKPassInputTypeAlgorithmType'
    bl_label  = 'vtkPassInputTypeAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPassInputTypeAlgorithm )        
TYPENAMES.append('VTKPassInputTypeAlgorithmType' )

#--------------------------------------------------------------
class VTKPassThrough(Node, VTKFilter1Node):

    bl_idname = 'VTKPassThroughType'
    bl_label  = 'vtkPassThrough'
    
    m_AllowNullInput = bpy.props.BoolProperty( name='AllowNullInput', default=False )
    m_DeepCopyInput  = bpy.props.BoolProperty( name='DeepCopyInput',  default=0 )
    
    def m_properties( self ):
        return ['m_AllowNullInput','m_DeepCopyInput',]
    
CLASSES.append  ( VTKPassThrough )        
TYPENAMES.append('VTKPassThroughType' )

#--------------------------------------------------------------
class VTKPassThroughFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPassThroughFilterType'
    bl_label  = 'vtkPassThroughFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPassThroughFilter )        
TYPENAMES.append('VTKPassThroughFilterType' )

#--------------------------------------------------------------
class VTKPerturbCoincidentVertices(Node, VTKFilter1Node):

    bl_idname = 'VTKPerturbCoincidentVerticesType'
    bl_label  = 'vtkPerturbCoincidentVertices'
    
    m_PerturbFactor = bpy.props.FloatProperty( name='PerturbFactor', default=1.0 )
    
    def m_properties( self ):
        return ['m_PerturbFactor',]
    
CLASSES.append  ( VTKPerturbCoincidentVertices )        
TYPENAMES.append('VTKPerturbCoincidentVerticesType' )

#--------------------------------------------------------------
class VTKPieceRequestFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPieceRequestFilterType'
    bl_label  = 'vtkPieceRequestFilter'
    
    m_NumberOfPieces = bpy.props.IntProperty( name='NumberOfPieces', default=1 )
    m_Piece          = bpy.props.IntProperty( name='Piece',          default=0 )
    
    def m_properties( self ):
        return ['m_NumberOfPieces','m_Piece',]
    
CLASSES.append  ( VTKPieceRequestFilter )        
TYPENAMES.append('VTKPieceRequestFilterType' )

#--------------------------------------------------------------
class VTKPieceScalars(Node, VTKFilter1Node):

    bl_idname = 'VTKPieceScalarsType'
    bl_label  = 'vtkPieceScalars'
    
    m_RandomMode = bpy.props.BoolProperty( name='RandomMode', default=0 )
    
    def m_properties( self ):
        return ['m_RandomMode',]
    
CLASSES.append  ( VTKPieceScalars )        
TYPENAMES.append('VTKPieceScalarsType' )

#--------------------------------------------------------------
class VTKPiecewiseFunctionAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKPiecewiseFunctionAlgorithmType'
    bl_label  = 'vtkPiecewiseFunctionAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPiecewiseFunctionAlgorithm )        
TYPENAMES.append('VTKPiecewiseFunctionAlgorithmType' )

#--------------------------------------------------------------
class VTKPiecewiseFunctionShiftScale(Node, VTKFilter1Node):

    bl_idname = 'VTKPiecewiseFunctionShiftScaleType'
    bl_label  = 'vtkPiecewiseFunctionShiftScale'
    
    m_PositionScale = bpy.props.FloatProperty( name='PositionScale', default=1.0 )
    m_PositionShift = bpy.props.FloatProperty( name='PositionShift', default=0.0 )
    m_ValueScale    = bpy.props.FloatProperty( name='ValueScale',    default=1.0 )
    m_ValueShift    = bpy.props.FloatProperty( name='ValueShift',    default=0.0 )
    
    def m_properties( self ):
        return ['m_PositionScale','m_PositionShift','m_ValueScale','m_ValueShift',]
    
CLASSES.append  ( VTKPiecewiseFunctionShiftScale )        
TYPENAMES.append('VTKPiecewiseFunctionShiftScaleType' )

#--------------------------------------------------------------
class VTKPlaneCutter(Node, VTKFilter1Node):

    bl_idname = 'VTKPlaneCutterType'
    bl_label  = 'vtkPlaneCutter'
    
    m_ComputeNormals        = bpy.props.BoolProperty( name='ComputeNormals',        default=0 )
    m_InterpolateAttributes = bpy.props.BoolProperty( name='InterpolateAttributes', default=1 )
    
    def m_properties( self ):
        return ['m_ComputeNormals','m_InterpolateAttributes',]
    
CLASSES.append  ( VTKPlaneCutter )        
TYPENAMES.append('VTKPlaneCutterType' )

#--------------------------------------------------------------
class VTKPointConnectivityFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPointConnectivityFilterType'
    bl_label  = 'vtkPointConnectivityFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPointConnectivityFilter )        
TYPENAMES.append('VTKPointConnectivityFilterType' )

#--------------------------------------------------------------
class VTKPointDataToCellData(Node, VTKFilter1Node):

    bl_idname = 'VTKPointDataToCellDataType'
    bl_label  = 'vtkPointDataToCellData'
    
    m_CategoricalData = bpy.props.BoolProperty( name='CategoricalData', default=0 )
    m_PassPointData   = bpy.props.BoolProperty( name='PassPointData',   default=0 )
    
    def m_properties( self ):
        return ['m_CategoricalData','m_PassPointData',]
    
CLASSES.append  ( VTKPointDataToCellData )        
TYPENAMES.append('VTKPointDataToCellDataType' )

#--------------------------------------------------------------
class VTKPointDensityFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPointDensityFilterType'
    bl_label  = 'vtkPointDensityFilter'
    e_DensityEstimate_items=[ (x,x,x) for x in ['FixedRadius', 'RelativeRadius']]
    e_DensityForm_items=[ (x,x,x) for x in ['VolumeNormalized', 'NumberOfPoints']]
    
    m_ComputeGradient  = bpy.props.BoolProperty       ( name='ComputeGradient',  default=False )
    m_ScalarWeighting  = bpy.props.BoolProperty       ( name='ScalarWeighting',  default=False )
    m_AdjustDistance   = bpy.props.FloatProperty      ( name='AdjustDistance',   default=0.1 )
    m_Radius           = bpy.props.FloatProperty      ( name='Radius',           default=1.0 )
    m_RelativeRadius   = bpy.props.FloatProperty      ( name='RelativeRadius',   default=1.0 )
    e_DensityEstimate  = bpy.props.EnumProperty       ( name='DensityEstimate',  default="RelativeRadius", items=e_DensityEstimate_items )
    e_DensityForm      = bpy.props.EnumProperty       ( name='DensityForm',      default="NumberOfPoints", items=e_DensityForm_items )
    m_SampleDimensions = bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[100, 100, 100], size=3 )
    m_ModelBounds      = bpy.props.FloatVectorProperty( name='ModelBounds',      default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_ComputeGradient','m_ScalarWeighting','m_AdjustDistance','m_Radius','m_RelativeRadius','e_DensityEstimate','e_DensityForm','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKPointDensityFilter )        
TYPENAMES.append('VTKPointDensityFilterType' )

#--------------------------------------------------------------
class VTKPointOccupancyFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPointOccupancyFilterType'
    bl_label  = 'vtkPointOccupancyFilter'
    
    m_EmptyValue       = bpy.props.IntProperty        ( name='EmptyValue',       default=0 )
    m_OccupiedValue    = bpy.props.IntProperty        ( name='OccupiedValue',    default=1 )
    m_SampleDimensions = bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[100, 100, 100], size=3 )
    m_ModelBounds      = bpy.props.FloatVectorProperty( name='ModelBounds',      default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_EmptyValue','m_OccupiedValue','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKPointOccupancyFilter )        
TYPENAMES.append('VTKPointOccupancyFilterType' )

#--------------------------------------------------------------
class VTKPointSetAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKPointSetAlgorithmType'
    bl_label  = 'vtkPointSetAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPointSetAlgorithm )        
TYPENAMES.append('VTKPointSetAlgorithmType' )

#--------------------------------------------------------------
class VTKPointSetToLabelHierarchy(Node, VTKFilter1Node):

    bl_idname = 'VTKPointSetToLabelHierarchyType'
    bl_label  = 'vtkPointSetToLabelHierarchy'
    
    m_UseUnicodeStrings    = bpy.props.BoolProperty  ( name='UseUnicodeStrings',    default=False )
    m_BoundedSizeArrayName = bpy.props.StringProperty( name='BoundedSizeArrayName', default="BoundedSize" )
    m_IconIndexArrayName   = bpy.props.StringProperty( name='IconIndexArrayName',   default="IconIndex" )
    m_LabelArrayName       = bpy.props.StringProperty( name='LabelArrayName',       default="LabelText" )
    m_OrientationArrayName = bpy.props.StringProperty( name='OrientationArrayName', default="Orientation" )
    m_PriorityArrayName    = bpy.props.StringProperty( name='PriorityArrayName',    default="Priority" )
    m_SizeArrayName        = bpy.props.StringProperty( name='SizeArrayName',        default="LabelSize" )
    m_MaximumDepth         = bpy.props.IntProperty   ( name='MaximumDepth',         default=5 )
    m_TargetLabelCount     = bpy.props.IntProperty   ( name='TargetLabelCount',     default=32 )
    
    def m_properties( self ):
        return ['m_UseUnicodeStrings','m_BoundedSizeArrayName','m_IconIndexArrayName','m_LabelArrayName','m_OrientationArrayName','m_PriorityArrayName','m_SizeArrayName','m_MaximumDepth','m_TargetLabelCount',]
    
CLASSES.append  ( VTKPointSetToLabelHierarchy )        
TYPENAMES.append('VTKPointSetToLabelHierarchyType' )

#--------------------------------------------------------------
class VTKPolyDataAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataAlgorithmType'
    bl_label  = 'vtkPolyDataAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKPolyDataAlgorithm )        
TYPENAMES.append('VTKPolyDataAlgorithmType' )

#--------------------------------------------------------------
class VTKPolyDataConnectivityFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataConnectivityFilterType'
    bl_label  = 'vtkPolyDataConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_ColorRegions           = bpy.props.BoolProperty       ( name='ColorRegions',           default=0 )
    m_FullScalarConnectivity = bpy.props.BoolProperty       ( name='FullScalarConnectivity', default=0 )
    m_MarkVisitedPointIds    = bpy.props.BoolProperty       ( name='MarkVisitedPointIds',    default=0 )
    m_ScalarConnectivity     = bpy.props.BoolProperty       ( name='ScalarConnectivity',     default=0 )
    e_ExtractionMode         = bpy.props.EnumProperty       ( name='ExtractionMode',         default="LargestRegion", items=e_ExtractionMode_items )
    m_ClosestPoint           = bpy.props.FloatVectorProperty( name='ClosestPoint',           default=(0.0, 0.0, 0.0), size=3 )
    m_ScalarRange            = bpy.props.FloatVectorProperty( name='ScalarRange',            default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_ColorRegions','m_FullScalarConnectivity','m_MarkVisitedPointIds','m_ScalarConnectivity','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    
CLASSES.append  ( VTKPolyDataConnectivityFilter )        
TYPENAMES.append('VTKPolyDataConnectivityFilterType' )

#--------------------------------------------------------------
class VTKPolyDataNormals(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataNormalsType'
    bl_label  = 'vtkPolyDataNormals'
    
    m_AutoOrientNormals    = bpy.props.BoolProperty ( name='AutoOrientNormals',    default=0 )
    m_ComputeCellNormals   = bpy.props.BoolProperty ( name='ComputeCellNormals',   default=0 )
    m_ComputePointNormals  = bpy.props.BoolProperty ( name='ComputePointNormals',  default=1 )
    m_Consistency          = bpy.props.BoolProperty ( name='Consistency',          default=1 )
    m_FlipNormals          = bpy.props.BoolProperty ( name='FlipNormals',          default=0 )
    m_NonManifoldTraversal = bpy.props.BoolProperty ( name='NonManifoldTraversal', default=1 )
    m_Splitting            = bpy.props.BoolProperty ( name='Splitting',            default=1 )
    m_FeatureAngle         = bpy.props.FloatProperty( name='FeatureAngle',         default=30.0 )
    
    def m_properties( self ):
        return ['m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_Splitting','m_FeatureAngle',]
    
CLASSES.append  ( VTKPolyDataNormals )        
TYPENAMES.append('VTKPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKPolyDataPointSampler(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataPointSamplerType'
    bl_label  = 'vtkPolyDataPointSampler'
    
    m_GenerateEdgePoints     = bpy.props.BoolProperty ( name='GenerateEdgePoints',     default=1 )
    m_GenerateInteriorPoints = bpy.props.BoolProperty ( name='GenerateInteriorPoints', default=1 )
    m_GenerateVertexPoints   = bpy.props.BoolProperty ( name='GenerateVertexPoints',   default=1 )
    m_GenerateVertices       = bpy.props.BoolProperty ( name='GenerateVertices',       default=1 )
    m_Distance               = bpy.props.FloatProperty( name='Distance',               default=0.01 )
    
    def m_properties( self ):
        return ['m_GenerateEdgePoints','m_GenerateInteriorPoints','m_GenerateVertexPoints','m_GenerateVertices','m_Distance',]
    
CLASSES.append  ( VTKPolyDataPointSampler )        
TYPENAMES.append('VTKPolyDataPointSamplerType' )

#--------------------------------------------------------------
class VTKPolyDataSilhouette(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataSilhouetteType'
    bl_label  = 'vtkPolyDataSilhouette'
    e_Direction_items=[ (x,x,x) for x in ['SpecifiedVector', 'SpecifiedOrigin', 'CameraOrigin', 'CameraVector']]
    
    m_BorderEdges        = bpy.props.BoolProperty       ( name='BorderEdges',        default=0 )
    m_PieceInvariant     = bpy.props.BoolProperty       ( name='PieceInvariant',     default=1 )
    m_EnableFeatureAngle = bpy.props.IntProperty        ( name='EnableFeatureAngle', default=1 )
    m_FeatureAngle       = bpy.props.FloatProperty      ( name='FeatureAngle',       default=60.0 )
    e_Direction          = bpy.props.EnumProperty       ( name='Direction',          default="CameraOrigin", items=e_Direction_items )
    m_Origin             = bpy.props.FloatVectorProperty( name='Origin',             default=(0.0, 0.0, 0.0), size=3 )
    m_Vector             = bpy.props.FloatVectorProperty( name='Vector',             default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_BorderEdges','m_PieceInvariant','m_EnableFeatureAngle','m_FeatureAngle','e_Direction','m_Origin','m_Vector',]
    
CLASSES.append  ( VTKPolyDataSilhouette )        
TYPENAMES.append('VTKPolyDataSilhouetteType' )

#--------------------------------------------------------------
class VTKPolyDataStreamer(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataStreamerType'
    bl_label  = 'vtkPolyDataStreamer'
    
    m_ColorByPiece            = bpy.props.BoolProperty( name='ColorByPiece',            default=0 )
    m_NumberOfStreamDivisions = bpy.props.IntProperty ( name='NumberOfStreamDivisions', default=2 )
    
    def m_properties( self ):
        return ['m_ColorByPiece','m_NumberOfStreamDivisions',]
    
CLASSES.append  ( VTKPolyDataStreamer )        
TYPENAMES.append('VTKPolyDataStreamerType' )

#--------------------------------------------------------------
class VTKPolyDataToImageStencil(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataToImageStencilType'
    bl_label  = 'vtkPolyDataToImageStencil'
    
    m_Tolerance         = bpy.props.FloatProperty      ( name='Tolerance',         default=7.62939453125e-06 )
    m_OutputWholeExtent = bpy.props.IntVectorProperty  ( name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6 )
    m_OutputOrigin      = bpy.props.FloatVectorProperty( name='OutputOrigin',      default=(0.0, 0.0, 0.0), size=3 )
    m_OutputSpacing     = bpy.props.FloatVectorProperty( name='OutputSpacing',     default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Tolerance','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    
CLASSES.append  ( VTKPolyDataToImageStencil )        
TYPENAMES.append('VTKPolyDataToImageStencilType' )

#--------------------------------------------------------------
class VTKPolyDataToReebGraphFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPolyDataToReebGraphFilterType'
    bl_label  = 'vtkPolyDataToReebGraphFilter'
    
    m_FieldId = bpy.props.IntProperty( name='FieldId', default=0 )
    
    def m_properties( self ):
        return ['m_FieldId',]
    
CLASSES.append  ( VTKPolyDataToReebGraphFilter )        
TYPENAMES.append('VTKPolyDataToReebGraphFilterType' )

#--------------------------------------------------------------
class VTKProcessIdScalars(Node, VTKFilter1Node):

    bl_idname = 'VTKProcessIdScalarsType'
    bl_label  = 'vtkProcessIdScalars'
    
    m_RandomMode = bpy.props.BoolProperty( name='RandomMode', default=0 )
    
    def m_properties( self ):
        return ['m_RandomMode',]
    
CLASSES.append  ( VTKProcessIdScalars )        
TYPENAMES.append('VTKProcessIdScalarsType' )

#--------------------------------------------------------------
class VTKProcrustesAlignmentFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKProcrustesAlignmentFilterType'
    bl_label  = 'vtkProcrustesAlignmentFilter'
    
    m_StartFromCentroid = bpy.props.BoolProperty( name='StartFromCentroid', default=False )
    
    def m_properties( self ):
        return ['m_StartFromCentroid',]
    
CLASSES.append  ( VTKProcrustesAlignmentFilter )        
TYPENAMES.append('VTKProcrustesAlignmentFilterType' )

#--------------------------------------------------------------
class VTKProgrammableAttributeDataFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKProgrammableAttributeDataFilterType'
    bl_label  = 'vtkProgrammableAttributeDataFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKProgrammableAttributeDataFilter )        
TYPENAMES.append('VTKProgrammableAttributeDataFilterType' )

#--------------------------------------------------------------
class VTKProgrammableFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKProgrammableFilterType'
    bl_label  = 'vtkProgrammableFilter'
    
    m_CopyArrays = bpy.props.BoolProperty( name='CopyArrays', default=False )
    
    def m_properties( self ):
        return ['m_CopyArrays',]
    
CLASSES.append  ( VTKProgrammableFilter )        
TYPENAMES.append('VTKProgrammableFilterType' )

#--------------------------------------------------------------
class VTKProjectSphereFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKProjectSphereFilterType'
    bl_label  = 'vtkProjectSphereFilter'
    
    m_KeepPolePoints = bpy.props.BoolProperty       ( name='KeepPolePoints', default=False )
    m_TranslateZ     = bpy.props.BoolProperty       ( name='TranslateZ',     default=False )
    m_Center         = bpy.props.FloatVectorProperty( name='Center',         default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_KeepPolePoints','m_TranslateZ','m_Center',]
    
CLASSES.append  ( VTKProjectSphereFilter )        
TYPENAMES.append('VTKProjectSphereFilterType' )

#--------------------------------------------------------------
class VTKProteinRibbonFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKProteinRibbonFilterType'
    bl_label  = 'vtkProteinRibbonFilter'
    
    m_DrawSmallMoleculesAsSpheres = bpy.props.BoolProperty ( name='DrawSmallMoleculesAsSpheres', default=True )
    m_SphereResolution            = bpy.props.IntProperty  ( name='SphereResolution',            default=20 )
    m_SubdivideFactor             = bpy.props.IntProperty  ( name='SubdivideFactor',             default=20 )
    m_CoilWidth                   = bpy.props.FloatProperty( name='CoilWidth',                   default=0.30000001192092896 )
    m_HelixWidth                  = bpy.props.FloatProperty( name='HelixWidth',                  default=1.2999999523162842 )
    
    def m_properties( self ):
        return ['m_DrawSmallMoleculesAsSpheres','m_SphereResolution','m_SubdivideFactor','m_CoilWidth','m_HelixWidth',]
    
CLASSES.append  ( VTKProteinRibbonFilter )        
TYPENAMES.append('VTKProteinRibbonFilterType' )

#--------------------------------------------------------------
class VTKPruneTreeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKPruneTreeFilterType'
    bl_label  = 'vtkPruneTreeFilter'
    
    m_ShouldPruneParentVertex = bpy.props.BoolProperty( name='ShouldPruneParentVertex', default=True )
    m_ParentVertex            = bpy.props.IntProperty ( name='ParentVertex',            default=0 )
    
    def m_properties( self ):
        return ['m_ShouldPruneParentVertex','m_ParentVertex',]
    
CLASSES.append  ( VTKPruneTreeFilter )        
TYPENAMES.append('VTKPruneTreeFilterType' )

#--------------------------------------------------------------
class VTKQuadRotationalExtrusionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKQuadRotationalExtrusionFilterType'
    bl_label  = 'vtkQuadRotationalExtrusionFilter'
    e_Axis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    
    m_Capping      = bpy.props.BoolProperty ( name='Capping',      default=1 )
    m_Resolution   = bpy.props.IntProperty  ( name='Resolution',   default=12 )
    m_DefaultAngle = bpy.props.FloatProperty( name='DefaultAngle', default=360.0 )
    m_DeltaRadius  = bpy.props.FloatProperty( name='DeltaRadius',  default=0.0 )
    m_Translation  = bpy.props.FloatProperty( name='Translation',  default=0.0 )
    e_Axis         = bpy.props.EnumProperty ( name='Axis',         default="Z", items=e_Axis_items )
    
    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_DefaultAngle','m_DeltaRadius','m_Translation','e_Axis',]
    
CLASSES.append  ( VTKQuadRotationalExtrusionFilter )        
TYPENAMES.append('VTKQuadRotationalExtrusionFilterType' )

#--------------------------------------------------------------
class VTKQuadraturePointInterpolator(Node, VTKFilter1Node):

    bl_idname = 'VTKQuadraturePointInterpolatorType'
    bl_label  = 'vtkQuadraturePointInterpolator'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKQuadraturePointInterpolator )        
TYPENAMES.append('VTKQuadraturePointInterpolatorType' )

#--------------------------------------------------------------
class VTKQuadraturePointsGenerator(Node, VTKFilter1Node):

    bl_idname = 'VTKQuadraturePointsGeneratorType'
    bl_label  = 'vtkQuadraturePointsGenerator'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKQuadraturePointsGenerator )        
TYPENAMES.append('VTKQuadraturePointsGeneratorType' )

#--------------------------------------------------------------
class VTKQuadratureSchemeDictionaryGenerator(Node, VTKFilter1Node):

    bl_idname = 'VTKQuadratureSchemeDictionaryGeneratorType'
    bl_label  = 'vtkQuadratureSchemeDictionaryGenerator'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKQuadratureSchemeDictionaryGenerator )        
TYPENAMES.append('VTKQuadratureSchemeDictionaryGeneratorType' )

#--------------------------------------------------------------
class VTKQuadricDecimation(Node, VTKFilter1Node):

    bl_idname = 'VTKQuadricDecimationType'
    bl_label  = 'vtkQuadricDecimation'
    
    m_AttributeErrorMetric = bpy.props.BoolProperty ( name='AttributeErrorMetric', default=0 )
    m_NormalsAttribute     = bpy.props.BoolProperty ( name='NormalsAttribute',     default=1 )
    m_ScalarsAttribute     = bpy.props.BoolProperty ( name='ScalarsAttribute',     default=1 )
    m_TCoordsAttribute     = bpy.props.BoolProperty ( name='TCoordsAttribute',     default=1 )
    m_TensorsAttribute     = bpy.props.BoolProperty ( name='TensorsAttribute',     default=1 )
    m_VectorsAttribute     = bpy.props.BoolProperty ( name='VectorsAttribute',     default=1 )
    m_VolumePreservation   = bpy.props.BoolProperty ( name='VolumePreservation',   default=0 )
    m_NormalsWeight        = bpy.props.FloatProperty( name='NormalsWeight',        default=0.1 )
    m_ScalarsWeight        = bpy.props.FloatProperty( name='ScalarsWeight',        default=0.1 )
    m_TCoordsWeight        = bpy.props.FloatProperty( name='TCoordsWeight',        default=0.1 )
    m_TargetReduction      = bpy.props.FloatProperty( name='TargetReduction',      default=0.9 )
    m_TensorsWeight        = bpy.props.FloatProperty( name='TensorsWeight',        default=0.1 )
    m_VectorsWeight        = bpy.props.FloatProperty( name='VectorsWeight',        default=0.1 )
    
    def m_properties( self ):
        return ['m_AttributeErrorMetric','m_NormalsAttribute','m_ScalarsAttribute','m_TCoordsAttribute','m_TensorsAttribute','m_VectorsAttribute','m_VolumePreservation','m_NormalsWeight','m_ScalarsWeight','m_TCoordsWeight','m_TargetReduction','m_TensorsWeight','m_VectorsWeight',]
    
CLASSES.append  ( VTKQuadricDecimation )        
TYPENAMES.append('VTKQuadricDecimationType' )

#--------------------------------------------------------------
class VTKQuantizePolyDataPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKQuantizePolyDataPointsType'
    bl_label  = 'vtkQuantizePolyDataPoints'
    
    m_ConvertLinesToPoints = bpy.props.BoolProperty ( name='ConvertLinesToPoints', default=1 )
    m_ConvertPolysToLines  = bpy.props.BoolProperty ( name='ConvertPolysToLines',  default=1 )
    m_ConvertStripsToPolys = bpy.props.BoolProperty ( name='ConvertStripsToPolys', default=1 )
    m_PieceInvariant       = bpy.props.BoolProperty ( name='PieceInvariant',       default=1 )
    m_PointMerging         = bpy.props.BoolProperty ( name='PointMerging',         default=1 )
    m_ToleranceIsAbsolute  = bpy.props.BoolProperty ( name='ToleranceIsAbsolute',  default=0 )
    m_AbsoluteTolerance    = bpy.props.FloatProperty( name='AbsoluteTolerance',    default=1.0 )
    m_QFactor              = bpy.props.FloatProperty( name='QFactor',              default=0.25 )
    m_Tolerance            = bpy.props.FloatProperty( name='Tolerance',            default=0.0 )
    
    def m_properties( self ):
        return ['m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_PointMerging','m_ToleranceIsAbsolute','m_AbsoluteTolerance','m_QFactor','m_Tolerance',]
    
CLASSES.append  ( VTKQuantizePolyDataPoints )        
TYPENAMES.append('VTKQuantizePolyDataPointsType' )

#--------------------------------------------------------------
class VTKRandomAttributeGenerator(Node, VTKFilter1Node):

    bl_idname = 'VTKRandomAttributeGeneratorType'
    bl_label  = 'vtkRandomAttributeGenerator'
    
    m_AttributesConstantPerBlock = bpy.props.BoolProperty ( name='AttributesConstantPerBlock', default=False )
    m_GenerateCellArray          = bpy.props.BoolProperty ( name='GenerateCellArray',          default=0 )
    m_GenerateCellNormals        = bpy.props.BoolProperty ( name='GenerateCellNormals',        default=0 )
    m_GenerateCellScalars        = bpy.props.BoolProperty ( name='GenerateCellScalars',        default=0 )
    m_GenerateCellTCoords        = bpy.props.BoolProperty ( name='GenerateCellTCoords',        default=0 )
    m_GenerateCellTensors        = bpy.props.BoolProperty ( name='GenerateCellTensors',        default=0 )
    m_GenerateCellVectors        = bpy.props.BoolProperty ( name='GenerateCellVectors',        default=0 )
    m_GenerateFieldArray         = bpy.props.BoolProperty ( name='GenerateFieldArray',         default=0 )
    m_GeneratePointArray         = bpy.props.BoolProperty ( name='GeneratePointArray',         default=0 )
    m_GeneratePointNormals       = bpy.props.BoolProperty ( name='GeneratePointNormals',       default=0 )
    m_GeneratePointScalars       = bpy.props.BoolProperty ( name='GeneratePointScalars',       default=0 )
    m_GeneratePointTCoords       = bpy.props.BoolProperty ( name='GeneratePointTCoords',       default=0 )
    m_GeneratePointTensors       = bpy.props.BoolProperty ( name='GeneratePointTensors',       default=0 )
    m_GeneratePointVectors       = bpy.props.BoolProperty ( name='GeneratePointVectors',       default=0 )
    m_NumberOfComponents         = bpy.props.IntProperty  ( name='NumberOfComponents',         default=1 )
    m_NumberOfTuples             = bpy.props.IntProperty  ( name='NumberOfTuples',             default=0 )
    m_MaximumComponentValue      = bpy.props.FloatProperty( name='MaximumComponentValue',      default=1.0 )
    m_MinimumComponentValue      = bpy.props.FloatProperty( name='MinimumComponentValue',      default=0.0 )
    
    def m_properties( self ):
        return ['m_AttributesConstantPerBlock','m_GenerateCellArray','m_GenerateCellNormals','m_GenerateCellScalars','m_GenerateCellTCoords','m_GenerateCellTensors','m_GenerateCellVectors','m_GenerateFieldArray','m_GeneratePointArray','m_GeneratePointNormals','m_GeneratePointScalars','m_GeneratePointTCoords','m_GeneratePointTensors','m_GeneratePointVectors','m_NumberOfComponents','m_NumberOfTuples','m_MaximumComponentValue','m_MinimumComponentValue',]
    
CLASSES.append  ( VTKRandomAttributeGenerator )        
TYPENAMES.append('VTKRandomAttributeGeneratorType' )

#--------------------------------------------------------------
class VTKRearrangeFields(Node, VTKFilter1Node):

    bl_idname = 'VTKRearrangeFieldsType'
    bl_label  = 'vtkRearrangeFields'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKRearrangeFields )        
TYPENAMES.append('VTKRearrangeFieldsType' )

#--------------------------------------------------------------
class VTKRectilinearGridAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKRectilinearGridAlgorithmType'
    bl_label  = 'vtkRectilinearGridAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKRectilinearGridAlgorithm )        
TYPENAMES.append('VTKRectilinearGridAlgorithmType' )

#--------------------------------------------------------------
class VTKRectilinearGridGeometryFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKRectilinearGridGeometryFilterType'
    bl_label  = 'vtkRectilinearGridGeometryFilter'
    
    m_Extent = bpy.props.IntVectorProperty( name='Extent', default=[0, 0, 0, 0, 0, 0], size=6 )
    
    def m_properties( self ):
        return ['m_Extent',]
    
CLASSES.append  ( VTKRectilinearGridGeometryFilter )        
TYPENAMES.append('VTKRectilinearGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKRectilinearGridOutlineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKRectilinearGridOutlineFilterType'
    bl_label  = 'vtkRectilinearGridOutlineFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKRectilinearGridOutlineFilter )        
TYPENAMES.append('VTKRectilinearGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKRectilinearGridPartitioner(Node, VTKFilter1Node):

    bl_idname = 'VTKRectilinearGridPartitionerType'
    bl_label  = 'vtkRectilinearGridPartitioner'
    
    m_DuplicateNodes      = bpy.props.BoolProperty( name='DuplicateNodes',      default=1 )
    m_NumberOfGhostLayers = bpy.props.IntProperty ( name='NumberOfGhostLayers', default=0 )
    m_NumberOfPartitions  = bpy.props.IntProperty ( name='NumberOfPartitions',  default=2 )
    
    def m_properties( self ):
        return ['m_DuplicateNodes','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    
CLASSES.append  ( VTKRectilinearGridPartitioner )        
TYPENAMES.append('VTKRectilinearGridPartitionerType' )

#--------------------------------------------------------------
class VTKRectilinearGridToPointSet(Node, VTKFilter1Node):

    bl_idname = 'VTKRectilinearGridToPointSetType'
    bl_label  = 'vtkRectilinearGridToPointSet'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKRectilinearGridToPointSet )        
TYPENAMES.append('VTKRectilinearGridToPointSetType' )

#--------------------------------------------------------------
class VTKRecursiveDividingCubes(Node, VTKFilter1Node):

    bl_idname = 'VTKRecursiveDividingCubesType'
    bl_label  = 'vtkRecursiveDividingCubes'
    
    m_Increment = bpy.props.IntProperty  ( name='Increment', default=1 )
    m_Distance  = bpy.props.FloatProperty( name='Distance',  default=0.1 )
    m_Value     = bpy.props.FloatProperty( name='Value',     default=0.0 )
    
    def m_properties( self ):
        return ['m_Increment','m_Distance','m_Value',]
    
CLASSES.append  ( VTKRecursiveDividingCubes )        
TYPENAMES.append('VTKRecursiveDividingCubesType' )

#--------------------------------------------------------------
class VTKReflectionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKReflectionFilterType'
    bl_label  = 'vtkReflectionFilter'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_CopyInput = bpy.props.BoolProperty ( name='CopyInput', default=1 )
    m_Center    = bpy.props.FloatProperty( name='Center',    default=0.0 )
    e_Plane     = bpy.props.EnumProperty ( name='Plane',     default="XMin", items=e_Plane_items )
    
    def m_properties( self ):
        return ['m_CopyInput','m_Center','e_Plane',]
    
CLASSES.append  ( VTKReflectionFilter )        
TYPENAMES.append('VTKReflectionFilterType' )

#--------------------------------------------------------------
class VTKRemoveIsolatedVertices(Node, VTKFilter1Node):

    bl_idname = 'VTKRemoveIsolatedVerticesType'
    bl_label  = 'vtkRemoveIsolatedVertices'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKRemoveIsolatedVertices )        
TYPENAMES.append('VTKRemoveIsolatedVerticesType' )

#--------------------------------------------------------------
class VTKReverseSense(Node, VTKFilter1Node):

    bl_idname = 'VTKReverseSenseType'
    bl_label  = 'vtkReverseSense'
    
    m_ReverseCells   = bpy.props.BoolProperty( name='ReverseCells',   default=1 )
    m_ReverseNormals = bpy.props.BoolProperty( name='ReverseNormals', default=0 )
    
    def m_properties( self ):
        return ['m_ReverseCells','m_ReverseNormals',]
    
CLASSES.append  ( VTKReverseSense )        
TYPENAMES.append('VTKReverseSenseType' )

#--------------------------------------------------------------
class VTKRibbonFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKRibbonFilterType'
    bl_label  = 'vtkRibbonFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    
    m_UseDefaultNormal = bpy.props.BoolProperty       ( name='UseDefaultNormal', default=0 )
    m_VaryWidth        = bpy.props.BoolProperty       ( name='VaryWidth',        default=0 )
    m_Angle            = bpy.props.FloatProperty      ( name='Angle',            default=0.0 )
    m_TextureLength    = bpy.props.FloatProperty      ( name='TextureLength',    default=1.0 )
    m_Width            = bpy.props.FloatProperty      ( name='Width',            default=0.5 )
    m_WidthFactor      = bpy.props.FloatProperty      ( name='WidthFactor',      default=2.0 )
    e_GenerateTCoords  = bpy.props.EnumProperty       ( name='GenerateTCoords',  default="Off", items=e_GenerateTCoords_items )
    m_DefaultNormal    = bpy.props.FloatVectorProperty( name='DefaultNormal',    default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_UseDefaultNormal','m_VaryWidth','m_Angle','m_TextureLength','m_Width','m_WidthFactor','e_GenerateTCoords','m_DefaultNormal',]
    
CLASSES.append  ( VTKRibbonFilter )        
TYPENAMES.append('VTKRibbonFilterType' )

#--------------------------------------------------------------
class VTKRotationFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKRotationFilterType'
    bl_label  = 'vtkRotationFilter'
    e_Axis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    
    m_CopyInput      = bpy.props.BoolProperty       ( name='CopyInput',      default=0 )
    m_NumberOfCopies = bpy.props.IntProperty        ( name='NumberOfCopies', default=0 )
    m_Angle          = bpy.props.FloatProperty      ( name='Angle',          default=0.0 )
    e_Axis           = bpy.props.EnumProperty       ( name='Axis',           default="Z", items=e_Axis_items )
    m_Center         = bpy.props.FloatVectorProperty( name='Center',         default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_CopyInput','m_NumberOfCopies','m_Angle','e_Axis','m_Center',]
    
CLASSES.append  ( VTKRotationFilter )        
TYPENAMES.append('VTKRotationFilterType' )

#--------------------------------------------------------------
class VTKRotationalExtrusionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKRotationalExtrusionFilterType'
    bl_label  = 'vtkRotationalExtrusionFilter'
    
    m_Capping     = bpy.props.BoolProperty ( name='Capping',     default=1 )
    m_Resolution  = bpy.props.IntProperty  ( name='Resolution',  default=12 )
    m_Angle       = bpy.props.FloatProperty( name='Angle',       default=360.0 )
    m_DeltaRadius = bpy.props.FloatProperty( name='DeltaRadius', default=0.0 )
    m_Translation = bpy.props.FloatProperty( name='Translation', default=0.0 )
    
    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_Angle','m_DeltaRadius','m_Translation',]
    
CLASSES.append  ( VTKRotationalExtrusionFilter )        
TYPENAMES.append('VTKRotationalExtrusionFilterType' )

#--------------------------------------------------------------
class VTKRuledSurfaceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKRuledSurfaceFilterType'
    bl_label  = 'vtkRuledSurfaceFilter'
    e_RuledMode_items=[ (x,x,x) for x in ['Resample', 'PointWalk']]
    
    m_CloseSurface   = bpy.props.BoolProperty     ( name='CloseSurface',   default=0 )
    m_OrientLoops    = bpy.props.BoolProperty     ( name='OrientLoops',    default=0 )
    m_PassLines      = bpy.props.BoolProperty     ( name='PassLines',      default=0 )
    m_Offset         = bpy.props.IntProperty      ( name='Offset',         default=0 )
    m_OnRatio        = bpy.props.IntProperty      ( name='OnRatio',        default=1 )
    m_DistanceFactor = bpy.props.FloatProperty    ( name='DistanceFactor', default=3.0 )
    e_RuledMode      = bpy.props.EnumProperty     ( name='RuledMode',      default="Resample", items=e_RuledMode_items )
    m_Resolution     = bpy.props.IntVectorProperty( name='Resolution',     default=[1, 1], size=2 )
    
    def m_properties( self ):
        return ['m_CloseSurface','m_OrientLoops','m_PassLines','m_Offset','m_OnRatio','m_DistanceFactor','e_RuledMode','m_Resolution',]
    
CLASSES.append  ( VTKRuledSurfaceFilter )        
TYPENAMES.append('VTKRuledSurfaceFilterType' )

#--------------------------------------------------------------
class VTKSMPWarpVector(Node, VTKFilter1Node):

    bl_idname = 'VTKSMPWarpVectorType'
    bl_label  = 'vtkSMPWarpVector'
    
    m_ScaleFactor = bpy.props.FloatProperty( name='ScaleFactor', default=1.0 )
    
    def m_properties( self ):
        return ['m_ScaleFactor',]
    
CLASSES.append  ( VTKSMPWarpVector )        
TYPENAMES.append('VTKSMPWarpVectorType' )

#--------------------------------------------------------------
class VTKSampleImplicitFunctionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSampleImplicitFunctionFilterType'
    bl_label  = 'vtkSampleImplicitFunctionFilter'
    
    m_ComputeGradients  = bpy.props.BoolProperty  ( name='ComputeGradients',  default=1 )
    m_GradientArrayName = bpy.props.StringProperty( name='GradientArrayName', default="Implicit gradients" )
    m_ScalarArrayName   = bpy.props.StringProperty( name='ScalarArrayName',   default="Implicit scalars" )
    
    def m_properties( self ):
        return ['m_ComputeGradients','m_GradientArrayName','m_ScalarArrayName',]
    
CLASSES.append  ( VTKSampleImplicitFunctionFilter )        
TYPENAMES.append('VTKSampleImplicitFunctionFilterType' )

#--------------------------------------------------------------
class VTKSelectVisiblePoints(Node, VTKFilter1Node):

    bl_idname = 'VTKSelectVisiblePointsType'
    bl_label  = 'vtkSelectVisiblePoints'
    
    m_SelectInvisible = bpy.props.BoolProperty     ( name='SelectInvisible', default=0 )
    m_SelectionWindow = bpy.props.BoolProperty     ( name='SelectionWindow', default=0 )
    m_Tolerance       = bpy.props.FloatProperty    ( name='Tolerance',       default=0.01 )
    m_Selection       = bpy.props.IntVectorProperty( name='Selection',       default=[0, 1600, 0, 1600], size=4 )
    
    def m_properties( self ):
        return ['m_SelectInvisible','m_SelectionWindow','m_Tolerance','m_Selection',]
    
CLASSES.append  ( VTKSelectVisiblePoints )        
TYPENAMES.append('VTKSelectVisiblePointsType' )

#--------------------------------------------------------------
class VTKSelectionAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKSelectionAlgorithmType'
    bl_label  = 'vtkSelectionAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKSelectionAlgorithm )        
TYPENAMES.append('VTKSelectionAlgorithmType' )

#--------------------------------------------------------------
class VTKShepardMethod(Node, VTKFilter1Node):

    bl_idname = 'VTKShepardMethodType'
    bl_label  = 'vtkShepardMethod'
    
    m_MaximumDistance  = bpy.props.FloatProperty      ( name='MaximumDistance',  default=0.25 )
    m_NullValue        = bpy.props.FloatProperty      ( name='NullValue',        default=0.0 )
    m_PowerParameter   = bpy.props.FloatProperty      ( name='PowerParameter',   default=2.0 )
    m_SampleDimensions = bpy.props.IntVectorProperty  ( name='SampleDimensions', default=[50, 50, 50], size=3 )
    m_ModelBounds      = bpy.props.FloatVectorProperty( name='ModelBounds',      default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_MaximumDistance','m_NullValue','m_PowerParameter','m_SampleDimensions','m_ModelBounds',]
    
CLASSES.append  ( VTKShepardMethod )        
TYPENAMES.append('VTKShepardMethodType' )

#--------------------------------------------------------------
class VTKShrinkFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKShrinkFilterType'
    bl_label  = 'vtkShrinkFilter'
    
    m_ShrinkFactor = bpy.props.FloatProperty( name='ShrinkFactor', default=0.5 )
    
    def m_properties( self ):
        return ['m_ShrinkFactor',]
    
CLASSES.append  ( VTKShrinkFilter )        
TYPENAMES.append('VTKShrinkFilterType' )

#--------------------------------------------------------------
class VTKShrinkPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKShrinkPolyDataType'
    bl_label  = 'vtkShrinkPolyData'
    
    m_ShrinkFactor = bpy.props.FloatProperty( name='ShrinkFactor', default=0.5 )
    
    def m_properties( self ):
        return ['m_ShrinkFactor',]
    
CLASSES.append  ( VTKShrinkPolyData )        
TYPENAMES.append('VTKShrinkPolyDataType' )

#--------------------------------------------------------------
class VTKSignedDistance(Node, VTKFilter1Node):

    bl_idname = 'VTKSignedDistanceType'
    bl_label  = 'vtkSignedDistance'
    
    m_Radius     = bpy.props.FloatProperty      ( name='Radius',     default=0.1 )
    m_Dimensions = bpy.props.IntVectorProperty  ( name='Dimensions', default=[256, 256, 256], size=3 )
    m_Bounds     = bpy.props.FloatVectorProperty( name='Bounds',     default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_Radius','m_Dimensions','m_Bounds',]
    
CLASSES.append  ( VTKSignedDistance )        
TYPENAMES.append('VTKSignedDistanceType' )

#--------------------------------------------------------------
class VTKSimpleBondPerceiver(Node, VTKFilter1Node):

    bl_idname = 'VTKSimpleBondPerceiverType'
    bl_label  = 'vtkSimpleBondPerceiver'
    
    m_Tolerance = bpy.props.FloatProperty( name='Tolerance', default=0.44999998807907104 )
    
    def m_properties( self ):
        return ['m_Tolerance',]
    
CLASSES.append  ( VTKSimpleBondPerceiver )        
TYPENAMES.append('VTKSimpleBondPerceiverType' )

#--------------------------------------------------------------
class VTKSimpleElevationFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSimpleElevationFilterType'
    bl_label  = 'vtkSimpleElevationFilter'
    
    m_Vector = bpy.props.FloatVectorProperty( name='Vector', default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Vector',]
    
CLASSES.append  ( VTKSimpleElevationFilter )        
TYPENAMES.append('VTKSimpleElevationFilterType' )

#--------------------------------------------------------------
class VTKSimpleImageFilterExample(Node, VTKFilter1Node):

    bl_idname = 'VTKSimpleImageFilterExampleType'
    bl_label  = 'vtkSimpleImageFilterExample'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKSimpleImageFilterExample )        
TYPENAMES.append('VTKSimpleImageFilterExampleType' )

#--------------------------------------------------------------
class VTKSparseArrayToTable(Node, VTKFilter1Node):

    bl_idname = 'VTKSparseArrayToTableType'
    bl_label  = 'vtkSparseArrayToTable'
    
    m_ValueColumn = bpy.props.StringProperty( name='ValueColumn', default="value" )
    
    def m_properties( self ):
        return ['m_ValueColumn',]
    
CLASSES.append  ( VTKSparseArrayToTable )        
TYPENAMES.append('VTKSparseArrayToTableType' )

#--------------------------------------------------------------
class VTKSpatialRepresentationFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSpatialRepresentationFilterType'
    bl_label  = 'vtkSpatialRepresentationFilter'
    
    m_GenerateLeaves = bpy.props.BoolProperty( name='GenerateLeaves', default=False )
    
    def m_properties( self ):
        return ['m_GenerateLeaves',]
    
CLASSES.append  ( VTKSpatialRepresentationFilter )        
TYPENAMES.append('VTKSpatialRepresentationFilterType' )

#--------------------------------------------------------------
class VTKSphereTreeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSphereTreeFilterType'
    bl_label  = 'vtkSphereTreeFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['Levels', 'Point', 'Line', 'Plane']]
    
    m_TreeHierarchy  = bpy.props.BoolProperty       ( name='TreeHierarchy',  default=1 )
    m_Level          = bpy.props.IntProperty        ( name='Level',          default=-1 )
    e_ExtractionMode = bpy.props.EnumProperty       ( name='ExtractionMode', default="Levels", items=e_ExtractionMode_items )
    m_Normal         = bpy.props.FloatVectorProperty( name='Normal',         default=(0.0, 0.0, 1.0), size=3 )
    m_Point          = bpy.props.FloatVectorProperty( name='Point',          default=(0.0, 0.0, 0.0), size=3 )
    m_Ray            = bpy.props.FloatVectorProperty( name='Ray',            default=(1.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_TreeHierarchy','m_Level','e_ExtractionMode','m_Normal','m_Point','m_Ray',]
    
CLASSES.append  ( VTKSphereTreeFilter )        
TYPENAMES.append('VTKSphereTreeFilterType' )

#--------------------------------------------------------------
class VTKSplineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSplineFilterType'
    bl_label  = 'vtkSplineFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    e_Subdivide_items=[ (x,x,x) for x in ['Specified', 'Length']]
    
    m_MaximumNumberOfSubdivisions = bpy.props.IntProperty  ( name='MaximumNumberOfSubdivisions', default=0 )
    m_NumberOfSubdivisions        = bpy.props.IntProperty  ( name='NumberOfSubdivisions',        default=100 )
    m_Length                      = bpy.props.FloatProperty( name='Length',                      default=0.1 )
    m_TextureLength               = bpy.props.FloatProperty( name='TextureLength',               default=1.0 )
    e_GenerateTCoords             = bpy.props.EnumProperty ( name='GenerateTCoords',             default="NormalizedLength", items=e_GenerateTCoords_items )
    e_Subdivide                   = bpy.props.EnumProperty ( name='Subdivide',                   default="Specified", items=e_Subdivide_items )
    
    def m_properties( self ):
        return ['m_MaximumNumberOfSubdivisions','m_NumberOfSubdivisions','m_Length','m_TextureLength','e_GenerateTCoords','e_Subdivide',]
    
CLASSES.append  ( VTKSplineFilter )        
TYPENAMES.append('VTKSplineFilterType' )

#--------------------------------------------------------------
class VTKSplineGraphEdges(Node, VTKFilter1Node):

    bl_idname = 'VTKSplineGraphEdgesType'
    bl_label  = 'vtkSplineGraphEdges'
    
    m_NumberOfSubdivisions = bpy.props.IntProperty( name='NumberOfSubdivisions', default=20 )
    m_SplineType           = bpy.props.IntProperty( name='SplineType',           default=1 )
    
    def m_properties( self ):
        return ['m_NumberOfSubdivisions','m_SplineType',]
    
CLASSES.append  ( VTKSplineGraphEdges )        
TYPENAMES.append('VTKSplineGraphEdgesType' )

#--------------------------------------------------------------
class VTKSplitByCellScalarFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSplitByCellScalarFilterType'
    bl_label  = 'vtkSplitByCellScalarFilter'
    
    m_PassAllPoints = bpy.props.BoolProperty( name='PassAllPoints', default=True )
    
    def m_properties( self ):
        return ['m_PassAllPoints',]
    
CLASSES.append  ( VTKSplitByCellScalarFilter )        
TYPENAMES.append('VTKSplitByCellScalarFilterType' )

#--------------------------------------------------------------
class VTKSplitColumnComponents(Node, VTKFilter1Node):

    bl_idname = 'VTKSplitColumnComponentsType'
    bl_label  = 'vtkSplitColumnComponents'
    e_NamingMode_items=[ (x,x,x) for x in ['NumberWithParens', 'NamesWithParens', 'NumberWithUnderscores', 'NamesWithUnderscores']]
    
    m_CalculateMagnitudes = bpy.props.BoolProperty( name='CalculateMagnitudes', default=True )
    e_NamingMode          = bpy.props.EnumProperty( name='NamingMode',          default="NumberWithParens", items=e_NamingMode_items )
    
    def m_properties( self ):
        return ['m_CalculateMagnitudes','e_NamingMode',]
    
CLASSES.append  ( VTKSplitColumnComponents )        
TYPENAMES.append('VTKSplitColumnComponentsType' )

#--------------------------------------------------------------
class VTKSplitField(Node, VTKFilter1Node):

    bl_idname = 'VTKSplitFieldType'
    bl_label  = 'vtkSplitField'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKSplitField )        
TYPENAMES.append('VTKSplitFieldType' )

#--------------------------------------------------------------
class VTKStrahlerMetric(Node, VTKFilter1Node):

    bl_idname = 'VTKStrahlerMetricType'
    bl_label  = 'vtkStrahlerMetric'
    
    m_Normalize = bpy.props.BoolProperty( name='Normalize', default=0 )
    
    def m_properties( self ):
        return ['m_Normalize',]
    
CLASSES.append  ( VTKStrahlerMetric )        
TYPENAMES.append('VTKStrahlerMetricType' )

#--------------------------------------------------------------
class VTKStreamGraph(Node, VTKFilter1Node):

    bl_idname = 'VTKStreamGraphType'
    bl_label  = 'vtkStreamGraph'
    
    m_UseEdgeWindow       = bpy.props.BoolProperty  ( name='UseEdgeWindow',       default=False )
    m_EdgeWindowArrayName = bpy.props.StringProperty( name='EdgeWindowArrayName', default="time" )
    m_EdgeWindow          = bpy.props.FloatProperty ( name='EdgeWindow',          default=10000.0 )
    
    def m_properties( self ):
        return ['m_UseEdgeWindow','m_EdgeWindowArrayName','m_EdgeWindow',]
    
CLASSES.append  ( VTKStreamGraph )        
TYPENAMES.append('VTKStreamGraphType' )

#--------------------------------------------------------------
class VTKStringToNumeric(Node, VTKFilter1Node):

    bl_idname = 'VTKStringToNumericType'
    bl_label  = 'vtkStringToNumeric'
    
    m_ConvertCellData                        = bpy.props.BoolProperty ( name='ConvertCellData',                        default=True )
    m_ConvertEdgeData                        = bpy.props.BoolProperty ( name='ConvertEdgeData',                        default=True )
    m_ConvertFieldData                       = bpy.props.BoolProperty ( name='ConvertFieldData',                       default=True )
    m_ConvertPointData                       = bpy.props.BoolProperty ( name='ConvertPointData',                       default=True )
    m_ConvertRowData                         = bpy.props.BoolProperty ( name='ConvertRowData',                         default=True )
    m_ConvertVertexData                      = bpy.props.BoolProperty ( name='ConvertVertexData',                      default=True )
    m_ForceDouble                            = bpy.props.BoolProperty ( name='ForceDouble',                            default=False )
    m_TrimWhitespacePriorToNumericConversion = bpy.props.BoolProperty ( name='TrimWhitespacePriorToNumericConversion', default=False )
    m_DefaultIntegerValue                    = bpy.props.IntProperty  ( name='DefaultIntegerValue',                    default=0 )
    m_DefaultDoubleValue                     = bpy.props.FloatProperty( name='DefaultDoubleValue',                     default=0.0 )
    
    def m_properties( self ):
        return ['m_ConvertCellData','m_ConvertEdgeData','m_ConvertFieldData','m_ConvertPointData','m_ConvertRowData','m_ConvertVertexData','m_ForceDouble','m_TrimWhitespacePriorToNumericConversion','m_DefaultIntegerValue','m_DefaultDoubleValue',]
    
CLASSES.append  ( VTKStringToNumeric )        
TYPENAMES.append('VTKStringToNumericType' )

#--------------------------------------------------------------
class VTKStripper(Node, VTKFilter1Node):

    bl_idname = 'VTKStripperType'
    bl_label  = 'vtkStripper'
    
    m_JoinContiguousSegments  = bpy.props.BoolProperty( name='JoinContiguousSegments',  default=0 )
    m_PassCellDataAsFieldData = bpy.props.BoolProperty( name='PassCellDataAsFieldData', default=0 )
    m_PassThroughCellIds      = bpy.props.BoolProperty( name='PassThroughCellIds',      default=0 )
    m_PassThroughPointIds     = bpy.props.BoolProperty( name='PassThroughPointIds',     default=0 )
    m_MaximumLength           = bpy.props.IntProperty ( name='MaximumLength',           default=1000 )
    
    def m_properties( self ):
        return ['m_JoinContiguousSegments','m_PassCellDataAsFieldData','m_PassThroughCellIds','m_PassThroughPointIds','m_MaximumLength',]
    
CLASSES.append  ( VTKStripper )        
TYPENAMES.append('VTKStripperType' )

#--------------------------------------------------------------
class VTKStructuredGridAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKStructuredGridAlgorithmType'
    bl_label  = 'vtkStructuredGridAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKStructuredGridAlgorithm )        
TYPENAMES.append('VTKStructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKStructuredGridAppend(Node, VTKFilter1Node):

    bl_idname = 'VTKStructuredGridAppendType'
    bl_label  = 'vtkStructuredGridAppend'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKStructuredGridAppend )        
TYPENAMES.append('VTKStructuredGridAppendType' )

#--------------------------------------------------------------
class VTKStructuredGridGeometryFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKStructuredGridGeometryFilterType'
    bl_label  = 'vtkStructuredGridGeometryFilter'
    
    m_Extent = bpy.props.IntVectorProperty( name='Extent', default=[0, 0, 0, 0, 0, 0], size=6 )
    
    def m_properties( self ):
        return ['m_Extent',]
    
CLASSES.append  ( VTKStructuredGridGeometryFilter )        
TYPENAMES.append('VTKStructuredGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKStructuredGridGhostDataGenerator(Node, VTKFilter1Node):

    bl_idname = 'VTKStructuredGridGhostDataGeneratorType'
    bl_label  = 'vtkStructuredGridGhostDataGenerator'
    
    m_NumberOfGhostLayers = bpy.props.IntProperty( name='NumberOfGhostLayers', default=0 )
    
    def m_properties( self ):
        return ['m_NumberOfGhostLayers',]
    
CLASSES.append  ( VTKStructuredGridGhostDataGenerator )        
TYPENAMES.append('VTKStructuredGridGhostDataGeneratorType' )

#--------------------------------------------------------------
class VTKStructuredGridOutlineFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKStructuredGridOutlineFilterType'
    bl_label  = 'vtkStructuredGridOutlineFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKStructuredGridOutlineFilter )        
TYPENAMES.append('VTKStructuredGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKStructuredGridPartitioner(Node, VTKFilter1Node):

    bl_idname = 'VTKStructuredGridPartitionerType'
    bl_label  = 'vtkStructuredGridPartitioner'
    
    m_DuplicateNodes      = bpy.props.BoolProperty( name='DuplicateNodes',      default=1 )
    m_NumberOfGhostLayers = bpy.props.IntProperty ( name='NumberOfGhostLayers', default=0 )
    m_NumberOfPartitions  = bpy.props.IntProperty ( name='NumberOfPartitions',  default=2 )
    
    def m_properties( self ):
        return ['m_DuplicateNodes','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    
CLASSES.append  ( VTKStructuredGridPartitioner )        
TYPENAMES.append('VTKStructuredGridPartitionerType' )

#--------------------------------------------------------------
class VTKSubdivideTetra(Node, VTKFilter1Node):

    bl_idname = 'VTKSubdivideTetraType'
    bl_label  = 'vtkSubdivideTetra'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKSubdivideTetra )        
TYPENAMES.append('VTKSubdivideTetraType' )

#--------------------------------------------------------------
class VTKSurfaceReconstructionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKSurfaceReconstructionFilterType'
    bl_label  = 'vtkSurfaceReconstructionFilter'
    
    m_NeighborhoodSize = bpy.props.IntProperty  ( name='NeighborhoodSize', default=20 )
    m_SampleSpacing    = bpy.props.FloatProperty( name='SampleSpacing',    default=-1.0 )
    
    def m_properties( self ):
        return ['m_NeighborhoodSize','m_SampleSpacing',]
    
CLASSES.append  ( VTKSurfaceReconstructionFilter )        
TYPENAMES.append('VTKSurfaceReconstructionFilterType' )

#--------------------------------------------------------------
class VTKTableAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKTableAlgorithmType'
    bl_label  = 'vtkTableAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTableAlgorithm )        
TYPENAMES.append('VTKTableAlgorithmType' )

#--------------------------------------------------------------
class VTKTableFFT(Node, VTKFilter1Node):

    bl_idname = 'VTKTableFFTType'
    bl_label  = 'vtkTableFFT'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTableFFT )        
TYPENAMES.append('VTKTableFFTType' )

#--------------------------------------------------------------
class VTKTableToArray(Node, VTKFilter1Node):

    bl_idname = 'VTKTableToArrayType'
    bl_label  = 'vtkTableToArray'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTableToArray )        
TYPENAMES.append('VTKTableToArrayType' )

#--------------------------------------------------------------
class VTKTableToPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKTableToPolyDataType'
    bl_label  = 'vtkTableToPolyData'
    
    m_Create2DPoints                        = bpy.props.BoolProperty  ( name='Create2DPoints',                        default=False )
    m_PreserveCoordinateColumnsAsDataArrays = bpy.props.BoolProperty  ( name='PreserveCoordinateColumnsAsDataArrays', default=False )
    m_XColumn                               = bpy.props.StringProperty( name='XColumn',                               default="" )
    m_YColumn                               = bpy.props.StringProperty( name='YColumn',                               default="" )
    m_ZColumn                               = bpy.props.StringProperty( name='ZColumn',                               default="" )
    m_XColumnIndex                          = bpy.props.IntProperty   ( name='XColumnIndex',                          default=-1 )
    m_XComponent                            = bpy.props.IntProperty   ( name='XComponent',                            default=0 )
    m_YColumnIndex                          = bpy.props.IntProperty   ( name='YColumnIndex',                          default=-1 )
    m_YComponent                            = bpy.props.IntProperty   ( name='YComponent',                            default=0 )
    m_ZColumnIndex                          = bpy.props.IntProperty   ( name='ZColumnIndex',                          default=-1 )
    m_ZComponent                            = bpy.props.IntProperty   ( name='ZComponent',                            default=0 )
    
    def m_properties( self ):
        return ['m_Create2DPoints','m_PreserveCoordinateColumnsAsDataArrays','m_XColumn','m_YColumn','m_ZColumn','m_XColumnIndex','m_XComponent','m_YColumnIndex','m_YComponent','m_ZColumnIndex','m_ZComponent',]
    
CLASSES.append  ( VTKTableToPolyData )        
TYPENAMES.append('VTKTableToPolyDataType' )

#--------------------------------------------------------------
class VTKTableToSparseArray(Node, VTKFilter1Node):

    bl_idname = 'VTKTableToSparseArrayType'
    bl_label  = 'vtkTableToSparseArray'
    
    m_ValueColumn = bpy.props.StringProperty( name='ValueColumn', default="" )
    
    def m_properties( self ):
        return ['m_ValueColumn',]
    
CLASSES.append  ( VTKTableToSparseArray )        
TYPENAMES.append('VTKTableToSparseArrayType' )

#--------------------------------------------------------------
class VTKTableToStructuredGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKTableToStructuredGridType'
    bl_label  = 'vtkTableToStructuredGrid'
    
    m_XColumn    = bpy.props.StringProperty( name='XColumn',    default="" )
    m_YColumn    = bpy.props.StringProperty( name='YColumn',    default="" )
    m_ZColumn    = bpy.props.StringProperty( name='ZColumn',    default="" )
    m_XComponent = bpy.props.IntProperty   ( name='XComponent', default=0 )
    m_YComponent = bpy.props.IntProperty   ( name='YComponent', default=0 )
    m_ZComponent = bpy.props.IntProperty   ( name='ZComponent', default=0 )
    
    def m_properties( self ):
        return ['m_XColumn','m_YColumn','m_ZColumn','m_XComponent','m_YComponent','m_ZComponent',]
    
CLASSES.append  ( VTKTableToStructuredGrid )        
TYPENAMES.append('VTKTableToStructuredGridType' )

#--------------------------------------------------------------
class VTKTableToTreeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTableToTreeFilterType'
    bl_label  = 'vtkTableToTreeFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTableToTreeFilter )        
TYPENAMES.append('VTKTableToTreeFilterType' )

#--------------------------------------------------------------
class VTKTemporalArrayOperatorFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTemporalArrayOperatorFilterType'
    bl_label  = 'vtkTemporalArrayOperatorFilter'
    
    m_OutputArrayNameSuffix = bpy.props.StringProperty( name='OutputArrayNameSuffix', default="" )
    m_FirstTimeStepIndex    = bpy.props.IntProperty   ( name='FirstTimeStepIndex',    default=0 )
    m_Operator              = bpy.props.IntProperty   ( name='Operator',              default=0 )
    m_SecondTimeStepIndex   = bpy.props.IntProperty   ( name='SecondTimeStepIndex',   default=0 )
    
    def m_properties( self ):
        return ['m_OutputArrayNameSuffix','m_FirstTimeStepIndex','m_Operator','m_SecondTimeStepIndex',]
    
CLASSES.append  ( VTKTemporalArrayOperatorFilter )        
TYPENAMES.append('VTKTemporalArrayOperatorFilterType' )

#--------------------------------------------------------------
class VTKTemporalDataSetCache(Node, VTKFilter1Node):

    bl_idname = 'VTKTemporalDataSetCacheType'
    bl_label  = 'vtkTemporalDataSetCache'
    
    m_CacheSize = bpy.props.IntProperty( name='CacheSize', default=10 )
    
    def m_properties( self ):
        return ['m_CacheSize',]
    
CLASSES.append  ( VTKTemporalDataSetCache )        
TYPENAMES.append('VTKTemporalDataSetCacheType' )

#--------------------------------------------------------------
class VTKTemporalInterpolator(Node, VTKFilter1Node):

    bl_idname = 'VTKTemporalInterpolatorType'
    bl_label  = 'vtkTemporalInterpolator'
    
    m_CacheData                = bpy.props.BoolProperty ( name='CacheData',                default=True )
    m_ResampleFactor           = bpy.props.IntProperty  ( name='ResampleFactor',           default=0 )
    m_DiscreteTimeStepInterval = bpy.props.FloatProperty( name='DiscreteTimeStepInterval', default=0.0 )
    
    def m_properties( self ):
        return ['m_CacheData','m_ResampleFactor','m_DiscreteTimeStepInterval',]
    
CLASSES.append  ( VTKTemporalInterpolator )        
TYPENAMES.append('VTKTemporalInterpolatorType' )

#--------------------------------------------------------------
class VTKTemporalShiftScale(Node, VTKFilter1Node):

    bl_idname = 'VTKTemporalShiftScaleType'
    bl_label  = 'vtkTemporalShiftScale'
    
    m_Periodic               = bpy.props.BoolProperty ( name='Periodic',               default=0 )
    m_PeriodicEndCorrection  = bpy.props.BoolProperty ( name='PeriodicEndCorrection',  default=1 )
    m_MaximumNumberOfPeriods = bpy.props.FloatProperty( name='MaximumNumberOfPeriods', default=1.0 )
    m_PostShift              = bpy.props.FloatProperty( name='PostShift',              default=0.0 )
    m_PreShift               = bpy.props.FloatProperty( name='PreShift',               default=0.0 )
    m_Scale                  = bpy.props.FloatProperty( name='Scale',                  default=1.0 )
    
    def m_properties( self ):
        return ['m_Periodic','m_PeriodicEndCorrection','m_MaximumNumberOfPeriods','m_PostShift','m_PreShift','m_Scale',]
    
CLASSES.append  ( VTKTemporalShiftScale )        
TYPENAMES.append('VTKTemporalShiftScaleType' )

#--------------------------------------------------------------
class VTKTemporalSnapToTimeStep(Node, VTKFilter1Node):

    bl_idname = 'VTKTemporalSnapToTimeStepType'
    bl_label  = 'vtkTemporalSnapToTimeStep'
    e_SnapMode_items=[ (x,x,x) for x in ['Nearest', 'NextBelowOrEqual', 'NextAboveOrEqual']]
    
    e_SnapMode = bpy.props.EnumProperty( name='SnapMode', default="Nearest", items=e_SnapMode_items )
    
    def m_properties( self ):
        return ['e_SnapMode',]
    
CLASSES.append  ( VTKTemporalSnapToTimeStep )        
TYPENAMES.append('VTKTemporalSnapToTimeStepType' )

#--------------------------------------------------------------
class VTKTemporalStatistics(Node, VTKFilter1Node):

    bl_idname = 'VTKTemporalStatisticsType'
    bl_label  = 'vtkTemporalStatistics'
    
    m_ComputeAverage           = bpy.props.BoolProperty( name='ComputeAverage',           default=1 )
    m_ComputeMaximum           = bpy.props.BoolProperty( name='ComputeMaximum',           default=1 )
    m_ComputeMinimum           = bpy.props.BoolProperty( name='ComputeMinimum',           default=1 )
    m_ComputeStandardDeviation = bpy.props.BoolProperty( name='ComputeStandardDeviation', default=1 )
    
    def m_properties( self ):
        return ['m_ComputeAverage','m_ComputeMaximum','m_ComputeMinimum','m_ComputeStandardDeviation',]
    
CLASSES.append  ( VTKTemporalStatistics )        
TYPENAMES.append('VTKTemporalStatisticsType' )

#--------------------------------------------------------------
class VTKTessellatorFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTessellatorFilterType'
    bl_label  = 'vtkTessellatorFilter'
    
    m_MergePoints                 = bpy.props.BoolProperty ( name='MergePoints',                 default=1 )
    m_MaximumNumberOfSubdivisions = bpy.props.IntProperty  ( name='MaximumNumberOfSubdivisions', default=3 )
    m_OutputDimension             = bpy.props.IntProperty  ( name='OutputDimension',             default=3 )
    m_ChordError                  = bpy.props.FloatProperty( name='ChordError',                  default=0.001 )
    
    def m_properties( self ):
        return ['m_MergePoints','m_MaximumNumberOfSubdivisions','m_OutputDimension','m_ChordError',]
    
CLASSES.append  ( VTKTessellatorFilter )        
TYPENAMES.append('VTKTessellatorFilterType' )

#--------------------------------------------------------------
class VTKTextureMapToCylinder(Node, VTKFilter1Node):

    bl_idname = 'VTKTextureMapToCylinderType'
    bl_label  = 'vtkTextureMapToCylinder'
    
    m_AutomaticCylinderGeneration = bpy.props.BoolProperty       ( name='AutomaticCylinderGeneration', default=1 )
    m_PreventSeam                 = bpy.props.BoolProperty       ( name='PreventSeam',                 default=1 )
    m_Point1                      = bpy.props.FloatVectorProperty( name='Point1',                      default=(0.0, 0.0, -0.5), size=3 )
    m_Point2                      = bpy.props.FloatVectorProperty( name='Point2',                      default=(0.0, 0.0, 0.5), size=3 )
    
    def m_properties( self ):
        return ['m_AutomaticCylinderGeneration','m_PreventSeam','m_Point1','m_Point2',]
    
CLASSES.append  ( VTKTextureMapToCylinder )        
TYPENAMES.append('VTKTextureMapToCylinderType' )

#--------------------------------------------------------------
class VTKTextureMapToPlane(Node, VTKFilter1Node):

    bl_idname = 'VTKTextureMapToPlaneType'
    bl_label  = 'vtkTextureMapToPlane'
    
    m_AutomaticPlaneGeneration = bpy.props.BoolProperty       ( name='AutomaticPlaneGeneration', default=1 )
    m_Normal                   = bpy.props.FloatVectorProperty( name='Normal',                   default=(0.0, 0.0, 1.0), size=3 )
    m_Origin                   = bpy.props.FloatVectorProperty( name='Origin',                   default=(0.0, 0.0, 0.0), size=3 )
    m_Point1                   = bpy.props.FloatVectorProperty( name='Point1',                   default=(0.0, 0.0, 0.0), size=3 )
    m_Point2                   = bpy.props.FloatVectorProperty( name='Point2',                   default=(0.0, 0.0, 0.0), size=3 )
    m_SRange                   = bpy.props.FloatVectorProperty( name='SRange',                   default=(0.0, 1.0), size=2 )
    m_TRange                   = bpy.props.FloatVectorProperty( name='TRange',                   default=(0.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_AutomaticPlaneGeneration','m_Normal','m_Origin','m_Point1','m_Point2','m_SRange','m_TRange',]
    
CLASSES.append  ( VTKTextureMapToPlane )        
TYPENAMES.append('VTKTextureMapToPlaneType' )

#--------------------------------------------------------------
class VTKTextureMapToSphere(Node, VTKFilter1Node):

    bl_idname = 'VTKTextureMapToSphereType'
    bl_label  = 'vtkTextureMapToSphere'
    
    m_AutomaticSphereGeneration = bpy.props.BoolProperty       ( name='AutomaticSphereGeneration', default=1 )
    m_PreventSeam               = bpy.props.BoolProperty       ( name='PreventSeam',               default=1 )
    m_Center                    = bpy.props.FloatVectorProperty( name='Center',                    default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_AutomaticSphereGeneration','m_PreventSeam','m_Center',]
    
CLASSES.append  ( VTKTextureMapToSphere )        
TYPENAMES.append('VTKTextureMapToSphereType' )

#--------------------------------------------------------------
class VTKThreshold(Node, VTKFilter1Node):

    bl_idname = 'VTKThresholdType'
    bl_label  = 'vtkThreshold'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData']]
    e_ComponentMode_items=[ (x,x,x) for x in ['UseSelected', 'UseAll', 'UseAny']]
    e_PointsDataType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_AllScalars             = bpy.props.BoolProperty( name='AllScalars',             default=1 )
    m_UseContinuousCellRange = bpy.props.BoolProperty( name='UseContinuousCellRange', default=0 )
    m_SelectedComponent      = bpy.props.IntProperty ( name='SelectedComponent',      default=0 )
    e_AttributeMode          = bpy.props.EnumProperty( name='AttributeMode',          default="Default", items=e_AttributeMode_items )
    e_ComponentMode          = bpy.props.EnumProperty( name='ComponentMode',          default="UseSelected", items=e_ComponentMode_items )
    e_PointsDataType         = bpy.props.EnumProperty( name='PointsDataType',         default="Double", items=e_PointsDataType_items )
    
    def m_properties( self ):
        return ['m_AllScalars','m_UseContinuousCellRange','m_SelectedComponent','e_AttributeMode','e_ComponentMode','e_PointsDataType',]
    
CLASSES.append  ( VTKThreshold )        
TYPENAMES.append('VTKThresholdType' )

#--------------------------------------------------------------
class VTKThresholdGraph(Node, VTKFilter1Node):

    bl_idname = 'VTKThresholdGraphType'
    bl_label  = 'vtkThresholdGraph'
    
    m_LowerThreshold = bpy.props.FloatProperty( name='LowerThreshold', default=0.0 )
    m_UpperThreshold = bpy.props.FloatProperty( name='UpperThreshold', default=0.0 )
    
    def m_properties( self ):
        return ['m_LowerThreshold','m_UpperThreshold',]
    
CLASSES.append  ( VTKThresholdGraph )        
TYPENAMES.append('VTKThresholdGraphType' )

#--------------------------------------------------------------
class VTKThresholdPoints(Node, VTKFilter1Node):

    bl_idname = 'VTKThresholdPointsType'
    bl_label  = 'vtkThresholdPoints'
    
    m_LowerThreshold = bpy.props.FloatProperty( name='LowerThreshold', default=0.0 )
    m_UpperThreshold = bpy.props.FloatProperty( name='UpperThreshold', default=1.0 )
    
    def m_properties( self ):
        return ['m_LowerThreshold','m_UpperThreshold',]
    
CLASSES.append  ( VTKThresholdPoints )        
TYPENAMES.append('VTKThresholdPointsType' )

#--------------------------------------------------------------
class VTKThresholdTable(Node, VTKFilter1Node):

    bl_idname = 'VTKThresholdTableType'
    bl_label  = 'vtkThresholdTable'
    
    m_Mode = bpy.props.IntProperty( name='Mode', default=0 )
    
    def m_properties( self ):
        return ['m_Mode',]
    
CLASSES.append  ( VTKThresholdTable )        
TYPENAMES.append('VTKThresholdTableType' )

#--------------------------------------------------------------
class VTKThresholdTextureCoords(Node, VTKFilter1Node):

    bl_idname = 'VTKThresholdTextureCoordsType'
    bl_label  = 'vtkThresholdTextureCoords'
    
    m_TextureDimension = bpy.props.IntProperty        ( name='TextureDimension', default=2 )
    m_InTextureCoord   = bpy.props.FloatVectorProperty( name='InTextureCoord',   default=(0.75, 0.0, 0.0), size=3 )
    m_OutTextureCoord  = bpy.props.FloatVectorProperty( name='OutTextureCoord',  default=(0.25, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_TextureDimension','m_InTextureCoord','m_OutTextureCoord',]
    
CLASSES.append  ( VTKThresholdTextureCoords )        
TYPENAMES.append('VTKThresholdTextureCoordsType' )

#--------------------------------------------------------------
class VTKTransformCoordinateSystems(Node, VTKFilter1Node):

    bl_idname = 'VTKTransformCoordinateSystemsType'
    bl_label  = 'vtkTransformCoordinateSystems'
    e_InputCoordinateSystem_items=[ (x,x,x) for x in ['Display', 'Viewport', 'World']]
    e_OutputCoordinateSystem_items=[ (x,x,x) for x in ['Display', 'Viewport', 'World']]
    
    e_InputCoordinateSystem  = bpy.props.EnumProperty( name='InputCoordinateSystem',  default="World", items=e_InputCoordinateSystem_items )
    e_OutputCoordinateSystem = bpy.props.EnumProperty( name='OutputCoordinateSystem', default="Display", items=e_OutputCoordinateSystem_items )
    
    def m_properties( self ):
        return ['e_InputCoordinateSystem','e_OutputCoordinateSystem',]
    
CLASSES.append  ( VTKTransformCoordinateSystems )        
TYPENAMES.append('VTKTransformCoordinateSystemsType' )

#--------------------------------------------------------------
class VTKTransformFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTransformFilterType'
    bl_label  = 'vtkTransformFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTransformFilter )        
TYPENAMES.append('VTKTransformFilterType' )

#--------------------------------------------------------------
class VTKTransformPolyDataFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTransformPolyDataFilterType'
    bl_label  = 'vtkTransformPolyDataFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTransformPolyDataFilter )        
TYPENAMES.append('VTKTransformPolyDataFilterType' )

#--------------------------------------------------------------
class VTKTransformTextureCoords(Node, VTKFilter1Node):

    bl_idname = 'VTKTransformTextureCoordsType'
    bl_label  = 'vtkTransformTextureCoords'
    
    m_FlipR    = bpy.props.BoolProperty       ( name='FlipR',    default=0 )
    m_FlipS    = bpy.props.BoolProperty       ( name='FlipS',    default=0 )
    m_FlipT    = bpy.props.BoolProperty       ( name='FlipT',    default=0 )
    m_Origin   = bpy.props.FloatVectorProperty( name='Origin',   default=(0.5, 0.5, 0.5), size=3 )
    m_Position = bpy.props.FloatVectorProperty( name='Position', default=(0.0, 0.0, 0.0), size=3 )
    m_Scale    = bpy.props.FloatVectorProperty( name='Scale',    default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FlipR','m_FlipS','m_FlipT','m_Origin','m_Position','m_Scale',]
    
CLASSES.append  ( VTKTransformTextureCoords )        
TYPENAMES.append('VTKTransformTextureCoordsType' )

#--------------------------------------------------------------
class VTKTransmitImageDataPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKTransmitImageDataPieceType'
    bl_label  = 'vtkTransmitImageDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKTransmitImageDataPiece )        
TYPENAMES.append('VTKTransmitImageDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitPolyDataPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKTransmitPolyDataPieceType'
    bl_label  = 'vtkTransmitPolyDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKTransmitPolyDataPiece )        
TYPENAMES.append('VTKTransmitPolyDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitRectilinearGridPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKTransmitRectilinearGridPieceType'
    bl_label  = 'vtkTransmitRectilinearGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKTransmitRectilinearGridPiece )        
TYPENAMES.append('VTKTransmitRectilinearGridPieceType' )

#--------------------------------------------------------------
class VTKTransmitStructuredDataPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKTransmitStructuredDataPieceType'
    bl_label  = 'vtkTransmitStructuredDataPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKTransmitStructuredDataPiece )        
TYPENAMES.append('VTKTransmitStructuredDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitStructuredGridPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKTransmitStructuredGridPieceType'
    bl_label  = 'vtkTransmitStructuredGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKTransmitStructuredGridPiece )        
TYPENAMES.append('VTKTransmitStructuredGridPieceType' )

#--------------------------------------------------------------
class VTKTransmitUnstructuredGridPiece(Node, VTKFilter1Node):

    bl_idname = 'VTKTransmitUnstructuredGridPieceType'
    bl_label  = 'vtkTransmitUnstructuredGridPiece'
    
    m_CreateGhostCells = bpy.props.BoolProperty( name='CreateGhostCells', default=1 )
    
    def m_properties( self ):
        return ['m_CreateGhostCells',]
    
CLASSES.append  ( VTKTransmitUnstructuredGridPiece )        
TYPENAMES.append('VTKTransmitUnstructuredGridPieceType' )

#--------------------------------------------------------------
class VTKTransposeMatrix(Node, VTKFilter1Node):

    bl_idname = 'VTKTransposeMatrixType'
    bl_label  = 'vtkTransposeMatrix'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTransposeMatrix )        
TYPENAMES.append('VTKTransposeMatrixType' )

#--------------------------------------------------------------
class VTKTransposeTable(Node, VTKFilter1Node):

    bl_idname = 'VTKTransposeTableType'
    bl_label  = 'vtkTransposeTable'
    
    m_AddIdColumn  = bpy.props.BoolProperty  ( name='AddIdColumn',  default=True )
    m_UseIdColumn  = bpy.props.BoolProperty  ( name='UseIdColumn',  default=False )
    m_IdColumnName = bpy.props.StringProperty( name='IdColumnName', default="ColName" )
    
    def m_properties( self ):
        return ['m_AddIdColumn','m_UseIdColumn','m_IdColumnName',]
    
CLASSES.append  ( VTKTransposeTable )        
TYPENAMES.append('VTKTransposeTableType' )

#--------------------------------------------------------------
class VTKTreeAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKTreeAlgorithmType'
    bl_label  = 'vtkTreeAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTreeAlgorithm )        
TYPENAMES.append('VTKTreeAlgorithmType' )

#--------------------------------------------------------------
class VTKTreeFieldAggregator(Node, VTKFilter1Node):

    bl_idname = 'VTKTreeFieldAggregatorType'
    bl_label  = 'vtkTreeFieldAggregator'
    
    m_LeafVertexUnitSize = bpy.props.BoolProperty  ( name='LeafVertexUnitSize', default=True )
    m_LogScale           = bpy.props.BoolProperty  ( name='LogScale',           default=False )
    m_Field              = bpy.props.StringProperty( name='Field',              default="" )
    m_MinValue           = bpy.props.FloatProperty ( name='MinValue',           default=0.0 )
    
    def m_properties( self ):
        return ['m_LeafVertexUnitSize','m_LogScale','m_Field','m_MinValue',]
    
CLASSES.append  ( VTKTreeFieldAggregator )        
TYPENAMES.append('VTKTreeFieldAggregatorType' )

#--------------------------------------------------------------
class VTKTreeLevelsFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTreeLevelsFilterType'
    bl_label  = 'vtkTreeLevelsFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTreeLevelsFilter )        
TYPENAMES.append('VTKTreeLevelsFilterType' )

#--------------------------------------------------------------
class VTKTreeMapLayout(Node, VTKFilter1Node):

    bl_idname = 'VTKTreeMapLayoutType'
    bl_label  = 'vtkTreeMapLayout'
    
    m_RectanglesFieldName = bpy.props.StringProperty( name='RectanglesFieldName', default="area" )
    
    def m_properties( self ):
        return ['m_RectanglesFieldName',]
    
CLASSES.append  ( VTKTreeMapLayout )        
TYPENAMES.append('VTKTreeMapLayoutType' )

#--------------------------------------------------------------
class VTKTreeMapToPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKTreeMapToPolyDataType'
    bl_label  = 'vtkTreeMapToPolyData'
    
    m_AddNormals  = bpy.props.BoolProperty ( name='AddNormals',  default=True )
    m_LevelDeltaZ = bpy.props.FloatProperty( name='LevelDeltaZ', default=0.001 )
    
    def m_properties( self ):
        return ['m_AddNormals','m_LevelDeltaZ',]
    
CLASSES.append  ( VTKTreeMapToPolyData )        
TYPENAMES.append('VTKTreeMapToPolyDataType' )

#--------------------------------------------------------------
class VTKTreeRingToPolyData(Node, VTKFilter1Node):

    bl_idname = 'VTKTreeRingToPolyDataType'
    bl_label  = 'vtkTreeRingToPolyData'
    
    m_ShrinkPercentage = bpy.props.FloatProperty( name='ShrinkPercentage', default=0.0 )
    
    def m_properties( self ):
        return ['m_ShrinkPercentage',]
    
CLASSES.append  ( VTKTreeRingToPolyData )        
TYPENAMES.append('VTKTreeRingToPolyDataType' )

#--------------------------------------------------------------
class VTKTriangleFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTriangleFilterType'
    bl_label  = 'vtkTriangleFilter'
    
    m_PassLines = bpy.props.BoolProperty( name='PassLines', default=1 )
    m_PassVerts = bpy.props.BoolProperty( name='PassVerts', default=1 )
    
    def m_properties( self ):
        return ['m_PassLines','m_PassVerts',]
    
CLASSES.append  ( VTKTriangleFilter )        
TYPENAMES.append('VTKTriangleFilterType' )

#--------------------------------------------------------------
class VTKTriangleMeshPointNormals(Node, VTKFilter1Node):

    bl_idname = 'VTKTriangleMeshPointNormalsType'
    bl_label  = 'vtkTriangleMeshPointNormals'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTriangleMeshPointNormals )        
TYPENAMES.append('VTKTriangleMeshPointNormalsType' )

#--------------------------------------------------------------
class VTKTriangularTCoords(Node, VTKFilter1Node):

    bl_idname = 'VTKTriangularTCoordsType'
    bl_label  = 'vtkTriangularTCoords'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKTriangularTCoords )        
TYPENAMES.append('VTKTriangularTCoordsType' )

#--------------------------------------------------------------
class VTKTubeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKTubeFilterType'
    bl_label  = 'vtkTubeFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    e_VaryRadius_items=[ (x,x,x) for x in ['VaryRadiusOff', 'VaryRadiusByScalar', 'VaryRadiusByVector', 'VaryRadiusByAbsoluteScalar']]
    
    m_Capping            = bpy.props.BoolProperty       ( name='Capping',            default=0 )
    m_SidesShareVertices = bpy.props.BoolProperty       ( name='SidesShareVertices', default=1 )
    m_UseDefaultNormal   = bpy.props.BoolProperty       ( name='UseDefaultNormal',   default=0 )
    m_NumberOfSides      = bpy.props.IntProperty        ( name='NumberOfSides',      default=3 )
    m_Offset             = bpy.props.IntProperty        ( name='Offset',             default=0 )
    m_OnRatio            = bpy.props.IntProperty        ( name='OnRatio',            default=1 )
    m_Radius             = bpy.props.FloatProperty      ( name='Radius',             default=0.5 )
    m_RadiusFactor       = bpy.props.FloatProperty      ( name='RadiusFactor',       default=10.0 )
    m_TextureLength      = bpy.props.FloatProperty      ( name='TextureLength',      default=1.0 )
    e_GenerateTCoords    = bpy.props.EnumProperty       ( name='GenerateTCoords',    default="Off", items=e_GenerateTCoords_items )
    e_VaryRadius         = bpy.props.EnumProperty       ( name='VaryRadius',         default="VaryRadiusOff", items=e_VaryRadius_items )
    m_DefaultNormal      = bpy.props.FloatVectorProperty( name='DefaultNormal',      default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Capping','m_SidesShareVertices','m_UseDefaultNormal','m_NumberOfSides','m_Offset','m_OnRatio','m_Radius','m_RadiusFactor','m_TextureLength','e_GenerateTCoords','e_VaryRadius','m_DefaultNormal',]
    
CLASSES.append  ( VTKTubeFilter )        
TYPENAMES.append('VTKTubeFilterType' )

#--------------------------------------------------------------
class VTKUncertaintyTubeFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKUncertaintyTubeFilterType'
    bl_label  = 'vtkUncertaintyTubeFilter'
    
    m_NumberOfSides = bpy.props.IntProperty( name='NumberOfSides', default=12 )
    
    def m_properties( self ):
        return ['m_NumberOfSides',]
    
CLASSES.append  ( VTKUncertaintyTubeFilter )        
TYPENAMES.append('VTKUncertaintyTubeFilterType' )

#--------------------------------------------------------------
class VTKUndirectedGraphAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKUndirectedGraphAlgorithmType'
    bl_label  = 'vtkUndirectedGraphAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKUndirectedGraphAlgorithm )        
TYPENAMES.append('VTKUndirectedGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKUniformGridAMRAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKUniformGridAMRAlgorithmType'
    bl_label  = 'vtkUniformGridAMRAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKUniformGridAMRAlgorithm )        
TYPENAMES.append('VTKUniformGridAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKUniformGridGhostDataGenerator(Node, VTKFilter1Node):

    bl_idname = 'VTKUniformGridGhostDataGeneratorType'
    bl_label  = 'vtkUniformGridGhostDataGenerator'
    
    m_NumberOfGhostLayers = bpy.props.IntProperty( name='NumberOfGhostLayers', default=0 )
    
    def m_properties( self ):
        return ['m_NumberOfGhostLayers',]
    
CLASSES.append  ( VTKUniformGridGhostDataGenerator )        
TYPENAMES.append('VTKUniformGridGhostDataGeneratorType' )

#--------------------------------------------------------------
class VTKUniformGridPartitioner(Node, VTKFilter1Node):

    bl_idname = 'VTKUniformGridPartitionerType'
    bl_label  = 'vtkUniformGridPartitioner'
    
    m_DuplicateNodes      = bpy.props.BoolProperty( name='DuplicateNodes',      default=1 )
    m_NumberOfGhostLayers = bpy.props.IntProperty ( name='NumberOfGhostLayers', default=0 )
    m_NumberOfPartitions  = bpy.props.IntProperty ( name='NumberOfPartitions',  default=2 )
    
    def m_properties( self ):
        return ['m_DuplicateNodes','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    
CLASSES.append  ( VTKUniformGridPartitioner )        
TYPENAMES.append('VTKUniformGridPartitionerType' )

#--------------------------------------------------------------
class VTKUnsignedDistance(Node, VTKFilter1Node):

    bl_idname = 'VTKUnsignedDistanceType'
    bl_label  = 'vtkUnsignedDistance'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_AdjustBounds     = bpy.props.BoolProperty       ( name='AdjustBounds',     default=1 )
    m_Capping          = bpy.props.BoolProperty       ( name='Capping',          default=1 )
    m_AdjustDistance   = bpy.props.FloatProperty      ( name='AdjustDistance',   default=0.0125 )
    m_CapValue         = bpy.props.FloatProperty      ( name='CapValue',         default=9.999999680285692e+37 )
    m_Radius           = bpy.props.FloatProperty      ( name='Radius',           default=0.1 )
    e_OutputScalarType = bpy.props.EnumProperty       ( name='OutputScalarType', default="Float", items=e_OutputScalarType_items )
    m_Dimensions       = bpy.props.IntVectorProperty  ( name='Dimensions',       default=[256, 256, 256], size=3 )
    m_Bounds           = bpy.props.FloatVectorProperty( name='Bounds',           default=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), size=6 )
    
    def m_properties( self ):
        return ['m_AdjustBounds','m_Capping','m_AdjustDistance','m_CapValue','m_Radius','e_OutputScalarType','m_Dimensions','m_Bounds',]
    
CLASSES.append  ( VTKUnsignedDistance )        
TYPENAMES.append('VTKUnsignedDistanceType' )

#--------------------------------------------------------------
class VTKUnstructuredGridAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKUnstructuredGridAlgorithmType'
    bl_label  = 'vtkUnstructuredGridAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKUnstructuredGridAlgorithm )        
TYPENAMES.append('VTKUnstructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKUnstructuredGridBaseAlgorithm(Node, VTKFilter1Node):

    bl_idname = 'VTKUnstructuredGridBaseAlgorithmType'
    bl_label  = 'vtkUnstructuredGridBaseAlgorithm'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKUnstructuredGridBaseAlgorithm )        
TYPENAMES.append('VTKUnstructuredGridBaseAlgorithmType' )

#--------------------------------------------------------------
class VTKUnstructuredGridQuadricDecimation(Node, VTKFilter1Node):

    bl_idname = 'VTKUnstructuredGridQuadricDecimationType'
    bl_label  = 'vtkUnstructuredGridQuadricDecimation'
    
    m_ScalarsName                = bpy.props.StringProperty( name='ScalarsName',                default="" )
    m_AutoAddCandidates          = bpy.props.IntProperty   ( name='AutoAddCandidates',          default=1 )
    m_NumberOfCandidates         = bpy.props.IntProperty   ( name='NumberOfCandidates',         default=8 )
    m_NumberOfEdgesToDecimate    = bpy.props.IntProperty   ( name='NumberOfEdgesToDecimate',    default=0 )
    m_NumberOfTetsOutput         = bpy.props.IntProperty   ( name='NumberOfTetsOutput',         default=0 )
    m_AutoAddCandidatesThreshold = bpy.props.FloatProperty ( name='AutoAddCandidatesThreshold', default=0.4 )
    m_BoundaryWeight             = bpy.props.FloatProperty ( name='BoundaryWeight',             default=100.0 )
    m_TargetReduction            = bpy.props.FloatProperty ( name='TargetReduction',            default=1.0 )
    
    def m_properties( self ):
        return ['m_ScalarsName','m_AutoAddCandidates','m_NumberOfCandidates','m_NumberOfEdgesToDecimate','m_NumberOfTetsOutput','m_AutoAddCandidatesThreshold','m_BoundaryWeight','m_TargetReduction',]
    
CLASSES.append  ( VTKUnstructuredGridQuadricDecimation )        
TYPENAMES.append('VTKUnstructuredGridQuadricDecimationType' )

#--------------------------------------------------------------
class VTKVectorDot(Node, VTKFilter1Node):

    bl_idname = 'VTKVectorDotType'
    bl_label  = 'vtkVectorDot'
    
    m_MapScalars  = bpy.props.BoolProperty       ( name='MapScalars',  default=1 )
    m_ScalarRange = bpy.props.FloatVectorProperty( name='ScalarRange', default=(-1.0, 1.0), size=2 )
    
    def m_properties( self ):
        return ['m_MapScalars','m_ScalarRange',]
    
CLASSES.append  ( VTKVectorDot )        
TYPENAMES.append('VTKVectorDotType' )

#--------------------------------------------------------------
class VTKVectorNorm(Node, VTKFilter1Node):

    bl_idname = 'VTKVectorNormType'
    bl_label  = 'vtkVectorNorm'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData']]
    
    m_Normalize     = bpy.props.BoolProperty( name='Normalize',     default=0 )
    e_AttributeMode = bpy.props.EnumProperty( name='AttributeMode', default="Default", items=e_AttributeMode_items )
    
    def m_properties( self ):
        return ['m_Normalize','e_AttributeMode',]
    
CLASSES.append  ( VTKVectorNorm )        
TYPENAMES.append('VTKVectorNormType' )

#--------------------------------------------------------------
class VTKVertexDegree(Node, VTKFilter1Node):

    bl_idname = 'VTKVertexDegreeType'
    bl_label  = 'vtkVertexDegree'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKVertexDegree )        
TYPENAMES.append('VTKVertexDegreeType' )

#--------------------------------------------------------------
class VTKVertexGlyphFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKVertexGlyphFilterType'
    bl_label  = 'vtkVertexGlyphFilter'
    
    
    def m_properties( self ):
        return []
    
CLASSES.append  ( VTKVertexGlyphFilter )        
TYPENAMES.append('VTKVertexGlyphFilterType' )

#--------------------------------------------------------------
class VTKVolumeOfRevolutionFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKVolumeOfRevolutionFilterType'
    bl_label  = 'vtkVolumeOfRevolutionFilter'
    
    m_Resolution    = bpy.props.IntProperty        ( name='Resolution',    default=12 )
    m_SweepAngle    = bpy.props.FloatProperty      ( name='SweepAngle',    default=360.0 )
    m_AxisDirection = bpy.props.FloatVectorProperty( name='AxisDirection', default=(0.0, 0.0, 1.0), size=3 )
    m_AxisPosition  = bpy.props.FloatVectorProperty( name='AxisPosition',  default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Resolution','m_SweepAngle','m_AxisDirection','m_AxisPosition',]
    
CLASSES.append  ( VTKVolumeOfRevolutionFilter )        
TYPENAMES.append('VTKVolumeOfRevolutionFilterType' )

#--------------------------------------------------------------
class VTKVolumeRayCastSpaceLeapingImageFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKVolumeRayCastSpaceLeapingImageFilterType'
    bl_label  = 'vtkVolumeRayCastSpaceLeapingImageFilter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_ComputeGradientOpacity     = bpy.props.BoolProperty       ( name='ComputeGradientOpacity',     default=0 )
    m_ComputeMinMax              = bpy.props.BoolProperty       ( name='ComputeMinMax',              default=0 )
    m_EnableSMP                  = bpy.props.BoolProperty       ( name='EnableSMP',                  default=False )
    m_GlobalDefaultEnableSMP     = bpy.props.BoolProperty       ( name='GlobalDefaultEnableSMP',     default=False )
    m_UpdateGradientOpacityFlags = bpy.props.BoolProperty       ( name='UpdateGradientOpacityFlags', default=0 )
    m_DesiredBytesPerPiece       = bpy.props.IntProperty        ( name='DesiredBytesPerPiece',       default=65536 )
    m_IndependentComponents      = bpy.props.IntProperty        ( name='IndependentComponents',      default=1 )
    m_NumberOfThreads            = bpy.props.IntProperty        ( name='NumberOfThreads',            default=8 )
    e_SplitMode                  = bpy.props.EnumProperty       ( name='SplitMode',                  default="Slab", items=e_SplitMode_items )
    m_MinimumPieceSize           = bpy.props.IntVectorProperty  ( name='MinimumPieceSize',           default=[16, 1, 1], size=3 )
    m_TableSize                  = bpy.props.IntVectorProperty  ( name='TableSize',                  default=[0, 0, 0, 0], size=4 )
    m_TableScale                 = bpy.props.FloatVectorProperty( name='TableScale',                 default=(1.0, 1.0, 1.0, 1.0), size=4 )
    m_TableShift                 = bpy.props.FloatVectorProperty( name='TableShift',                 default=(0.0, 0.0, 0.0, 0.0), size=4 )
    
    def m_properties( self ):
        return ['m_ComputeGradientOpacity','m_ComputeMinMax','m_EnableSMP','m_GlobalDefaultEnableSMP','m_UpdateGradientOpacityFlags','m_DesiredBytesPerPiece','m_IndependentComponents','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_TableSize','m_TableScale','m_TableShift',]
    
CLASSES.append  ( VTKVolumeRayCastSpaceLeapingImageFilter )        
TYPENAMES.append('VTKVolumeRayCastSpaceLeapingImageFilterType' )

#--------------------------------------------------------------
class VTKVoxelContoursToSurfaceFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKVoxelContoursToSurfaceFilterType'
    bl_label  = 'vtkVoxelContoursToSurfaceFilter'
    
    m_MemoryLimitInBytes = bpy.props.IntProperty        ( name='MemoryLimitInBytes', default=10000000 )
    m_Spacing            = bpy.props.FloatVectorProperty( name='Spacing',            default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_MemoryLimitInBytes','m_Spacing',]
    
CLASSES.append  ( VTKVoxelContoursToSurfaceFilter )        
TYPENAMES.append('VTKVoxelContoursToSurfaceFilterType' )

#--------------------------------------------------------------
class VTKVoxelGrid(Node, VTKFilter1Node):

    bl_idname = 'VTKVoxelGridType'
    bl_label  = 'vtkVoxelGrid'
    e_ConfigurationStyle_items=[ (x,x,x) for x in ['Manual', 'LeafSize', 'Automatic']]
    
    m_NumberOfPointsPerBin = bpy.props.IntProperty        ( name='NumberOfPointsPerBin', default=10 )
    e_ConfigurationStyle   = bpy.props.EnumProperty       ( name='ConfigurationStyle',   default="Automatic", items=e_ConfigurationStyle_items )
    m_Divisions            = bpy.props.IntVectorProperty  ( name='Divisions',            default=[50, 50, 50], size=3 )
    m_LeafSize             = bpy.props.FloatVectorProperty( name='LeafSize',             default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_NumberOfPointsPerBin','e_ConfigurationStyle','m_Divisions','m_LeafSize',]
    
CLASSES.append  ( VTKVoxelGrid )        
TYPENAMES.append('VTKVoxelGridType' )

#--------------------------------------------------------------
class VTKWarpLens(Node, VTKFilter1Node):

    bl_idname = 'VTKWarpLensType'
    bl_label  = 'vtkWarpLens'
    
    m_ImageHeight    = bpy.props.IntProperty        ( name='ImageHeight',    default=1 )
    m_ImageWidth     = bpy.props.IntProperty        ( name='ImageWidth',     default=1 )
    m_FormatHeight   = bpy.props.FloatProperty      ( name='FormatHeight',   default=1.0 )
    m_FormatWidth    = bpy.props.FloatProperty      ( name='FormatWidth',    default=1.0 )
    m_K1             = bpy.props.FloatProperty      ( name='K1',             default=-1e-06 )
    m_K2             = bpy.props.FloatProperty      ( name='K2',             default=0.0 )
    m_Kappa          = bpy.props.FloatProperty      ( name='Kappa',          default=-1e-06 )
    m_P1             = bpy.props.FloatProperty      ( name='P1',             default=0.0 )
    m_P2             = bpy.props.FloatProperty      ( name='P2',             default=0.0 )
    m_Center         = bpy.props.FloatVectorProperty( name='Center',         default=(0.0, 0.0), size=2 )
    m_PrincipalPoint = bpy.props.FloatVectorProperty( name='PrincipalPoint', default=(0.0, 0.0), size=2 )
    
    def m_properties( self ):
        return ['m_ImageHeight','m_ImageWidth','m_FormatHeight','m_FormatWidth','m_K1','m_K2','m_Kappa','m_P1','m_P2','m_Center','m_PrincipalPoint',]
    
CLASSES.append  ( VTKWarpLens )        
TYPENAMES.append('VTKWarpLensType' )

#--------------------------------------------------------------
class VTKWarpScalar(Node, VTKFilter1Node):

    bl_idname = 'VTKWarpScalarType'
    bl_label  = 'vtkWarpScalar'
    
    m_UseNormal   = bpy.props.BoolProperty       ( name='UseNormal',   default=0 )
    m_XYPlane     = bpy.props.BoolProperty       ( name='XYPlane',     default=0 )
    m_ScaleFactor = bpy.props.FloatProperty      ( name='ScaleFactor', default=1.0 )
    m_Normal      = bpy.props.FloatVectorProperty( name='Normal',      default=(0.0, 0.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_UseNormal','m_XYPlane','m_ScaleFactor','m_Normal',]
    
CLASSES.append  ( VTKWarpScalar )        
TYPENAMES.append('VTKWarpScalarType' )

#--------------------------------------------------------------
class VTKWarpTo(Node, VTKFilter1Node):

    bl_idname = 'VTKWarpToType'
    bl_label  = 'vtkWarpTo'
    
    m_Absolute    = bpy.props.BoolProperty       ( name='Absolute',    default=0 )
    m_ScaleFactor = bpy.props.FloatProperty      ( name='ScaleFactor', default=0.5 )
    m_Position    = bpy.props.FloatVectorProperty( name='Position',    default=(0.0, 0.0, 0.0), size=3 )
    
    def m_properties( self ):
        return ['m_Absolute','m_ScaleFactor','m_Position',]
    
CLASSES.append  ( VTKWarpTo )        
TYPENAMES.append('VTKWarpToType' )

#--------------------------------------------------------------
class VTKWarpVector(Node, VTKFilter1Node):

    bl_idname = 'VTKWarpVectorType'
    bl_label  = 'vtkWarpVector'
    
    m_ScaleFactor = bpy.props.FloatProperty( name='ScaleFactor', default=1.0 )
    
    def m_properties( self ):
        return ['m_ScaleFactor',]
    
CLASSES.append  ( VTKWarpVector )        
TYPENAMES.append('VTKWarpVectorType' )

#--------------------------------------------------------------
class VTKWindowedSincPolyDataFilter(Node, VTKFilter1Node):

    bl_idname = 'VTKWindowedSincPolyDataFilterType'
    bl_label  = 'vtkWindowedSincPolyDataFilter'
    
    m_BoundarySmoothing    = bpy.props.BoolProperty ( name='BoundarySmoothing',    default=1 )
    m_FeatureEdgeSmoothing = bpy.props.BoolProperty ( name='FeatureEdgeSmoothing', default=0 )
    m_GenerateErrorScalars = bpy.props.BoolProperty ( name='GenerateErrorScalars', default=0 )
    m_GenerateErrorVectors = bpy.props.BoolProperty ( name='GenerateErrorVectors', default=0 )
    m_NonManifoldSmoothing = bpy.props.BoolProperty ( name='NonManifoldSmoothing', default=0 )
    m_NormalizeCoordinates = bpy.props.BoolProperty ( name='NormalizeCoordinates', default=0 )
    m_NumberOfIterations   = bpy.props.IntProperty  ( name='NumberOfIterations',   default=20 )
    m_EdgeAngle            = bpy.props.FloatProperty( name='EdgeAngle',            default=15.0 )
    m_FeatureAngle         = bpy.props.FloatProperty( name='FeatureAngle',         default=45.0 )
    m_PassBand             = bpy.props.FloatProperty( name='PassBand',             default=0.1 )
    
    def m_properties( self ):
        return ['m_BoundarySmoothing','m_FeatureEdgeSmoothing','m_GenerateErrorScalars','m_GenerateErrorVectors','m_NonManifoldSmoothing','m_NormalizeCoordinates','m_NumberOfIterations','m_EdgeAngle','m_FeatureAngle','m_PassBand',]
    
CLASSES.append  ( VTKWindowedSincPolyDataFilter )        
TYPENAMES.append('VTKWindowedSincPolyDataFilterType' )

#--------------------------------------------------------------
class VTKYoungsMaterialInterface(Node, VTKFilter1Node):

    bl_idname = 'VTKYoungsMaterialInterfaceType'
    bl_label  = 'vtkYoungsMaterialInterface'
    
    m_AxisSymetric          = bpy.props.BoolProperty       ( name='AxisSymetric',          default=0 )
    m_FillMaterial          = bpy.props.BoolProperty       ( name='FillMaterial',          default=0 )
    m_InverseNormal         = bpy.props.BoolProperty       ( name='InverseNormal',         default=0 )
    m_OnionPeel             = bpy.props.BoolProperty       ( name='OnionPeel',             default=0 )
    m_ReverseMaterialOrder  = bpy.props.BoolProperty       ( name='ReverseMaterialOrder',  default=0 )
    m_UseAllBlocks          = bpy.props.BoolProperty       ( name='UseAllBlocks',          default=True )
    m_UseFractionAsDistance = bpy.props.BoolProperty       ( name='UseFractionAsDistance', default=0 )
    m_NumberOfMaterials     = bpy.props.IntProperty        ( name='NumberOfMaterials',     default=0 )
    m_VolumeFractionRange   = bpy.props.FloatVectorProperty( name='VolumeFractionRange',   default=(0.01, 0.99), size=2 )
    
    def m_properties( self ):
        return ['m_AxisSymetric','m_FillMaterial','m_InverseNormal','m_OnionPeel','m_ReverseMaterialOrder','m_UseAllBlocks','m_UseFractionAsDistance','m_NumberOfMaterials','m_VolumeFractionRange',]
    
CLASSES.append  ( VTKYoungsMaterialInterface )        
TYPENAMES.append('VTKYoungsMaterialInterfaceType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( 'filter1', 'filter1', items=menu_items) )