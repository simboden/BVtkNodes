# <pep8 compliant>
# -----------------------------------------------------------------------------
# MODULES IMPORT 
# -----------------------------------------------------------------------------
import bpy
from bpy.types import NodeTree, Node, NodeSocket
from nodeitems_utils import NodeCategory, NodeItem
import os

import vtk
   
from . import b_properties # Boolean properties
b_path = b_properties.__file__ # Boolean properties config file path
from .update import *

# -----------------------------------------------------------------------------
# Node Cache and related functions
# -----------------------------------------------------------------------------
NodesMaxId = 1   # Maximum node id number. 0 means invalid
NodesMap   = {}  # node_id -> node
VTKCache   = {}  # node_id -> vtkobj


def node_created(node):
    '''Add node to Node Cache. Called from node.init() and from
    check_cache. Give the node a unique node_id, then add it in
    NodesMap, and finally instantiate it's vtkobj and store it in
    VTKCache.
    '''
    global NodesMaxId, NodesMap, VTKCache  

    # Ensure each node has a node_id
    if node.node_id == 0:
        node.node_id = NodesMaxId
        NodesMaxId += 1
        NodesMap[node.node_id] = node
        VTKCache[node.node_id] = None

    # create the node vtk_obj if needed
    if node.bl_label.startswith('vtk'):
        vtk_class = getattr(vtk, node.bl_label, None)
        if vtk_class is None:
            print("VTKNodeData: - bad classname", node.bl_label ) 
            return
        VTKCache[node.node_id] = vtk_class() # make an instance of node.vtk_class

        # setting properties tips
        # if hasattr(node,'m_properties'):
        #     for m_property in node.m_properties():
        #         prop=getattr(getattr(bpy.types, node.bl_idname), m_property)
        #         prop_doc=getattr(node.get_vtkobj(), m_property.replace('m_','Set'), 'Doc not found')
        #
        #         if prop_doc!='Doc not found':
        #             prop_doc=prop_doc.__doc__
        #
        #         s=''
        #         for a in prop[1].keys():
        #             if a!='attr' and a!='description':
        #                 s+=a+'='+repr(prop[1][a])+', '
        #
        #         exec('bpy.types.'+node.bl_idname+'.'+m_property+'=bpy.props.'+prop[0].__name__+'('+s+' description='+repr(prop_doc)+')')
    
    # print( "node_created", node.bl_label, node.node_id )


def node_deleted(node):
    '''Remove node from Node Cache. To be called from node.free().
    Remove node from NodesMap and its vtkobj from VTKCache
    '''
    global NodesMap, VTKCache  
    if node.node_id in NodesMap:
        del NodesMap[node.node_id]

    if node.node_id in VTKCache:
        obj = VTKCache[node.node_id]
        # if obj: 
        #     obj.UnRegister(obj)  # vtkObjects have no Delete in Python -- maybe is not needed
        del VTKCache[node.node_id]
    # print("node_deleted", node.bl_label, node.node_id)


def get_node(node_id):
    '''Get node corresponding to node_id.'''
    node = NodesMap.get(node_id)
    if node is None:
        print("get_node - node not found, node_id=", node_id)
    return node


def get_vtkobj(node):
    '''Get the VTK object associated to a node'''
    if node is None:
        print("get_vtkobj - bad node")
        return None

    if not node.node_id in VTKCache:
        # print("get_vtkobj - node_id not in cache", node.node_id)
        return None

    return VTKCache[node.node_id]


def init_cache():
    '''Initialize Node Cache'''
    global NodesMaxId, NodesMap, VTKCache  
    print("init_cache")
    NodesMaxId = 1
    NodesMap   = {}
    VTKCache   = {}
    check_cache()
    print_nodes()


def check_cache():
    '''Rebuild Node Cache. Called by all operators.
    TODO: Check this description:
    If an operator is called a button exist,
    if at the same time NodesMaxId == 1.
    This means that the Cache is out of sync (this happen after reloading addons).
    We must rebuild the Cache, and the operator must be interrupted.
    ( the next try will work )
    '''
    global NodesMaxId

    # After F8 or FileOpen VTKCache is empty and NodesMaxId == 1
    # any previous node_id must be invalidated
    if NodesMaxId == 1:
        for nt in bpy.data.node_groups:
            if nt.bl_idname == 'VTKTreeType':
                for n in nt.nodes:
                    n.node_id = 0

    # For each node check if it has a node_id
    # and if it has a vtk_obj associated
    for nt in bpy.data.node_groups:
        if nt.bl_idname == 'VTKTreeType':
            for n in nt.nodes:
                if get_vtkobj(n) == None or n.node_id == 0:
                    node_created(n)


# -----------------------------------------------------------------------------
# VTKTree
# -----------------------------------------------------------------------------

class VTKTree(NodeTree):
    '''VTK Node Tree'''         # description string - used for tooltip
    bl_idname = 'VTKTreeType'   # typename string - defaults to class name
    bl_label  = 'VTK'           # label
    bl_icon   = 'COLOR_RED'     # icon


# -----------------------------------------------------------------------------
# Custom socket type
# -----------------------------------------------------------------------------

class VTKSocket(NodeSocket):
    '''VTK Socket'''            # description / tooltip
    bl_idname = 'VTKSocketType' # typename
    bl_label  = 'vtk Socket'    # label
    
    def draw(self, context, layout, node, text):
        layout.label(text)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


# -----------------------------------------------------------------------------
# base class for all VTKNodes
# -----------------------------------------------------------------------------

class VTKNode:
    
    node_id = bpy.props.IntProperty(default=0)

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'VTKTreeType'

    def free(self):
        node_deleted(self)

    def get_output(self, socketname):
        '''Get output object. Return an object depending on socket
        name. Used to simplify custom node usage such as info
        node and custom filter.
        '''
        vtkobj = self.get_vtkobj()
        if not vtkobj:
            return None
        if socketname == 'self':
            return vtkobj
        if socketname == 'output' or socketname == 'output 0':
            return vtkobj.GetOutputPort()
        if socketname == 'output 1':
            return vtkobj.GetOutputPort(1)
        else:
            print('bad output link name:', '"' + socketname + '"')
            return None
        # TODO: handle output 2,3,....

    def get_input_nodes(self, name):
        '''Return inputs of a node. Name argument specifies the type of inputs: 
        'self'                 -> input_node.get_vtkobj()
        'output' or 'output 0' -> get_vtkobj().getOutputPort()
        'output x'             -> get_vtkobj().getOutputPort(x)
        '''
        if name not in self.inputs:
            return []
        input = self.inputs[name]
        if len(input.links) < 1:  # is_linked could be true even with 0 links
            return []
        nodes = []
        for link in input.links:
            input_node = link.from_node
            socket_name = link.from_socket.name
            if not input_node:
                continue
            nodes.append((input_node, input_node.get_output(socket_name)))
        return nodes

    def get_input_node(self, *args):
        '''Return input of a node'''
        nodes = self.get_input_nodes(*args)
        if nodes:
            return nodes[0]
        return (0,0)

    def get_vtkobj(self):
        '''Shortcut to get vtkobj'''
        return get_vtkobj(self)

    def draw_buttons(self, context, layout):
        '''Draw button'''
        m_properties=self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                layout.prop(self, m_properties[i])
        if self.bl_idname.endswith('WriterType'):
            layout.operator('vtk.node_write').id = self.node_id

    def copy(self, node):
        '''Copies setup from another node'''
        self.node_id = 0
        check_cache()
        if hasattr(self, 'copy_setup'):
            # some nodes need to set properties (such as color ramp elements)
            # after being copied
            self.copy_setup(node)

    def apply_properties(self, vtkobj):
        '''Sets properties from node to vtkobj based on property name'''
        m_properties=self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            # SetXFileName(Y)
            if 'FileName' in x:
                value = os.path.realpath(bpy.path.abspath(getattr(self, x)))
                cmd = 'vtkobj.Set' + x[2:] + '(value)'
            # SetXToY()
            elif x.startswith('e_'):
                value = getattr( self, x )
                cmd = 'vtkobj.Set'+x[2:]+'To'+value+'()'
            # SetX(self.Y)
            else:
                cmd = 'vtkobj.Set'+x[2:]+'(self.'+x+')'
            exec(cmd, globals(), locals())

    def input_nodes(self):
        '''Return input nodes'''
        nodes = []
        for input in self.inputs:
            for link in input.links:
                nodes.append(link.from_node)
        return nodes

    def apply_inputs(self, vtkobj):
        '''Set node inputs/connections to vtkobj'''
        input_ports, output_ports, extra_input, extra_output = self.m_connections()
        for i, name in enumerate(input_ports):
            input_node, input_obj = self.get_input_node(name)
            if input_node:
                if vtkobj:
                    if input_obj.IsA('vtkAlgorithmOutput'):
                        vtkobj.SetInputConnection(i, input_obj)
                    else:
                        # needed for custom filter
                        vtkobj.SetInputData(i, input_obj)
        for name in extra_input:
            input_node, input_obj = self.get_input_node(name)
            if input_node:
                if vtkobj:
                    cmd = 'vtkobj.Set' + name + '( input_obj )'
                    exec(cmd, globals(), locals())

    def init(self, context):
        '''Initialize node'''
        self.width = 200
        self.use_custom_color = True
        self.color = 0.5,0.5,0.5
        check_cache()
        input_ports, output_ports, extra_input, extra_output = self.m_connections()
        input_ports.extend(extra_input)
        output_ports.extend(extra_output)
        for x in input_ports:
            self.inputs.new('VTKSocketType', x)
        for x in output_ports:
            self.outputs.new('VTKSocketType', x)
        # Some nodes need to set properties (such as link limit) after creation
        if hasattr(self, 'setup'):
            self.setup()

    def get_b(self):
        '''Get boolean property'''
        return b_properties.b[self.bl_idname]

    def set_b(self, value):
        '''Set boolean property a value and update boolean properties file'''
        b_properties.b[self.bl_idname] = [v for v in value]
        bpy.ops.node.select_all(action='SELECT')
        bpy.ops.node.select_all(action='DESELECT')
        open(b_path,'w').write('b='+str(b_properties.b).replace('],','],\n'))


# -----------------------------------------------------------------------------
# VTK Node Write
# -----------------------------------------------------------------------------

class VTKNodeWrite(bpy.types.Operator):
    '''Operator to call VTK Write() for a node'''
    bl_idname = "vtk.node_write"
    bl_label = "write"

    id = bpy.props.IntProperty()

    def execute(self, context):
        check_cache()
        node = get_node(self.id)  # TODO: change node_id to node_path
        if node:
            def cb():
                node.get_vtkobj().Write()
            Update(node, cb)

        return {'FINISHED'}


# -----------------------------------------------------------------------------
# Registering
# -----------------------------------------------------------------------------

CLASSES = {}  # dictionary of classes is used to allow class overriding
UI_CLASSES = []

def add_class(obj):
    CLASSES[obj.bl_idname]=obj

def add_ui_class(obj):
    UI_CLASSES.append(obj)

def check_b_properties():
    '''Sets all boolean properties to True, unless correct number of properties
    is specified in b_properties
    '''
    for obj in CLASSES.values():
        if hasattr(obj, 'm_properties') and hasattr(obj, 'b_properties'):
            np = len(obj.m_properties(obj))
            name = obj.bl_idname
            b = b_properties.b
            if (not name in b) or (name in b and len(b[name]) != np):
                b[name] = [True for i in range(np)]

# Register classes
add_class(VTKTree)
add_class(VTKSocket)
add_ui_class(VTKNodeWrite)


# -----------------------------------------------------------------------------
# VTK Node Category
# -----------------------------------------------------------------------------

class VTKNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'VTKTreeType'

CATEGORIES = []            


# -----------------------------------------------------------------------------
# Debug utilities
# -----------------------------------------------------------------------------

def ls(o):
    print('\n'.join(sorted(dir(o))))


def print_cls(obj):
    print( "------------------------------" )
    print( "Class =",obj.__class__.__name__ )
    print( "------------------------------" )
    for m in sorted(dir(obj)):
        if not m.startswith('__'):
            attr = getattr(obj,m)
            rep = str(attr)
            if len(rep) > 100:
                rep = rep[:100] + '  [...]'
            print (m.ljust(30),"=",rep )


def print_nodes(): 
    print( "########################")
    print( "maxid = ", NodesMaxId )
    for nt in bpy.data.node_groups:
        if nt.bl_idname == "VTKTreeType":
            print( "## tree", nt.name)
            for n in nt.nodes:
                if get_vtkobj(n) is None:
                    x = "vtkObj:NO"
                else:
                    x = 'vtkobj:ok'
                print( "##    node", n.node_id, n.name.ljust(30,'.'), x )
    print( "########################")


# -----------------------------------------------------------------------------
# Useful help functions
# -----------------------------------------------------------------------------


def resolve_algorithm_output(vtkobj):
    '''Return vtkobj from vtkAlgorithmOutput'''
    if vtkobj.IsA('vtkAlgorithmOutput'):
        vtkobj = vtkobj.GetProducer().GetOutputDataObject(vtkobj.GetIndex())
    return vtkobj


def update_3d_view():
    '''Force update of 3D View'''
    screen = bpy.context.screen
    if(screen):
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        # This updates viewport, not sure why
                        space.viewport_shade = space.viewport_shade


def node_path(node):
    '''Return node path of a node'''
    return 'bpy.data.node_groups['+repr(node.id_data.name)+'].nodes['+repr(node.name)+']'


def node_prop_path(node, propname):
    '''Return node property path'''
    return node_path(node)+'.'+propname
