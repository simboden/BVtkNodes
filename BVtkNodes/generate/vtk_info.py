import sys

import vtk
#from .vtk_patch import vtk

BannedNames = (
'vtk', # not a class
'vtkAlgorithm', # abstract
'vtkAbstractInteractionDevice', # abstract
'vtkAbstractRenderDevice',  # abstract
'vtkInteractorStyleTrackball', # deprecated
'vtkStructuredPointsGeometryFilter', # deprecated
'vtkVolumeRayCastCompositeFunction', # deprecated
'vtkVolumeRayCastIsosurfaceFunction', # deprecated
'vtkVolumeRayCastMapper',# deprecated
'vtkVolumeRayCastMIPFunction', # deprecated
'vtkVolumeTextureMapper2D', # deprecated
'vtkVolumeTextureMapper3D',
'vtkOpenGLVolumeTextureMapper2D',# deprecated
'vtkOpenGLVolumeTextureMapper3D',# deprecated
'vtkOpenGLPolyDataMapper',# deprecated ??
'vtkRenderState',
'vtkRendererDelegate',
'vtkRenderWidget', # instantiate internally some deprecated class
'vtkThreadedSynchronizedTemplatesCutter3D', # some exposed feature are non more supported
'vtkSynchronizedTemplates3D', # some exposed feature are non more supported
'vtkNetCDFCAMReader', # got obsolete methods
'vtkQImageToImageSource', # need qt, requires VTK built with SIP support
'vtkThreadedSynchronizedTemplates3D', # give problem
'vtkSynchronizedTemplatesCutter3D',   # give problem

'vtkRenderedRepresentation',
'vtkRenderedGraphRepresentation',
'vtkRenderedHierarchyRepresentation',
'vtkRenderedSurfaceRepresentation',
'vtkRenderedTreeAreaRepresentation',
'vtkConvexHull2D',        # take a Renderer as  input
'vtkDistanceToCamera',    # take a Renderer as  input
'vtkGeoAdaptiveArcs',     # take a Renderer as  input
'vtkGraphToGlyps',        # take a Renderer as  input
'vtkLabelPlacer',         # take a Renderer as  input
'vtkSelectVisiblePoints', # take a Renderer as  input
'vtkVolumeOutlineSource', # take a VolumeMapper as  input
'vtkRendererSource',
'vtkRenderLargeImage',

#geovis
'vtkCompassRepresentation',
'vtkCompassWidget',
'vtkGeoAdaptiveArcs',
'vtkGeoAlignedImageRepresentation',
'vtkGeoAlignedImageSource',
'vtkGeoArcs',
'vtkGeoAssignCoordinates',
'vtkGeoCamera',
'vtkGeoFileImageSource',
'vtkGeoFileTerrainSource',
'vtkGeoGlobeSource',
'vtkGeoGraticule',
'vtkGeoImageNode',
'vtkGeoInteractorStyle',
'vtkGeoProjection',
'vtkGeoProjectionSource',
'vtkGeoRandomGraphSource',
'vtkGeoSampleArcs',
'vtkGeoSource',
'vtkGeoSphereTransform',
'vtkGeoTerrain',
'vtkGeoTerrain2D',
'vtkGeoTerrainNode',
'vtkGeoTransform',
'vtkGeoTreeNode',
'vtkGeoTreeNodeCache',
'vtkGlobeSource',

#infovis
'vtkAreaLayout',
'vtkPerturbCoincidentVertices',
'vtkGraphLayoutStrategy',
'vtkArcParallelEdgeStrategy',
'vtkBoxLayoutStrategy',
'vtkPassThroughEdgeStrategy',
'vtkConstrained2DLayoutStrategy',
'vtkStackedTreeLayoutStrategy',
'vtkCirclePackLayout',
'vtkSquarifyLayoutStrategy',
'vtkCirclePackFrontChainLayoutStrategy',
'vtkSpanTreeLayoutStrategy',
'vtkAttributeClustering2DLayoutStrategy',
'vtkPassThroughLayoutStrategy',
'vtkSplineGraphEdges',
'vtkGraphLayout',
'vtkTreeRingToPolyData',
'vtkForceDirectedLayoutStrategy',
'vtkEdgeLayout',
'vtkFast2DLayoutStrategy',
'vtkGeoMath',
'vtkTreeOrbitLayoutStrategy',
'vtkRandomLayoutStrategy',
'vtkGeoEdgeStrategy',
'vtkIncrementalForceLayout',
'vtkAssignCoordinates',
'vtkSimple2DLayoutStrategy',
'vtkTreeLayoutStrategy',
'vtkAreaLayoutStrategy',
'vtkCommunity2DLayoutStrategy',
'vtkCirclePackToPolyData',
'vtkTreeMapLayout',
'vtkSimple3DCirclesStrategy',
'vtkKCoreLayout',
'vtkSliceAndDiceLayoutStrategy',
'vtkClustering2DLayoutStrategy',
'vtkAssignCoordinatesLayoutStrategy',
'vtkCosmicTreeLayoutStrategy',
'vtkCirclePackLayoutStrategy',
'vtkConeLayoutStrategy',
'vtkCircularLayoutStrategy',
'vtkEdgeLayoutStrategy',
'vtkTreeMapLayoutStrategy',
'vtkTreeMapToPolyData',
'vtkCollapseGraph',
'vtkTreeDifferenceFilter',
'vtkRemoveIsolatedVertices',
'vtkAdjacencyMatrixToEdgeTable',
'vtkDotProductSimilarity',
'vtkMutableGraphHelper',
'vtkArrayToTable',
'vtkTreeLevelsFilter',
'vtkRemoveHiddenData',
'vtkSparseArrayToTable',
'vtkTransposeMatrix',
'vtkEdgeCenters',
'vtkPipelineGraphSource',
'vtkTableToTreeFilter',
'vtkStringToNumeric',
'vtkMergeTables',
'vtkReduceTable',
'vtkTableToArray',
'vtkCollapseVerticesByArray',
'vtkStreamGraph',
'vtkExtractSelectedTree',
'vtkRandomGraphSource',
'vtkGenerateIndexArray',
'vtkDataObjectToTable',
'vtkTreeFieldAggregator',
'vtkMergeGraphs',
'vtkTableToGraph',
'vtkStringToCategory',
'vtkPruneTreeFilter',
'vtkGroupLeafVertices',
'vtkExtractSelectedGraph',
'vtkAddMembershipArray',
'vtkVertexDegree',
'vtkKCoreDecomposition',
'vtkNetworkHierarchy',
'vtkGraphHierarchicalBundleEdges',
'vtkThresholdGraph',
'vtkThresholdTable',
'vtkTransferAttributes',
'vtkArrayNorm',
'vtkContinuousScatterplot',
'vtkTableToSparseArray',
'vtkMergeColumns',
'vtkExpandSelectedGraph',
'vtkBoostDividedEdgeBundling',
'vtkBoostBiconnectedComponents',
'vtkBoostConnectedComponents',
'vtkBoostKruskalMinimumSpanningTree',
'vtkBoostSplitTableField',
'vtkBoostBetweennessClustering',
'vtkBoostPrimMinimumSpanningTree',
'vtkBoostBrandesCentrality',
'vtkBoostExtractLargestComponent',
'vtkBoostLogWeighting',
'vtkBoostRandomSparseArraySource',
'vtkBoostGraphAdapter',
'vtkBoostBreadthFirstSearch',
'vtkBoostBreadthFirstSearchTree',
'vtkPBGLCollapseParallelEdges',
'vtkPBGLCollectGraph',
'vtkPBGLRMATGraphSource',
'vtkPBGLRandomGraphSource',
'vtkPBGLGraphSQLReader',
'vtkPBGLVertexColoring',
'vtkPBGLMinimumSpanningTree',
'vtkPBGLGraphAdapter',
'vtkPBGLCollapseGraph',
'vtkPBGLShortestPaths',
'vtkPBGLDistributedGraphHelper',
'vtkPBGLConnectedComponents',
'vtkPBGLBreadthFirstSearch',
'vtkTryDowncast',
'vtkVariantBoostSerialization'

)

HiddenMethods = (
'AbortExecuteOff',
'AbortExecuteOn',
'AddObserver',
'BreakOnError',
'ComputeInputUpdateExtents',
'DebugOff',
'DebugOn',
'Delete',
'EnlargeOutputUpdateExtents',
'GetAbortExecute',
'GetAddressAsString',
'GetClassName',
'GetDebug',
'GetErrorCode',
'GetGlobalWarningDisplay',
'GetMTime',
'GetOutputIndex',
'GetProgress',
'GetProgressMaxValue',
'GetProgressText',
'GetReferenceCount',
'GetReleaseDataFlag',
'GlobalWarningDisplayOn',
'GlobalWarningDisplayOff',
'HasObserver',
'InRegisterLoop',
'InvokeEvent',
'IsA',
'IsTypeOf',
'New',
'NewInstance',
'PrintRevisions',
'PropagateUpdateExtent',
'Register',
'ReleaseDataFlagOff',
'ReleaseDataFlagOn',
'RemoveAllInputs',
'RemoveObserver',
'RemoveObservers',
'SetAbortExecute',
'SafeDownCast',
'SetDebug',
'SetEndMethod',
'SetGlobalWarningDisplay',
'SetProgress',
'SetProgress',
'SetProgressMethod',
'SetProgressText',
'SetReleaseDataFlag',
'SetReferenceCount',
'SetRequestedRenderModeToRayCastAndTexture',
'SetRequestedRenderModeToTexture',
'SetStartMethod',
'SqueezeInputArray',
'TriggerAsynchronousUpdate',
'UnRegister',
'UnRegisterAllOutputs',
'UpdateData',
'UpdateInformation',
'UpdateProgress',
'UpdateWholeExtent',
'GetUserTransformMatrixMTime',
'ReleaseGraphicsResources',
'RenderOpaqueGeometry',
'RenderTranslucentGeometry',
'ApplyProperties',
'ComputeMatrix',
'ShallowCopy',
'WholeExtent'
)

HiddenProp = (
'DataExtent',
'DataType',
'Executive',
'Information',
'InputConnection',
'InputDataObject',
'Locator',
'Output', ###
'OutputPointsPrecision',
'ProgressObserver',
'ScalarTree',
'UpdateExtent',
'UseScalarTree',
'WholeExtent',
'ParserErrorObserver',
'Kernel7x7',  # vtkImageConvolve
'Kernel7x7x7', # vtkImageConvolve -- Setter has no doc
'ResolveCoincidentTopologyPointOffsetParameter', # bad getter: Set(float) Get(float) -- is in all the Mapper Classes
'ResolveCoincidentTopologyLineOffsetParameters',
'RelativeCoincidentTopologyPointOffsetParameter', # bad getter: Set(float) Get(float) -- is in all the Mapper Classes
'RelativeCoincidentTopologyLineOffsetParameters',

'Controller',         # parallel filters
'SocketController',   # parallel filters
'Compressor',         # xml writers
'AssessNames',        # hystogram and statistics
'Camera',             # cant pass the camera in blender Nodes yet
'FileNames',          # image readers for volumes on multiple slices with non generable names
'InformationInput',   # optiona in some image filters
'LayoutStrategy',     # graph layout --- not addressed yet
'MemoryBuffer',       # on image readers, allow reading from memory instead of file
'ReaderErrorObserver' # xml readers
'Renderer',           # cant pass the renderer in blender Nodes yet
'VolumeMapper',       # VolumeOutlineSource
'Result',             # vtkUnsignedCharArray used in PNG and JPEG writer
'CallbackUserData'    # in ImageImport
'ImportVoidPointer'   # in ImageImport

)

InterestingClasses = (
vtk.vtkAlgorithm,                  # sources, reader, writers, filters
vtk.vtkAbstractTransform,          # transform
vtk.vtkImplicitFunction,           # implicti functions
vtk.vtkInitialValueProblemSolver,  # Integrator
vtk.vtkParametricFunction          # parametric function
)
#-------------------------------------------------
# collect infos
#-------------------------------------------------

infos = []

counter = 0
for name in sorted( dir(vtk)):

    if not name.startswith('vtk'):
        continue

    if name in BannedNames:
        #print( 'skipping', name )
        continue

    c = getattr( vtk, name, None )
    if c is None:
        continue

    try:
        o = c()
    except:
        continue

    interesting = issubclass( c, vtk.vtkAlgorithm )
    if not interesting : interesting = issubclass(c, vtk.vtkAbstractTransform)
    if not interesting : interesting = issubclass(c, vtk.vtkImplicitFunction)
    if not interesting : interesting = issubclass(c, vtk.vtkInitialValueProblemSolver)
    if not interesting : interesting = issubclass(c, vtk.vtkParametricFunction)
    if not interesting :
        continue

    counter +=1
    #if counter >50:
    #    break

    out_type = None
    get_output = getattr( o, 'GetOutput', None )
    if get_output:
        out_type = get_output.__doc__.split('\n')[0].split('>')[1].strip()

    num_in = 0
    if hasattr(o, "GetNumberOfInputPorts") :
        num_in  = o.GetNumberOfInputPorts()

    num_out = 0
    if hasattr(o, "GetNumberOfOutputPorts") :
        num_out = o.GetNumberOfOutputPorts()

    props   = []

    #print()
    #print( counter, name.ljust(40), num_in, num_out, out_type )

    # if not issubclass(c, vtk.vtkAlgorithm):
    #     print(counter, name.ljust(40), num_in, num_out, out_type)


    # retrieve the interesting methods
    m = [ x for x in dir(o) if not x.startswith('__') and not x in HiddenMethods and not x[3:] in HiddenProp ]
    m.sort()

    # scan methods searching for properties
    for x in m:
        if x.startswith('Set') and 'Get'+x[3:] in m : # if method is a Setter and there is a matching Getter
            p = x[3:]
            setter = getattr(o, 'Set'+p )
            getter = getattr(o, 'Get'+p )

            # the first line in the method doc is the python-function-signature --- example: SetXXX(int) -- GetXXX()->int
            setter_doc = setter.__doc__.split('\n')[0]
            getter_doc = getter.__doc__.split('\n')[0]

            # extract the arguments.
            # sometime getter have no '->' - meaning that they return the value in the arguments,
            # in some case these properties are reduntant, so lets ignore them
            setter_arg = setter_doc.split('(')[1].replace(')','').replace(' ','')
            if '>' in getter_doc:
                getter_arg = getter_doc.split('>')[1].replace(')','').replace('(','').replace(' ','')  
            else:
                getter_arg = "none"

            p_note = ''
            # setter and getter args should match
            if setter_arg != getter_arg:
                setter_doc = setter_doc.replace("V.",'').replace(p, '')
                getter_doc = getter_doc.replace("V.",'').replace(p, '')
                p_note = '# ko: arg mismatch ' + setter_doc + ' ' + getter_doc 
                #print( 'ko ', p.ljust(30), 'args mismatch:', setter_doc, getter_doc)
            else:
                

                # it this property return a vtkObject, which is already created, this is an optional-input-property
                if not ',' in getter_arg and getter_arg.startswith('vtk'):
                    po = getter()
                    if po:
                        p_value = po.__class__.__name__
                        p_note += '# - optional'
                    else:
                        p_value = '0'
                else:
                    value = getter() # get the default value by calling the getter
                    if value == float( 'inf'): value =  1e300
                    if value == float('-inf'): value = -1e300
                    p_value = str( value )

                if getter_arg == 'string':
                    if p_value is None or p_value == 'None':
                        p_value = '""'
                
                # if there are also the methods p+On and p+Off this property is a bool
                if p+'On' in m and p+'Off' in m :
                    setter_arg = 'bool'

                # if there are also methods Set+p+To+xxx this property is an Enum  (WIP)
                p_items = [] # enum-names ordered by their value --- or nothing
                if setter_arg == 'int':
                    q = 'Set'+p+'To'
                    names = [ y.replace(q,'') for y in m if y.startswith( q ) ]
                    if len(names):
                        setter_arg = 'enum'
                        # retrieve the numerical value matching the enum-names
                        enum_value_to_name = {}
                        for y in names:
                            getattr(o,q+y)()                     # call Set+p+To+y()
                            enum_value_to_name[ getter() ] = y   # call Get+p()

                        if not int(p_value) in enum_value_to_name:
                            p_value = sorted( names )[0]                  # fallback for weird cases
                        else:
                            p_value = enum_value_to_name[ int(p_value) ]  # translate the default value
                            
                        p_items = [ (x,enum_value_to_name[x]) for x in enum_value_to_name.keys() ]
                        p_items.sort()
                    
            props.append( { 'name':p, 'args':setter_arg, 'value':p_value, 'items':p_items, 'note':p_note } )
            if not p_items: p_items='' # just for the printout
            #print( '   ', p.ljust(30), setter_arg, p_value, p_items, p_note )


    infos.append( {'name':name[3:], 'num_in':num_in, 'num_out':num_out, 'out_type':out_type, 'props':props, 'docs':c.__doc__ } )


print()
print('info done')


