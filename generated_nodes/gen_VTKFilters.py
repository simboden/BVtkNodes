# Generated definitions for VTK class group: Filter
# VTK version: 9.2.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAnnotationLink(Node, BVTK_Node):

    bl_idname = 'VTKAnnotationLinkType'
    bl_label  = 'vtkAnnotationLink'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1', 'output 2'], ['AnnotationLayers', 'CurrentSelection'], []) 
    
add_class( VTKAnnotationLink )        
TYPENAMES.append('VTKAnnotationLinkType' )

#--------------------------------------------------------------
class VTKAutoCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKAutoCorrelativeStatisticsType'
    bl_label  = 'vtkAutoCorrelativeStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    m_SliceCardinality: bpy.props.IntProperty(name='SliceCardinality', default=0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables','m_SliceCardinality',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKAutoCorrelativeStatistics )        
TYPENAMES.append('VTKAutoCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKBandedPolyDataContourFilter(Node, BVTK_Node):

    bl_idname = 'VTKBandedPolyDataContourFilterType'
    bl_label  = 'vtkBandedPolyDataContourFilter'
    e_ScalarMode_items=[ (x,x,x) for x in ['Index', 'Value']]
    
    m_Clipping: bpy.props.BoolProperty(name='Clipping', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateContourEdges: bpy.props.BoolProperty(name='GenerateContourEdges', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Component: bpy.props.IntProperty(name='Component', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=BVTK_Node.outdate_vtk_status)
    m_ClipTolerance: bpy.props.FloatProperty(name='ClipTolerance', default=1.1920928955078125e-07, update=BVTK_Node.outdate_vtk_status)
    e_ScalarMode: bpy.props.EnumProperty(name='ScalarMode', default="Index", items=e_ScalarMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Clipping','m_GenerateContourEdges','m_ObjectName','m_Component','m_NumberOfContours','m_ClipTolerance','e_ScalarMode',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBandedPolyDataContourFilter )        
TYPENAMES.append('VTKBandedPolyDataContourFilterType' )

#--------------------------------------------------------------
class VTKBivariateLinearTableThreshold(Node, BVTK_Node):

    bl_idname = 'VTKBivariateLinearTableThresholdType'
    bl_label  = 'vtkBivariateLinearTableThreshold'
    e_LinearThresholdType_items=[ (x,x,x) for x in ['Above', 'Below', 'Near', 'Between']]
    
    m_UseNormalizedDistance: bpy.props.BoolProperty(name='UseNormalizedDistance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Inclusive: bpy.props.IntProperty(name='Inclusive', default=0, update=BVTK_Node.outdate_vtk_status)
    m_DistanceThreshold: bpy.props.FloatProperty(name='DistanceThreshold', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_LinearThresholdType: bpy.props.EnumProperty(name='LinearThresholdType', default="Near", items=e_LinearThresholdType_items, update=BVTK_Node.outdate_vtk_status)
    m_ColumnRanges: bpy.props.FloatVectorProperty(name='ColumnRanges', default=[1.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseNormalizedDistance','m_ObjectName','m_Inclusive','m_DistanceThreshold','e_LinearThresholdType','m_ColumnRanges',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBivariateLinearTableThreshold )        
TYPENAMES.append('VTKBivariateLinearTableThresholdType' )

#--------------------------------------------------------------
class VTKBooleanOperationPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKBooleanOperationPolyDataFilterType'
    bl_label  = 'vtkBooleanOperationPolyDataFilter'
    e_Operation_items=[ (x,x,x) for x in ['Union', 'Intersection', 'Difference']]
    
    m_ReorientDifferenceCells: bpy.props.BoolProperty(name='ReorientDifferenceCells', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1e-06, update=BVTK_Node.outdate_vtk_status)
    e_Operation: bpy.props.EnumProperty(name='Operation', default="Union", items=e_Operation_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReorientDifferenceCells','m_ObjectName','m_Tolerance','e_Operation',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBooleanOperationPolyDataFilter )        
TYPENAMES.append('VTKBooleanOperationPolyDataFilterType' )

#--------------------------------------------------------------
class VTKBoxClipDataSet(Node, BVTK_Node):

    bl_idname = 'VTKBoxClipDataSetType'
    bl_label  = 'vtkBoxClipDataSet'
    
    m_GenerateClipScalars: bpy.props.BoolProperty(name='GenerateClipScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateClippedOutput: bpy.props.BoolProperty(name='GenerateClippedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Orientation: bpy.props.IntProperty(name='Orientation', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_ObjectName','m_Orientation',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKBoxClipDataSet )        
TYPENAMES.append('VTKBoxClipDataSetType' )

#--------------------------------------------------------------
class VTKClipDataSet(Node, BVTK_Node):

    bl_idname = 'VTKClipDataSetType'
    bl_label  = 'vtkClipDataSet'
    
    m_GenerateClipScalars: bpy.props.BoolProperty(name='GenerateClipScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateClippedOutput: bpy.props.BoolProperty(name='GenerateClippedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseValueAsOffset: bpy.props.BoolProperty(name='UseValueAsOffset', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MergeTolerance: bpy.props.FloatProperty(name='MergeTolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_UseValueAsOffset','m_ObjectName','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipDataSet )        
TYPENAMES.append('VTKClipDataSetType' )

#--------------------------------------------------------------
class VTKClipPolyData(Node, BVTK_Node):

    bl_idname = 'VTKClipPolyDataType'
    bl_label  = 'vtkClipPolyData'
    
    m_GenerateClipScalars: bpy.props.BoolProperty(name='GenerateClipScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateClippedOutput: bpy.props.BoolProperty(name='GenerateClippedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_ObjectName','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipPolyData )        
TYPENAMES.append('VTKClipPolyDataType' )

#--------------------------------------------------------------
class VTKClipVolume(Node, BVTK_Node):

    bl_idname = 'VTKClipVolumeType'
    bl_label  = 'vtkClipVolume'
    
    m_GenerateClipScalars: bpy.props.BoolProperty(name='GenerateClipScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateClippedOutput: bpy.props.BoolProperty(name='GenerateClippedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Mixed3DCellGeneration: bpy.props.BoolProperty(name='Mixed3DCellGeneration', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MergeTolerance: bpy.props.FloatProperty(name='MergeTolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_Mixed3DCellGeneration','m_ObjectName','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKClipVolume )        
TYPENAMES.append('VTKClipVolumeType' )

#--------------------------------------------------------------
class VTKCollisionDetectionFilter(Node, BVTK_Node):

    bl_idname = 'VTKCollisionDetectionFilterType'
    bl_label  = 'vtkCollisionDetectionFilter'
    e_CollisionMode_items=[ (x,x,x) for x in ['AllContacts', 'FirstContact', 'HalfContacts']]
    
    m_GenerateScalars: bpy.props.BoolProperty(name='GenerateScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfCellsPerNode: bpy.props.IntProperty(name='NumberOfCellsPerNode', default=2, update=BVTK_Node.outdate_vtk_status)
    m_BoxTolerance: bpy.props.FloatProperty(name='BoxTolerance', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_CellTolerance: bpy.props.FloatProperty(name='CellTolerance', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_Opacity: bpy.props.FloatProperty(name='Opacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_CollisionMode: bpy.props.EnumProperty(name='CollisionMode', default="AllContacts", items=e_CollisionMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateScalars','m_ObjectName','m_NumberOfCellsPerNode','m_BoxTolerance','m_CellTolerance','m_Opacity','e_CollisionMode',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKCollisionDetectionFilter )        
TYPENAMES.append('VTKCollisionDetectionFilterType' )

#--------------------------------------------------------------
class VTKComputeHistogram2DOutliers(Node, BVTK_Node):

    bl_idname = 'VTKComputeHistogram2DOutliersType'
    bl_label  = 'vtkComputeHistogram2DOutliers'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PreferredNumberOfOutliers: bpy.props.IntProperty(name='PreferredNumberOfOutliers', default=10, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_PreferredNumberOfOutliers',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKComputeHistogram2DOutliers )        
TYPENAMES.append('VTKComputeHistogram2DOutliersType' )

#--------------------------------------------------------------
class VTKContingencyStatistics(Node, BVTK_Node):

    bl_idname = 'VTKContingencyStatisticsType'
    bl_label  = 'vtkContingencyStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKContingencyStatistics )        
TYPENAMES.append('VTKContingencyStatisticsType' )

#--------------------------------------------------------------
class VTKConvertSelectionDomain(Node, BVTK_Node):

    bl_idname = 'VTKConvertSelectionDomainType'
    bl_label  = 'vtkConvertSelectionDomain'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKConvertSelectionDomain )        
TYPENAMES.append('VTKConvertSelectionDomainType' )

#--------------------------------------------------------------
class VTKCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKCorrelativeStatisticsType'
    bl_label  = 'vtkCorrelativeStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKCorrelativeStatistics )        
TYPENAMES.append('VTKCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKDescriptiveStatistics(Node, BVTK_Node):

    bl_idname = 'VTKDescriptiveStatisticsType'
    bl_label  = 'vtkDescriptiveStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_G1Skewness: bpy.props.BoolProperty(name='G1Skewness', default=True, update=BVTK_Node.outdate_vtk_status)
    m_G2Kurtosis: bpy.props.BoolProperty(name='G2Kurtosis', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SampleEstimate: bpy.props.BoolProperty(name='SampleEstimate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SignedDeviations: bpy.props.BoolProperty(name='SignedDeviations', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UnbiasedVariance: bpy.props.BoolProperty(name='UnbiasedVariance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_G1Skewness','m_G2Kurtosis','m_LearnOption','m_SampleEstimate','m_SignedDeviations','m_TestOption','m_UnbiasedVariance','m_ObjectName','m_GhostsToSkip','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKDescriptiveStatistics )        
TYPENAMES.append('VTKDescriptiveStatisticsType' )

#--------------------------------------------------------------
class VTKDistancePolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKDistancePolyDataFilterType'
    bl_label  = 'vtkDistancePolyDataFilter'
    
    m_ComputeCellCenterDistance: bpy.props.BoolProperty(name='ComputeCellCenterDistance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ComputeSecondDistance: bpy.props.BoolProperty(name='ComputeSecondDistance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_NegateDistance: bpy.props.BoolProperty(name='NegateDistance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SignedDistance: bpy.props.BoolProperty(name='SignedDistance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeCellCenterDistance','m_ComputeSecondDistance','m_NegateDistance','m_SignedDistance','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKDistancePolyDataFilter )        
TYPENAMES.append('VTKDistancePolyDataFilterType' )

#--------------------------------------------------------------
class VTKEqualizerFilter(Node, BVTK_Node):

    bl_idname = 'VTKEqualizerFilterType'
    bl_label  = 'vtkEqualizerFilter'
    
    m_AllColumns: bpy.props.BoolProperty(name='AllColumns', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Array: bpy.props.StringProperty(name='Array', default="", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Points: bpy.props.StringProperty(name='Points', default="", update=BVTK_Node.outdate_vtk_status)
    m_SamplingFrequency: bpy.props.IntProperty(name='SamplingFrequency', default=1000, update=BVTK_Node.outdate_vtk_status)
    m_SpectrumGain: bpy.props.IntProperty(name='SpectrumGain', default=0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AllColumns','m_Array','m_ObjectName','m_Points','m_SamplingFrequency','m_SpectrumGain',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKEqualizerFilter )        
TYPENAMES.append('VTKEqualizerFilterType' )

#--------------------------------------------------------------
class VTKEquirectangularToCubeMapTexture(Node, BVTK_Node):

    bl_idname = 'VTKEquirectangularToCubeMapTextureType'
    bl_label  = 'vtkEquirectangularToCubeMapTexture'
    e_ColorMode_items=[ (x,x,x) for x in ['Default', 'MapScalars', 'DirectScalars']]
    e_Quality_items=[ (x,x,x) for x in ['Default', '16Bit', '32Bit']]
    
    m_CubeMap: bpy.props.BoolProperty(name='CubeMap', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EdgeClamp: bpy.props.BoolProperty(name='EdgeClamp', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Mipmap: bpy.props.BoolProperty(name='Mipmap', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PremultipliedAlpha: bpy.props.BoolProperty(name='PremultipliedAlpha', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Repeat: bpy.props.BoolProperty(name='Repeat', default=True, update=BVTK_Node.outdate_vtk_status)
    m_RestrictPowerOf2ImageSmaller: bpy.props.BoolProperty(name='RestrictPowerOf2ImageSmaller', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseSRGBColorSpace: bpy.props.BoolProperty(name='UseSRGBColorSpace', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_BlendingMode: bpy.props.IntProperty(name='BlendingMode', default=0, update=BVTK_Node.outdate_vtk_status)
    m_CubeMapSize: bpy.props.IntProperty(name='CubeMapSize', default=512, update=BVTK_Node.outdate_vtk_status)
    m_IsDepthTexture: bpy.props.IntProperty(name='IsDepthTexture', default=0, update=BVTK_Node.outdate_vtk_status)
    m_TextureType: bpy.props.IntProperty(name='TextureType', default=3553, update=BVTK_Node.outdate_vtk_status)
    m_Wrap: bpy.props.IntProperty(name='Wrap', default=1, update=BVTK_Node.outdate_vtk_status)
    m_MaximumAnisotropicFiltering: bpy.props.FloatProperty(name='MaximumAnisotropicFiltering', default=4.0, update=BVTK_Node.outdate_vtk_status)
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="Default", items=e_ColorMode_items, update=BVTK_Node.outdate_vtk_status)
    e_Quality: bpy.props.EnumProperty(name='Quality', default="Default", items=e_Quality_items, update=BVTK_Node.outdate_vtk_status)
    m_BorderColor: bpy.props.FloatVectorProperty(name='BorderColor', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CubeMap','m_EdgeClamp','m_Interpolate','m_Mipmap','m_PremultipliedAlpha','m_Repeat','m_RestrictPowerOf2ImageSmaller','m_UseSRGBColorSpace','m_ObjectName','m_BlendingMode','m_CubeMapSize','m_IsDepthTexture','m_TextureType','m_Wrap','m_MaximumAnisotropicFiltering','e_ColorMode','e_Quality','m_BorderColor',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2', 'input 3', 'input 4', 'input 5'], [], ['InputTexture', 'LookupTable', 'TextureObject', 'Transform'], []) 
    
add_class( VTKEquirectangularToCubeMapTexture )        
TYPENAMES.append('VTKEquirectangularToCubeMapTextureType' )

#--------------------------------------------------------------
class VTKExtractEnclosedPoints(Node, BVTK_Node):

    bl_idname = 'VTKExtractEnclosedPointsType'
    bl_label  = 'vtkExtractEnclosedPoints'
    
    m_CheckSurface: bpy.props.BoolProperty(name='CheckSurface', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.001, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckSurface','m_GenerateOutliers','m_GenerateVertices','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKExtractEnclosedPoints )        
TYPENAMES.append('VTKExtractEnclosedPointsType' )

#--------------------------------------------------------------
class VTKExtractHierarchicalBins(Node, BVTK_Node):

    bl_idname = 'VTKExtractHierarchicalBinsType'
    bl_label  = 'vtkExtractHierarchicalBins'
    
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Bin: bpy.props.IntProperty(name='Bin', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_Level: bpy.props.IntProperty(name='Level', default=0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_ObjectName','m_Bin','m_Level',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['BinningFilter'], []) 
    
add_class( VTKExtractHierarchicalBins )        
TYPENAMES.append('VTKExtractHierarchicalBinsType' )

#--------------------------------------------------------------
class VTKExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKExtractHistogram2DType'
    bl_label  = 'vtkExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong', 'Float', 'Double']]
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SwapColumns: bpy.props.BoolProperty(name='SwapColumns', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseCustomHistogramExtents: bpy.props.BoolProperty(name='UseCustomHistogramExtents', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    e_ScalarType: bpy.props.EnumProperty(name='ScalarType', default="UnsignedInt", items=e_ScalarType_items, update=BVTK_Node.outdate_vtk_status)
    m_ComponentsToProcess: bpy.props.IntVectorProperty(name='ComponentsToProcess', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntVectorProperty(name='NumberOfBins', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    m_CustomHistogramExtents: bpy.props.FloatVectorProperty(name='CustomHistogramExtents', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_SwapColumns','m_TestOption','m_UseCustomHistogramExtents','m_ObjectName','m_NumberOfPrimaryTables','e_ScalarType','m_ComponentsToProcess','m_NumberOfBins','m_CustomHistogramExtents',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], ['RowMask'], []) 
    
add_class( VTKExtractHistogram2D )        
TYPENAMES.append('VTKExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKExtractPoints(Node, BVTK_Node):

    bl_idname = 'VTKExtractPointsType'
    bl_label  = 'vtkExtractPoints'
    
    m_ExtractInside: bpy.props.BoolProperty(name='ExtractInside', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractInside','m_GenerateOutliers','m_GenerateVertices','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ImplicitFunction'], []) 
    
add_class( VTKExtractPoints )        
TYPENAMES.append('VTKExtractPointsType' )

#--------------------------------------------------------------
class VTKExtractSelectedRows(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedRowsType'
    bl_label  = 'vtkExtractSelectedRows'
    
    m_AddOriginalRowIdsArray: bpy.props.BoolProperty(name='AddOriginalRowIdsArray', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddOriginalRowIdsArray','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output'], [], []) 
    
add_class( VTKExtractSelectedRows )        
TYPENAMES.append('VTKExtractSelectedRowsType' )

#--------------------------------------------------------------
class VTKExtractVectorComponents(Node, BVTK_Node):

    bl_idname = 'VTKExtractVectorComponentsType'
    bl_label  = 'vtkExtractVectorComponents'
    
    m_ExtractToFieldData: bpy.props.BoolProperty(name='ExtractToFieldData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ExtractToFieldData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKExtractVectorComponents )        
TYPENAMES.append('VTKExtractVectorComponentsType' )

#--------------------------------------------------------------
class VTKFitImplicitFunction(Node, BVTK_Node):

    bl_idname = 'VTKFitImplicitFunctionType'
    bl_label  = 'vtkFitImplicitFunction'
    
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Threshold: bpy.props.FloatProperty(name='Threshold', default=0.01, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_ObjectName','m_Threshold',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ImplicitFunction'], []) 
    
add_class( VTKFitImplicitFunction )        
TYPENAMES.append('VTKFitImplicitFunctionType' )

#--------------------------------------------------------------
class VTKGenericClip(Node, BVTK_Node):

    bl_idname = 'VTKGenericClipType'
    bl_label  = 'vtkGenericClip'
    
    m_GenerateClipScalars: bpy.props.BoolProperty(name='GenerateClipScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateClippedOutput: bpy.props.BoolProperty(name='GenerateClippedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MergeTolerance: bpy.props.FloatProperty(name='MergeTolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_ObjectName','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKGenericClip )        
TYPENAMES.append('VTKGenericClipType' )

#--------------------------------------------------------------
class VTKGraphAnnotationLayersFilter(Node, BVTK_Node):

    bl_idname = 'VTKGraphAnnotationLayersFilterType'
    bl_label  = 'vtkGraphAnnotationLayersFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKGraphAnnotationLayersFilter )        
TYPENAMES.append('VTKGraphAnnotationLayersFilterType' )

#--------------------------------------------------------------
class VTKGraphToPolyData(Node, BVTK_Node):

    bl_idname = 'VTKGraphToPolyDataType'
    bl_label  = 'vtkGraphToPolyData'
    
    m_EdgeGlyphOutput: bpy.props.BoolProperty(name='EdgeGlyphOutput', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_EdgeGlyphPosition: bpy.props.FloatProperty(name='EdgeGlyphPosition', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EdgeGlyphOutput','m_ObjectName','m_EdgeGlyphPosition',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKGraphToPolyData )        
TYPENAMES.append('VTKGraphToPolyDataType' )

#--------------------------------------------------------------
class VTKHausdorffDistancePointSetFilter(Node, BVTK_Node):

    bl_idname = 'VTKHausdorffDistancePointSetFilterType'
    bl_label  = 'vtkHausdorffDistancePointSetFilter'
    e_TargetDistanceMethod_items=[ (x,x,x) for x in ['PointToPoint', 'PointToCell']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_TargetDistanceMethod: bpy.props.EnumProperty(name='TargetDistanceMethod', default="PointToPoint", items=e_TargetDistanceMethod_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','e_TargetDistanceMethod',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKHausdorffDistancePointSetFilter )        
TYPENAMES.append('VTKHausdorffDistancePointSetFilterType' )

#--------------------------------------------------------------
class VTKHighestDensityRegionsStatistics(Node, BVTK_Node):

    bl_idname = 'VTKHighestDensityRegionsStatisticsType'
    bl_label  = 'vtkHighestDensityRegionsStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKHighestDensityRegionsStatistics )        
TYPENAMES.append('VTKHighestDensityRegionsStatisticsType' )

#--------------------------------------------------------------
class VTKImageConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'VTKImageConnectivityFilterType'
    bl_label  = 'vtkImageConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['SeededRegions', 'AllRegions', 'LargestRegion']]
    e_LabelMode_items=[ (x,x,x) for x in ['SeedScalar', 'ConstantValue', 'SizeRank']]
    e_LabelScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'Short', 'UnsignedShort', 'Int']]
    
    m_GenerateRegionExtents: bpy.props.BoolProperty(name='GenerateRegionExtents', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=0, update=BVTK_Node.outdate_vtk_status)
    m_LabelConstantValue: bpy.props.IntProperty(name='LabelConstantValue', default=255, update=BVTK_Node.outdate_vtk_status)
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="SeededRegions", items=e_ExtractionMode_items, update=BVTK_Node.outdate_vtk_status)
    e_LabelMode: bpy.props.EnumProperty(name='LabelMode', default="SeedScalar", items=e_LabelMode_items, update=BVTK_Node.outdate_vtk_status)
    e_LabelScalarType: bpy.props.EnumProperty(name='LabelScalarType', default="UnsignedChar", items=e_LabelScalarType_items, update=BVTK_Node.outdate_vtk_status)
    m_SizeRange: bpy.props.IntVectorProperty(name='SizeRange', default=[1, 1000000000], size=2, update=BVTK_Node.outdate_vtk_status)
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.5, 1e+30], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateRegionExtents','m_ObjectName','m_ActiveComponent','m_LabelConstantValue','e_ExtractionMode','e_LabelMode','e_LabelScalarType','m_SizeRange','m_ScalarRange',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output'], ['SeedConnection', 'StencilConnection'], []) 
    
add_class( VTKImageConnectivityFilter )        
TYPENAMES.append('VTKImageConnectivityFilterType' )

#--------------------------------------------------------------
class VTKImagePermute(Node, BVTK_Node):

    bl_idname = 'VTKImagePermuteType'
    bl_label  = 'vtkImagePermute'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput: bpy.props.BoolProperty(name='AutoCropOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Border: bpy.props.BoolProperty(name='Border', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateStencilOutput: bpy.props.BoolProperty(name='GenerateStencilOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Mirror: bpy.props.BoolProperty(name='Mirror', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Optimization: bpy.props.BoolProperty(name='Optimization', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty(name='SlabTrapezoidIntegration', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TransformInputSampling: bpy.props.BoolProperty(name='TransformInputSampling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Wrap: bpy.props.BoolProperty(name='Wrap', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputDimensionality: bpy.props.IntProperty(name='OutputDimensionality', default=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputScalarType: bpy.props.IntProperty(name='OutputScalarType', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_SlabNumberOfSlices: bpy.props.IntProperty(name='SlabNumberOfSlices', default=1, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundLevel: bpy.props.FloatProperty(name='BackgroundLevel', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_BorderThickness: bpy.props.FloatProperty(name='BorderThickness', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_ScalarScale: bpy.props.FloatProperty(name='ScalarScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_ScalarShift: bpy.props.FloatProperty(name='ScalarShift', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty(name='SlabSliceSpacingFraction', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_InterpolationMode: bpy.props.EnumProperty(name='InterpolationMode', default="NearestNeighbor", items=e_InterpolationMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SlabMode: bpy.props.EnumProperty(name='SlabMode', default="Mean", items=e_SlabMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_FilteredAxes: bpy.props.IntVectorProperty(name='FilteredAxes', default=[0, 1, 2], size=3, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputExtent: bpy.props.IntVectorProperty(name='OutputExtent', default=[0, 0, 0, 0, 0, 0], size=6, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundColor: bpy.props.FloatVectorProperty(name='BackgroundColor', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=31, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_BorderThickness','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_FilteredAxes','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImagePermute )        
TYPENAMES.append('VTKImagePermuteType' )

#--------------------------------------------------------------
class VTKImageResample(Node, BVTK_Node):

    bl_idname = 'VTKImageResampleType'
    bl_label  = 'vtkImageResample'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput: bpy.props.BoolProperty(name='AutoCropOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Border: bpy.props.BoolProperty(name='Border', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateStencilOutput: bpy.props.BoolProperty(name='GenerateStencilOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Mirror: bpy.props.BoolProperty(name='Mirror', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Optimization: bpy.props.BoolProperty(name='Optimization', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty(name='SlabTrapezoidIntegration', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TransformInputSampling: bpy.props.BoolProperty(name='TransformInputSampling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Wrap: bpy.props.BoolProperty(name='Wrap', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputDimensionality: bpy.props.IntProperty(name='OutputDimensionality', default=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputScalarType: bpy.props.IntProperty(name='OutputScalarType', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_SlabNumberOfSlices: bpy.props.IntProperty(name='SlabNumberOfSlices', default=1, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundLevel: bpy.props.FloatProperty(name='BackgroundLevel', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_BorderThickness: bpy.props.FloatProperty(name='BorderThickness', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_ScalarScale: bpy.props.FloatProperty(name='ScalarScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_ScalarShift: bpy.props.FloatProperty(name='ScalarShift', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty(name='SlabSliceSpacingFraction', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_InterpolationMode: bpy.props.EnumProperty(name='InterpolationMode', default="Linear", items=e_InterpolationMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SlabMode: bpy.props.EnumProperty(name='SlabMode', default="Mean", items=e_SlabMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputExtent: bpy.props.IntVectorProperty(name='OutputExtent', default=[0, 0, 0, 0, 0, 0], size=6, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundColor: bpy.props.FloatVectorProperty(name='BackgroundColor', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    m_MagnificationFactors: bpy.props.FloatVectorProperty(name='MagnificationFactors', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_BorderThickness','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_MagnificationFactors','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageResample )        
TYPENAMES.append('VTKImageResampleType' )

#--------------------------------------------------------------
class VTKImageReslice(Node, BVTK_Node):

    bl_idname = 'VTKImageResliceType'
    bl_label  = 'vtkImageReslice'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput: bpy.props.BoolProperty(name='AutoCropOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Border: bpy.props.BoolProperty(name='Border', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateStencilOutput: bpy.props.BoolProperty(name='GenerateStencilOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Mirror: bpy.props.BoolProperty(name='Mirror', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Optimization: bpy.props.BoolProperty(name='Optimization', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty(name='SlabTrapezoidIntegration', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TransformInputSampling: bpy.props.BoolProperty(name='TransformInputSampling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Wrap: bpy.props.BoolProperty(name='Wrap', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputDimensionality: bpy.props.IntProperty(name='OutputDimensionality', default=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputScalarType: bpy.props.IntProperty(name='OutputScalarType', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_SlabNumberOfSlices: bpy.props.IntProperty(name='SlabNumberOfSlices', default=1, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundLevel: bpy.props.FloatProperty(name='BackgroundLevel', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_BorderThickness: bpy.props.FloatProperty(name='BorderThickness', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_ScalarScale: bpy.props.FloatProperty(name='ScalarScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_ScalarShift: bpy.props.FloatProperty(name='ScalarShift', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty(name='SlabSliceSpacingFraction', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_InterpolationMode: bpy.props.EnumProperty(name='InterpolationMode', default="NearestNeighbor", items=e_InterpolationMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SlabMode: bpy.props.EnumProperty(name='SlabMode', default="Mean", items=e_SlabMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputExtent: bpy.props.IntVectorProperty(name='OutputExtent', default=[0, 0, 0, 0, 0, 0], size=6, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundColor: bpy.props.FloatVectorProperty(name='BackgroundColor', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=30, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_BorderThickness','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageReslice )        
TYPENAMES.append('VTKImageResliceType' )

#--------------------------------------------------------------
class VTKImageResliceToColors(Node, BVTK_Node):

    bl_idname = 'VTKImageResliceToColorsType'
    bl_label  = 'vtkImageResliceToColors'
    e_InterpolationMode_items=[ (x,x,x) for x in ['NearestNeighbor', 'Linear', 'Cubic']]
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SlabMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutoCropOutput: bpy.props.BoolProperty(name='AutoCropOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Border: bpy.props.BoolProperty(name='Border', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Bypass: bpy.props.BoolProperty(name='Bypass', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateStencilOutput: bpy.props.BoolProperty(name='GenerateStencilOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Mirror: bpy.props.BoolProperty(name='Mirror', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Optimization: bpy.props.BoolProperty(name='Optimization', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SlabTrapezoidIntegration: bpy.props.BoolProperty(name='SlabTrapezoidIntegration', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TransformInputSampling: bpy.props.BoolProperty(name='TransformInputSampling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Wrap: bpy.props.BoolProperty(name='Wrap', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputDimensionality: bpy.props.IntProperty(name='OutputDimensionality', default=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputScalarType: bpy.props.IntProperty(name='OutputScalarType', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_SlabNumberOfSlices: bpy.props.IntProperty(name='SlabNumberOfSlices', default=1, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundLevel: bpy.props.FloatProperty(name='BackgroundLevel', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_BorderThickness: bpy.props.FloatProperty(name='BorderThickness', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_ScalarScale: bpy.props.FloatProperty(name='ScalarScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_ScalarShift: bpy.props.FloatProperty(name='ScalarShift', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_SlabSliceSpacingFraction: bpy.props.FloatProperty(name='SlabSliceSpacingFraction', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_InterpolationMode: bpy.props.EnumProperty(name='InterpolationMode', default="NearestNeighbor", items=e_InterpolationMode_items, update=BVTK_Node.outdate_vtk_status)
    e_OutputFormat: bpy.props.EnumProperty(name='OutputFormat', default="RGBA", items=e_OutputFormat_items, update=BVTK_Node.outdate_vtk_status)
    e_SlabMode: bpy.props.EnumProperty(name='SlabMode', default="Mean", items=e_SlabMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputExtent: bpy.props.IntVectorProperty(name='OutputExtent', default=[0, 0, 0, 0, 0, 0], size=6, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundColor: bpy.props.FloatVectorProperty(name='BackgroundColor', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutoCropOutput','m_Border','m_Bypass','m_EnableSMP','m_GenerateStencilOutput','m_GlobalDefaultEnableSMP','m_Interpolate','m_Mirror','m_Optimization','m_SlabTrapezoidIntegration','m_TransformInputSampling','m_Wrap','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputDimensionality','m_OutputScalarType','m_SlabNumberOfSlices','m_BackgroundLevel','m_BorderThickness','m_ScalarScale','m_ScalarShift','m_SlabSliceSpacingFraction','e_InterpolationMode','e_OutputFormat','e_SlabMode','e_SplitMode','m_MinimumPieceSize','m_OutputExtent','m_BackgroundColor','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Interpolator', 'StencilOutput', 'LookupTable', 'ResliceAxes', 'ResliceTransform'], []) 
    
add_class( VTKImageResliceToColors )        
TYPENAMES.append('VTKImageResliceToColorsType' )

#--------------------------------------------------------------
class VTKImageStencil(Node, BVTK_Node):

    bl_idname = 'VTKImageStencilType'
    bl_label  = 'vtkImageStencil'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ReverseStencil: bpy.props.BoolProperty(name='ReverseStencil', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundValue: bpy.props.FloatProperty(name='BackgroundValue', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_BackgroundColor: bpy.props.FloatVectorProperty(name='BackgroundColor', default=[1.0, 1.0, 1.0, 1.0], size=4, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ReverseStencil','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_BackgroundValue','e_SplitMode','m_MinimumPieceSize','m_BackgroundColor',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output'], [], []) 
    
add_class( VTKImageStencil )        
TYPENAMES.append('VTKImageStencilType' )

#--------------------------------------------------------------
class VTKImprintFilter(Node, BVTK_Node):

    bl_idname = 'VTKImprintFilterType'
    bl_label  = 'vtkImprintFilter'
    e_DebugOutputType_items=[ (x,x,x) for x in ['NoDebugOutput', 'TriangulationInput', 'TriangulationOutput']]
    e_MergeToleranceType_items=[ (x,x,x) for x in ['Absolute', 'RelativeToProjection', 'MinEdge']]
    e_OutputType_items=[ (x,x,x) for x in ['TargetCells', 'ImprintedCells', 'ProjectedImprint', 'ImprintedRegion', 'MergedImprint']]
    e_PointInterpolation_items=[ (x,x,x) for x in ['TargetEdges', 'ImprintEdges']]
    
    m_BoundaryEdgeInsertion: bpy.props.BoolProperty(name='BoundaryEdgeInsertion', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassCellData: bpy.props.BoolProperty(name='PassCellData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointData: bpy.props.BoolProperty(name='PassPointData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TriangulateOutput: bpy.props.BoolProperty(name='TriangulateOutput', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DebugCellId: bpy.props.IntProperty(name='DebugCellId', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_MergeTolerance: bpy.props.FloatProperty(name='MergeTolerance', default=0.025, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.001, update=BVTK_Node.outdate_vtk_status)
    e_DebugOutputType: bpy.props.EnumProperty(name='DebugOutputType', default="NoDebugOutput", items=e_DebugOutputType_items, update=BVTK_Node.outdate_vtk_status)
    e_MergeToleranceType: bpy.props.EnumProperty(name='MergeToleranceType', default="MinEdge", items=e_MergeToleranceType_items, update=BVTK_Node.outdate_vtk_status)
    e_OutputType: bpy.props.EnumProperty(name='OutputType', default="MergedImprint", items=e_OutputType_items, update=BVTK_Node.outdate_vtk_status)
    e_PointInterpolation: bpy.props.EnumProperty(name='PointInterpolation', default="TargetEdges", items=e_PointInterpolation_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BoundaryEdgeInsertion','m_PassCellData','m_PassPointData','m_TriangulateOutput','m_ObjectName','m_DebugCellId','m_MergeTolerance','m_Tolerance','e_DebugOutputType','e_MergeToleranceType','e_OutputType','e_PointInterpolation',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['ImprintConnection', 'TargetConnection'], []) 
    
add_class( VTKImprintFilter )        
TYPENAMES.append('VTKImprintFilterType' )

#--------------------------------------------------------------
class VTKIntersectionPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKIntersectionPolyDataFilterType'
    bl_label  = 'vtkIntersectionPolyDataFilter'
    
    m_CheckInput: bpy.props.BoolProperty(name='CheckInput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_CheckMesh: bpy.props.BoolProperty(name='CheckMesh', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ComputeIntersectionPointArray: bpy.props.BoolProperty(name='ComputeIntersectionPointArray', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SplitFirstOutput: bpy.props.BoolProperty(name='SplitFirstOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SplitSecondOutput: bpy.props.BoolProperty(name='SplitSecondOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_RelativeSubtriangleArea: bpy.props.FloatProperty(name='RelativeSubtriangleArea', default=0.0001, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1e-06, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckInput','m_CheckMesh','m_ComputeIntersectionPointArray','m_SplitFirstOutput','m_SplitSecondOutput','m_ObjectName','m_RelativeSubtriangleArea','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKIntersectionPolyDataFilter )        
TYPENAMES.append('VTKIntersectionPolyDataFilterType' )

#--------------------------------------------------------------
class VTKKMeansStatistics(Node, BVTK_Node):

    bl_idname = 'VTKKMeansStatisticsType'
    bl_label  = 'vtkKMeansStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_KValuesArrayName: bpy.props.StringProperty(name='KValuesArrayName', default="K", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DefaultNumberOfClusters: bpy.props.IntProperty(name='DefaultNumberOfClusters', default=3, update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_MaxNumIterations: bpy.props.IntProperty(name='MaxNumIterations', default=50, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_KValuesArrayName','m_ObjectName','m_DefaultNumberOfClusters','m_GhostsToSkip','m_MaxNumIterations','m_NumberOfPrimaryTables','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], ['DistanceFunctor'], []) 
    
add_class( VTKKMeansStatistics )        
TYPENAMES.append('VTKKMeansStatisticsType' )

#--------------------------------------------------------------
class VTKLagrangianParticleTracker(Node, BVTK_Node):

    bl_idname = 'VTKLagrangianParticleTrackerType'
    bl_label  = 'vtkLagrangianParticleTracker'
    
    m_AdaptiveStepReintegration: bpy.props.BoolProperty(name='AdaptiveStepReintegration', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateParticlePathsOutput: bpy.props.BoolProperty(name='GenerateParticlePathsOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GeneratePolyVertexInteractionOutput: bpy.props.BoolProperty(name='GeneratePolyVertexInteractionOutput', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_CellLengthComputationMode: bpy.props.IntProperty(name='CellLengthComputationMode', default=1, update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfSteps: bpy.props.IntProperty(name='MaximumNumberOfSteps', default=100, update=BVTK_Node.outdate_vtk_status)
    m_MaximumIntegrationTime: bpy.props.FloatProperty(name='MaximumIntegrationTime', default=-1.0, update=BVTK_Node.outdate_vtk_status)
    m_StepFactor: bpy.props.FloatProperty(name='StepFactor', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_StepFactorMax: bpy.props.FloatProperty(name='StepFactorMax', default=1.5, update=BVTK_Node.outdate_vtk_status)
    m_StepFactorMin: bpy.props.FloatProperty(name='StepFactorMin', default=0.5, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AdaptiveStepReintegration','m_GenerateParticlePathsOutput','m_GeneratePolyVertexInteractionOutput','m_ObjectName','m_CellLengthComputationMode','m_MaximumNumberOfSteps','m_MaximumIntegrationTime','m_StepFactor','m_StepFactorMax','m_StepFactorMin',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], ['IntegrationModel', 'Integrator'], []) 
    
add_class( VTKLagrangianParticleTracker )        
TYPENAMES.append('VTKLagrangianParticleTrackerType' )

#--------------------------------------------------------------
class VTKLoopBooleanPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKLoopBooleanPolyDataFilterType'
    bl_label  = 'vtkLoopBooleanPolyDataFilter'
    e_Operation_items=[ (x,x,x) for x in ['Union', 'Intersection', 'Difference']]
    
    m_NoIntersectionOutput: bpy.props.BoolProperty(name='NoIntersectionOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1e-06, update=BVTK_Node.outdate_vtk_status)
    e_Operation: bpy.props.EnumProperty(name='Operation', default="Union", items=e_Operation_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NoIntersectionOutput','m_ObjectName','m_Tolerance','e_Operation',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKLoopBooleanPolyDataFilter )        
TYPENAMES.append('VTKLoopBooleanPolyDataFilterType' )

#--------------------------------------------------------------
class VTKMaskPointsFilter(Node, BVTK_Node):

    bl_idname = 'VTKMaskPointsFilterType'
    bl_label  = 'vtkMaskPointsFilter'
    
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_EmptyValue: bpy.props.IntProperty(name='EmptyValue', default=0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_ObjectName','m_EmptyValue',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKMaskPointsFilter )        
TYPENAMES.append('VTKMaskPointsFilterType' )

#--------------------------------------------------------------
class VTKMergeFilter(Node, BVTK_Node):

    bl_idname = 'VTKMergeFilterType'
    bl_label  = 'vtkMergeFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2', 'input 3', 'input 4', 'input 5'], ['output'], [], []) 
    
add_class( VTKMergeFilter )        
TYPENAMES.append('VTKMergeFilterType' )

#--------------------------------------------------------------
class VTKMultiCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKMultiCorrelativeStatisticsType'
    bl_label  = 'vtkMultiCorrelativeStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_MedianAbsoluteDeviation: bpy.props.BoolProperty(name='MedianAbsoluteDeviation', default=False, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_MedianAbsoluteDeviation','m_TestOption','m_ObjectName','m_GhostsToSkip','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKMultiCorrelativeStatistics )        
TYPENAMES.append('VTKMultiCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKOrderStatistics(Node, BVTK_Node):

    bl_idname = 'VTKOrderStatisticsType'
    bl_label  = 'vtkOrderStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Quantize: bpy.props.BoolProperty(name='Quantize', default=False, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_MaximumHistogramSize: bpy.props.IntProperty(name='MaximumHistogramSize', default=1000, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfIntervals: bpy.props.IntProperty(name='NumberOfIntervals', default=4, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=-1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_Quantize','m_TestOption','m_ObjectName','m_GhostsToSkip','m_MaximumHistogramSize','m_NumberOfIntervals','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKOrderStatistics )        
TYPENAMES.append('VTKOrderStatisticsType' )

#--------------------------------------------------------------
class VTKPAutoCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPAutoCorrelativeStatisticsType'
    bl_label  = 'vtkPAutoCorrelativeStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    m_SliceCardinality: bpy.props.IntProperty(name='SliceCardinality', default=0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables','m_SliceCardinality',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKPAutoCorrelativeStatistics )        
TYPENAMES.append('VTKPAutoCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKPBivariateLinearTableThreshold(Node, BVTK_Node):

    bl_idname = 'VTKPBivariateLinearTableThresholdType'
    bl_label  = 'vtkPBivariateLinearTableThreshold'
    e_LinearThresholdType_items=[ (x,x,x) for x in ['Above', 'Below', 'Near', 'Between']]
    
    m_UseNormalizedDistance: bpy.props.BoolProperty(name='UseNormalizedDistance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Inclusive: bpy.props.IntProperty(name='Inclusive', default=0, update=BVTK_Node.outdate_vtk_status)
    m_DistanceThreshold: bpy.props.FloatProperty(name='DistanceThreshold', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_LinearThresholdType: bpy.props.EnumProperty(name='LinearThresholdType', default="Near", items=e_LinearThresholdType_items, update=BVTK_Node.outdate_vtk_status)
    m_ColumnRanges: bpy.props.FloatVectorProperty(name='ColumnRanges', default=[1.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseNormalizedDistance','m_ObjectName','m_Inclusive','m_DistanceThreshold','e_LinearThresholdType','m_ColumnRanges',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKPBivariateLinearTableThreshold )        
TYPENAMES.append('VTKPBivariateLinearTableThresholdType' )

#--------------------------------------------------------------
class VTKPCAStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPCAStatisticsType'
    bl_label  = 'vtkPCAStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_MedianAbsoluteDeviation: bpy.props.BoolProperty(name='MedianAbsoluteDeviation', default=False, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_BasisScheme: bpy.props.IntProperty(name='BasisScheme', default=0, update=BVTK_Node.outdate_vtk_status)
    m_FixedBasisSize: bpy.props.IntProperty(name='FixedBasisSize', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_NormalizationScheme: bpy.props.IntProperty(name='NormalizationScheme', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    m_FixedBasisEnergy: bpy.props.FloatProperty(name='FixedBasisEnergy', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_MedianAbsoluteDeviation','m_TestOption','m_ObjectName','m_BasisScheme','m_FixedBasisSize','m_GhostsToSkip','m_NormalizationScheme','m_NumberOfPrimaryTables','m_FixedBasisEnergy',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2', 'input 3'], ['output 0', 'output 1', 'output 2'], ['SpecifiedNormalization'], []) 
    
add_class( VTKPCAStatistics )        
TYPENAMES.append('VTKPCAStatisticsType' )

#--------------------------------------------------------------
class VTKPComputeHistogram2DOutliers(Node, BVTK_Node):

    bl_idname = 'VTKPComputeHistogram2DOutliersType'
    bl_label  = 'vtkPComputeHistogram2DOutliers'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PreferredNumberOfOutliers: bpy.props.IntProperty(name='PreferredNumberOfOutliers', default=10, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_PreferredNumberOfOutliers',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKPComputeHistogram2DOutliers )        
TYPENAMES.append('VTKPComputeHistogram2DOutliersType' )

#--------------------------------------------------------------
class VTKPContingencyStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPContingencyStatisticsType'
    bl_label  = 'vtkPContingencyStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKPContingencyStatistics )        
TYPENAMES.append('VTKPContingencyStatisticsType' )

#--------------------------------------------------------------
class VTKPCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPCorrelativeStatisticsType'
    bl_label  = 'vtkPCorrelativeStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKPCorrelativeStatistics )        
TYPENAMES.append('VTKPCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKPDescriptiveStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPDescriptiveStatisticsType'
    bl_label  = 'vtkPDescriptiveStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_G1Skewness: bpy.props.BoolProperty(name='G1Skewness', default=True, update=BVTK_Node.outdate_vtk_status)
    m_G2Kurtosis: bpy.props.BoolProperty(name='G2Kurtosis', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SampleEstimate: bpy.props.BoolProperty(name='SampleEstimate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SignedDeviations: bpy.props.BoolProperty(name='SignedDeviations', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UnbiasedVariance: bpy.props.BoolProperty(name='UnbiasedVariance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_G1Skewness','m_G2Kurtosis','m_LearnOption','m_SampleEstimate','m_SignedDeviations','m_TestOption','m_UnbiasedVariance','m_ObjectName','m_GhostsToSkip','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKPDescriptiveStatistics )        
TYPENAMES.append('VTKPDescriptiveStatisticsType' )

#--------------------------------------------------------------
class VTKPExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKPExtractHistogram2DType'
    bl_label  = 'vtkPExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong', 'Float', 'Double']]
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SwapColumns: bpy.props.BoolProperty(name='SwapColumns', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseCustomHistogramExtents: bpy.props.BoolProperty(name='UseCustomHistogramExtents', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    e_ScalarType: bpy.props.EnumProperty(name='ScalarType', default="UnsignedInt", items=e_ScalarType_items, update=BVTK_Node.outdate_vtk_status)
    m_ComponentsToProcess: bpy.props.IntVectorProperty(name='ComponentsToProcess', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntVectorProperty(name='NumberOfBins', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    m_CustomHistogramExtents: bpy.props.FloatVectorProperty(name='CustomHistogramExtents', default=[0.0, 0.0, 0.0, 0.0], size=4, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_SwapColumns','m_TestOption','m_UseCustomHistogramExtents','m_ObjectName','m_NumberOfPrimaryTables','e_ScalarType','m_ComponentsToProcess','m_NumberOfBins','m_CustomHistogramExtents',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], ['RowMask'], []) 
    
add_class( VTKPExtractHistogram2D )        
TYPENAMES.append('VTKPExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKPKMeansStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPKMeansStatisticsType'
    bl_label  = 'vtkPKMeansStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_KValuesArrayName: bpy.props.StringProperty(name='KValuesArrayName', default="K", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DefaultNumberOfClusters: bpy.props.IntProperty(name='DefaultNumberOfClusters', default=3, update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_MaxNumIterations: bpy.props.IntProperty(name='MaxNumIterations', default=50, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_KValuesArrayName','m_ObjectName','m_DefaultNumberOfClusters','m_GhostsToSkip','m_MaxNumIterations','m_NumberOfPrimaryTables','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], ['DistanceFunctor'], []) 
    
add_class( VTKPKMeansStatistics )        
TYPENAMES.append('VTKPKMeansStatisticsType' )

#--------------------------------------------------------------
class VTKPMultiCorrelativeStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPMultiCorrelativeStatisticsType'
    bl_label  = 'vtkPMultiCorrelativeStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_MedianAbsoluteDeviation: bpy.props.BoolProperty(name='MedianAbsoluteDeviation', default=False, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_MedianAbsoluteDeviation','m_TestOption','m_ObjectName','m_GhostsToSkip','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKPMultiCorrelativeStatistics )        
TYPENAMES.append('VTKPMultiCorrelativeStatisticsType' )

#--------------------------------------------------------------
class VTKPOrderStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPOrderStatisticsType'
    bl_label  = 'vtkPOrderStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Quantize: bpy.props.BoolProperty(name='Quantize', default=False, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_MaximumHistogramSize: bpy.props.IntProperty(name='MaximumHistogramSize', default=1000, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfIntervals: bpy.props.IntProperty(name='NumberOfIntervals', default=4, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=-1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_Quantize','m_TestOption','m_ObjectName','m_GhostsToSkip','m_MaximumHistogramSize','m_NumberOfIntervals','m_NumberOfPrimaryTables',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKPOrderStatistics )        
TYPENAMES.append('VTKPOrderStatisticsType' )

#--------------------------------------------------------------
class VTKPPCAStatistics(Node, BVTK_Node):

    bl_idname = 'VTKPPCAStatisticsType'
    bl_label  = 'vtkPPCAStatistics'
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_MedianAbsoluteDeviation: bpy.props.BoolProperty(name='MedianAbsoluteDeviation', default=False, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_BasisScheme: bpy.props.IntProperty(name='BasisScheme', default=0, update=BVTK_Node.outdate_vtk_status)
    m_FixedBasisSize: bpy.props.IntProperty(name='FixedBasisSize', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_GhostsToSkip: bpy.props.IntProperty(name='GhostsToSkip', default=255, update=BVTK_Node.outdate_vtk_status)
    m_NormalizationScheme: bpy.props.IntProperty(name='NormalizationScheme', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    m_FixedBasisEnergy: bpy.props.FloatProperty(name='FixedBasisEnergy', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_MedianAbsoluteDeviation','m_TestOption','m_ObjectName','m_BasisScheme','m_FixedBasisSize','m_GhostsToSkip','m_NormalizationScheme','m_NumberOfPrimaryTables','m_FixedBasisEnergy',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2', 'input 3'], ['output 0', 'output 1', 'output 2'], ['SpecifiedNormalization'], []) 
    
add_class( VTKPPCAStatistics )        
TYPENAMES.append('VTKPPCAStatisticsType' )

#--------------------------------------------------------------
class VTKPPairwiseExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKPPairwiseExtractHistogram2DType'
    bl_label  = 'vtkPPairwiseExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong']]
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    e_ScalarType: bpy.props.EnumProperty(name='ScalarType', default="UnsignedInt", items=e_ScalarType_items, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntVectorProperty(name='NumberOfBins', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables','e_ScalarType','m_NumberOfBins',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], [], []) 
    
add_class( VTKPPairwiseExtractHistogram2D )        
TYPENAMES.append('VTKPPairwiseExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKPairwiseExtractHistogram2D(Node, BVTK_Node):

    bl_idname = 'VTKPairwiseExtractHistogram2DType'
    bl_label  = 'vtkPairwiseExtractHistogram2D'
    e_ScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong']]
    
    m_AssessOption: bpy.props.BoolProperty(name='AssessOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_DeriveOption: bpy.props.BoolProperty(name='DeriveOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_LearnOption: bpy.props.BoolProperty(name='LearnOption', default=True, update=BVTK_Node.outdate_vtk_status)
    m_TestOption: bpy.props.BoolProperty(name='TestOption', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfPrimaryTables: bpy.props.IntProperty(name='NumberOfPrimaryTables', default=1, update=BVTK_Node.outdate_vtk_status)
    e_ScalarType: bpy.props.EnumProperty(name='ScalarType', default="UnsignedInt", items=e_ScalarType_items, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntVectorProperty(name='NumberOfBins', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AssessOption','m_DeriveOption','m_LearnOption','m_TestOption','m_ObjectName','m_NumberOfPrimaryTables','e_ScalarType','m_NumberOfBins',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2', 'output 3'], [], []) 
    
add_class( VTKPairwiseExtractHistogram2D )        
TYPENAMES.append('VTKPairwiseExtractHistogram2DType' )

#--------------------------------------------------------------
class VTKPolyDataPlaneClipper(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataPlaneClipperType'
    bl_label  = 'vtkPolyDataPlaneClipper'
    
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ClippingLoops: bpy.props.BoolProperty(name='ClippingLoops', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCapPointData: bpy.props.BoolProperty(name='PassCapPointData', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_BatchSize: bpy.props.IntProperty(name='BatchSize', default=10000, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_ClippingLoops','m_PassCapPointData','m_ObjectName','m_BatchSize',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['Plane'], []) 
    
add_class( VTKPolyDataPlaneClipper )        
TYPENAMES.append('VTKPolyDataPlaneClipperType' )

#--------------------------------------------------------------
class VTKProgrammableSource(Node, BVTK_Node):

    bl_idname = 'VTKProgrammableSourceType'
    bl_label  = 'vtkProgrammableSource'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1', 'output 2', 'output 3', 'output 4', 'output 5', 'output 6', 'output 7'], [], []) 
    
add_class( VTKProgrammableSource )        
TYPENAMES.append('VTKProgrammableSourceType' )

#--------------------------------------------------------------
class VTKRadiusOutlierRemoval(Node, BVTK_Node):

    bl_idname = 'VTKRadiusOutlierRemovalType'
    bl_label  = 'vtkRadiusOutlierRemoval'
    
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfNeighbors: bpy.props.IntProperty(name='NumberOfNeighbors', default=2, update=BVTK_Node.outdate_vtk_status)
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_ObjectName','m_NumberOfNeighbors','m_Radius',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKRadiusOutlierRemoval )        
TYPENAMES.append('VTKRadiusOutlierRemovalType' )

#--------------------------------------------------------------
class VTKResliceCursorPolyDataAlgorithm(Node, BVTK_Node):

    bl_idname = 'VTKResliceCursorPolyDataAlgorithmType'
    bl_label  = 'vtkResliceCursorPolyDataAlgorithm'
    e_ReslicePlaneNormal_items=[ (x,x,x) for x in ['XAxis', 'YAxis', 'ZAxis']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_ReslicePlaneNormal: bpy.props.EnumProperty(name='ReslicePlaneNormal', default="XAxis", items=e_ReslicePlaneNormal_items, update=BVTK_Node.outdate_vtk_status)
    m_SliceBounds: bpy.props.FloatVectorProperty(name='SliceBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','e_ReslicePlaneNormal','m_SliceBounds',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1', 'output 2', 'output 3'], ['ResliceCursor'], []) 
    
add_class( VTKResliceCursorPolyDataAlgorithm )        
TYPENAMES.append('VTKResliceCursorPolyDataAlgorithmType' )

#--------------------------------------------------------------
class VTKScalarsToTextureFilter(Node, BVTK_Node):

    bl_idname = 'VTKScalarsToTextureFilterType'
    bl_label  = 'vtkScalarsToTextureFilter'
    
    m_UseTransferFunction: bpy.props.BoolProperty(name='UseTransferFunction', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_TextureDimensions: bpy.props.IntVectorProperty(name='TextureDimensions', default=[128, 128], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseTransferFunction','m_ObjectName','m_TextureDimensions',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['TransferFunction'], []) 
    
add_class( VTKScalarsToTextureFilter )        
TYPENAMES.append('VTKScalarsToTextureFilterType' )

#--------------------------------------------------------------
class VTKSelectPolyData(Node, BVTK_Node):

    bl_idname = 'VTKSelectPolyDataType'
    bl_label  = 'vtkSelectPolyData'
    e_EdgeSearchMode_items=[ (x,x,x) for x in ['Greedy', 'Dijkstra']]
    e_SelectionMode_items=[ (x,x,x) for x in ['SmallestRegion', 'LargestRegion', 'ClosestPointRegion']]
    
    m_GenerateSelectionScalars: bpy.props.BoolProperty(name='GenerateSelectionScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateUnselectedOutput: bpy.props.BoolProperty(name='GenerateUnselectedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_EdgeSearchMode: bpy.props.EnumProperty(name='EdgeSearchMode', default="Greedy", items=e_EdgeSearchMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SelectionMode: bpy.props.EnumProperty(name='SelectionMode', default="SmallestRegion", items=e_SelectionMode_items, update=BVTK_Node.outdate_vtk_status)
    m_ClosestPoint: bpy.props.FloatVectorProperty(name='ClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateSelectionScalars','m_GenerateUnselectedOutput','m_InsideOut','m_ObjectName','e_EdgeSearchMode','e_SelectionMode','m_ClosestPoint',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2'], ['Loop'], []) 
    
add_class( VTKSelectPolyData )        
TYPENAMES.append('VTKSelectPolyDataType' )

#--------------------------------------------------------------
class VTKStatisticalOutlierRemoval(Node, BVTK_Node):

    bl_idname = 'VTKStatisticalOutlierRemovalType'
    bl_label  = 'vtkStatisticalOutlierRemoval'
    
    m_GenerateOutliers: bpy.props.BoolProperty(name='GenerateOutliers', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_SampleSize: bpy.props.IntProperty(name='SampleSize', default=25, update=BVTK_Node.outdate_vtk_status)
    m_ComputedMean: bpy.props.FloatProperty(name='ComputedMean', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_ComputedStandardDeviation: bpy.props.FloatProperty(name='ComputedStandardDeviation', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_StandardDeviationFactor: bpy.props.FloatProperty(name='StandardDeviationFactor', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateOutliers','m_GenerateVertices','m_ObjectName','m_SampleSize','m_ComputedMean','m_ComputedStandardDeviation','m_StandardDeviationFactor',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKStatisticalOutlierRemoval )        
TYPENAMES.append('VTKStatisticalOutlierRemovalType' )

#--------------------------------------------------------------
class VTKStreamingStatistics(Node, BVTK_Node):

    bl_idname = 'VTKStreamingStatisticsType'
    bl_label  = 'vtkStreamingStatistics'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1', 'input 2'], ['output 0', 'output 1', 'output 2'], [], []) 
    
add_class( VTKStreamingStatistics )        
TYPENAMES.append('VTKStreamingStatisticsType' )

#--------------------------------------------------------------
class VTKStructuredGridLIC2D(Node, BVTK_Node):

    bl_idname = 'VTKStructuredGridLIC2DType'
    bl_label  = 'vtkStructuredGridLIC2D'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Magnification: bpy.props.IntProperty(name='Magnification', default=1, update=BVTK_Node.outdate_vtk_status)
    m_Steps: bpy.props.IntProperty(name='Steps', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StepSize: bpy.props.FloatProperty(name='StepSize', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Magnification','m_Steps','m_StepSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], ['Context'], []) 
    
add_class( VTKStructuredGridLIC2D )        
TYPENAMES.append('VTKStructuredGridLIC2DType' )

#--------------------------------------------------------------
class VTKTableBasedClipDataSet(Node, BVTK_Node):

    bl_idname = 'VTKTableBasedClipDataSetType'
    bl_label  = 'vtkTableBasedClipDataSet'
    
    m_GenerateClipScalars: bpy.props.BoolProperty(name='GenerateClipScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateClippedOutput: bpy.props.BoolProperty(name='GenerateClippedOutput', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseValueAsOffset: bpy.props.BoolProperty(name='UseValueAsOffset', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MergeTolerance: bpy.props.FloatProperty(name='MergeTolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateClipScalars','m_GenerateClippedOutput','m_InsideOut','m_UseValueAsOffset','m_ObjectName','m_MergeTolerance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1'], ['ClipFunction'], []) 
    
add_class( VTKTableBasedClipDataSet )        
TYPENAMES.append('VTKTableBasedClipDataSetType' )

#--------------------------------------------------------------
class VTKTemporalPathLineFilter(Node, BVTK_Node):

    bl_idname = 'VTKTemporalPathLineFilterType'
    bl_label  = 'vtkTemporalPathLineFilter'
    
    m_BackwardTime: bpy.props.BoolProperty(name='BackwardTime', default=False, update=BVTK_Node.outdate_vtk_status)
    m_KeepDeadTrails: bpy.props.BoolProperty(name='KeepDeadTrails', default=False, update=BVTK_Node.outdate_vtk_status)
    m_IdChannelArray: bpy.props.StringProperty(name='IdChannelArray', default="", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MaskPoints: bpy.props.IntProperty(name='MaskPoints', default=200, update=BVTK_Node.outdate_vtk_status)
    m_MaxTrackLength: bpy.props.IntProperty(name='MaxTrackLength', default=10, update=BVTK_Node.outdate_vtk_status)
    m_MaxStepDistance: bpy.props.FloatVectorProperty(name='MaxStepDistance', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BackwardTime','m_KeepDeadTrails','m_IdChannelArray','m_ObjectName','m_MaskPoints','m_MaxTrackLength','m_MaxStepDistance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output 0', 'output 1'], [], []) 
    
add_class( VTKTemporalPathLineFilter )        
TYPENAMES.append('VTKTemporalPathLineFilterType' )

#--------------------------------------------------------------
class VTKVectorFieldTopology(Node, BVTK_Node):

    bl_idname = 'VTKVectorFieldTopologyType'
    bl_label  = 'vtkVectorFieldTopology'
    
    m_ComputeSurfaces: bpy.props.BoolProperty(name='ComputeSurfaces', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ExcludeBoundary: bpy.props.BoolProperty(name='ExcludeBoundary', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseBoundarySwitchPoints: bpy.props.BoolProperty(name='UseBoundarySwitchPoints', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseIterativeSeeding: bpy.props.BoolProperty(name='UseIterativeSeeding', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_IntegrationStepUnit: bpy.props.IntProperty(name='IntegrationStepUnit', default=2, update=BVTK_Node.outdate_vtk_status)
    m_MaxNumSteps: bpy.props.IntProperty(name='MaxNumSteps', default=100, update=BVTK_Node.outdate_vtk_status)
    m_EpsilonCriticalPoint: bpy.props.FloatProperty(name='EpsilonCriticalPoint', default=1e-10, update=BVTK_Node.outdate_vtk_status)
    m_IntegrationStepSize: bpy.props.FloatProperty(name='IntegrationStepSize', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_OffsetAwayFromBoundary: bpy.props.FloatProperty(name='OffsetAwayFromBoundary', default=0.001, update=BVTK_Node.outdate_vtk_status)
    m_SeparatrixDistance: bpy.props.FloatProperty(name='SeparatrixDistance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_VectorAngleThreshold: bpy.props.FloatProperty(name='VectorAngleThreshold', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeSurfaces','m_ExcludeBoundary','m_UseBoundarySwitchPoints','m_UseIterativeSeeding','m_ObjectName','m_IntegrationStepUnit','m_MaxNumSteps','m_EpsilonCriticalPoint','m_IntegrationStepSize','m_OffsetAwayFromBoundary','m_SeparatrixDistance','m_VectorAngleThreshold',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2', 'output 3', 'output 4'], [], []) 
    
add_class( VTKVectorFieldTopology )        
TYPENAMES.append('VTKVectorFieldTopologyType' )

#--------------------------------------------------------------
class VTKVoronoi2D(Node, BVTK_Node):

    bl_idname = 'VTKVoronoi2DType'
    bl_label  = 'vtkVoronoi2D'
    e_GenerateScalars_items=[ (x,x,x) for x in ['None', 'PointIds', 'ThreadIds']]
    e_ProjectionPlaneMode_items=[ (x,x,x) for x in ['XYPlane', 'SpecifiedTransformPlane', 'BestFittingPlane']]
    
    m_GenerateVoronoiFlower: bpy.props.BoolProperty(name='GenerateVoronoiFlower', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfTileClips: bpy.props.IntProperty(name='MaximumNumberOfTileClips', default=1000000000, update=BVTK_Node.outdate_vtk_status)
    m_PointOfInterest: bpy.props.IntProperty(name='PointOfInterest', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_Padding: bpy.props.FloatProperty(name='Padding', default=0.01, update=BVTK_Node.outdate_vtk_status)
    e_GenerateScalars: bpy.props.EnumProperty(name='GenerateScalars', default="None", items=e_GenerateScalars_items, update=BVTK_Node.outdate_vtk_status)
    e_ProjectionPlaneMode: bpy.props.EnumProperty(name='ProjectionPlaneMode', default="XYPlane", items=e_ProjectionPlaneMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_GenerateVoronoiFlower','m_ObjectName','m_MaximumNumberOfTileClips','m_PointOfInterest','m_Padding','e_GenerateScalars','e_ProjectionPlaneMode',]
    def m_connections( self ):
        return (['input'], ['output 0', 'output 1', 'output 2'], ['Transform'], []) 
    
add_class( VTKVoronoi2D )        
TYPENAMES.append('VTKVoronoi2DType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Filter', 'Filter', items=menu_items) )