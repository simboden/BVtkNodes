# Generated definitions for VTK class group: ImplicitFunc
# VTK version: 9.2.6

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKBox(Node, BVTK_Node):

    bl_idname = 'VTKBoxType'
    bl_label  = 'vtkBox'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKBox )        
TYPENAMES.append('VTKBoxType' )

#--------------------------------------------------------------
class VTKCone(Node, BVTK_Node):

    bl_idname = 'VTKConeType'
    bl_label  = 'vtkCone'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Angle: bpy.props.FloatProperty(name='Angle', default=45.0, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Angle',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKCone )        
TYPENAMES.append('VTKConeType' )

#--------------------------------------------------------------
class VTKCoordinateFrame(Node, BVTK_Node):

    bl_idname = 'VTKCoordinateFrameType'
    bl_label  = 'vtkCoordinateFrame'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_XAxis: bpy.props.FloatVectorProperty(name='XAxis', default=[1.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_YAxis: bpy.props.FloatVectorProperty(name='YAxis', default=[0.0, 1.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_ZAxis: bpy.props.FloatVectorProperty(name='ZAxis', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Origin','m_XAxis','m_YAxis','m_ZAxis',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKCoordinateFrame )        
TYPENAMES.append('VTKCoordinateFrameType' )

#--------------------------------------------------------------
class VTKCylinder(Node, BVTK_Node):

    bl_idname = 'VTKCylinderType'
    bl_label  = 'vtkCylinder'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_Axis: bpy.props.FloatVectorProperty(name='Axis', default=[0.0, 1.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Radius','m_Axis','m_Center',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKCylinder )        
TYPENAMES.append('VTKCylinderType' )

#--------------------------------------------------------------
class VTKImplicitBoolean(Node, BVTK_Node):

    bl_idname = 'VTKImplicitBooleanType'
    bl_label  = 'vtkImplicitBoolean'
    e_OperationType_items=[ (x,x,x) for x in ['Union', 'Intersection', 'Difference', 'UnionOfMagnitudes']]
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    e_OperationType: bpy.props.EnumProperty(name='OperationType', default="Union", items=e_OperationType_items, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','e_OperationType',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitBoolean )        
TYPENAMES.append('VTKImplicitBooleanType' )

#--------------------------------------------------------------
class VTKImplicitDataSet(Node, BVTK_Node):

    bl_idname = 'VTKImplicitDataSetType'
    bl_label  = 'vtkImplicitDataSet'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_OutValue: bpy.props.FloatProperty(name='OutValue', default=-1e+30, update=BVTK_Node.outdate_vtk_status)
    m_OutGradient: bpy.props.FloatVectorProperty(name='OutGradient', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_OutValue','m_OutGradient',]
    def m_connections( self ):
        return ([], [], ['DataSet', 'Transform'], ['self']) 
    
add_class( VTKImplicitDataSet )        
TYPENAMES.append('VTKImplicitDataSetType' )

#--------------------------------------------------------------
class VTKImplicitHalo(Node, BVTK_Node):

    bl_idname = 'VTKImplicitHaloType'
    bl_label  = 'vtkImplicitHalo'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_FadeOut: bpy.props.FloatProperty(name='FadeOut', default=0.01, update=BVTK_Node.outdate_vtk_status)
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_FadeOut','m_Radius','m_Center',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitHalo )        
TYPENAMES.append('VTKImplicitHaloType' )

#--------------------------------------------------------------
class VTKImplicitPolyDataDistance(Node, BVTK_Node):

    bl_idname = 'VTKImplicitPolyDataDistanceType'
    bl_label  = 'vtkImplicitPolyDataDistance'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_NoValue: bpy.props.FloatProperty(name='NoValue', default=0.0, update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1e-12, update=BVTK_Node.outdate_vtk_status)
    m_NoClosestPoint: bpy.props.FloatVectorProperty(name='NoClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_NoGradient: bpy.props.FloatVectorProperty(name='NoGradient', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_NoValue','m_Tolerance','m_NoClosestPoint','m_NoGradient',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitPolyDataDistance )        
TYPENAMES.append('VTKImplicitPolyDataDistanceType' )

#--------------------------------------------------------------
class VTKImplicitProjectOnPlaneDistance(Node, BVTK_Node):

    bl_idname = 'VTKImplicitProjectOnPlaneDistanceType'
    bl_label  = 'vtkImplicitProjectOnPlaneDistance'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.01, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return ([], [], ['Norm', 'Transform'], ['self']) 
    
add_class( VTKImplicitProjectOnPlaneDistance )        
TYPENAMES.append('VTKImplicitProjectOnPlaneDistanceType' )

#--------------------------------------------------------------
class VTKImplicitSelectionLoop(Node, BVTK_Node):

    bl_idname = 'VTKImplicitSelectionLoopType'
    bl_label  = 'vtkImplicitSelectionLoop'
    
    m_AutomaticNormalGeneration: bpy.props.BoolProperty(name='AutomaticNormalGeneration', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_AutomaticNormalGeneration','m_ObjectName','m_Normal',]
    def m_connections( self ):
        return ([], [], ['Loop', 'Transform'], ['self']) 
    
add_class( VTKImplicitSelectionLoop )        
TYPENAMES.append('VTKImplicitSelectionLoopType' )

#--------------------------------------------------------------
class VTKImplicitSum(Node, BVTK_Node):

    bl_idname = 'VTKImplicitSumType'
    bl_label  = 'vtkImplicitSum'
    
    m_NormalizeByWeight: bpy.props.BoolProperty(name='NormalizeByWeight', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_NormalizeByWeight','m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKImplicitSum )        
TYPENAMES.append('VTKImplicitSumType' )

#--------------------------------------------------------------
class VTKImplicitVolume(Node, BVTK_Node):

    bl_idname = 'VTKImplicitVolumeType'
    bl_label  = 'vtkImplicitVolume'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_OutValue: bpy.props.FloatProperty(name='OutValue', default=-1e+30, update=BVTK_Node.outdate_vtk_status)
    m_OutGradient: bpy.props.FloatVectorProperty(name='OutGradient', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_OutValue','m_OutGradient',]
    def m_connections( self ):
        return ([], [], ['Transform', 'Volume'], ['self']) 
    
add_class( VTKImplicitVolume )        
TYPENAMES.append('VTKImplicitVolumeType' )

#--------------------------------------------------------------
class VTKImplicitWindowFunction(Node, BVTK_Node):

    bl_idname = 'VTKImplicitWindowFunctionType'
    bl_label  = 'vtkImplicitWindowFunction'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_WindowRange: bpy.props.FloatVectorProperty(name='WindowRange', default=[0.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    m_WindowValues: bpy.props.FloatVectorProperty(name='WindowValues', default=[0.0, 1.0], size=2, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_WindowRange','m_WindowValues',]
    def m_connections( self ):
        return ([], [], ['ImplicitFunction', 'Transform'], ['self']) 
    
add_class( VTKImplicitWindowFunction )        
TYPENAMES.append('VTKImplicitWindowFunctionType' )

#--------------------------------------------------------------
class VTKPerlinNoise(Node, BVTK_Node):

    bl_idname = 'VTKPerlinNoiseType'
    bl_label  = 'vtkPerlinNoise'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Amplitude: bpy.props.FloatProperty(name='Amplitude', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_Frequency: bpy.props.FloatVectorProperty(name='Frequency', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_Phase: bpy.props.FloatVectorProperty(name='Phase', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Amplitude','m_Frequency','m_Phase',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKPerlinNoise )        
TYPENAMES.append('VTKPerlinNoiseType' )

#--------------------------------------------------------------
class VTKPlane(Node, BVTK_Node):

    bl_idname = 'VTKPlaneType'
    bl_label  = 'vtkPlane'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Normal','m_Origin',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKPlane )        
TYPENAMES.append('VTKPlaneType' )

#--------------------------------------------------------------
class VTKPlanes(Node, BVTK_Node):

    bl_idname = 'VTKPlanesType'
    bl_label  = 'vtkPlanes'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['Normals', 'Points', 'Transform'], ['self']) 
    
add_class( VTKPlanes )        
TYPENAMES.append('VTKPlanesType' )

#--------------------------------------------------------------
class VTKPlanesIntersection(Node, BVTK_Node):

    bl_idname = 'VTKPlanesIntersectionType'
    bl_label  = 'vtkPlanesIntersection'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['Normals', 'Points', 'Transform'], ['self']) 
    
add_class( VTKPlanesIntersection )        
TYPENAMES.append('VTKPlanesIntersectionType' )

#--------------------------------------------------------------
class VTKPolyPlane(Node, BVTK_Node):

    bl_idname = 'VTKPolyPlaneType'
    bl_label  = 'vtkPolyPlane'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['PolyLine', 'Transform'], ['self']) 
    
add_class( VTKPolyPlane )        
TYPENAMES.append('VTKPolyPlaneType' )

#--------------------------------------------------------------
class VTKQuadric(Node, BVTK_Node):

    bl_idname = 'VTKQuadricType'
    bl_label  = 'vtkQuadric'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKQuadric )        
TYPENAMES.append('VTKQuadricType' )

#--------------------------------------------------------------
class VTKSphere(Node, BVTK_Node):

    bl_idname = 'VTKSphereType'
    bl_label  = 'vtkSphere'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName','m_Radius','m_Center',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKSphere )        
TYPENAMES.append('VTKSphereType' )

#--------------------------------------------------------------
class VTKSpheres(Node, BVTK_Node):

    bl_idname = 'VTKSpheresType'
    bl_label  = 'vtkSpheres'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['Centers', 'Radii', 'Transform'], ['self']) 
    
add_class( VTKSpheres )        
TYPENAMES.append('VTKSpheresType' )

#--------------------------------------------------------------
class VTKSuperquadric(Node, BVTK_Node):

    bl_idname = 'VTKSuperquadricType'
    bl_label  = 'vtkSuperquadric'
    
    m_Toroidal: bpy.props.BoolProperty(name='Toroidal', default=True, update=BVTK_Node.outdate_vtk_status)
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    m_PhiRoundness: bpy.props.FloatProperty(name='PhiRoundness', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_Size: bpy.props.FloatProperty(name='Size', default=0.5, update=BVTK_Node.outdate_vtk_status)
    m_ThetaRoundness: bpy.props.FloatProperty(name='ThetaRoundness', default=1.0, update=BVTK_Node.outdate_vtk_status)
    m_Thickness: bpy.props.FloatProperty(name='Thickness', default=0.3333, update=BVTK_Node.outdate_vtk_status)
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=BVTK_Node.outdate_vtk_status)
    m_Scale: bpy.props.FloatVectorProperty(name='Scale', default=[1.0, 1.0, 1.0], size=3, update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_Toroidal','m_ObjectName','m_PhiRoundness','m_Size','m_ThetaRoundness','m_Thickness','m_Center','m_Scale',]
    def m_connections( self ):
        return ([], [], ['Transform'], ['self']) 
    
add_class( VTKSuperquadric )        
TYPENAMES.append('VTKSuperquadricType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'ImplicitFunc', 'ImplicitFunc', items=menu_items) )