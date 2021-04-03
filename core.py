# <pep8 compliant>
# -----------------------------------------------------------------------------
# MODULES IMPORT 
# -----------------------------------------------------------------------------

# Set up logging of messages using Python logging
# Logging is nicely explained in:
# https://code.blender.org/2016/05/logging-from-python-code-in-blender/
# To see debug messages, configure logging in file
# $HOME/.config/blender/{version}/scripts/startup/setup_logging.py
# add there something like:
# import logging
# logging.basicConfig(format='%(funcName)s: %(message)s', level=logging.DEBUG)
import logging
l = logging.getLogger(__name__)

import bpy
from bpy.types import NodeTree, Node, NodeSocket
from nodeitems_utils import NodeCategory, NodeItem
import os
import vtk
import functools # for decorators

from . import b_properties # Boolean properties
b_path = b_properties.__file__ # Boolean properties config file path
from .update import *
# from .cache import BVTKCache

# -----------------------------------------------------------------------------
# BVTK_NodeTree
# -----------------------------------------------------------------------------

class BVTK_NodeTree(NodeTree):
    '''BVTK Node Tree'''
    bl_idname = 'BVTK_NodeTreeType'
    bl_label  = 'BVTK Node Tree'
    bl_icon   = 'COLOR_BLUE'


# -----------------------------------------------------------------------------
# Custom socket type
# -----------------------------------------------------------------------------

class BVTK_NodeSocket(NodeSocket):
    '''BVTK Node Socket'''
    bl_idname = 'BVTK_NodeSocketType'
    bl_label  = 'BVTK Node Socket'
    
    def draw(self, context, layout, node, txt):
        layout.label(text=txt)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


# -----------------------------------------------------------------------------
# Custom Code decorators
# -----------------------------------------------------------------------------

def show_custom_code(func):
    '''Decorator to show custom code in nodes. Used in draw_buttons().'''
    @functools.wraps(func)
    def show_custom_code_wrapper(self, context, layout):
        # Call function first
        value = func(self, context, layout)
        # Then show Custom Code
        row = layout.row()
        if self.expanded:
            row.label(text="Custom Code:")
        elif len(self.custom_code) > 0:
            pseudo_code = self.custom_code[:self.custom_code.find('(')]
            row.label(text="Custom Code: "+pseudo_code+"...")
        else:
            row.label(text="Custom Code: None")
        # Expand button
        # TODO: Make proper expandable menu with triangle icon and text
        row.prop(self, "expanded",
            icon="HIDE_OFF" if self.expanded else "HIDE_ON",
            icon_only=True, emboss=False, expand=True)
        
        if self.expanded:
            col = layout.column(align=True)
            row = col.row()
            op = row.operator('node.bvtk_custom_code_edit', text="Edit", icon="TEXT")
            op.node_id = self.node_id # Set node id in operator
            op = row.operator('node.bvtk_custom_code_save', text="Save", icon="FILE_TICK")
            op.node_id = self.node_id # Set node id in operator
            if len(self.custom_code) > 0:
                    box = layout.box()
                    col = box.column()
                    for text in self.custom_code.splitlines():
                        row = col.row()
                        row.label(text=text)
        return value
    return show_custom_code_wrapper


def run_custom_code(func):
    '''Decorator to run custom code. Used in apply_properties().'''
    @functools.wraps(func)
    def run_custom_code_wrapper(self):
        # Call function first
        value = func(self)
        # Then run Custom Code
        if self.vtk_obj and len(self.custom_code) > 0:
            for x in self.custom_code.splitlines():
                if x.startswith("#"):
                    continue
                cmd = 'self.vtk_obj.' + x
                l.debug("%s run %r" % (vtk_obj.__vtkname__, cmd))
                exec(cmd, globals(), locals())
        return value
    return run_custom_code_wrapper

# -----------------------------------------------------------------------------
# base class for all BVTK_Nodes
# -----------------------------------------------------------------------------

class BVTK_Node:
    '''Base class for VTK nodes and special nodes'''

    # node's VTK object (or None)
    vtk_obj: object # This does not work
    # vtk_obj: bpy.props.PointerProperty(type=object) # This is not allowed

    vtk_status: bpy.props.EnumProperty(
        name="VTK Status",
        description="Status of BVTK node",
        items={
            # no status information
            ('none', 'none', 'none', 0),

            # VTK object exists but no values / commands for it has been run yet
            ('uninitialized', 'uninitialized', 'uninitialized', 1),

            # setting a value/running a command has failed, execution has been stopped
            ('error', 'error', 'error', 2),

            # a change has been made to an upstream node, may need to update
            ('upstream-changed', 'upstream-changed', 'upstream-changed', 3),

            # a change has been made to this node, may need to run update
            ('out-of-date', 'out-of-date', 'out-of-date', 4),

            # input node(s) are running an update
            ('waiting-for-upstream', 'waiting-for-upstream', 'waiting-for-upstream', 5),

            # setting values / running commands for this node
            ('updating', 'updating', 'updating', 6),

            # finished running commands for this node
            ('up-to-date', 'up-to-date', 'up-to-date', 7),
        },
        default='none',
    )
    custom_code: bpy.props.StringProperty(
        name="Custom Code",
        description="Custom Python Code to Run for This Node's VTK Object",
        default="",
        maxlen=0,
    )
    expanded: bpy.props.BoolProperty(
        name="Show Code",
        description="Boolean to Show/Hide Custom Code Panel",
        default=False,
    )

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'BVTK_NodeTreeType'

    def m_properties(self):
        '''Return list of node specific property names.
        Implement this for each node class.
        '''
        return []

    def m_connections(self):
        '''Return lists of node specific connection names:
        input socket names, output socket names, extra inputs, and extra outputs.
        Implement this for each node class.
        '''
        return([], [], [], [])

    def get_input_socket_names(self):
        '''Return input socket names from m_connections.
        '''
        m_connections = self.m_connections()
        return m_connections[0]

    def init(self, context):
        '''Create and initialize a new BVTK node.
        '''
        # Node properties
        self.width = 200
        self.use_custom_color = True
        self.color = 0.5, 0.5, 0.5

        # Create sockets to node
        inputs, outputs, extra_inputs, extra_outputs = self.m_connections()
        inputs.extend(extra_inputs)
        outputs.extend(extra_outputs)
        for x in inputs:
            self.inputs.new('BVTK_NodeSocketType', x)
        for x in outputs:
            self.outputs.new('BVTK_NodeSocketType', x)

        self.vtk_obj = None
        self.init_vtk()
        l.debug("initialized " + str(self))


#    def reset_vtkobj(self, update_id):
#        '''Resets node's vtkobj'''
#        update_necessary = BVTKCache.update_necessary(self, update_id)
#        BVTKCache.update_id(self, update_id)
#        if update_necessary:
#            BVTKCache.init_vtkobj(self)

    def init_vtk(self):
        '''Initialize a VTK object for the node and set initial status.
        This is a general implementation for VTK nodes.
        Special nodes need to implement their own initialization.
        '''
        if hasattr(self, 'vtk_obj'):
            del self.vtk_obj
        vtk_class = getattr(vtk, self.bl_label, None)
        l.debug("initializing " + self.bl_label)
        if vtk_class is None:
            self.vtk_status = 'none'
            l.error("Bad VTK class name " + self.bl_label)
            return None
        vtk_obj = vtk_class()
        if not vtk_obj:
            raise Exception("Could not create" + self.bl_label)
        self.vtk_obj = vtk_obj
        self.vtk_status = 'uninitialized'

    @classmethod
    def init_vtk_for_existing_nodes(cls):
        '''Call init_vtk for all nodes in all BVTK node trees.
        Called after loading Blender file to initialize VTK objects.
        '''
        for nodetree in bpy.data.node_groups:
            if not nodetree.bl_idname == 'BVTK_NodeTreeType':
                continue
            for node in nodetree.nodes:
                node.init_vtk()

    def free(self):
        '''Function to delete VTK object and clean up node on removal.
        '''
        if hasattr(self, 'vtk_obj'):
            del self.vtk_obj

    @show_custom_code
    def draw_buttons(self, context, layout):
        '''Show properties in the node. General implementation for VTK nodes.
        '''
        # Debug
        row = layout.row()
        row.label(text="status: " + str(self.vtk_status))

        # Get properties and show visible ones
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                layout.prop(self, m_properties[i])

        # Write button for writer nodes
        if self.bl_idname.endswith('WriterType'):
            layout.operator('node.bvtk_node_write').id = self.node_id

    @run_custom_code
    def apply_properties(self):
        '''Set properties from node to VTK object based on property name.
        General implementation for VTK nodes.
        '''
        if not self.vtk_obj:
            raise Exception("No vtk_obj for" + self.bl_label)

        m_properties = self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            # Skip setting any empty values
            inputval = getattr(self, x)
            if len(str(inputval)) == 0:
                continue
            # SetXFileName(Y) only if attribute is a string
            if 'FileName' in x and isinstance(inputval, str):
                value = os.path.realpath(bpy.path.abspath(inputval))
                cmd = 'self.vtk_obj.Set' + x[2:] + '(value)'
            # SetXToY()
            elif x.startswith('e_'):
                cmd = 'self.vtk_obj.Set'+x[2:]+'To'+inputval+'()'
            # SetX(self.Y)
            else:
                cmd = 'self.vtk_obj.Set'+x[2:]+'(self.'+x+')'
            exec(cmd, globals(), locals())

    def get_vtk_obj_and_connection(self, socketname='output'):
        '''Return VTK object and VTK output connection object for argument
        output socket name of this node. General implementation for VTK nodes.
        '''
        # Apply inputs and properties if needed. TODO: Extract to own function.
        if self.vtk_status != 'up-to-date':
            self.vtk_status = 'updating'
            self.apply_inputs()
            self.apply_properties()
            self.vtk_status = 'up-to-date'

        vtk_obj = self.vtk_obj
        if not vtk_obj:
            raise Exception("No vtk_obj" + self.bl_label)

        # VTK Nodes are derived from vtkAlgorithm, which implements VTK connections
        if not isinstance(vtk_obj, vtk.vtkAlgorithm):
            raise Exception("not instance of vtkAlgorithm:" + self.bl_label)

        # Verify number of input connections match VTK input connection count
        if not len(self.get_input_socket_names()) == vtk_obj.GetTotalNumberOfInputConnections():
            raise Exception("input connections don't match:" + self.bl_label)

        if socketname == 'output' or socketname == 'output 0':
            return vtk_obj, vtk_obj.GetOutputPort()
        elif socketname == 'output 1':
            return vtk_obj, vtk_obj.GetOutputPort(1)
        raise Exception("Not implemented connection:" + socketname)

    def apply_inputs(self):
        '''Set/update node input connections to this node's VTK object.
        This is called from get_vtk_output() during update.
        General implementation for VTK nodes.
        '''
        inputs, dummy1, extra_inputs, dummy2 = self.m_connections()

        # Regular vtkAlgorithms
        for i, socketname in enumerate(inputs):
            input_node, vtk_obj, vtk_connection = self.get_input_node_and_vtk_objects(socketname)
            if not vtk_connection:
                raise Exception("Failed to get output connection from" + socketname)
            if vtk_obj.IsA('vtkAlgorithmOutput'):
                vtk_obj.SetInputConnection(i, vtk_connection)
            else:
                # needed for custom filter, TODO: remove
                vtk_obj.SetInputData(i, vtk_connection)

        # Extra connections (call method SetX(vtk_obj))
        for socketname in extra_inputs:
            raise Exception("WIP TODO extra_input:" + socketname)
            input_node, vtk_obj, dummy = self.get_input_node_and_vtk_objects(socketname)
            if not vtk_obj:
                raise Exception("Failed to get output from" + socketname)
            cmd = 'vtk_obj.Set' + socketname + '( vtk_obj )'
            exec(cmd, globals(), locals())

    def get_input_node_and_vtk_objects(self, input_socket_name='input'):
        '''Return input node, it's VTK object and the VTK output connection of
        the node which is connected to this node's argument input socket name.
        '''
        input_node, socketname = self.get_input_node_and_socketname(input_socket_name)
        vtk_obj, vtk_connection = input_node.get_vtk_output(socketname)
        return input_node, vtk_obj, vtk_connection

    def get_input_node_and_socketname(self, input_socket_name='input'):
        '''Get one input node and it's output socket name using this nodes'
        input socket name.
        '''
        nodes, socket_names = self.get_input_nodes_and_socketnames()
        for node, socket_name in zip(nodes, socket_names):
            if node.name == input_socket_name:
                return node, socket_name
        return None, None

    def get_input_nodes_and_socketnames(self):
        '''Return list of all input nodes and each input node's output socket
        names leading to this node.
        '''
        nodes = []
        socket_names = []
        # Get all input nodes
        for input in self.inputs:
            nodes.append(input)
            if len(input.links) != 1:
                raise Exception("Number of inputs != 1" + self.bl_label)
            socket_name = input.links[0].from_socket.name
            socket_names.append(socket_name)
        return nodes, socket_names

    def get_vtkobj(self):
        '''Accessor of nodes vtkobj from cache'''
        raise Exception("shouldn't be called")
        return BVTKCache.get_vtkobj(self)

    def reset_vtkobj(self):
        '''Resets node's vtkobj'''
        raise Exception("shouldn't be called")
        return BVTKCache.init_vtkobj(self)

    def copy(self, node):
        '''Copies setup from another node'''
        raise Exception("TODO")
        self.node_id = 0
        BVTKCache.check_cache()
        if hasattr(self, 'copy_setup'):
            # some nodes need to set properties (such as color ramp elements)
            # after being copied
            self.copy_setup(node)

    def get_b(self):
        '''Get list of booleans to show/hide boolean properties'''
        n_properties = len(self.b_properties)
        # If there are correct number of saved properties, return those
        if self.bl_idname in b_properties.b:
            saved_properties = b_properties.b[self.bl_idname]
            if len(saved_properties) == n_properties:
                return saved_properties
        # Otherwise return correct number of Trues (=show all properties by default)
        return [True] * n_properties

    def set_b(self, value):
        '''Set boolean property list and update boolean properties file'''
        b_properties.b[self.bl_idname] = [v for v in value]
        bpy.ops.node.select_all(action='SELECT')
        bpy.ops.node.select_all(action='DESELECT')

        # Write sorted b_properties.b dictionary
        # Note: lambda function used to force sort on dictionary key
        txt="b={"
        for key, value in sorted(b_properties.b.items(), key=lambda s: str.lower(s[0])):
            txt += " '" + key + "': " + str(value) + ",\n"
        txt += "}\n"
        open(b_path,'w').write(txt)



# -----------------------------------------------------------------------------
# VTK Node Write
# -----------------------------------------------------------------------------
update_id = 0
class BVTK_OT_NodeWrite(bpy.types.Operator):
    '''Operator to call VTK Write() for a node'''
    bl_idname = "node.bvtk_node_write"
    bl_label = "Write"

    id: bpy.props.IntProperty()

    def execute(self, context):
        global update_id
        update_id += 1
        BVTKCache.check_cache()
        node = BVTKCache.get_node(self.id)  # TODO: change node_id to node_path?
        if node:
            def cb():
                node.get_vtkobj().Write()
            Update(node, cb, update_id)

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
add_class(BVTK_NodeTree)
add_class(BVTK_NodeSocket)
add_ui_class(BVTK_OT_NodeWrite)

# -----------------------------------------------------------------------------
# VTK Node Category
# -----------------------------------------------------------------------------

class BVTK_NodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'BVTK_NodeTreeType'

CATEGORIES = []            


# -----------------------------------------------------------------------------
# Debug utilities
# -----------------------------------------------------------------------------

def ls(o):
    l.debug('\n'.join(sorted(dir(o))))


def print_cls(obj):
    l.debug( "------------------------------" )
    l.debug( "Class = " + obj.__class__.__name__ )
    l.debug( "------------------------------" )
    for m in sorted(dir(obj)):
        if not m.startswith('__'):
            attr = getattr(obj,m)
            rep = str(attr)
            if len(rep) > 100:
                rep = rep[:100] + '  [...]'
            l.debug (m.ljust(30) + "=" + rep)


def print_nodes(): 
    l.debug("maxid = " + str(NodesMaxId))
    for nt in bpy.data.node_groups:
        if nt.bl_idname == "BVTK_NodeTreeType":
            l.debug( "tree " + nt.name)
            for n in nt.nodes:
                if get_vtkobj(n) is None:
                    x = ""
                else:
                    x = "VTK object"
                l.debug("node " + str(n.node_id) + ": " + n.name.ljust(30,' ') + x)


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
    return # No need for this in Blender 2.8? Remove function when certain.
    screen = bpy.context.screen
    if(screen):
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        # This updates viewport in Blender 2.79, not sure why
                        # space.viewport_shade = space.viewport_shade
                        continue


def node_path(node):
    '''Return node path of a node'''
    return 'bpy.data.node_groups['+repr(node.id_data.name)+'].nodes['+repr(node.name)+']'


def node_prop_path(node, propname):
    '''Return node property path'''
    return node_path(node)+'.'+propname

def assert_bvtk(condition, message):
    if not condition:
        raise(AssertionError(message))
