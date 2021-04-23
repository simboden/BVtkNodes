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
from .cache import BVTKCache

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
        vtk_obj = BVTKCache.get_vtk_obj(self.node_id)
        if vtk_obj and len(self.custom_code) > 0:
            for x in self.custom_code.splitlines():
                if x.startswith("#"):
                    continue
                cmd = 'vtk_obj.' + x
                l.debug("%s run %r" % (vtk_obj.__vtkname__, cmd))
                exec(cmd, globals(), locals())

        # Call Update() but only if all inputs have been connected, to
        # avoid vtkCompositeDataPipeline failure for request: vtkInformation.
        # Note: This does not work if node does not require all input connections.
        # In that case you need to prepare custom apply_properties().

        # TODO: OK to remove? apply_properties() is checking for connections.

        if hasattr(vtk_obj, "Update"):
            num_missing_connections = len(self.get_input_socket_names()) - vtk_obj.GetTotalNumberOfInputConnections()
            if num_missing_connections > 0 :
                self.ui_message = "Missing %d VTK input connection(s)" % num_missing_connections
                return 'error'
            else:
                try:
                    vtk_obj.Update()
                except:
                    self.ui_message = "Failed to run Update() for VTK object"
                    value = 'error'

        # Finally call custom finishing function (optional).
        # Added up-to-date requirement so that error does not
        # get overwritten. OK?
        if hasattr(self, "apply_properties_post") and value == 'up-to-date':
            value = self.apply_properties_post()
        return value
    return run_custom_code_wrapper

# -----------------------------------------------------------------------------
# base class for all BVTK_Nodes
#
# General implementation for VTK nodes below. Special nodes likely
# need to provide own versions of following methods:
# - m_properties() - names of node properties
# - m_connections() - names of node connections
# - draw_buttons() - node UI contents
# - init_vtk() - creation and initialization of VTK object
# - apply_inputs() - update input connections to VTK object
# - apply_properties_post()- special function to run for setting properties
#                            for special nodes (optional)
# -----------------------------------------------------------------------------

class BVTK_Node:
    '''Base class for VTK nodes and special nodes'''

    node_id: bpy.props.IntProperty(
        name="Node ID Number",
        description="Node ID Number for mapping VTK objects in BVTKcache",
        default=0,
    )
    connected_input_names: bpy.props.StringProperty(
        name="Names of Connected Input Nodes",
        description="Names of connected input nodes, used for triggering status change in update()",
        default="",
    )
    ui_message: bpy.props.StringProperty(
        name="Result Message",
        description="Latest Result Message from Node Update, Information for User",
        default="",
    )
    vtk_status: bpy.props.EnumProperty(
        name="VTK Status",
        description="Status of BVTK node",
        items={
            # no status information
            ('none', 'none', 'none', 0),

            # VTK object exists but no values / commands for it has been run yet
            ('initialized', 'initialized', 'initialized', 1),

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

        vtk_obj = self.init_vtk()
        BVTKCache.map_node(self, vtk_obj) # Add VTK object to cache
        l.debug("Init done for node: %s, id #%d" % (self.name, self.node_id))

#    def reset_vtkobj(self, update_id):
#        '''Resets node's vtkobj'''
#        update_necessary = BVTKCache.update_necessary(self, update_id)
#        BVTKCache.update_id(self, update_id)
#        if update_necessary:
#            BVTKCache.init_vtkobj(self)

    def init_vtk(self):
        '''Initialize and return a VTK object for the node.
        This is a general implementation for VTK nodes.
        Special nodes need to implement their own initialization.
        '''
        vtk_class = getattr(vtk, self.bl_label, None)
        if vtk_class is None:
            raise Exception("Bad VTK class name " + self.bl_label)
        vtk_obj = vtk_class()
        if not vtk_obj:
            raise Exception("Could not create " + self.bl_label)
        self.vtk_status = 'initialized'
        l.debug("Init VTK done for node: %s, id #%d" % (self.name, self.node_id))
        return vtk_obj

    def free(self):
        '''Clean up node information upon node removal.
        '''
        BVTKCache.unmap_node(self)

    @show_custom_code
    def draw_buttons(self, context, layout):
        '''Show properties in the node. General implementation for VTK nodes.
        '''
        # Debug
        row = layout.row()
        row.label(text="node_id #%d: %r" % (self.node_id, str(self.vtk_status)))

        # Show and reset message if any
        if len(self.ui_message)>0:
            box = layout.box()
            for line in self.ui_message.split('\n'):
                row = box.row()
                row.label(text=line)

        # Get properties and show visible ones
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if not hasattr(self, "b_properties") or self.b_properties[i]:
                layout.prop(self, m_properties[i])

        # Write button for writer nodes
        if self.bl_idname.endswith('WriterType'):
            layout.operator('node.bvtk_node_write').id = self.node_id

        # Update button is shown when there is something to update
        if self.vtk_status != 'up-to-date':
            row = layout.row()
            row.operator("node.bvtk_node_update").node_path = node_path(self)

    @run_custom_code
    def apply_properties(self):
        '''Set properties from node to VTK object, and update the VTK object.
        Return appropriate vtk_status according to success of update.
        General implementation for both VTK and special nodes.
        '''

        # For all nodes: Do nothing if some of the inputs are not connected.
        # Is this OK, or are there VTK nodes which fail because of this?
        namelist = [link.to_socket.name for socket in self.inputs for link in socket.links]
        missing_inputs = ""
        for input in self.get_input_socket_names():
            l.debug("testing %r in %r" % (input, namelist))
            if input not in namelist:
                missing_inputs += input + " "
        if len(missing_inputs) > 0:
            self.ui_message = "Missing input connection(s): " + missing_inputs
            return 'error'

        # Stop here if there is a custom post routine, meaning this is a special node
        if hasattr(self, "apply_properties_post"):
            return 'up-to-date'

        # Require an object exists in cache
        vtk_obj = BVTKCache.get_vtk_obj(self.node_id)
        if not vtk_obj:
            self.ui_message = "Internal Error: No VTK object found in cache"
            return 'error'

        m_properties = self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            # Skip setting any empty values
            inputval = getattr(self, x)
            if len(str(inputval)) == 0:
                continue
            # SetXFileName(Y) only if attribute is a string
            if 'FileName' in x and isinstance(inputval, str):
                value = os.path.realpath(bpy.path.abspath(inputval))
                cmd = 'vtk_obj.Set' + x[2:] + '(value)'
            # SetXToY()
            elif x.startswith('e_'):
                cmd = 'vtk_obj.Set'+x[2:]+'To'+inputval+'()'
            # SetX(self.Y)
            else:
                cmd = 'vtk_obj.Set'+x[2:]+'(self.'+x+')'

            # Run the command and stop if error occurs
            try:
                exec(cmd, globals(), locals())
            except:
                return 'error'

        # Everything was set successfully
        return 'up-to-date'

    def get_vtk_obj(self):
        '''Return only the VTK object of this node.
        '''
        vtk_obj = BVTKCache.get_vtk_obj(self.node_id)
        return vtk_obj

    def get_vtk_obj_and_connection(self, socketname='output'):
        '''Return existing cached VTK object and VTK output connection object
        for argument output socket name of this node. Assumes VTK
        object is up-to-date. General implementation for VTK nodes.
        '''

        vtk_obj = BVTKCache.get_vtk_obj(self.node_id)
        if not vtk_obj:
            return None, None

        # VTK Nodes are derived from vtkAlgorithm, which implements VTK connections
        if not isinstance(vtk_obj, vtk.vtkAlgorithm):
            raise Exception("not instance of vtkAlgorithm for #" + str(self.node_id))

        if socketname == 'output' or socketname == 'output 0':
            return vtk_obj, vtk_obj.GetOutputPort()
        elif socketname == 'output 1':
            return vtk_obj, vtk_obj.GetOutputPort(1)
        raise Exception("Not implemented connection for #" + str(self.node_id) + ": " + socketname)

    def apply_inputs(self):
        '''Set/update node input connections to this node's VTK object.
        This is called from get_vtk_output() during update.
        General implementation for VTK nodes.
        '''
        inputs, dummy1, extra_inputs, dummy2 = self.m_connections()
        vtk_obj = BVTKCache.get_vtk_obj(self.node_id)
        if not vtk_obj:
            return None

        # Regular vtkAlgorithms
        for i, socketname in enumerate(inputs):
            input_node, input_vtk_obj, vtk_connection = self.get_input_node_and_vtk_objects(socketname)
            if not input_node:
               vtk_obj.RemoveInputConnection(i, i)
               continue
            if not vtk_connection:
                raise Exception("Failed to get output connection from %r" % socketname)
            # Normal algorithms provide normal output
            if vtk_connection.IsA('vtkAlgorithmOutput'):
                vtk_obj.SetInputConnection(i, vtk_connection)
            # Special algorithms can use SetInputData
            elif input_vtk_obj.IsA('vtkDataObject'):
                vtk_obj.SetInputData(i, input_vtk_obj)
            else:
                raise Exception("Not implemented input type for #" + str(self.node_id) + ": " + str(type(vtk_obj)))

        # Extra connections (call method SetX(vtk_obj))
        for socketname in extra_inputs:
            raise Exception("WIP TODO extra_input:" + socketname)
            input_node, vtk_obj, dummy = self.get_input_node_and_vtk_objects(socketname)
            if not input_node:
                continue
            if not vtk_obj:
                raise Exception("Failed to get output from" + socketname)
            cmd = 'vtk_obj.Set' + socketname + '( vtk_obj )'
            exec(cmd, globals(), locals())

    def get_input_node_and_vtk_objects(self, input_socket_name='input'):
        '''Return input node, it's VTK object and the VTK output connection of
        the node which is connected to this node's argument input socket name.
        '''
        input_node, from_socket_name = self.get_input_node_and_socketname(input_socket_name)
        if not input_node:
            return None, None, None
        vtk_obj, vtk_connection = input_node.get_vtk_obj_and_connection(from_socket_name)
        return input_node, vtk_obj, vtk_connection

    def get_input_node_and_socketname(self, input_socket_name='input'):
        '''Get one input node and it's output socket name using this nodes'
        input socket name.
        '''
        nodes, from_socket_names, to_socket_names = self.get_input_nodes_and_socketnames()
        for node, from_socket_name, to_socket_name in zip(nodes, from_socket_names, to_socket_names):
            if to_socket_name == input_socket_name:
                return node, from_socket_name
        return None, None

    def get_input_nodes(self):
        '''Return list of all input nodes.
        '''
        nodes, dummy1, dummy2 = self.get_input_nodes_and_socketnames()
        return nodes

    def get_input_nodes_and_socketnames(self):
        '''Return list of all input nodes of this node, node socket names in
        this node, and node socket names in input node.
        '''
        nodes = []
        from_socket_names = []
        to_socket_names = []
        # Get all input nodes
        for socket in self.inputs:
            for link in socket.links:
                nodes.append(link.from_node)
                from_socket_names.append(link.from_socket.name)
                to_socket_names.append(link.to_socket.name)
        return nodes, from_socket_names, to_socket_names

    def get_output_nodes(self):
        '''Return list of all output nodes from this node.
        '''
        output_nodes = []
        for socket in self.outputs:
            for link in socket.links:
                output_nodes.append(link.to_node)
        return output_nodes

    def copy(self, node):
        '''Copy setup from another node.
        '''
        self.node_id = 0 # Force node_id update in map_node()
        vtk_obj = self.init_vtk()
        BVTKCache.map_node(self, vtk_obj) # Add VTK object to cache
        if hasattr(self, 'copy_setup'):
            # some nodes need to set properties (such as color ramp elements)
            # after being copied
            self.copy_setup(node)
        l.debug("Copy done for node: %s, id #%d" % (self.name, self.node_id))

    def get_b(self):
        '''Get list of booleans to show/hide boolean properties.
        '''
        n_properties = len(self.b_properties)
        # If there are correct number of saved properties, return those
        if self.bl_idname in b_properties.b:
            saved_properties = b_properties.b[self.bl_idname]
            if len(saved_properties) == n_properties:
                return saved_properties
        # Otherwise return correct number of Trues (=show all properties by default)
        return [True] * n_properties

    def set_b(self, value):
        '''Set boolean property list and update boolean properties file.
        '''
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

    def outdate_vtk_status(self, context):
        '''Set node VTK status to out-of-date and notify downstream when a
        property value is changed in UI.
        '''
        update_mode = bpy.context.scene.bvtknodes_settings.update_mode
        if update_mode == 'update-current':
            self.vtk_status = 'out-of-date'
            self.update_vtk()
        else:
            self.notify_downstream(vtk_status='out-of-date')
        if update_mode == 'update-all':
            BVTKCache.update_all()


    def update(self):
        '''Update routine triggered on node UI topology changes (adding or
        removing nodes and links).
        '''
        # Check if connected input node names have changed. If yes,
        # then set VTK status to out-of-date and notify downstream.

        update_mode = bpy.context.scene.bvtknodes_settings.update_mode
        namelist = [[link.from_node.name for link in socket.links] for socket in self.inputs]
        names = str(namelist)
        if self.connected_input_names != names:
            self.connected_input_names = names
            self.apply_inputs()
            if update_mode == 'update-current':
                self.vtk_status = 'out-of-date'
                self.update_vtk()
            else:
                self.notify_downstream(vtk_status='out-of-date')
            if update_mode == 'update-all':
                BVTKCache.update_all()

    def notify_downstream(self, vtk_status='out-of-date', origin_node=True):
        '''Make status changes in downstream nodes, to advertise update made
        in this node.
        '''
        # Recursively call for downstream nodes
        for node in self.get_output_nodes():
            node.notify_downstream(vtk_status='out-of-date', origin_node=False)
        # For downstream nodes, out-of-date supercedes upstream-changed
        if self.vtk_status != 'out-of-date':
            self.vtk_status = 'upstream-changed'
        if origin_node:
            self.vtk_status = vtk_status

    def update_vtk(self):
        '''Recursively update upstream nodes and this node if not up-to-date.
        '''
        # Recursively call for upstream nodes
        for node in self.get_input_nodes():
            if node.vtk_status != 'up-to-date':
                node.update_vtk()

        # Do nothing if upstream was not successfully updated
        for node in self.get_input_nodes():
            if node.vtk_status != 'up-to-date':
                self.ui_message = "Can't update, upstream update failed."
                return 'out-of-date'

        # Remove old messages
        self.ui_message = ""

        # Update this node's properties to VTK object only if needed
        if self.vtk_status != 'up-to-date':
            self.vtk_status = 'updating'
            l.debug("Updating " + self.name)

            # This is the only point where apply_properties() is called
            new_status = self.apply_properties()

            if new_status == None:
                self.ui_message = "Node failure:\napply_properties() does not return a valid status string"
                new_status = 'error'
            self.notify_downstream(vtk_status=new_status)


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
