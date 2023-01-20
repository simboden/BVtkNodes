# Generated definitions for VTK class group: Filter2
# VTK version: 9.2.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKApplyColors(Node, BVTK_Node):

    bl_idname = 'VTKApplyColorsType'
    bl_label  = 'vtkApplyColors'
    
    m_ScaleCellLookupTable: bpy.props.BoolProperty(name='ScaleCellLookupTable', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ScalePointLookupTable: bpy.props.BoolProperty(name='ScalePointLookupTable', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseCellLookupTable: bpy.props.BoolProperty(name='UseCellLookupTable', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseCurrentAnnotationColor: bpy.props.BoolProperty(name='UseCurrentAnnotationColor', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UsePointLookupTable: bpy.props.BoolProperty(name='UsePointLookupTable', default=False, update=BVTK_Node.outdate_vtk_status)
    m_CellColorOutputArrayName: bpy.props.StringProperty(name='CellColorOutputArrayName', default="vtkApplyColors color", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PointColorOutputArrayName: bpy.props.StringProperty(name='PointColorOutputArrayName', default="vtkApplyColors color", update=BVTK_Node.outdate_vtk_status)
    m_DefaultCellOpacity: bpy.props.FloatProperty(name='DefaultCellOpacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_DefaultPointOpacity: bpy.props.FloatProperty(name='DefaultPointOpacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_SelectedCellOpacity: bpy.props.FloatProperty(name='SelectedCellOpacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_SelectedPointOpacity: bpy.props.FloatProperty(name='SelectedPointOpacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_DefaultCellColor: bpy.props.FloatVectorProperty(name='DefaultCellColor', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_DefaultPointColor: bpy.props.FloatVectorProperty(name='DefaultPointColor', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_SelectedCellColor: bpy.props.FloatVectorProperty(name='SelectedCellColor', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_SelectedPointColor: bpy.props.FloatVectorProperty(name='SelectedPointColor', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ScaleCellLookupTable','m_ScalePointLookupTable','m_UseCellLookupTable','m_UseCurrentAnnotationColor','m_UsePointLookupTable','m_CellColorOutputArrayName','m_ObjectName','m_PointColorOutputArrayName','m_DefaultCellOpacity','m_DefaultPointOpacity','m_SelectedCellOpacity','m_SelectedPointOpacity','m_DefaultCellColor','m_DefaultPointColor','m_SelectedCellColor','m_SelectedPointColor',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLookupTable', 'PointLookupTable'], []) 
    
add_class( VTKApplyColors )        
TYPENAMES.append('VTKApplyColorsType' )

#--------------------------------------------------------------
class VTKApplyIcons(Node, BVTK_Node):

    bl_idname = 'VTKApplyIconsType'
    bl_label  = 'vtkApplyIcons'
    e_SelectionMode_items=[ (x,x,x) for x in ['SelectedIcon', 'SelectedOffset', 'AnnotationIcon', 'IgnoreSelection']]
    
    m_UseLookupTable: bpy.props.BoolProperty(name='UseLookupTable', default=False, update=BVTK_Node.outdate_vtk_status)
    m_IconOutputArrayName: bpy.props.StringProperty(name='IconOutputArrayName', default="vtkApplyIcons icon", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_AttributeType: bpy.props.IntProperty(name='AttributeType', default=4, update=BVTK_Node.outdate_vtk_status)
    m_DefaultIcon: bpy.props.IntProperty(name='DefaultIcon', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_SelectedIcon: bpy.props.IntProperty(name='SelectedIcon', default=0, update=BVTK_Node.outdate_vtk_status)
    e_SelectionMode: bpy.props.EnumProperty(name='SelectionMode', default="IgnoreSelection", items=e_SelectionMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseLookupTable','m_IconOutputArrayName','m_ObjectName','m_AttributeType','m_DefaultIcon','m_SelectedIcon','e_SelectionMode',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKApplyIcons )        
TYPENAMES.append('VTKApplyIconsType' )

#--------------------------------------------------------------
class VTKAreaContourSpectrumFilter(Node, BVTK_Node):

    bl_idname = 'VTKAreaContourSpectrumFilterType'
    bl_label  = 'vtkAreaContourSpectrumFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ArcId: bpy.props.IntProperty(name='ArcId', default=0, update=BVTK_Node.outdate_vtk_status)
    m_FieldId: bpy.props.IntProperty(name='FieldId', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfSamples: bpy.props.IntProperty(name='NumberOfSamples', default=100, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_ArcId','m_FieldId','m_NumberOfSamples',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKAreaContourSpectrumFilter )        
TYPENAMES.append('VTKAreaContourSpectrumFilterType' )

#--------------------------------------------------------------
class VTKBinCellDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKBinCellDataFilterType'
    bl_label  = 'vtkBinCellDataFilter'
    
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=False, update=BVTK_Node.outdate_vtk_status)
    m_SpatialMatch: bpy.props.BoolProperty(name='SpatialMatch', default=True, update=BVTK_Node.outdate_vtk_status)
    m_StoreNumberOfNonzeroBins: bpy.props.BoolProperty(name='StoreNumberOfNonzeroBins', default=True, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfNonzeroBinsArrayName: bpy.props.StringProperty(name='NumberOfNonzeroBinsArrayName', default="NumberOfNonzeroBins", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=BVTK_Node.outdate_vtk_status)
    m_CellOverlapMethod: bpy.props.IntProperty(name='CellOverlapMethod', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntProperty(name='NumberOfBins', default=2, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeTolerance','m_SpatialMatch','m_StoreNumberOfNonzeroBins','m_NumberOfNonzeroBinsArrayName','m_ObjectName','m_ArrayComponent','m_CellOverlapMethod','m_NumberOfBins','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLocator'], []) 
    
add_class( VTKBinCellDataFilter )        
TYPENAMES.append('VTKBinCellDataFilterType' )

#--------------------------------------------------------------
class VTKBlankStructuredGridWithImage(Node, BVTK_Node):

    bl_idname = 'VTKBlankStructuredGridWithImageType'
    bl_label  = 'vtkBlankStructuredGridWithImage'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKBlankStructuredGridWithImage )        
TYPENAMES.append('VTKBlankStructuredGridWithImageType' )

#--------------------------------------------------------------
class VTKCellDistanceSelector(Node, BVTK_Node):

    bl_idname = 'VTKCellDistanceSelectorType'
    bl_label  = 'vtkCellDistanceSelector'
    
    m_AddIntermediate: bpy.props.BoolProperty(name='AddIntermediate', default=True, update=BVTK_Node.outdate_vtk_status)
    m_IncludeSeed: bpy.props.BoolProperty(name='IncludeSeed', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Distance: bpy.props.IntProperty(name='Distance', default=1, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AddIntermediate','m_IncludeSeed','m_ObjectName','m_Distance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKCellDistanceSelector )        
TYPENAMES.append('VTKCellDistanceSelectorType' )

#--------------------------------------------------------------
class VTKCompositeDataProbeFilter(Node, BVTK_Node):

    bl_idname = 'VTKCompositeDataProbeFilterType'
    bl_label  = 'vtkCompositeDataProbeFilter'
    
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPartialArrays: bpy.props.BoolProperty(name='PassPartialArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SpatialMatch: bpy.props.BoolProperty(name='SpatialMatch', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointMaskArrayName: bpy.props.StringProperty(name='ValidPointMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CategoricalData','m_ComputeTolerance','m_PassCellArrays','m_PassFieldArrays','m_PassPartialArrays','m_PassPointArrays','m_SpatialMatch','m_ObjectName','m_ValidPointMaskArrayName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLocatorPrototype', 'FindCellStrategy'], []) 
    
add_class( VTKCompositeDataProbeFilter )        
TYPENAMES.append('VTKCompositeDataProbeFilterType' )

#--------------------------------------------------------------
class VTKConvertSelection(Node, BVTK_Node):

    bl_idname = 'VTKConvertSelectionType'
    bl_label  = 'vtkConvertSelection'
    
    m_AllowMissingArray: bpy.props.BoolProperty(name='AllowMissingArray', default=False, update=BVTK_Node.outdate_vtk_status)
    m_MatchAnyValues: bpy.props.BoolProperty(name='MatchAnyValues', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ArrayName: bpy.props.StringProperty(name='ArrayName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_InputFieldType: bpy.props.IntProperty(name='InputFieldType', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_OutputType: bpy.props.IntProperty(name='OutputType', default=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AllowMissingArray','m_MatchAnyValues','m_ArrayName','m_ObjectName','m_InputFieldType','m_OutputType',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['ArrayNames', 'SelectionExtractor'], []) 
    
add_class( VTKConvertSelection )        
TYPENAMES.append('VTKConvertSelectionType' )

#--------------------------------------------------------------
class VTKCookieCutter(Node, BVTK_Node):

    bl_idname = 'VTKCookieCutterType'
    bl_label  = 'vtkCookieCutter'
    e_PointInterpolation_items=[ (x,x,x) for x in ['MeshEdges', 'LoopEdges']]
    
    m_PassCellData: bpy.props.BoolProperty(name='PassCellData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointData: bpy.props.BoolProperty(name='PassPointData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_PointInterpolation: bpy.props.EnumProperty(name='PointInterpolation', default="MeshEdges", items=e_PointInterpolation_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassCellData','m_PassPointData','m_ObjectName','e_PointInterpolation',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['LoopsConnection'], []) 
    
add_class( VTKCookieCutter )        
TYPENAMES.append('VTKCookieCutterType' )

#--------------------------------------------------------------
class VTKDeformPointSet(Node, BVTK_Node):

    bl_idname = 'VTKDeformPointSetType'
    bl_label  = 'vtkDeformPointSet'
    
    m_InitializeWeights: bpy.props.BoolProperty(name='InitializeWeights', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InitializeWeights','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['ControlMeshData'], []) 
    
add_class( VTKDeformPointSet )        
TYPENAMES.append('VTKDeformPointSetType' )

#--------------------------------------------------------------
class VTKDelaunay2D(Node, BVTK_Node):

    bl_idname = 'VTKDelaunay2DType'
    bl_label  = 'vtkDelaunay2D'
    
    m_BoundingTriangulation: bpy.props.BoolProperty(name='BoundingTriangulation', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ProjectionPlaneMode: bpy.props.IntProperty(name='ProjectionPlaneMode', default=0, update=BVTK_Node.outdate_vtk_status)
    m_Alpha: bpy.props.FloatProperty(name='Alpha', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_Offset: bpy.props.FloatProperty(name='Offset', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1e-05, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BoundingTriangulation','m_ObjectName','m_ProjectionPlaneMode','m_Alpha','m_Offset','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Transform'], []) 
    
add_class( VTKDelaunay2D )        
TYPENAMES.append('VTKDelaunay2DType' )

#--------------------------------------------------------------
class VTKDepthImageToPointCloud(Node, BVTK_Node):

    bl_idname = 'VTKDepthImageToPointCloudType'
    bl_label  = 'vtkDepthImageToPointCloud'
    
    m_CullFarPoints: bpy.props.BoolProperty(name='CullFarPoints', default=True, update=BVTK_Node.outdate_vtk_status)
    m_CullNearPoints: bpy.props.BoolProperty(name='CullNearPoints', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ProduceColorScalars: bpy.props.BoolProperty(name='ProduceColorScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ProduceVertexCellArray: bpy.props.BoolProperty(name='ProduceVertexCellArray', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CullFarPoints','m_CullNearPoints','m_ProduceColorScalars','m_ProduceVertexCellArray','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKDepthImageToPointCloud )        
TYPENAMES.append('VTKDepthImageToPointCloudType' )

#--------------------------------------------------------------
class VTKExtractCellsAlongPolyLine(Node, BVTK_Node):

    bl_idname = 'VTKExtractCellsAlongPolyLineType'
    bl_label  = 'vtkExtractCellsAlongPolyLine'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractCellsAlongPolyLine )        
TYPENAMES.append('VTKExtractCellsAlongPolyLineType' )

#--------------------------------------------------------------
class VTKExtractFunctionalBagPlot(Node, BVTK_Node):

    bl_idname = 'VTKExtractFunctionalBagPlotType'
    bl_label  = 'vtkExtractFunctionalBagPlot'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractFunctionalBagPlot )        
TYPENAMES.append('VTKExtractFunctionalBagPlotType' )

#--------------------------------------------------------------
class VTKExtractParticlesOverTime(Node, BVTK_Node):

    bl_idname = 'VTKExtractParticlesOverTimeType'
    bl_label  = 'vtkExtractParticlesOverTime'
    
    m_IdChannelArray: bpy.props.StringProperty(name='IdChannelArray', default="", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IdChannelArray','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractParticlesOverTime )        
TYPENAMES.append('VTKExtractParticlesOverTimeType' )

#--------------------------------------------------------------
class VTKExtractSelectedArraysOverTime(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedArraysOverTimeType'
    bl_label  = 'vtkExtractSelectedArraysOverTime'
    
    m_ReportStatisticsOnly: bpy.props.BoolProperty(name='ReportStatisticsOnly', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReportStatisticsOnly','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['SelectionExtractor'], []) 
    
add_class( VTKExtractSelectedArraysOverTime )        
TYPENAMES.append('VTKExtractSelectedArraysOverTimeType' )

#--------------------------------------------------------------
class VTKExtractSelectedBlock(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedBlockType'
    bl_label  = 'vtkExtractSelectedBlock'
    
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreserveTopology','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractSelectedBlock )        
TYPENAMES.append('VTKExtractSelectedBlockType' )

#--------------------------------------------------------------
class VTKExtractSelectedFrustum(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedFrustumType'
    bl_label  = 'vtkExtractSelectedFrustum'
    
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ShowBounds: bpy.props.BoolProperty(name='ShowBounds', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ContainingCells: bpy.props.IntProperty(name='ContainingCells', default=0, update=BVTK_Node.outdate_vtk_status)
    m_FieldType: bpy.props.IntProperty(name='FieldType', default=0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InsideOut','m_PreserveTopology','m_ShowBounds','m_ObjectName','m_ContainingCells','m_FieldType',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Frustum'], []) 
    
add_class( VTKExtractSelectedFrustum )        
TYPENAMES.append('VTKExtractSelectedFrustumType' )

#--------------------------------------------------------------
class VTKExtractSelectedIds(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedIdsType'
    bl_label  = 'vtkExtractSelectedIds'
    
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreserveTopology','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractSelectedIds )        
TYPENAMES.append('VTKExtractSelectedIdsType' )

#--------------------------------------------------------------
class VTKExtractSelectedLocations(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedLocationsType'
    bl_label  = 'vtkExtractSelectedLocations'
    
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreserveTopology','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractSelectedLocations )        
TYPENAMES.append('VTKExtractSelectedLocationsType' )

#--------------------------------------------------------------
class VTKExtractSelectedPolyDataIds(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedPolyDataIdsType'
    bl_label  = 'vtkExtractSelectedPolyDataIds'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractSelectedPolyDataIds )        
TYPENAMES.append('VTKExtractSelectedPolyDataIdsType' )

#--------------------------------------------------------------
class VTKExtractSelectedThresholds(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectedThresholdsType'
    bl_label  = 'vtkExtractSelectedThresholds'
    
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreserveTopology','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractSelectedThresholds )        
TYPENAMES.append('VTKExtractSelectedThresholdsType' )

#--------------------------------------------------------------
class VTKExtractSelection(Node, BVTK_Node):

    bl_idname = 'VTKExtractSelectionType'
    bl_label  = 'vtkExtractSelection'
    
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreserveTopology','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKExtractSelection )        
TYPENAMES.append('VTKExtractSelectionType' )

#--------------------------------------------------------------
class VTKFastSplatter(Node, BVTK_Node):

    bl_idname = 'VTKFastSplatterType'
    bl_label  = 'vtkFastSplatter'
    e_LimitMode_items=[ (x,x,x) for x in ['None', 'Clamp', 'Scale', 'FreezeScale']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MaxValue: bpy.props.FloatProperty(name='MaxValue', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_MinValue: bpy.props.FloatProperty(name='MinValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_LimitMode: bpy.props.EnumProperty(name='LimitMode', default="None", items=e_LimitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_OutputDimensions: bpy.props.IntVectorProperty(name='OutputDimensions', default=[100, 100, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, -1.0, 0.0, -1.0, 0.0, -1.0], size=6, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_MaxValue','m_MinValue','e_LimitMode','m_OutputDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKFastSplatter )        
TYPENAMES.append('VTKFastSplatterType' )

#--------------------------------------------------------------
class VTKFiberSurface(Node, BVTK_Node):

    bl_idname = 'VTKFiberSurfaceType'
    bl_label  = 'vtkFiberSurface'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKFiberSurface )        
TYPENAMES.append('VTKFiberSurfaceType' )

#--------------------------------------------------------------
class VTKFitToHeightMapFilter(Node, BVTK_Node):

    bl_idname = 'VTKFitToHeightMapFilterType'
    bl_label  = 'vtkFitToHeightMapFilter'
    e_FittingStrategy_items=[ (x,x,x) for x in ['PointProjection', 'PointMinimumHeight', 'PointMaximumHeight', 'AverageHeight', 'CellMinimumHeight', 'CellMaximumHeight', 'CellAverageHeight']]
    
    m_UseHeightMapOffset: bpy.props.BoolProperty(name='UseHeightMapOffset', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_FittingStrategy: bpy.props.EnumProperty(name='FittingStrategy', default="PointProjection", items=e_FittingStrategy_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_UseHeightMapOffset','m_ObjectName','e_FittingStrategy',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKFitToHeightMapFilter )        
TYPENAMES.append('VTKFitToHeightMapFilterType' )

#--------------------------------------------------------------
class VTKGenericGlyph3DFilter(Node, BVTK_Node):

    bl_idname = 'VTKGenericGlyph3DFilterType'
    bl_label  = 'vtkGenericGlyph3DFilter'
    e_ColorMode_items=[ (x,x,x) for x in ['ColorByScale', 'ColorByScalar', 'ColorByVector']]
    e_IndexMode_items=[ (x,x,x) for x in ['Off', 'Scalar', 'Vector']]
    e_ScaleMode_items=[ (x,x,x) for x in ['ScaleByScalar', 'ScaleByVector', 'ScaleByVectorComponents', 'DataScalingOff']]
    e_VectorMode_items=[ (x,x,x) for x in ['UseVector', 'UseNormal', 'VectorRotationOff']]
    
    m_Clamping: bpy.props.BoolProperty(name='Clamping', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GeneratePointIds: bpy.props.BoolProperty(name='GeneratePointIds', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Orient: bpy.props.BoolProperty(name='Orient', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Scaling: bpy.props.BoolProperty(name='Scaling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PointIdsName: bpy.props.StringProperty(name='PointIdsName', default="InputPointIds", update=BVTK_Node.outdate_vtk_status)
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="ColorByScale", items=e_ColorMode_items, update=BVTK_Node.outdate_vtk_status)
    e_IndexMode: bpy.props.EnumProperty(name='IndexMode', default="Off", items=e_IndexMode_items, update=BVTK_Node.outdate_vtk_status)
    e_ScaleMode: bpy.props.EnumProperty(name='ScaleMode', default="ScaleByScalar", items=e_ScaleMode_items, update=BVTK_Node.outdate_vtk_status)
    e_VectorMode: bpy.props.EnumProperty(name='VectorMode', default="UseVector", items=e_VectorMode_items, update=BVTK_Node.outdate_vtk_status)
    m_Range: bpy.props.FloatVectorProperty(name='Range', default=[0.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Clamping','m_GeneratePointIds','m_Orient','m_Scaling','m_ObjectName','m_PointIdsName','m_ScaleFactor','e_ColorMode','e_IndexMode','e_ScaleMode','e_VectorMode','m_Range',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKGenericGlyph3DFilter )        
TYPENAMES.append('VTKGenericGlyph3DFilterType' )

#--------------------------------------------------------------
class VTKGenericProbeFilter(Node, BVTK_Node):

    bl_idname = 'VTKGenericProbeFilterType'
    bl_label  = 'vtkGenericProbeFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKGenericProbeFilter )        
TYPENAMES.append('VTKGenericProbeFilterType' )

#--------------------------------------------------------------
class VTKGenericStreamTracer(Node, BVTK_Node):

    bl_idname = 'VTKGenericStreamTracerType'
    bl_label  = 'vtkGenericStreamTracer'
    e_InitialIntegrationStepUnit_items=[ (x,x,x) for x in ['TimeUnit', 'LengthUnit', 'CellLengthUnit']]
    e_IntegrationDirection_items=[ (x,x,x) for x in ['Forward', 'Backward', 'Both']]
    e_IntegratorType_items=[ (x,x,x) for x in ['RungeKutta2', 'RungeKutta4', 'RungeKutta45']]
    e_MaximumIntegrationStepUnit_items=[ (x,x,x) for x in ['TimeUnit', 'LengthUnit', 'CellLengthUnit']]
    e_MaximumPropagationUnit_items=[ (x,x,x) for x in ['TimeUnit', 'LengthUnit', 'CellLengthUnit']]
    e_MinimumIntegrationStepUnit_items=[ (x,x,x) for x in ['TimeUnit', 'LengthUnit', 'CellLengthUnit']]
    
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfSteps: bpy.props.IntProperty(name='MaximumNumberOfSteps', default=2000, update=BVTK_Node.outdate_vtk_status)
    m_MaximumError: bpy.props.FloatProperty(name='MaximumError', default=1e-06, update=BVTK_Node.outdate_vtk_status)
    m_RotationScale: bpy.props.FloatProperty(name='RotationScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    e_InitialIntegrationStepUnit: bpy.props.EnumProperty(name='InitialIntegrationStepUnit', default="CellLengthUnit", items=e_InitialIntegrationStepUnit_items, update=BVTK_Node.outdate_vtk_status)
    e_IntegrationDirection: bpy.props.EnumProperty(name='IntegrationDirection', default="Forward", items=e_IntegrationDirection_items, update=BVTK_Node.outdate_vtk_status)
    e_IntegratorType: bpy.props.EnumProperty(name='IntegratorType', default="RungeKutta2", items=e_IntegratorType_items, update=BVTK_Node.outdate_vtk_status)
    e_MaximumIntegrationStepUnit: bpy.props.EnumProperty(name='MaximumIntegrationStepUnit', default="CellLengthUnit", items=e_MaximumIntegrationStepUnit_items, update=BVTK_Node.outdate_vtk_status)
    e_MaximumPropagationUnit: bpy.props.EnumProperty(name='MaximumPropagationUnit', default="LengthUnit", items=e_MaximumPropagationUnit_items, update=BVTK_Node.outdate_vtk_status)
    e_MinimumIntegrationStepUnit: bpy.props.EnumProperty(name='MinimumIntegrationStepUnit', default="CellLengthUnit", items=e_MinimumIntegrationStepUnit_items, update=BVTK_Node.outdate_vtk_status)
    m_StartPosition: bpy.props.FloatVectorProperty(name='StartPosition', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_ObjectName','m_MaximumNumberOfSteps','m_MaximumError','m_RotationScale','m_TerminalSpeed','e_InitialIntegrationStepUnit','e_IntegrationDirection','e_IntegratorType','e_MaximumIntegrationStepUnit','e_MaximumPropagationUnit','e_MinimumIntegrationStepUnit','m_StartPosition',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Integrator'], []) 
    
add_class( VTKGenericStreamTracer )        
TYPENAMES.append('VTKGenericStreamTracerType' )

#--------------------------------------------------------------
class VTKGeometryFilter(Node, BVTK_Node):

    bl_idname = 'VTKGeometryFilterType'
    bl_label  = 'vtkGeometryFilter'
    
    m_CellClipping: bpy.props.BoolProperty(name='CellClipping', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Delegation: bpy.props.BoolProperty(name='Delegation', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ExtentClipping: bpy.props.BoolProperty(name='ExtentClipping', default=False, update=BVTK_Node.outdate_vtk_status)
    m_FastMode: bpy.props.BoolProperty(name='FastMode', default=False, update=BVTK_Node.outdate_vtk_status)
    m_Merging: bpy.props.BoolProperty(name='Merging', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PointClipping: bpy.props.BoolProperty(name='PointClipping', default=False, update=BVTK_Node.outdate_vtk_status)
    m_RemoveGhostInterfaces: bpy.props.BoolProperty(name='RemoveGhostInterfaces', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_OriginalCellIdsName: bpy.props.StringProperty(name='OriginalCellIdsName', default="vtkOriginalCellIds", update=BVTK_Node.outdate_vtk_status)
    m_OriginalPointIdsName: bpy.props.StringProperty(name='OriginalPointIdsName', default="vtkOriginalPointIds", update=BVTK_Node.outdate_vtk_status)
    m_CellMaximum: bpy.props.IntProperty(name='CellMaximum', default=1000000000, update=BVTK_Node.outdate_vtk_status)
    m_CellMinimum: bpy.props.IntProperty(name='CellMinimum', default=0, update=BVTK_Node.outdate_vtk_status)
    m_Degree: bpy.props.IntProperty(name='Degree', default=4, update=BVTK_Node.outdate_vtk_status)
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty(name='NonlinearSubdivisionLevel', default=1, update=BVTK_Node.outdate_vtk_status)
    m_PieceInvariant: bpy.props.IntProperty(name='PieceInvariant', default=0, update=BVTK_Node.outdate_vtk_status)
    m_PointMaximum: bpy.props.IntProperty(name='PointMaximum', default=1000000000, update=BVTK_Node.outdate_vtk_status)
    m_PointMinimum: bpy.props.IntProperty(name='PointMinimum', default=0, update=BVTK_Node.outdate_vtk_status)
    m_Extent: bpy.props.FloatVectorProperty(name='Extent', default=[-1e+30, 1e+30, -1e+30, 1e+30, -1e+30, 1e+30], size=6, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CellClipping','m_Delegation','m_ExtentClipping','m_FastMode','m_Merging','m_PassThroughCellIds','m_PassThroughPointIds','m_PointClipping','m_RemoveGhostInterfaces','m_ObjectName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_CellMaximum','m_CellMinimum','m_Degree','m_NonlinearSubdivisionLevel','m_PieceInvariant','m_PointMaximum','m_PointMinimum','m_Extent',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKGeometryFilter )        
TYPENAMES.append('VTKGeometryFilterType' )

#--------------------------------------------------------------
class VTKGlyph2D(Node, BVTK_Node):

    bl_idname = 'VTKGlyph2DType'
    bl_label  = 'vtkGlyph2D'
    e_ColorMode_items=[ (x,x,x) for x in ['ColorByScale', 'ColorByScalar', 'ColorByVector']]
    e_IndexMode_items=[ (x,x,x) for x in ['Off', 'Scalar', 'Vector']]
    e_ScaleMode_items=[ (x,x,x) for x in ['ScaleByScalar', 'ScaleByVector', 'ScaleByVectorComponents', 'DataScalingOff']]
    e_VectorMode_items=[ (x,x,x) for x in ['UseVector', 'UseNormal', 'VectorRotationOff', 'FollowCameraDirection']]
    
    m_Clamping: bpy.props.BoolProperty(name='Clamping', default=True, update=BVTK_Node.outdate_vtk_status)
    m_FillCellData: bpy.props.BoolProperty(name='FillCellData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GeneratePointIds: bpy.props.BoolProperty(name='GeneratePointIds', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Orient: bpy.props.BoolProperty(name='Orient', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Scaling: bpy.props.BoolProperty(name='Scaling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PointIdsName: bpy.props.StringProperty(name='PointIdsName', default="InputPointIds", update=BVTK_Node.outdate_vtk_status)
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="ColorByScale", items=e_ColorMode_items, update=BVTK_Node.outdate_vtk_status)
    e_IndexMode: bpy.props.EnumProperty(name='IndexMode', default="Off", items=e_IndexMode_items, update=BVTK_Node.outdate_vtk_status)
    e_ScaleMode: bpy.props.EnumProperty(name='ScaleMode', default="ScaleByScalar", items=e_ScaleMode_items, update=BVTK_Node.outdate_vtk_status)
    e_VectorMode: bpy.props.EnumProperty(name='VectorMode', default="UseVector", items=e_VectorMode_items, update=BVTK_Node.outdate_vtk_status)
    m_Range: bpy.props.FloatVectorProperty(name='Range', default=[0.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Clamping','m_FillCellData','m_GeneratePointIds','m_Orient','m_Scaling','m_ObjectName','m_PointIdsName','m_ScaleFactor','e_ColorMode','e_IndexMode','e_ScaleMode','e_VectorMode','m_Range',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['SourceTransform'], []) 
    
add_class( VTKGlyph2D )        
TYPENAMES.append('VTKGlyph2DType' )

#--------------------------------------------------------------
class VTKGlyph3D(Node, BVTK_Node):

    bl_idname = 'VTKGlyph3DType'
    bl_label  = 'vtkGlyph3D'
    e_ColorMode_items=[ (x,x,x) for x in ['ColorByScale', 'ColorByScalar', 'ColorByVector']]
    e_IndexMode_items=[ (x,x,x) for x in ['Off', 'Scalar', 'Vector']]
    e_ScaleMode_items=[ (x,x,x) for x in ['ScaleByScalar', 'ScaleByVector', 'ScaleByVectorComponents', 'DataScalingOff']]
    e_VectorMode_items=[ (x,x,x) for x in ['UseVector', 'UseNormal', 'VectorRotationOff', 'FollowCameraDirection']]
    
    m_Clamping: bpy.props.BoolProperty(name='Clamping', default=True, update=BVTK_Node.outdate_vtk_status)
    m_FillCellData: bpy.props.BoolProperty(name='FillCellData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GeneratePointIds: bpy.props.BoolProperty(name='GeneratePointIds', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Orient: bpy.props.BoolProperty(name='Orient', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Scaling: bpy.props.BoolProperty(name='Scaling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PointIdsName: bpy.props.StringProperty(name='PointIdsName', default="InputPointIds", update=BVTK_Node.outdate_vtk_status)
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="ColorByScale", items=e_ColorMode_items, update=BVTK_Node.outdate_vtk_status)
    e_IndexMode: bpy.props.EnumProperty(name='IndexMode', default="Off", items=e_IndexMode_items, update=BVTK_Node.outdate_vtk_status)
    e_ScaleMode: bpy.props.EnumProperty(name='ScaleMode', default="ScaleByScalar", items=e_ScaleMode_items, update=BVTK_Node.outdate_vtk_status)
    e_VectorMode: bpy.props.EnumProperty(name='VectorMode', default="UseVector", items=e_VectorMode_items, update=BVTK_Node.outdate_vtk_status)
    m_Range: bpy.props.FloatVectorProperty(name='Range', default=[0.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Clamping','m_FillCellData','m_GeneratePointIds','m_Orient','m_Scaling','m_ObjectName','m_PointIdsName','m_ScaleFactor','e_ColorMode','e_IndexMode','e_ScaleMode','e_VectorMode','m_Range',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['SourceTransform'], []) 
    
add_class( VTKGlyph3D )        
TYPENAMES.append('VTKGlyph3DType' )

#--------------------------------------------------------------
class VTKImageAccumulate(Node, BVTK_Node):

    bl_idname = 'VTKImageAccumulateType'
    bl_label  = 'vtkImageAccumulate'
    
    m_IgnoreZero: bpy.props.BoolProperty(name='IgnoreZero', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ReverseStencil: bpy.props.BoolProperty(name='ReverseStencil', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ComponentOrigin: bpy.props.FloatVectorProperty(name='ComponentOrigin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_ComponentSpacing: bpy.props.FloatVectorProperty(name='ComponentSpacing', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_IgnoreZero','m_ReverseStencil','m_ObjectName','m_ComponentOrigin','m_ComponentSpacing',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['ComponentExtent'], []) 
    
add_class( VTKImageAccumulate )        
TYPENAMES.append('VTKImageAccumulateType' )

#--------------------------------------------------------------
class VTKImageBlend(Node, BVTK_Node):

    bl_idname = 'VTKImageBlendType'
    bl_label  = 'vtkImageBlend'
    e_BlendMode_items=[ (x,x,x) for x in ['Normal', 'Compound']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_CompoundAlpha: bpy.props.BoolProperty(name='CompoundAlpha', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_CompoundThreshold: bpy.props.FloatProperty(name='CompoundThreshold', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_BlendMode: bpy.props.EnumProperty(name='BlendMode', default="Normal", items=e_BlendMode_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CompoundAlpha','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_CompoundThreshold','e_BlendMode','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageBlend )        
TYPENAMES.append('VTKImageBlendType' )

#--------------------------------------------------------------
class VTKImageChangeInformation(Node, BVTK_Node):

    bl_idname = 'VTKImageChangeInformationType'
    bl_label  = 'vtkImageChangeInformation'
    
    m_CenterImage: bpy.props.BoolProperty(name='CenterImage', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ExtentTranslation: bpy.props.IntVectorProperty(name='ExtentTranslation', default=[0, 0, 0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputExtentStart: bpy.props.IntVectorProperty(name='OutputExtentStart', default=[1000000000, 1000000000, 1000000000], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OriginScale: bpy.props.FloatVectorProperty(name='OriginScale', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OriginTranslation: bpy.props.FloatVectorProperty(name='OriginTranslation', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[1e+30, 1e+30, 1e+30], size=3, update=BVTK_Node.outdate_vtk_status)
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1e+30, 1e+30, 1e+30], size=3, update=BVTK_Node.outdate_vtk_status)
    m_SpacingScale: bpy.props.FloatVectorProperty(name='SpacingScale', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CenterImage','m_ObjectName','m_ExtentTranslation','m_OutputExtentStart','m_OriginScale','m_OriginTranslation','m_OutputOrigin','m_OutputSpacing','m_SpacingScale',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageChangeInformation )        
TYPENAMES.append('VTKImageChangeInformationType' )

#--------------------------------------------------------------
class VTKImageCheckerboard(Node, BVTK_Node):

    bl_idname = 'VTKImageCheckerboardType'
    bl_label  = 'vtkImageCheckerboard'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfDivisions: bpy.props.IntVectorProperty(name='NumberOfDivisions', default=[2, 2, 2], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_NumberOfDivisions',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageCheckerboard )        
TYPENAMES.append('VTKImageCheckerboardType' )

#--------------------------------------------------------------
class VTKImageCorrelation(Node, BVTK_Node):

    bl_idname = 'VTKImageCorrelationType'
    bl_label  = 'vtkImageCorrelation'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=2, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageCorrelation )        
TYPENAMES.append('VTKImageCorrelationType' )

#--------------------------------------------------------------
class VTKImageDataLIC2D(Node, BVTK_Node):

    bl_idname = 'VTKImageDataLIC2DType'
    bl_label  = 'vtkImageDataLIC2D'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Magnification: bpy.props.IntProperty(name='Magnification', default=1, update=BVTK_Node.outdate_vtk_status)
    m_Steps: bpy.props.IntProperty(name='Steps', default=20, update=BVTK_Node.outdate_vtk_status)
    m_StepSize: bpy.props.FloatProperty(name='StepSize', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Magnification','m_Steps','m_StepSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Context'], []) 
    
add_class( VTKImageDataLIC2D )        
TYPENAMES.append('VTKImageDataLIC2DType' )

#--------------------------------------------------------------
class VTKImageDifference(Node, BVTK_Node):

    bl_idname = 'VTKImageDifferenceType'
    bl_label  = 'vtkImageDifference'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AllowShift: bpy.props.BoolProperty(name='AllowShift', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Averaging: bpy.props.BoolProperty(name='Averaging', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_Threshold: bpy.props.IntProperty(name='Threshold', default=105, update=BVTK_Node.outdate_vtk_status)
    m_AverageThresholdFactor: bpy.props.FloatProperty(name='AverageThresholdFactor', default=0.65, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AllowShift','m_Averaging','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Threshold','m_AverageThresholdFactor','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageDifference )        
TYPENAMES.append('VTKImageDifferenceType' )

#--------------------------------------------------------------
class VTKImageDotProduct(Node, BVTK_Node):

    bl_idname = 'VTKImageDotProductType'
    bl_label  = 'vtkImageDotProduct'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageDotProduct )        
TYPENAMES.append('VTKImageDotProductType' )

#--------------------------------------------------------------
class VTKImageHistogram(Node, BVTK_Node):

    bl_idname = 'VTKImageHistogramType'
    bl_label  = 'vtkImageHistogram'
    e_HistogramImageScale_items=[ (x,x,x) for x in ['Linear', 'Log', 'Sqrt']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutomaticBinning: bpy.props.BoolProperty(name='AutomaticBinning', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateHistogramImage: bpy.props.BoolProperty(name='GenerateHistogramImage', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfBins: bpy.props.IntProperty(name='MaximumNumberOfBins', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntProperty(name='NumberOfBins', default=256, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_BinOrigin: bpy.props.FloatProperty(name='BinOrigin', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_BinSpacing: bpy.props.FloatProperty(name='BinSpacing', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_HistogramImageScale: bpy.props.EnumProperty(name='HistogramImageScale', default="Linear", items=e_HistogramImageScale_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_HistogramImageSize: bpy.props.IntVectorProperty(name='HistogramImageSize', default=[256, 256], size=2, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticBinning','m_EnableSMP','m_GenerateHistogramImage','m_GlobalDefaultEnableSMP','m_ObjectName','m_ActiveComponent','m_DesiredBytesPerPiece','m_MaximumNumberOfBins','m_NumberOfBins','m_NumberOfThreads','m_BinOrigin','m_BinSpacing','e_HistogramImageScale','e_SplitMode','m_HistogramImageSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageHistogram )        
TYPENAMES.append('VTKImageHistogramType' )

#--------------------------------------------------------------
class VTKImageHistogramStatistics(Node, BVTK_Node):

    bl_idname = 'VTKImageHistogramStatisticsType'
    bl_label  = 'vtkImageHistogramStatistics'
    e_HistogramImageScale_items=[ (x,x,x) for x in ['Linear', 'Log', 'Sqrt']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AutomaticBinning: bpy.props.BoolProperty(name='AutomaticBinning', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GenerateHistogramImage: bpy.props.BoolProperty(name='GenerateHistogramImage', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfBins: bpy.props.IntProperty(name='MaximumNumberOfBins', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfBins: bpy.props.IntProperty(name='NumberOfBins', default=256, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_BinOrigin: bpy.props.FloatProperty(name='BinOrigin', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_BinSpacing: bpy.props.FloatProperty(name='BinSpacing', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_HistogramImageScale: bpy.props.EnumProperty(name='HistogramImageScale', default="Linear", items=e_HistogramImageScale_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_HistogramImageSize: bpy.props.IntVectorProperty(name='HistogramImageSize', default=[256, 256], size=2, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_AutoRangeExpansionFactors: bpy.props.FloatVectorProperty(name='AutoRangeExpansionFactors', default=[0.1, 0.1], size=2, update=BVTK_Node.outdate_vtk_status)
    m_AutoRangePercentiles: bpy.props.FloatVectorProperty(name='AutoRangePercentiles', default=[1.0, 99.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticBinning','m_EnableSMP','m_GenerateHistogramImage','m_GlobalDefaultEnableSMP','m_ObjectName','m_ActiveComponent','m_DesiredBytesPerPiece','m_MaximumNumberOfBins','m_NumberOfBins','m_NumberOfThreads','m_BinOrigin','m_BinSpacing','e_HistogramImageScale','e_SplitMode','m_HistogramImageSize','m_MinimumPieceSize','m_AutoRangeExpansionFactors','m_AutoRangePercentiles',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageHistogramStatistics )        
TYPENAMES.append('VTKImageHistogramStatisticsType' )

#--------------------------------------------------------------
class VTKImageLogic(Node, BVTK_Node):

    bl_idname = 'VTKImageLogicType'
    bl_label  = 'vtkImageLogic'
    e_Operation_items=[ (x,x,x) for x in ['And', 'Or', 'Xor', 'Nand', 'Nor', 'Not']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_OutputTrueValue: bpy.props.FloatProperty(name='OutputTrueValue', default=255.0, update=BVTK_Node.outdate_vtk_status)
    e_Operation: bpy.props.EnumProperty(name='Operation', default="And", items=e_Operation_items, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputTrueValue','e_Operation','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageLogic )        
TYPENAMES.append('VTKImageLogicType' )

#--------------------------------------------------------------
class VTKImageMask(Node, BVTK_Node):

    bl_idname = 'VTKImageMaskType'
    bl_label  = 'vtkImageMask'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_NotMask: bpy.props.BoolProperty(name='NotMask', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    m_MaskAlpha: bpy.props.FloatProperty(name='MaskAlpha', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_NotMask','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_MaskAlpha','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageMask )        
TYPENAMES.append('VTKImageMaskType' )

#--------------------------------------------------------------
class VTKImageNonMaximumSuppression(Node, BVTK_Node):

    bl_idname = 'VTKImageNonMaximumSuppressionType'
    bl_label  = 'vtkImageNonMaximumSuppression'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_HandleBoundaries: bpy.props.BoolProperty(name='HandleBoundaries', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=2, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageNonMaximumSuppression )        
TYPENAMES.append('VTKImageNonMaximumSuppressionType' )

#--------------------------------------------------------------
class VTKImageProbeFilter(Node, BVTK_Node):

    bl_idname = 'VTKImageProbeFilterType'
    bl_label  = 'vtkImageProbeFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Interpolator'], []) 
    
add_class( VTKImageProbeFilter )        
TYPENAMES.append('VTKImageProbeFilterType' )

#--------------------------------------------------------------
class VTKImageRectilinearWipe(Node, BVTK_Node):

    bl_idname = 'VTKImageRectilinearWipeType'
    bl_label  = 'vtkImageRectilinearWipe'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    e_Wipe_items=[ (x,x,x) for x in ['Quad', 'Horizontal', 'Vertical', 'LowerLeft', 'LowerRight', 'UpperLeft', 'UpperRight']]
    
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=4, update=BVTK_Node.outdate_vtk_status)
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=BVTK_Node.outdate_vtk_status)
    e_Wipe: bpy.props.EnumProperty(name='Wipe', default="Quad", items=e_Wipe_items, update=BVTK_Node.outdate_vtk_status)
    m_Axis: bpy.props.IntVectorProperty(name='Axis', default=[0, 1], size=2, update=BVTK_Node.outdate_vtk_status)
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=BVTK_Node.outdate_vtk_status)
    m_Position: bpy.props.IntVectorProperty(name='Position', default=[0, 0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','e_Wipe','m_Axis','m_MinimumPieceSize','m_Position',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageRectilinearWipe )        
TYPENAMES.append('VTKImageRectilinearWipeType' )

#--------------------------------------------------------------
class VTKImageThresholdConnectivity(Node, BVTK_Node):

    bl_idname = 'VTKImageThresholdConnectivityType'
    bl_label  = 'vtkImageThresholdConnectivity'
    
    m_ReplaceIn: bpy.props.BoolProperty(name='ReplaceIn', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ReplaceOut: bpy.props.BoolProperty(name='ReplaceOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=-1, update=BVTK_Node.outdate_vtk_status)
    m_InValue: bpy.props.FloatProperty(name='InValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_NeighborhoodFraction: bpy.props.FloatProperty(name='NeighborhoodFraction', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_OutValue: bpy.props.FloatProperty(name='OutValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_SliceRangeX: bpy.props.IntVectorProperty(name='SliceRangeX', default=[-1000000000, 1000000000], size=2, update=BVTK_Node.outdate_vtk_status)
    m_SliceRangeY: bpy.props.IntVectorProperty(name='SliceRangeY', default=[-1000000000, 1000000000], size=2, update=BVTK_Node.outdate_vtk_status)
    m_SliceRangeZ: bpy.props.IntVectorProperty(name='SliceRangeZ', default=[-1000000000, 1000000000], size=2, update=BVTK_Node.outdate_vtk_status)
    m_NeighborhoodRadius: bpy.props.FloatVectorProperty(name='NeighborhoodRadius', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReplaceIn','m_ReplaceOut','m_ObjectName','m_ActiveComponent','m_InValue','m_NeighborhoodFraction','m_OutValue','m_SliceRangeX','m_SliceRangeY','m_SliceRangeZ','m_NeighborhoodRadius',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['SeedPoints'], []) 
    
add_class( VTKImageThresholdConnectivity )        
TYPENAMES.append('VTKImageThresholdConnectivityType' )

#--------------------------------------------------------------
class VTKImageToPoints(Node, BVTK_Node):

    bl_idname = 'VTKImageToPointsType'
    bl_label  = 'vtkImageToPoints'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['StencilConnection'], []) 
    
add_class( VTKImageToPoints )        
TYPENAMES.append('VTKImageToPointsType' )

#--------------------------------------------------------------
class VTKImageToStructuredPoints(Node, BVTK_Node):

    bl_idname = 'VTKImageToStructuredPointsType'
    bl_label  = 'vtkImageToStructuredPoints'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKImageToStructuredPoints )        
TYPENAMES.append('VTKImageToStructuredPointsType' )

#--------------------------------------------------------------
class VTKJoinTables(Node, BVTK_Node):

    bl_idname = 'VTKJoinTablesType'
    bl_label  = 'vtkJoinTables'
    
    m_LeftKey: bpy.props.StringProperty(name='LeftKey', default="", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_RightKey: bpy.props.StringProperty(name='RightKey', default="", update=BVTK_Node.outdate_vtk_status)
    m_Mode: bpy.props.IntProperty(name='Mode', default=0, update=BVTK_Node.outdate_vtk_status)
    m_ReplacementValue: bpy.props.FloatProperty(name='ReplacementValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_LeftKey','m_ObjectName','m_RightKey','m_Mode','m_ReplacementValue',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKJoinTables )        
TYPENAMES.append('VTKJoinTablesType' )

#--------------------------------------------------------------
class VTKMergeDataObjectFilter(Node, BVTK_Node):

    bl_idname = 'VTKMergeDataObjectFilterType'
    bl_label  = 'vtkMergeDataObjectFilter'
    e_OutputField_items=[ (x,x,x) for x in ['DataObjectField', 'PointDataField', 'CellDataField']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_OutputField: bpy.props.EnumProperty(name='OutputField', default="DataObjectField", items=e_OutputField_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','e_OutputField',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKMergeDataObjectFilter )        
TYPENAMES.append('VTKMergeDataObjectFilterType' )

#--------------------------------------------------------------
class VTKPExtractSelectedArraysOverTime(Node, BVTK_Node):

    bl_idname = 'VTKPExtractSelectedArraysOverTimeType'
    bl_label  = 'vtkPExtractSelectedArraysOverTime'
    
    m_ReportStatisticsOnly: bpy.props.BoolProperty(name='ReportStatisticsOnly', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ReportStatisticsOnly','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['SelectionExtractor'], []) 
    
add_class( VTKPExtractSelectedArraysOverTime )        
TYPENAMES.append('VTKPExtractSelectedArraysOverTimeType' )

#--------------------------------------------------------------
class VTKPProbeFilter(Node, BVTK_Node):

    bl_idname = 'VTKPProbeFilterType'
    bl_label  = 'vtkPProbeFilter'
    
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPartialArrays: bpy.props.BoolProperty(name='PassPartialArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SpatialMatch: bpy.props.BoolProperty(name='SpatialMatch', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointMaskArrayName: bpy.props.StringProperty(name='ValidPointMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CategoricalData','m_ComputeTolerance','m_PassCellArrays','m_PassFieldArrays','m_PassPartialArrays','m_PassPointArrays','m_SpatialMatch','m_ObjectName','m_ValidPointMaskArrayName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLocatorPrototype', 'FindCellStrategy'], []) 
    
add_class( VTKPProbeFilter )        
TYPENAMES.append('VTKPProbeFilterType' )

#--------------------------------------------------------------
class VTKPResampleWithDataSet(Node, BVTK_Node):

    bl_idname = 'VTKPResampleWithDataSetType'
    bl_label  = 'vtkPResampleWithDataSet'
    
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_MarkBlankPointsAndCells: bpy.props.BoolProperty(name='MarkBlankPointsAndCells', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPartialArrays: bpy.props.BoolProperty(name='PassPartialArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseBalancedPartitionForPointsLookup: bpy.props.BoolProperty(name='UseBalancedPartitionForPointsLookup', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CategoricalData','m_ComputeTolerance','m_MarkBlankPointsAndCells','m_PassCellArrays','m_PassFieldArrays','m_PassPartialArrays','m_PassPointArrays','m_UseBalancedPartitionForPointsLookup','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLocatorPrototype'], []) 
    
add_class( VTKPResampleWithDataSet )        
TYPENAMES.append('VTKPResampleWithDataSetType' )

#--------------------------------------------------------------
class VTKParallelCoordinatesHistogramRepresentation(Node, BVTK_Node):

    bl_idname = 'VTKParallelCoordinatesHistogramRepresentationType'
    bl_label  = 'vtkParallelCoordinatesHistogramRepresentation'
    
    m_Selectable: bpy.props.BoolProperty(name='Selectable', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ShowOutliers: bpy.props.BoolProperty(name='ShowOutliers', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseCurves: bpy.props.BoolProperty(name='UseCurves', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseHistograms: bpy.props.BoolProperty(name='UseHistograms', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_SelectionArrayName: bpy.props.StringProperty(name='SelectionArrayName', default="", update=BVTK_Node.outdate_vtk_status)
    m_CurveResolution: bpy.props.IntProperty(name='CurveResolution', default=20, update=BVTK_Node.outdate_vtk_status)
    m_LabelRenderMode: bpy.props.IntProperty(name='LabelRenderMode', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfAxisLabels: bpy.props.IntProperty(name='NumberOfAxisLabels', default=2, update=BVTK_Node.outdate_vtk_status)
    m_PreferredNumberOfOutliers: bpy.props.IntProperty(name='PreferredNumberOfOutliers', default=100, update=BVTK_Node.outdate_vtk_status)
    m_SelectionType: bpy.props.IntProperty(name='SelectionType', default=3, update=BVTK_Node.outdate_vtk_status)
    m_AngleBrushThreshold: bpy.props.FloatProperty(name='AngleBrushThreshold', default=0.03, update=BVTK_Node.outdate_vtk_status)
    m_FontSize: bpy.props.FloatProperty(name='FontSize', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_FunctionBrushThreshold: bpy.props.FloatProperty(name='FunctionBrushThreshold', default=0.1, update=BVTK_Node.outdate_vtk_status)
    m_LineOpacity: bpy.props.FloatProperty(name='LineOpacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfHistogramBins: bpy.props.IntVectorProperty(name='NumberOfHistogramBins', default=[10, 10], size=2, update=BVTK_Node.outdate_vtk_status)
    m_AxisColor: bpy.props.FloatVectorProperty(name='AxisColor', default=[1.0, 0.8, 0.3], size=3, update=BVTK_Node.outdate_vtk_status)
    m_AxisLabelColor: bpy.props.FloatVectorProperty(name='AxisLabelColor', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_HistogramLookupTableRange: bpy.props.FloatVectorProperty(name='HistogramLookupTableRange', default=[0.0, 10.0], size=2, update=BVTK_Node.outdate_vtk_status)
    m_LineColor: bpy.props.FloatVectorProperty(name='LineColor', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Selectable','m_ShowOutliers','m_UseCurves','m_UseHistograms','m_ObjectName','m_SelectionArrayName','m_CurveResolution','m_LabelRenderMode','m_NumberOfAxisLabels','m_PreferredNumberOfOutliers','m_SelectionType','m_AngleBrushThreshold','m_FontSize','m_FunctionBrushThreshold','m_LineOpacity','m_NumberOfHistogramBins','m_AxisColor','m_AxisLabelColor','m_HistogramLookupTableRange','m_LineColor',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['PositionAndSize', 'RangeAtPosition', 'AnnotationLink', 'SelectionArrayNames'], []) 
    
add_class( VTKParallelCoordinatesHistogramRepresentation )        
TYPENAMES.append('VTKParallelCoordinatesHistogramRepresentationType' )

#--------------------------------------------------------------
class VTKParallelCoordinatesRepresentation(Node, BVTK_Node):

    bl_idname = 'VTKParallelCoordinatesRepresentationType'
    bl_label  = 'vtkParallelCoordinatesRepresentation'
    
    m_Selectable: bpy.props.BoolProperty(name='Selectable', default=True, update=BVTK_Node.outdate_vtk_status)
    m_UseCurves: bpy.props.BoolProperty(name='UseCurves', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_SelectionArrayName: bpy.props.StringProperty(name='SelectionArrayName', default="", update=BVTK_Node.outdate_vtk_status)
    m_CurveResolution: bpy.props.IntProperty(name='CurveResolution', default=20, update=BVTK_Node.outdate_vtk_status)
    m_LabelRenderMode: bpy.props.IntProperty(name='LabelRenderMode', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfAxisLabels: bpy.props.IntProperty(name='NumberOfAxisLabels', default=2, update=BVTK_Node.outdate_vtk_status)
    m_SelectionType: bpy.props.IntProperty(name='SelectionType', default=3, update=BVTK_Node.outdate_vtk_status)
    m_AngleBrushThreshold: bpy.props.FloatProperty(name='AngleBrushThreshold', default=0.03, update=BVTK_Node.outdate_vtk_status)
    m_FontSize: bpy.props.FloatProperty(name='FontSize', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_FunctionBrushThreshold: bpy.props.FloatProperty(name='FunctionBrushThreshold', default=0.1, update=BVTK_Node.outdate_vtk_status)
    m_LineOpacity: bpy.props.FloatProperty(name='LineOpacity', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_AxisColor: bpy.props.FloatVectorProperty(name='AxisColor', default=[1.0, 0.8, 0.3], size=3, update=BVTK_Node.outdate_vtk_status)
    m_AxisLabelColor: bpy.props.FloatVectorProperty(name='AxisLabelColor', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_LineColor: bpy.props.FloatVectorProperty(name='LineColor', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Selectable','m_UseCurves','m_ObjectName','m_SelectionArrayName','m_CurveResolution','m_LabelRenderMode','m_NumberOfAxisLabels','m_SelectionType','m_AngleBrushThreshold','m_FontSize','m_FunctionBrushThreshold','m_LineOpacity','m_AxisColor','m_AxisLabelColor','m_LineColor',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['PositionAndSize', 'RangeAtPosition', 'AnnotationLink', 'SelectionArrayNames'], []) 
    
add_class( VTKParallelCoordinatesRepresentation )        
TYPENAMES.append('VTKParallelCoordinatesRepresentationType' )

#--------------------------------------------------------------
class VTKParticlePathFilter(Node, BVTK_Node):

    bl_idname = 'VTKParticlePathFilterType'
    bl_label  = 'vtkParticlePathFilter'
    e_MeshOverTime_items=[ (x,x,x) for x in ['Different', 'Static', 'LinearTransformation', 'SameTopology']]
    
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_DisableResetCache: bpy.props.BoolProperty(name='DisableResetCache', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableParticleWriting: bpy.props.BoolProperty(name='EnableParticleWriting', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ForceSerialExecution: bpy.props.BoolProperty(name='ForceSerialExecution', default=False, update=BVTK_Node.outdate_vtk_status)
    m_IgnorePipelineTime: bpy.props.BoolProperty(name='IgnorePipelineTime', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ParticleFileName: bpy.props.StringProperty(name='ParticleFileName', default="", subtype='FILE_PATH', update=BVTK_Node.outdate_vtk_status)
    m_ForceReinjectionEveryNSteps: bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', default=0, update=BVTK_Node.outdate_vtk_status)
    m_IntegratorType: bpy.props.IntProperty(name='IntegratorType', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StaticMesh: bpy.props.IntProperty(name='StaticMesh', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StaticSeeds: bpy.props.IntProperty(name='StaticSeeds', default=0, update=BVTK_Node.outdate_vtk_status)
    m_RotationScale: bpy.props.FloatProperty(name='RotationScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_StartTime: bpy.props.FloatProperty(name='StartTime', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    m_TerminationTime: bpy.props.FloatProperty(name='TerminationTime', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_MeshOverTime: bpy.props.EnumProperty(name='MeshOverTime', default="Different", items=e_MeshOverTime_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_DisableResetCache','m_EnableParticleWriting','m_ForceSerialExecution','m_IgnorePipelineTime','m_ObjectName','m_ParticleFileName','m_ForceReinjectionEveryNSteps','m_IntegratorType','m_StaticMesh','m_StaticSeeds','m_RotationScale','m_StartTime','m_TerminalSpeed','m_TerminationTime','e_MeshOverTime',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Integrator', 'ParticleWriter'], []) 
    
add_class( VTKParticlePathFilter )        
TYPENAMES.append('VTKParticlePathFilterType' )

#--------------------------------------------------------------
class VTKParticleTracer(Node, BVTK_Node):

    bl_idname = 'VTKParticleTracerType'
    bl_label  = 'vtkParticleTracer'
    e_MeshOverTime_items=[ (x,x,x) for x in ['Different', 'Static', 'LinearTransformation', 'SameTopology']]
    
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_DisableResetCache: bpy.props.BoolProperty(name='DisableResetCache', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableParticleWriting: bpy.props.BoolProperty(name='EnableParticleWriting', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ForceSerialExecution: bpy.props.BoolProperty(name='ForceSerialExecution', default=False, update=BVTK_Node.outdate_vtk_status)
    m_IgnorePipelineTime: bpy.props.BoolProperty(name='IgnorePipelineTime', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ParticleFileName: bpy.props.StringProperty(name='ParticleFileName', default="", subtype='FILE_PATH', update=BVTK_Node.outdate_vtk_status)
    m_ForceReinjectionEveryNSteps: bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', default=0, update=BVTK_Node.outdate_vtk_status)
    m_IntegratorType: bpy.props.IntProperty(name='IntegratorType', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StaticMesh: bpy.props.IntProperty(name='StaticMesh', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StaticSeeds: bpy.props.IntProperty(name='StaticSeeds', default=0, update=BVTK_Node.outdate_vtk_status)
    m_RotationScale: bpy.props.FloatProperty(name='RotationScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_StartTime: bpy.props.FloatProperty(name='StartTime', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    m_TerminationTime: bpy.props.FloatProperty(name='TerminationTime', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_MeshOverTime: bpy.props.EnumProperty(name='MeshOverTime', default="Different", items=e_MeshOverTime_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_DisableResetCache','m_EnableParticleWriting','m_ForceSerialExecution','m_IgnorePipelineTime','m_ObjectName','m_ParticleFileName','m_ForceReinjectionEveryNSteps','m_IntegratorType','m_StaticMesh','m_StaticSeeds','m_RotationScale','m_StartTime','m_TerminalSpeed','m_TerminationTime','e_MeshOverTime',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Integrator', 'ParticleWriter'], []) 
    
add_class( VTKParticleTracer )        
TYPENAMES.append('VTKParticleTracerType' )

#--------------------------------------------------------------
class VTKPointInterpolator(Node, BVTK_Node):

    bl_idname = 'VTKPointInterpolatorType'
    bl_label  = 'vtkPointInterpolator'
    e_NullPointsStrategy_items=[ (x,x,x) for x in ['MaskPoints', 'NullValue', 'ClosestPoint']]
    
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PromoteOutputArrays: bpy.props.BoolProperty(name='PromoteOutputArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointsMaskArrayName: bpy.props.StringProperty(name='ValidPointsMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    m_NullValue: bpy.props.FloatProperty(name='NullValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_NullPointsStrategy: bpy.props.EnumProperty(name='NullPointsStrategy', default="NullValue", items=e_NullPointsStrategy_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassCellArrays','m_PassFieldArrays','m_PassPointArrays','m_PromoteOutputArrays','m_ObjectName','m_ValidPointsMaskArrayName','m_NullValue','e_NullPointsStrategy',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Kernel'], []) 
    
add_class( VTKPointInterpolator )        
TYPENAMES.append('VTKPointInterpolatorType' )

#--------------------------------------------------------------
class VTKPointInterpolator2D(Node, BVTK_Node):

    bl_idname = 'VTKPointInterpolator2DType'
    bl_label  = 'vtkPointInterpolator2D'
    e_NullPointsStrategy_items=[ (x,x,x) for x in ['MaskPoints', 'NullValue', 'ClosestPoint']]
    
    m_InterpolateZ: bpy.props.BoolProperty(name='InterpolateZ', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PromoteOutputArrays: bpy.props.BoolProperty(name='PromoteOutputArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointsMaskArrayName: bpy.props.StringProperty(name='ValidPointsMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    m_ZArrayName: bpy.props.StringProperty(name='ZArrayName', default="Elevation", update=BVTK_Node.outdate_vtk_status)
    m_NullValue: bpy.props.FloatProperty(name='NullValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_NullPointsStrategy: bpy.props.EnumProperty(name='NullPointsStrategy', default="NullValue", items=e_NullPointsStrategy_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_InterpolateZ','m_PassCellArrays','m_PassFieldArrays','m_PassPointArrays','m_PromoteOutputArrays','m_ObjectName','m_ValidPointsMaskArrayName','m_ZArrayName','m_NullValue','e_NullPointsStrategy',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Kernel'], []) 
    
add_class( VTKPointInterpolator2D )        
TYPENAMES.append('VTKPointInterpolator2DType' )

#--------------------------------------------------------------
class VTKPolyDataEdgeConnectivityFilter(Node, BVTK_Node):

    bl_idname = 'VTKPolyDataEdgeConnectivityFilterType'
    bl_label  = 'vtkPolyDataEdgeConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion', 'LargeRegions']]
    e_RegionGrowing_items=[ (x,x,x) for x in ['LargeRegions', 'SmallRegions']]
    
    m_BarrierEdges: bpy.props.BoolProperty(name='BarrierEdges', default=True, update=BVTK_Node.outdate_vtk_status)
    m_CellRegionAreas: bpy.props.BoolProperty(name='CellRegionAreas', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ColorRegions: bpy.props.BoolProperty(name='ColorRegions', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ScalarConnectivity: bpy.props.BoolProperty(name='ScalarConnectivity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_LargeRegionThreshold: bpy.props.FloatProperty(name='LargeRegionThreshold', default=0.1, update=BVTK_Node.outdate_vtk_status)
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="LargestRegion", items=e_ExtractionMode_items, update=BVTK_Node.outdate_vtk_status)
    e_RegionGrowing: bpy.props.EnumProperty(name='RegionGrowing', default="LargeRegions", items=e_RegionGrowing_items, update=BVTK_Node.outdate_vtk_status)
    m_BarrierEdgeLength: bpy.props.FloatVectorProperty(name='BarrierEdgeLength', default=[1e+30, 1e+30], size=2, update=BVTK_Node.outdate_vtk_status)
    m_ClosestPoint: bpy.props.FloatVectorProperty(name='ClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BarrierEdges','m_CellRegionAreas','m_ColorRegions','m_ScalarConnectivity','m_ObjectName','m_LargeRegionThreshold','e_ExtractionMode','e_RegionGrowing','m_BarrierEdgeLength','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKPolyDataEdgeConnectivityFilter )        
TYPENAMES.append('VTKPolyDataEdgeConnectivityFilterType' )

#--------------------------------------------------------------
class VTKProbeFilter(Node, BVTK_Node):

    bl_idname = 'VTKProbeFilterType'
    bl_label  = 'vtkProbeFilter'
    
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_SpatialMatch: bpy.props.BoolProperty(name='SpatialMatch', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointMaskArrayName: bpy.props.StringProperty(name='ValidPointMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CategoricalData','m_ComputeTolerance','m_PassCellArrays','m_PassFieldArrays','m_PassPointArrays','m_SpatialMatch','m_ObjectName','m_ValidPointMaskArrayName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLocatorPrototype', 'FindCellStrategy'], []) 
    
add_class( VTKProbeFilter )        
TYPENAMES.append('VTKProbeFilterType' )

#--------------------------------------------------------------
class VTKProbeLineFilter(Node, BVTK_Node):

    bl_idname = 'VTKProbeLineFilterType'
    bl_label  = 'vtkProbeLineFilter'
    
    m_AggregateAsPolyData: bpy.props.BoolProperty(name='AggregateAsPolyData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassPartialArrays: bpy.props.BoolProperty(name='PassPartialArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_LineResolution: bpy.props.IntProperty(name='LineResolution', default=1000, update=BVTK_Node.outdate_vtk_status)
    m_SamplingPattern: bpy.props.IntProperty(name='SamplingPattern', default=0, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AggregateAsPolyData','m_ComputeTolerance','m_PassCellArrays','m_PassFieldArrays','m_PassPartialArrays','m_PassPointArrays','m_ObjectName','m_LineResolution','m_SamplingPattern','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKProbeLineFilter )        
TYPENAMES.append('VTKProbeLineFilterType' )

#--------------------------------------------------------------
class VTKProbePolyhedron(Node, BVTK_Node):

    bl_idname = 'VTKProbePolyhedronType'
    bl_label  = 'vtkProbePolyhedron'
    
    m_ProbeCellData: bpy.props.BoolProperty(name='ProbeCellData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ProbePointData: bpy.props.BoolProperty(name='ProbePointData', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ProbeCellData','m_ProbePointData','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKProbePolyhedron )        
TYPENAMES.append('VTKProbePolyhedronType' )

#--------------------------------------------------------------
class VTKProbeSelectedLocations(Node, BVTK_Node):

    bl_idname = 'VTKProbeSelectedLocationsType'
    bl_label  = 'vtkProbeSelectedLocations'
    
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PreserveTopology','m_ObjectName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKProbeSelectedLocations )        
TYPENAMES.append('VTKProbeSelectedLocationsType' )

#--------------------------------------------------------------
class VTKProgrammableGlyphFilter(Node, BVTK_Node):

    bl_idname = 'VTKProgrammableGlyphFilterType'
    bl_label  = 'vtkProgrammableGlyphFilter'
    e_ColorMode_items=[ (x,x,x) for x in ['ColorByInput', 'ColorBySource']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="ColorByInput", items=e_ColorMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','e_ColorMode',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKProgrammableGlyphFilter )        
TYPENAMES.append('VTKProgrammableGlyphFilterType' )

#--------------------------------------------------------------
class VTKProjectedTerrainPath(Node, BVTK_Node):

    bl_idname = 'VTKProjectedTerrainPathType'
    bl_label  = 'vtkProjectedTerrainPath'
    e_ProjectionMode_items=[ (x,x,x) for x in ['Simple', 'NonOccluded', 'Hug']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfLines: bpy.props.IntProperty(name='MaximumNumberOfLines', default=1000000000, update=BVTK_Node.outdate_vtk_status)
    m_HeightOffset: bpy.props.FloatProperty(name='HeightOffset', default=10.0, update=BVTK_Node.outdate_vtk_status)
    m_HeightTolerance: bpy.props.FloatProperty(name='HeightTolerance', default=10.0, update=BVTK_Node.outdate_vtk_status)
    e_ProjectionMode: bpy.props.EnumProperty(name='ProjectionMode', default="Simple", items=e_ProjectionMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_MaximumNumberOfLines','m_HeightOffset','m_HeightTolerance','e_ProjectionMode',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKProjectedTerrainPath )        
TYPENAMES.append('VTKProjectedTerrainPathType' )

#--------------------------------------------------------------
class VTKResampleWithDataSet(Node, BVTK_Node):

    bl_idname = 'VTKResampleWithDataSetType'
    bl_label  = 'vtkResampleWithDataSet'
    
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ComputeTolerance: bpy.props.BoolProperty(name='ComputeTolerance', default=True, update=BVTK_Node.outdate_vtk_status)
    m_MarkBlankPointsAndCells: bpy.props.BoolProperty(name='MarkBlankPointsAndCells', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPartialArrays: bpy.props.BoolProperty(name='PassPartialArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseBalancedPartitionForPointsLookup: bpy.props.BoolProperty(name='UseBalancedPartitionForPointsLookup', default=False, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CategoricalData','m_ComputeTolerance','m_MarkBlankPointsAndCells','m_PassCellArrays','m_PassFieldArrays','m_PassPartialArrays','m_PassPointArrays','m_UseBalancedPartitionForPointsLookup','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['CellLocatorPrototype'], []) 
    
add_class( VTKResampleWithDataSet )        
TYPENAMES.append('VTKResampleWithDataSetType' )

#--------------------------------------------------------------
class VTKSPHInterpolator(Node, BVTK_Node):

    bl_idname = 'VTKSPHInterpolatorType'
    bl_label  = 'vtkSPHInterpolator'
    e_NullPointsStrategy_items=[ (x,x,x) for x in ['MaskPoints', 'NullValue']]
    
    m_ComputeShepardSum: bpy.props.BoolProperty(name='ComputeShepardSum', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PromoteOutputArrays: bpy.props.BoolProperty(name='PromoteOutputArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ShepardNormalization: bpy.props.BoolProperty(name='ShepardNormalization', default=True, update=BVTK_Node.outdate_vtk_status)
    m_CutoffArrayName: bpy.props.StringProperty(name='CutoffArrayName', default="", update=BVTK_Node.outdate_vtk_status)
    m_DensityArrayName: bpy.props.StringProperty(name='DensityArrayName', default="Rho", update=BVTK_Node.outdate_vtk_status)
    m_MassArrayName: bpy.props.StringProperty(name='MassArrayName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ShepardSumArrayName: bpy.props.StringProperty(name='ShepardSumArrayName', default="Shepard Summation", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointsMaskArrayName: bpy.props.StringProperty(name='ValidPointsMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    m_NullValue: bpy.props.FloatProperty(name='NullValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_NullPointsStrategy: bpy.props.EnumProperty(name='NullPointsStrategy', default="NullValue", items=e_NullPointsStrategy_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeShepardSum','m_PassCellArrays','m_PassFieldArrays','m_PassPointArrays','m_PromoteOutputArrays','m_ShepardNormalization','m_CutoffArrayName','m_DensityArrayName','m_MassArrayName','m_ObjectName','m_ShepardSumArrayName','m_ValidPointsMaskArrayName','m_NullValue','e_NullPointsStrategy',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Kernel'], []) 
    
add_class( VTKSPHInterpolator )        
TYPENAMES.append('VTKSPHInterpolatorType' )

#--------------------------------------------------------------
class VTKSelectEnclosedPoints(Node, BVTK_Node):

    bl_idname = 'VTKSelectEnclosedPointsType'
    bl_label  = 'vtkSelectEnclosedPoints'
    
    m_CheckSurface: bpy.props.BoolProperty(name='CheckSurface', default=True, update=BVTK_Node.outdate_vtk_status)
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0001, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_CheckSurface','m_InsideOut','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKSelectEnclosedPoints )        
TYPENAMES.append('VTKSelectEnclosedPointsType' )

#--------------------------------------------------------------
class VTKSmoothPolyDataFilter(Node, BVTK_Node):

    bl_idname = 'VTKSmoothPolyDataFilterType'
    bl_label  = 'vtkSmoothPolyDataFilter'
    
    m_BoundarySmoothing: bpy.props.BoolProperty(name='BoundarySmoothing', default=True, update=BVTK_Node.outdate_vtk_status)
    m_FeatureEdgeSmoothing: bpy.props.BoolProperty(name='FeatureEdgeSmoothing', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateErrorScalars: bpy.props.BoolProperty(name='GenerateErrorScalars', default=True, update=BVTK_Node.outdate_vtk_status)
    m_GenerateErrorVectors: bpy.props.BoolProperty(name='GenerateErrorVectors', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=20, update=BVTK_Node.outdate_vtk_status)
    m_Convergence: bpy.props.FloatProperty(name='Convergence', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_EdgeAngle: bpy.props.FloatProperty(name='EdgeAngle', default=15.0, update=BVTK_Node.outdate_vtk_status)
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=45.0, update=BVTK_Node.outdate_vtk_status)
    m_RelaxationFactor: bpy.props.FloatProperty(name='RelaxationFactor', default=0.01, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_BoundarySmoothing','m_FeatureEdgeSmoothing','m_GenerateErrorScalars','m_GenerateErrorVectors','m_ObjectName','m_NumberOfIterations','m_Convergence','m_EdgeAngle','m_FeatureAngle','m_RelaxationFactor',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKSmoothPolyDataFilter )        
TYPENAMES.append('VTKSmoothPolyDataFilterType' )

#--------------------------------------------------------------
class VTKStreaklineFilter(Node, BVTK_Node):

    bl_idname = 'VTKStreaklineFilterType'
    bl_label  = 'vtkStreaklineFilter'
    e_MeshOverTime_items=[ (x,x,x) for x in ['Different', 'Static', 'LinearTransformation', 'SameTopology']]
    
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_DisableResetCache: bpy.props.BoolProperty(name='DisableResetCache', default=True, update=BVTK_Node.outdate_vtk_status)
    m_EnableParticleWriting: bpy.props.BoolProperty(name='EnableParticleWriting', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ForceSerialExecution: bpy.props.BoolProperty(name='ForceSerialExecution', default=False, update=BVTK_Node.outdate_vtk_status)
    m_IgnorePipelineTime: bpy.props.BoolProperty(name='IgnorePipelineTime', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ParticleFileName: bpy.props.StringProperty(name='ParticleFileName', default="", subtype='FILE_PATH', update=BVTK_Node.outdate_vtk_status)
    m_ForceReinjectionEveryNSteps: bpy.props.IntProperty(name='ForceReinjectionEveryNSteps', default=1, update=BVTK_Node.outdate_vtk_status)
    m_IntegratorType: bpy.props.IntProperty(name='IntegratorType', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StaticMesh: bpy.props.IntProperty(name='StaticMesh', default=1, update=BVTK_Node.outdate_vtk_status)
    m_StaticSeeds: bpy.props.IntProperty(name='StaticSeeds', default=0, update=BVTK_Node.outdate_vtk_status)
    m_RotationScale: bpy.props.FloatProperty(name='RotationScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_StartTime: bpy.props.FloatProperty(name='StartTime', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    m_TerminationTime: bpy.props.FloatProperty(name='TerminationTime', default=0.0, update=BVTK_Node.outdate_vtk_status)
    e_MeshOverTime: bpy.props.EnumProperty(name='MeshOverTime', default="Different", items=e_MeshOverTime_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_DisableResetCache','m_EnableParticleWriting','m_ForceSerialExecution','m_IgnorePipelineTime','m_ObjectName','m_ParticleFileName','m_ForceReinjectionEveryNSteps','m_IntegratorType','m_StaticMesh','m_StaticSeeds','m_RotationScale','m_StartTime','m_TerminalSpeed','m_TerminationTime','e_MeshOverTime',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Integrator', 'ParticleWriter'], []) 
    
add_class( VTKStreaklineFilter )        
TYPENAMES.append('VTKStreaklineFilterType' )

#--------------------------------------------------------------
class VTKStreamSurface(Node, BVTK_Node):

    bl_idname = 'VTKStreamSurfaceType'
    bl_label  = 'vtkStreamSurface'
    e_IntegrationDirection_items=[ (x,x,x) for x in ['Forward', 'Backward', 'Both']]
    e_IntegratorType_items=[ (x,x,x) for x in ['RungeKutta2', 'RungeKutta4', 'RungeKutta45']]
    
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ForceSerialExecution: bpy.props.BoolProperty(name='ForceSerialExecution', default=False, update=BVTK_Node.outdate_vtk_status)
    m_SurfaceStreamlines: bpy.props.BoolProperty(name='SurfaceStreamlines', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseIterativeSeeding: bpy.props.BoolProperty(name='UseIterativeSeeding', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseLocalSeedSource: bpy.props.BoolProperty(name='UseLocalSeedSource', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_IntegrationStepUnit: bpy.props.IntProperty(name='IntegrationStepUnit', default=2, update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfSteps: bpy.props.IntProperty(name='MaximumNumberOfSteps', default=2000, update=BVTK_Node.outdate_vtk_status)
    m_InitialIntegrationStep: bpy.props.FloatProperty(name='InitialIntegrationStep', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_MaximumError: bpy.props.FloatProperty(name='MaximumError', default=1e-06, update=BVTK_Node.outdate_vtk_status)
    m_MaximumIntegrationStep: bpy.props.FloatProperty(name='MaximumIntegrationStep', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_MaximumPropagation: bpy.props.FloatProperty(name='MaximumPropagation', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_MinimumIntegrationStep: bpy.props.FloatProperty(name='MinimumIntegrationStep', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_RotationScale: bpy.props.FloatProperty(name='RotationScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    e_IntegrationDirection: bpy.props.EnumProperty(name='IntegrationDirection', default="Forward", items=e_IntegrationDirection_items, update=BVTK_Node.outdate_vtk_status)
    e_IntegratorType: bpy.props.EnumProperty(name='IntegratorType', default="RungeKutta2", items=e_IntegratorType_items, update=BVTK_Node.outdate_vtk_status)
    m_StartPosition: bpy.props.FloatVectorProperty(name='StartPosition', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_ForceSerialExecution','m_SurfaceStreamlines','m_UseIterativeSeeding','m_UseLocalSeedSource','m_ObjectName','m_IntegrationStepUnit','m_MaximumNumberOfSteps','m_InitialIntegrationStep','m_MaximumError','m_MaximumIntegrationStep','m_MaximumPropagation','m_MinimumIntegrationStep','m_RotationScale','m_TerminalSpeed','e_IntegrationDirection','e_IntegratorType','m_StartPosition',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Integrator'], []) 
    
add_class( VTKStreamSurface )        
TYPENAMES.append('VTKStreamSurfaceType' )

#--------------------------------------------------------------
class VTKStreamTracer(Node, BVTK_Node):

    bl_idname = 'VTKStreamTracerType'
    bl_label  = 'vtkStreamTracer'
    e_IntegrationDirection_items=[ (x,x,x) for x in ['Forward', 'Backward', 'Both']]
    e_IntegratorType_items=[ (x,x,x) for x in ['RungeKutta2', 'RungeKutta4', 'RungeKutta45']]
    
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ForceSerialExecution: bpy.props.BoolProperty(name='ForceSerialExecution', default=False, update=BVTK_Node.outdate_vtk_status)
    m_SurfaceStreamlines: bpy.props.BoolProperty(name='SurfaceStreamlines', default=False, update=BVTK_Node.outdate_vtk_status)
    m_UseLocalSeedSource: bpy.props.BoolProperty(name='UseLocalSeedSource', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_IntegrationStepUnit: bpy.props.IntProperty(name='IntegrationStepUnit', default=2, update=BVTK_Node.outdate_vtk_status)
    m_MaximumNumberOfSteps: bpy.props.IntProperty(name='MaximumNumberOfSteps', default=2000, update=BVTK_Node.outdate_vtk_status)
    m_InitialIntegrationStep: bpy.props.FloatProperty(name='InitialIntegrationStep', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_MaximumError: bpy.props.FloatProperty(name='MaximumError', default=1e-06, update=BVTK_Node.outdate_vtk_status)
    m_MaximumIntegrationStep: bpy.props.FloatProperty(name='MaximumIntegrationStep', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_MaximumPropagation: bpy.props.FloatProperty(name='MaximumPropagation', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_MinimumIntegrationStep: bpy.props.FloatProperty(name='MinimumIntegrationStep', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_RotationScale: bpy.props.FloatProperty(name='RotationScale', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    e_IntegrationDirection: bpy.props.EnumProperty(name='IntegrationDirection', default="Forward", items=e_IntegrationDirection_items, update=BVTK_Node.outdate_vtk_status)
    e_IntegratorType: bpy.props.EnumProperty(name='IntegratorType', default="RungeKutta2", items=e_IntegratorType_items, update=BVTK_Node.outdate_vtk_status)
    m_StartPosition: bpy.props.FloatVectorProperty(name='StartPosition', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ComputeVorticity','m_ForceSerialExecution','m_SurfaceStreamlines','m_UseLocalSeedSource','m_ObjectName','m_IntegrationStepUnit','m_MaximumNumberOfSteps','m_InitialIntegrationStep','m_MaximumError','m_MaximumIntegrationStep','m_MaximumPropagation','m_MinimumIntegrationStep','m_RotationScale','m_TerminalSpeed','e_IntegrationDirection','e_IntegratorType','m_StartPosition',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], ['Integrator'], []) 
    
add_class( VTKStreamTracer )        
TYPENAMES.append('VTKStreamTracerType' )

#--------------------------------------------------------------
class VTKSubPixelPositionEdgels(Node, BVTK_Node):

    bl_idname = 'VTKSubPixelPositionEdgelsType'
    bl_label  = 'vtkSubPixelPositionEdgels'
    
    m_TargetFlag: bpy.props.BoolProperty(name='TargetFlag', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_TargetValue: bpy.props.FloatProperty(name='TargetValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_TargetFlag','m_ObjectName','m_TargetValue',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKSubPixelPositionEdgels )        
TYPENAMES.append('VTKSubPixelPositionEdgelsType' )

#--------------------------------------------------------------
class VTKSynchronizeTimeFilter(Node, BVTK_Node):

    bl_idname = 'VTKSynchronizeTimeFilterType'
    bl_label  = 'vtkSynchronizeTimeFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_RelativeTolerance: bpy.props.FloatProperty(name='RelativeTolerance', default=1e-05, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_RelativeTolerance',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKSynchronizeTimeFilter )        
TYPENAMES.append('VTKSynchronizeTimeFilterType' )

#--------------------------------------------------------------
class VTKTensorGlyph(Node, BVTK_Node):

    bl_idname = 'VTKTensorGlyphType'
    bl_label  = 'vtkTensorGlyph'
    e_ColorMode_items=[ (x,x,x) for x in ['Scalars', 'Eigenvalues']]
    
    m_ClampScaling: bpy.props.BoolProperty(name='ClampScaling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ColorGlyphs: bpy.props.BoolProperty(name='ColorGlyphs', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ExtractEigenvalues: bpy.props.BoolProperty(name='ExtractEigenvalues', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Scaling: bpy.props.BoolProperty(name='Scaling', default=True, update=BVTK_Node.outdate_vtk_status)
    m_Symmetric: bpy.props.BoolProperty(name='Symmetric', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ThreeGlyphs: bpy.props.BoolProperty(name='ThreeGlyphs', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Length: bpy.props.FloatProperty(name='Length', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_MaxScaleFactor: bpy.props.FloatProperty(name='MaxScaleFactor', default=100.0, update=BVTK_Node.outdate_vtk_status)
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=BVTK_Node.outdate_vtk_status)
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="Scalars", items=e_ColorMode_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ClampScaling','m_ColorGlyphs','m_ExtractEigenvalues','m_Scaling','m_Symmetric','m_ThreeGlyphs','m_ObjectName','m_Length','m_MaxScaleFactor','m_ScaleFactor','e_ColorMode',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKTensorGlyph )        
TYPENAMES.append('VTKTensorGlyphType' )

#--------------------------------------------------------------
class VTKTrimmedExtrusionFilter(Node, BVTK_Node):

    bl_idname = 'VTKTrimmedExtrusionFilterType'
    bl_label  = 'vtkTrimmedExtrusionFilter'
    e_CappingStrategy_items=[ (x,x,x) for x in ['Intersection', 'MinimumDistance', 'MaximumDistance', 'AverageDistance']]
    e_ExtrusionStrategy_items=[ (x,x,x) for x in ['BoundaryEdges', 'AllEdges']]
    
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_CappingStrategy: bpy.props.EnumProperty(name='CappingStrategy', default="MaximumDistance", items=e_CappingStrategy_items, update=BVTK_Node.outdate_vtk_status)
    e_ExtrusionStrategy: bpy.props.EnumProperty(name='ExtrusionStrategy', default="BoundaryEdges", items=e_ExtrusionStrategy_items, update=BVTK_Node.outdate_vtk_status)
    m_ExtrusionDirection: bpy.props.FloatVectorProperty(name='ExtrusionDirection', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Capping','m_ObjectName','e_CappingStrategy','e_ExtrusionStrategy','m_ExtrusionDirection',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKTrimmedExtrusionFilter )        
TYPENAMES.append('VTKTrimmedExtrusionFilterType' )

#--------------------------------------------------------------
class VTKVolumeContourSpectrumFilter(Node, BVTK_Node):

    bl_idname = 'VTKVolumeContourSpectrumFilterType'
    bl_label  = 'vtkVolumeContourSpectrumFilter'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ArcId: bpy.props.IntProperty(name='ArcId', default=0, update=BVTK_Node.outdate_vtk_status)
    m_FieldId: bpy.props.IntProperty(name='FieldId', default=0, update=BVTK_Node.outdate_vtk_status)
    m_NumberOfSamples: bpy.props.IntProperty(name='NumberOfSamples', default=100, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_ArcId','m_FieldId','m_NumberOfSamples',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKVolumeContourSpectrumFilter )        
TYPENAMES.append('VTKVolumeContourSpectrumFilterType' )

#--------------------------------------------------------------
class VTKmProbe(Node, BVTK_Node):

    bl_idname = 'VTKmProbeType'
    bl_label  = 'vtkmProbe'
    
    m_PassCellArrays: bpy.props.BoolProperty(name='PassCellArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassFieldArrays: bpy.props.BoolProperty(name='PassFieldArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_PassPointArrays: bpy.props.BoolProperty(name='PassPointArrays', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_ValidCellMaskArrayName: bpy.props.StringProperty(name='ValidCellMaskArrayName', default="vtkValidCellMask", update=BVTK_Node.outdate_vtk_status)
    m_ValidPointMaskArrayName: bpy.props.StringProperty(name='ValidPointMaskArrayName', default="vtkValidPointMask", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_PassCellArrays','m_PassFieldArrays','m_PassPointArrays','m_ObjectName','m_ValidCellMaskArrayName','m_ValidPointMaskArrayName',]
    def m_connections( self ):
        return (['input 0', 'input 1'], ['output'], [], []) 
    
add_class( VTKmProbe )        
TYPENAMES.append('VTKmProbeType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Filter2', 'Filter2', items=menu_items) )