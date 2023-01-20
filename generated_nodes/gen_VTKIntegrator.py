# Generated definitions for VTK class group: Integrator
# VTK version: 9.2.2

from ..core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKRungeKutta2(Node, BVTK_Node):

    bl_idname = 'VTKRungeKutta2Type'
    bl_label  = 'vtkRungeKutta2'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['FunctionSet'], ['self']) 
    
add_class( VTKRungeKutta2 )        
TYPENAMES.append('VTKRungeKutta2Type' )

#--------------------------------------------------------------
class VTKRungeKutta4(Node, BVTK_Node):

    bl_idname = 'VTKRungeKutta4Type'
    bl_label  = 'vtkRungeKutta4'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['FunctionSet'], ['self']) 
    
add_class( VTKRungeKutta4 )        
TYPENAMES.append('VTKRungeKutta4Type' )

#--------------------------------------------------------------
class VTKRungeKutta45(Node, BVTK_Node):

    bl_idname = 'VTKRungeKutta45Type'
    bl_label  = 'vtkRungeKutta45'
    
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=BVTK_Node.outdate_vtk_status)
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties( self ):
        return ['m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['FunctionSet'], ['self']) 
    
add_class( VTKRungeKutta45 )        
TYPENAMES.append('VTKRungeKutta45Type' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( BVTK_NodeCategory( 'Integrator', 'Integrator', items=menu_items) )