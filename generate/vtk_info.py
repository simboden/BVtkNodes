# ------------------------------------------------------------------------------
# vtk_info.py - Initialization data for parsing Python vtk classes
#               Called from populate_db.py
# ------------------------------------------------------------------------------
import sys

import vtk

# from .vtk_patch import vtk

skip_count = 0
debug_print = False

def print_skip(name):
    """Prints class name that was not included in class database"""
    global skip_count
    print("Skipped " + name)
    skip_count += 1


# Print basic VTK information
print("VTK base: " + vtk.__file__)
print("VTK version: " + vtk.vtkVersion().GetVTKVersion())
print("len(dir(vtk)): " + str(len(dir(vtk))))
print("Begin to parse VTK Python classes")

BannedNames = (
    "vtk",  # not a class
    "vtkAlgorithm",  # abstract
    "vtkAbstractInteractionDevice",  # abstract
    "vtkAbstractRenderDevice",  # abstract
    "vtkInteractorStyleTrackball",  # deprecated
    "vtkStructuredPointsGeometryFilter",  # deprecated
    "vtkVolumeRayCastCompositeFunction",  # deprecated
    "vtkVolumeRayCastIsosurfaceFunction",  # deprecated
    "vtkVolumeRayCastMapper",  # deprecated
    "vtkVolumeRayCastMIPFunction",  # deprecated
    "vtkVolumeTextureMapper2D",  # deprecated
    "vtkVolumeTextureMapper3D",
    "vtkOpenGLVolumeTextureMapper2D",  # deprecated
    "vtkOpenGLVolumeTextureMapper3D",  # deprecated
    "vtkOpenGLPolyDataMapper",  # deprecated ??
    "vtkRenderState",
    "vtkRendererDelegate",
    "vtkRenderWidget",  # instantiate internally some deprecated class
    "vtkThreadedSynchronizedTemplatesCutter3D",  # some exposed feature are non more supported
    "vtkSynchronizedTemplates3D",  # some exposed feature are non more supported
    "vtkNetCDFCAMReader",  # got obsolete methods
    "vtkQImageToImageSource",  # need qt, requires VTK built with SIP support
    "vtkThreadedSynchronizedTemplates3D",  # give problem
    "vtkSynchronizedTemplatesCutter3D",  # give problem
    "vtkRenderedRepresentation",
    "vtkRenderedGraphRepresentation",
    "vtkRenderedHierarchyRepresentation",
    "vtkRenderedSurfaceRepresentation",
    "vtkRenderedTreeAreaRepresentation",
    "vtkConvexHull2D",  # take a Renderer as  input
    "vtkDistanceToCamera",  # take a Renderer as  input
    "vtkGeoAdaptiveArcs",  # take a Renderer as  input
    "vtkGraphToGlyps",  # take a Renderer as  input
    "vtkLabelPlacer",  # take a Renderer as  input
    "vtkSelectVisiblePoints",  # take a Renderer as  input
    "vtkVolumeOutlineSource",  # take a VolumeMapper as  input
    "vtkRendererSource",
    "vtkRenderLargeImage",
    # geovis
    "vtkCompassRepresentation",
    "vtkCompassWidget",
    "vtkGeoAdaptiveArcs",
    "vtkGeoAlignedImageRepresentation",
    "vtkGeoAlignedImageSource",
    "vtkGeoArcs",
    "vtkGeoAssignCoordinates",
    "vtkGeoCamera",
    "vtkGeoFileImageSource",
    "vtkGeoFileTerrainSource",
    "vtkGeoGlobeSource",
    "vtkGeoGraticule",
    "vtkGeoImageNode",
    "vtkGeoInteractorStyle",
    "vtkGeoProjection",
    "vtkGeoProjectionSource",
    "vtkGeoRandomGraphSource",
    "vtkGeoSampleArcs",
    "vtkGeoSource",
    "vtkGeoSphereTransform",
    "vtkGeoTerrain",
    "vtkGeoTerrain2D",
    "vtkGeoTerrainNode",
    "vtkGeoTransform",
    "vtkGeoTreeNode",
    "vtkGeoTreeNodeCache",
    "vtkGlobeSource",
    # infovis
    "vtkAreaLayout",
    "vtkPerturbCoincidentVertices",
    "vtkGraphLayoutStrategy",
    "vtkArcParallelEdgeStrategy",
    "vtkBoxLayoutStrategy",
    "vtkPassThroughEdgeStrategy",
    "vtkConstrained2DLayoutStrategy",
    "vtkStackedTreeLayoutStrategy",
    "vtkCirclePackLayout",
    "vtkSquarifyLayoutStrategy",
    "vtkCirclePackFrontChainLayoutStrategy",
    "vtkSpanTreeLayoutStrategy",
    "vtkAttributeClustering2DLayoutStrategy",
    "vtkPassThroughLayoutStrategy",
    "vtkSplineGraphEdges",
    "vtkGraphLayout",
    "vtkTreeRingToPolyData",
    "vtkForceDirectedLayoutStrategy",
    "vtkEdgeLayout",
    "vtkFast2DLayoutStrategy",
    "vtkGeoMath",
    "vtkTreeOrbitLayoutStrategy",
    "vtkRandomLayoutStrategy",
    "vtkGeoEdgeStrategy",
    "vtkIncrementalForceLayout",
    "vtkAssignCoordinates",
    "vtkSimple2DLayoutStrategy",
    "vtkTreeLayoutStrategy",
    "vtkAreaLayoutStrategy",
    "vtkCommunity2DLayoutStrategy",
    "vtkCirclePackToPolyData",
    "vtkTreeMapLayout",
    "vtkSimple3DCirclesStrategy",
    "vtkKCoreLayout",
    "vtkSliceAndDiceLayoutStrategy",
    "vtkClustering2DLayoutStrategy",
    "vtkAssignCoordinatesLayoutStrategy",
    "vtkCosmicTreeLayoutStrategy",
    "vtkCirclePackLayoutStrategy",
    "vtkConeLayoutStrategy",
    "vtkCircularLayoutStrategy",
    "vtkEdgeLayoutStrategy",
    "vtkTreeMapLayoutStrategy",
    "vtkTreeMapToPolyData",
    "vtkCollapseGraph",
    "vtkTreeDifferenceFilter",
    "vtkRemoveIsolatedVertices",
    "vtkAdjacencyMatrixToEdgeTable",
    "vtkDotProductSimilarity",
    "vtkMutableGraphHelper",
    "vtkArrayToTable",
    "vtkTreeLevelsFilter",
    "vtkRemoveHiddenData",
    "vtkSparseArrayToTable",
    "vtkTransposeMatrix",
    "vtkEdgeCenters",
    "vtkPipelineGraphSource",
    "vtkTableToTreeFilter",
    "vtkStringToNumeric",
    "vtkMergeTables",
    "vtkReduceTable",
    "vtkTableToArray",
    "vtkCollapseVerticesByArray",
    "vtkStreamGraph",
    "vtkExtractSelectedTree",
    "vtkRandomGraphSource",
    "vtkGenerateIndexArray",
    "vtkDataObjectToTable",
    "vtkTreeFieldAggregator",
    "vtkMergeGraphs",
    "vtkTableToGraph",
    "vtkStringToCategory",
    "vtkPruneTreeFilter",
    "vtkGroupLeafVertices",
    "vtkExtractSelectedGraph",
    "vtkAddMembershipArray",
    "vtkVertexDegree",
    "vtkKCoreDecomposition",
    "vtkNetworkHierarchy",
    "vtkGraphHierarchicalBundleEdges",
    "vtkThresholdGraph",
    "vtkThresholdTable",
    "vtkTransferAttributes",
    "vtkArrayNorm",
    "vtkContinuousScatterplot",
    "vtkTableToSparseArray",
    "vtkMergeColumns",
    "vtkExpandSelectedGraph",
    "vtkBoostDividedEdgeBundling",
    "vtkBoostBiconnectedComponents",
    "vtkBoostConnectedComponents",
    "vtkBoostKruskalMinimumSpanningTree",
    "vtkBoostSplitTableField",
    "vtkBoostBetweennessClustering",
    "vtkBoostPrimMinimumSpanningTree",
    "vtkBoostBrandesCentrality",
    "vtkBoostExtractLargestComponent",
    "vtkBoostLogWeighting",
    "vtkBoostRandomSparseArraySource",
    "vtkBoostGraphAdapter",
    "vtkBoostBreadthFirstSearch",
    "vtkBoostBreadthFirstSearchTree",
    "vtkPBGLCollapseParallelEdges",
    "vtkPBGLCollectGraph",
    "vtkPBGLRMATGraphSource",
    "vtkPBGLRandomGraphSource",
    "vtkPBGLGraphSQLReader",
    "vtkPBGLVertexColoring",
    "vtkPBGLMinimumSpanningTree",
    "vtkPBGLGraphAdapter",
    "vtkPBGLCollapseGraph",
    "vtkPBGLShortestPaths",
    "vtkPBGLDistributedGraphHelper",
    "vtkPBGLConnectedComponents",
    "vtkPBGLBreadthFirstSearch",
    "vtkTryDowncast",
    "vtkVariantBoostSerialization",
    #
    # VTK 9.1.0 additions, with problematic method names
    #
    "vtkWebApplication",  # double free or corruption (fasttop)
)

HiddenMethods = (
    "AbortExecuteOff",
    "AbortExecuteOn",
    "AddObserver",
    "BreakOnError",
    "ComputeInputUpdateExtents",
    "DebugOff",
    "DebugOn",
    "Delete",
    "EnlargeOutputUpdateExtents",
    "GetAbortExecute",
    "GetAddressAsString",
    "GetClassName",
    "GetDebug",
    "GetErrorCode",
    "GetGlobalWarningDisplay",
    "GetMTime",
    "GetOutputIndex",
    "GetProgress",
    "GetProgressMaxValue",
    "GetProgressText",
    "GetReferenceCount",
    "GetReleaseDataFlag",
    "GlobalWarningDisplayOn",
    "GlobalWarningDisplayOff",
    "HasObserver",
    "InRegisterLoop",
    "InvokeEvent",
    "IsA",
    "IsTypeOf",
    "New",
    "NewInstance",
    "PrintRevisions",
    "PropagateUpdateExtent",
    "Register",
    "ReleaseDataFlagOff",
    "ReleaseDataFlagOn",
    "RemoveAllInputs",
    "RemoveObserver",
    "RemoveObservers",
    "SetAbortExecute",
    "SafeDownCast",
    "SetDebug",
    "SetEndMethod",
    "SetGlobalWarningDisplay",
    "SetProgress",
    "SetProgress",
    "SetProgressMethod",
    "SetProgressText",
    "SetReleaseDataFlag",
    "SetReferenceCount",
    "SetRequestedRenderModeToRayCastAndTexture",
    "SetRequestedRenderModeToTexture",
    "SetStartMethod",
    "SqueezeInputArray",
    "TriggerAsynchronousUpdate",
    "UnRegister",
    "UnRegisterAllOutputs",
    "UpdateData",
    "UpdateInformation",
    "UpdateProgress",
    "UpdateWholeExtent",
    "GetUserTransformMatrixMTime",
    "ReleaseGraphicsResources",
    "RenderOpaqueGeometry",
    "RenderTranslucentGeometry",
    "ApplyProperties",
    "ComputeMatrix",
    "ShallowCopy",
    "WholeExtent",
)

HiddenProp = (
    "DataExtent",
    "DataType",
    "Executive",
    "Information",
    "InputConnection",
    "InputDataObject",
    "Locator",
    "Output",  ###
    "OutputPointsPrecision",
    "ProgressObserver",
    "ScalarTree",
    "UpdateExtent",
    "UseScalarTree",
    "WholeExtent",
    "ParserErrorObserver",
    "Kernel7x7",  # vtkImageConvolve
    "Kernel7x7x7",  # vtkImageConvolve -- Setter has no doc
    "ResolveCoincidentTopologyPointOffsetParameter",  # bad getter: Set(float) Get(float) -- is in all the Mapper Classes
    "ResolveCoincidentTopologyLineOffsetParameters",
    "RelativeCoincidentTopologyPointOffsetParameter",  # bad getter: Set(float) Get(float) -- is in all the Mapper Classes
    "RelativeCoincidentTopologyLineOffsetParameters",
    "Controller",  # parallel filters
    "SocketController",  # parallel filters
    "Compressor",  # xml writers
    "AssessNames",  # hystogram and statistics
    "Camera",  # cant pass the camera in blender Nodes yet
    "FileNames",  # image readers for volumes on multiple slices with non generable names
    "InformationInput",  # optiona in some image filters
    "LayoutStrategy",  # graph layout --- not addressed yet
    "MemoryBuffer",  # on image readers, allow reading from memory instead of file
    "ReaderErrorObserver"  # xml readers
    "Renderer",  # cant pass the renderer in blender Nodes yet
    "VolumeMapper",  # VolumeOutlineSource
    "Result",  # vtkUnsignedCharArray used in PNG and JPEG writer
    "CallbackUserData" "ImportVoidPointer",  # in ImageImport  # in ImageImport
)

InterestingClasses = (
    vtk.vtkAlgorithm,  # sources, reader, writers, filters
    vtk.vtkAbstractTransform,  # transform
    vtk.vtkImplicitFunction,  # implicit functions
    vtk.vtkInitialValueProblemSolver,  # Integrator
    vtk.vtkParametricFunction,  # parametric function
)

def text_in_parenthesis(s):
    """Return substring of s which is inside parenthesis"""
    return s[s.find("(")+1:s.find(")")]

def remove_argument_names(s):
    """Remove argument names from argument text string of arguments, e.g.
    'self, _arg1:float, _arg2:float' -> 'float, float'
    """
    args = []
    for x in s.split(","):
        if x == 'self':
            continue
        if ":" in x:
            args.append(x.split(":")[1].strip())
        else:
            args.append(x.strip())
    return ",".join(args)

def extract_args(s):
    """Extract return variable types from VTK Python doc strings for both
    Set and Get methods.
    """

    # Examples used for developing extraction:
    # Processing vtk3DLinearGridCrinkleExtractor.SetCopyCellData
    # setter_doc: SetCopyCellData(self, _arg:bool) -> None
    # getter_doc: GetCopyCellData(self) -> bool
    # Processing vtkAxes.SetOrigin
    # setter_doc: SetOrigin(self, _arg1:float, _arg2:float, _arg3:float) -> None
    # getter_doc: GetOrigin(self) -> (float, float, float)
    # Processing vtkExtractBlockUsingDataAssembly.SetSelector
    # setter_doc: SetSelector(self, selector:str) -> None
    # getter_doc: GetSelector(self, index:int) -> str

    if ">" in s:
        if s.startswith("Get"):
            s = s.split(">")[1]  # take text right to ->
        if s.startswith("Set"):
            s = s.split(">")[0]  # take text left to ->
    if "(" in s:
        s = text_in_parenthesis(s)
    s = remove_argument_names(s)
    return s

# -------------------------------------------------
# collect infos
# -------------------------------------------------

infos = []

counter = 0
for name in sorted(dir(vtk)):

    if not name.startswith("vtk"):
        print_skip(name)
        continue

    if name in BannedNames:
        # print( 'skipping', name )
        print_skip(name)
        continue

    c = getattr(vtk, name, None)
    if c is None:
        print_skip(name)
        continue

    try:
        o = c()
    except:
        print_skip(name)
        continue

    interesting = issubclass(c, vtk.vtkAlgorithm)
    if not interesting:
        interesting = issubclass(c, vtk.vtkAbstractTransform)
    if not interesting:
        interesting = issubclass(c, vtk.vtkImplicitFunction)
    if not interesting:
        interesting = issubclass(c, vtk.vtkInitialValueProblemSolver)
    if not interesting:
        interesting = issubclass(c, vtk.vtkParametricFunction)
    if not interesting:
        print_skip(name)
        continue

    counter += 1
    # if counter >50:
    #    break

    out_type = None
    get_output = getattr(o, "GetOutput", None)
    if get_output:
        out_type = get_output.__doc__.split("\n")[0].split(">")[1].strip()

    num_in = 0
    if hasattr(o, "GetNumberOfInputPorts"):
        num_in = o.GetNumberOfInputPorts()

    num_out = 0
    if hasattr(o, "GetNumberOfOutputPorts"):
        num_out = o.GetNumberOfOutputPorts()

    props = []

    # print()
    # print( counter, name.ljust(40), num_in, num_out, out_type )

    # if not issubclass(c, vtk.vtkAlgorithm):
    #     print(counter, name.ljust(40), num_in, num_out, out_type)

    # retrieve the interesting methods
    m = [
        x
        for x in dir(o)
        if not x.startswith("__") and not x in HiddenMethods and not x[3:] in HiddenProp
    ]
    m.sort()

    # scan methods searching for properties
    for x in m:
        if debug_print:
            print("Processing " + str(name) + "." + str(x))

        # Handle function pairs like SetXyz and GetXyz
        if (
            x.startswith("Set") and "Get" + x[3:] in m
        ):
            p = x[3:]
            setter = getattr(o, "Set" + p)
            getter = getattr(o, "Get" + p)

            # Assumes that first line in the method doc is the Python
            # function signature. If no end parenthesis is found, add
            # also second line.
            setter_doc = setter.__doc__.split("\n")[0]
            if not ")" in setter_doc:
                setter_doc += setter.__doc__.split("\n")[1]
            setter_arg = extract_args(setter_doc)

            getter_doc = getter.__doc__.split("\n")[0]
            if not ")" in getter_doc:
                getter_doc += getter.__doc__.split("\n")[1]
            getter_arg = extract_args(getter_doc)

            p_note = ""

            # Setter and getter args should match
            if debug_print:
                print("setter_doc: " + str(setter_doc))  # + " -- detected args: " + setter_arg)
                print("getter_doc: " + str(getter_doc))  # + " -- detected args: " + getter_arg)
            if setter_arg != getter_arg:
                setter_doc = setter_doc.replace("V.", "").replace(p, "")
                getter_doc = getter_doc.replace("V.", "").replace(p, "")
                p_note = "# ko: arg mismatch " + setter_doc + " :: " + getter_doc
                # print( 'ko ', p.ljust(30), 'args mismatch:', setter_doc, getter_doc)
            else:
                # if this property returns a vtkObject, which is already created, then this is an optional input property
                if not "," in getter_arg and getter_arg.startswith("vtk"):
                    po = getter()
                    if po:
                        p_value = po.__class__.__name__
                        p_note += "# - optional"
                    else:
                        p_value = "0"
                else:
                    # Get the default value by calling the getter
                    try:
                        value = getter()
                    except:
                        value = 0
                    if value == float("inf"):
                        value = 1e300
                    if value == float("-inf"):
                        value = -1e300
                    p_value = str(value)

                if getter_arg == "string" or getter_arg == "str":
                    if p_value is None or p_value == "None":
                        p_value = '""'

                # if there are also the methods p+On and p+Off this property is a bool
                if p + "On" in m and p + "Off" in m:
                    setter_arg = "bool"

                # if there are also methods Set+p+To+xxx this property is an Enum  (WIP)
                p_items = []  # enum-names ordered by their value --- or nothing
                if setter_arg == "int":
                    q = "Set" + p + "To"
                    names = [y.replace(q, "") for y in m if y.startswith(q)]
                    if len(names):
                        setter_arg = "enum"
                        # retrieve the numerical value matching the enum-names
                        enum_value_to_name = {}
                        for y in names:
                            getattr(o, q + y)()  # call Set+p+To+y()
                            enum_value_to_name[getter()] = y  # call Get+p()

                        if not int(p_value) in enum_value_to_name:
                            p_value = sorted(names)[0]  # fallback for weird cases
                        else:
                            p_value = enum_value_to_name[
                                int(p_value)
                            ]  # translate the default value

                        p_items = [
                            (x, enum_value_to_name[x])
                            for x in enum_value_to_name.keys()
                        ]
                        p_items.sort()

            if "p_value" not in locals():
                raise Exception("No p_value for " + str(name) + "." + str(p))

            props.append(
                {
                    "name": p,
                    "args": setter_arg,
                    "value": p_value,
                    "items": p_items,
                    "note": p_note,
                }
            )
            if not p_items:
                p_items = ""  # just for the printout
            # print( '   ', p.ljust(30), setter_arg, p_value, p_items, p_note )

    infos.append(
        {
            "name": name[3:],
            "num_in": num_in,
            "num_out": num_out,
            "out_type": out_type,
            "props": props,
            "docs": c.__doc__,
        }
    )
    print("Appended " + name)

print()
print(
    "Generated info for "
    + str(counter)
    + " and skipped "
    + str(skip_count)
    + " classes"
)
