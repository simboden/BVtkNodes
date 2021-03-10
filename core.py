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
    def run_custom_code_wrapper(self, vtkobj):
        # Call function first
        value = func(self, vtkobj)
        # Then run Custom Code
        if len(self.custom_code) > 0:
            for x in self.custom_code.splitlines():
                if x.startswith("#"):
                    continue
                cmd = 'vtkobj.' + x
                l.debug("%s run %r" % (vtkobj.__vtkname__, cmd))
                exec(cmd, globals(), locals())
        return value
    return run_custom_code_wrapper

# -----------------------------------------------------------------------------
# base class for all BVTK_Nodes
# -----------------------------------------------------------------------------

class BVTK_Node:
    '''Base class for VTK Nodes'''

    node_id: bpy.props.IntProperty(default=0)

    custom_code: bpy.props.StringProperty(
        name="Custom Code",
        description="Custom Python Code to Run for This VTK Object." \
        + " Use semicolon without spaces as separator",
        default="",
        maxlen=0,
    )

    expanded: bpy.props.BoolProperty(name="Show Code", default=False)

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'BVTK_NodeTreeType'

    def free(self):
        '''Clean up node on removal
        '''
        BVTKCache.unmap_node(self)

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
        # Make sure object is of type vtkAlgorithm
        if isinstance(vtkobj, vtk.vtkAlgorithm):
            # Verify input connections have been initialized before giving any output ports
            if not len(self.m_connections()[0]) == vtkobj.GetTotalNumberOfInputConnections():
                return None    
            if socketname == 'output' or socketname == 'output 0':
                return vtkobj.GetOutputPort()
            if socketname == 'output 1':
                return vtkobj.GetOutputPort(1)
            # TODO: handle output 2,3,....

        l.error("bad output link name " + socketname)
        return None

    def get_input_nodes(self, name):
        '''Return inputs of a node. Name argument specifies the type of inputs: 
        'self'                 -> input_node.get_vtkobj()
        'output' or 'output 0' -> get_vtkobj().getOutputPort()
        'output x'             -> get_vtkobj().getOutputPort(x)
        '''
        if not name in self.inputs:
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
        '''Accessor of nodes vtkobj from cache'''
        return BVTKCache.get_vtkobj(self)

    def reset_vtkobj(self):
        '''Resets node's vtkobj'''
        return BVTKCache.init_vtkobj(self)

    @show_custom_code
    def draw_buttons(self, context, layout):
        '''Draw button'''
        m_properties=self.m_properties()
        for i in range(len(m_properties)):
            if self.b_properties[i]:
                layout.prop(self, m_properties[i])
        if self.bl_idname.endswith('WriterType'):
            layout.operator('node.bvtk_node_write').id = self.node_id

    def copy(self, node):
        '''Copies setup from another node'''
        self.node_id = 0
        BVTKCache.check_cache()
        if hasattr(self, 'copy_setup'):
            # some nodes need to set properties (such as color ramp elements)
            # after being copied
            self.copy_setup(node)

    @run_custom_code
    def apply_properties(self, vtkobj):
        '''Sets properties from node to vtkobj based on property name'''
        m_properties=self.m_properties()
        for x in [m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]]:
            # Skip setting any empty values
            inputval = getattr(self, x)
            if len(str(inputval)) == 0:
                continue
            # SetXFileName(Y) only if attribute is a string
            if 'FileName' in x and isinstance(inputval, str):
                value = os.path.realpath(bpy.path.abspath(inputval))
                cmd = 'vtkobj.Set' + x[2:] + '(value)'
            # SetXToY()
            elif x.startswith('e_'):
                cmd = 'vtkobj.Set'+x[2:]+'To'+inputval+'()'
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
        BVTKCache.check_cache()
        input_ports, output_ports, extra_input, extra_output = self.m_connections()
        input_ports.extend(extra_input)
        output_ports.extend(extra_output)
        for x in input_ports:
            self.inputs.new('BVTK_NodeSocketType', x)
        for x in output_ports:
            self.outputs.new('BVTK_NodeSocketType', x)
        # Some nodes need to set properties (such as link limit) after creation
        if hasattr(self, 'setup'):
            self.setup()

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

class BVTK_OT_NodeWrite(bpy.types.Operator):
    '''Operator to call VTK Write() for a node'''
    bl_idname = "node.bvtk_node_write"
    bl_label = "Write"

    id: bpy.props.IntProperty()

    def execute(self, context):
        BVTKCache.check_cache()
        node = get_node(self.id)  # TODO: change node_id to node_path?
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
