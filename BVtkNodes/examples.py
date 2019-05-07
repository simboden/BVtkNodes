import bpy
from mathutils import *
from math import *
from . import core
from bpy_extras.io_utils import ExportHelper
import json
import os

examples_dir = os.path.realpath(__file__).replace('examples.py', 'examples/')
examples_data_dir = os.path.realpath(__file__).replace('examples.py', 'examples_data/')

# ---------------------------------------------------------------------------------
# Functions to save node state into a dictionary
# ---------------------------------------------------------------------------------


class IEPanel(bpy.types.Panel):
    '''Import and export vtk node trees as jsons'''
    bl_label = 'Import export'
    bl_idname = 'vtk_utilities_importexport'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'examples'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.tree_type == 'VTKTreeType'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.operator('vtk_node_tree.export', text='Save as json', icon='FILE_TEXT')

        row = layout.row()
        row.operator('vtk_node_tree.import', text='Import from json', icon='FILESEL')


core.add_ui_class(IEPanel)


class ArrangePanel(bpy.types.Panel):
    """ Arrange node tree """
    bl_label = 'Arrange tree'
    bl_idname = 'vtk_utilities_arrangetree'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'examples'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.tree_type == 'VTKTreeType'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column(align=True)
        op = col.operator('vtk.arrange_tree', text='arrange', icon='NODETREE')
        col.prop(scene, 'vtk_arrange_x_spacing', text='x spacing')
        col.prop(scene, 'vtk_arrange_y_spacing', text='y spacing')

def arrange(scene, context):
    bpy.ops.vtk.arrange_tree()

bpy.types.Scene.vtk_arrange_x_spacing = bpy.props.IntProperty(default=10, update=arrange)
bpy.types.Scene.vtk_arrange_y_spacing = bpy.props.IntProperty(default=10, update=arrange)
core.add_ui_class(ArrangePanel)


class ExamplesPanel(bpy.types.Panel):
    '''Example pipelines'''
    bl_label = 'Examples'
    bl_idname = 'vtk_utilities_examples'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'examples'

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.tree_type == 'VTKTreeType'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        layout.menu('ExamplesMenu')



core.add_ui_class(ExamplesPanel)


class ExamplesMenu(bpy.types.Menu):
    bl_label = "Examples"
    bl_idname = 'ExamplesMenu'

    def draw(self, context):
        layout = self.layout
        for i in os.listdir(examples_dir):
            if i.endswith('.json'):
                layout.operator('vtk_node_tree.import', text=i.replace('.json', '')).filepath = examples_dir + i

        for em in ExamplesMenus:
            layout.menu(em.bl_idname)


core.add_ui_class(ExamplesMenu)
ExamplesMenus = []

for name in [name for name in os.listdir(examples_dir) if os.path.isdir(os.path.join(examples_dir, name))]:
    def menu_draw(self, context):
        layout = self.layout
        for i in os.listdir(self.filepath):
            if i.endswith('.json'):
                layout.operator('vtk_node_tree.import', text=i.replace('.json', '')).filepath = os.path.join(
                    self.filepath, i)


    menu_type = type("ExamplesCategory_" + name, (bpy.types.Menu,), {
        "bl_label": name,
        "bl_idname": "ExamplesCategory_" + name,
        "draw": menu_draw,
        "filepath": os.path.join(examples_dir, name)
    })

    ExamplesMenus.append(menu_type)
    core.add_ui_class(menu_type)


# ---------------------------------------------------------------------------------
# Import export functions
# ---------------------------------------------------------------------------------
def gisbi(node, identifier):  # get input socket by identifier
    inputs = node.inputs
    for input in inputs:
        if input.identifier == identifier:
            return input
    return None


def gosbi(node, identifier):  # get output socket by identifier
    outputs = node.outputs
    for output in outputs:
        if output.identifier == identifier:
            return output
    return None


def gnbn(nodes, name):  # get node by name
    for node in nodes:
        if node.name == name:
            return node
    return None


def node_tree_from_dict(context, node_tree_dict):
    space = context.space_data
    nodes = space.node_tree.nodes
    links = space.node_tree.links
    new_nodes_dicts = node_tree_dict['nodes']
    for new_node_dict in new_nodes_dicts:
        node_from_dict(nodes, new_node_dict)
    new_links_dicts = node_tree_dict['links']
    for new_link_dict in new_links_dicts:
        link_from_dict(nodes, links, new_link_dict)


def node_from_dict(nodes, node_dict):
    idname = node_dict['bl_idname']
    if not hasattr(bpy.types, idname):
        print('Node type not found:', idname)
    else:
        new_node = nodes.new(type=idname)
        for prop in node_dict:
            value = node_dict[prop]
            if prop == 'additional_properties':
                if hasattr(new_node, 'import_properties'):
                    new_node.import_properties(value)
            else:
                if 'FileName' in prop and value.startswith('$/'):
                    value = value.replace('$/', examples_data_dir)
                try:
                    setattr(new_node, prop, value)
                except:
                    pass

def link_from_dict(nodes, links, new_link_dict):
    to_node = gnbn(nodes, new_link_dict['to_node_name'])
    from_node = gnbn(nodes, new_link_dict['from_node_name'])
    if from_node and to_node:
        from_socket = gosbi(from_node, new_link_dict['from_socket_identifier'])
        to_socket = gisbi(to_node, new_link_dict['to_socket_identifier'])
        if to_socket and from_socket:
            links.new(to_socket, from_socket)


def node_tree_to_dict(node_tree):
    nodes = node_tree.nodes
    links = node_tree.links
    n = []
    for node in nodes:
        n.append(node_to_dict(node))
    l = []
    for link in links:
        l.append(link_to_dict(link))
    return {"nodes": n, "links": l}


def link_to_dict(link):
    dict = {}
    dict['from_node_name'] = link.from_node.name
    dict['to_node_name'] = link.to_node.name
    dict['from_socket_identifier'] = link.from_socket.identifier
    dict['to_socket_identifier'] = link.to_socket.identifier
    return dict

def node_to_dict(node):
    dict = {}
    props = [k for k in node.m_properties()]
    props.extend(['bl_idname',
                  'name',
                  'color',
                  'height',
                  'hide',
                  'label',
                  'location',
                  'mute',
                  'show_options',
                  'show_preview',
                  'width'
                  ])
    for prop in props:
        attr = getattr(node, prop)
        classname = attr.__class__.__name__
        if classname in ['Vector','Color','bpy_prop_array']:
            attr = [i for i in attr]
        if 'FileName' in prop and issubclass(attr.__class__, str):
            attr = os.path.realpath(bpy.path.abspath(attr)).replace(examples_data_dir, '$/')
        print(prop.ljust(20), classname.ljust(20), str(attr))
        dict[prop] = attr
    if hasattr(node, 'export_properties'):
        ep = node.export_properties()
        dict['additional_properties'] = ep
        for k in ep:
            if k in dict:
                dict.pop(k)
    return dict


# ---------------------------------------------------------------------------------
# Import export operators
# ---------------------------------------------------------------------------------


class ImportVtkNodeTree(bpy.types.Operator):
    bl_idname = "vtk_node_tree.import"
    bl_label = "choose file"

    filepath = bpy.props.StringProperty(subtype='FILE_PATH', default='')

    confirm = bpy.props.BoolProperty(default=True)

    def invoke(self, context, event):
        node_tree = context.space_data.node_tree

        if node_tree is None:
            node_tree = bpy.data.node_groups.new('NodeTree', 'VTKTreeType')
            context.space_data.node_tree = node_tree

        if self.confirm and node_tree.nodes:
            def draw(self2, context):
                self2.layout.label("This will erase current node tree")
                self2.layout.operator_context = 'INVOKE_DEFAULT'
                self2.layout.operator(self.bl_idname, text='Confirm').confirm=False
            bpy.context.window_manager.popup_menu(draw, title="Are you sure?", icon='QUESTION')
            return {'FINISHED'}

        self.confirm=True

        if self.filepath == '':
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

        return self.execute(context)

    def execute(self, context):
        f = open(self.filepath, 'r', encoding='utf-8')
        text = f.read()
        f.close()
        bpy.ops.node.select_all(action='SELECT')
        bpy.ops.node.delete()

        dic =  json.loads( text )      
        node_tree_from_dict( context, dic )
        bpy.ops.node.select_all(action='DESELECT')
        self.filepath = ''
        return {'FINISHED'}


core.add_ui_class(ImportVtkNodeTree)


class ExportVtkNodeTree(bpy.types.Operator, ExportHelper):
    '''Save vtk node tree into a json file'''
    bl_idname = "vtk_node_tree.export"
    bl_label = "Export Vtk Node Tree"
    filename_ext = ".json"

    def execute(self, context):
        node_tree = context.space_data.node_tree
        if node_tree is None:
            self.report({'ERROR'}, 'Select a node tree')
            return {'CANCELLED'}
        dic = node_tree_to_dict(node_tree)
        text = json.dumps( dic, indent=4, sort_keys=True) 
        f = open(self.filepath, 'w', encoding='utf-8')
        f.write( text )
        f.close()
        return {'FINISHED'}


core.add_ui_class(ExportVtkNodeTree)


class ImportVtkNodeTreeFromPy(bpy.types.Operator):
    bl_idname = "vtk_node_tree.import_py"
    bl_label = "choose file"

    filepath = bpy.props.StringProperty(subtype='FILE_PATH', default='')

    confirm = bpy.props.BoolProperty(default=True)

    def invoke(self, context, event):
        node_tree = context.space_data.node_tree
        if node_tree is None:
            self.report({'ERROR'}, 'Select a node tree')
            return {'CANCELLED'}

        if self.confirm and node_tree.nodes:
            def draw(self2, context):
                self2.layout.label("This will erase current node tree")
                self2.layout.operator_context = 'INVOKE_DEFAULT'
                self2.layout.operator(self.bl_idname, text='Confirm').confirm=False
            bpy.context.window_manager.popup_menu(draw, title="Are you sure?", icon='QUESTION')
            return {'FINISHED'}

        self.confirm=True

        if (self.filepath == ''):
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

        return self.execute(context)

    def execute(self, context):
        s = open(self.filepath, 'r', encoding='utf-8').read()
        bpy.ops.node.select_all(action='SELECT')
        bpy.ops.node.delete()
        node_tree_from_py(context, s)
        bpy.ops.node.select_all(action='DESELECT')
        self.filepath = ''
        return {'FINISHED'}

#
# --- experiment meant to interpreting an existing vtk-python-example 
# --- and translate it to a node-network
#
# --- it is not completed, do not use it
#
def node_tree_from_py(context, py):
    space = context.space_data
    nodes = space.node_tree.nodes
    links = space.node_tree.links
    lines = py.split('\n')
    vtkObjs = {}
    linked = []  # [input,output]

    for line in lines:
        line = line.replace(' ', '')
        if not line.startswith('#'):
            if '#' in line:
                line = line.split('#', 1)[0]
            if '=vtk.' in line:
                a = line.split('=vtk.')
                type = a[1].replace('()', '').replace('vtk', 'VTK') + 'Type'
                if type in core.CLASSES:
                    vtkObjs[a[0]] = nodes.new(type)
                    linked.append(vtkObjs[a[0]])
                else:
                    print(a[1] + " can't be converted to node")
            elif '=' not in line and '.' in line:
                if '.SetInputConnection' in line:
                    n1 = line.split('.SetInputConnection')[0]
                    n2 = line.split('(', 1)[1][:-1]
                    if ('.GetOutputPort()' in n2):
                        n2 = n2.replace('.GetOutputPort()', '')
                        if n2 in vtkObjs.keys() and n1 in vtkObjs.keys():
                            links.new(vtkObjs[n1].inputs[0], vtkObjs[n2].outputs[0])
                elif '.Set' in line:
                    if line.count('(') > 1:
                        print(line + ": I'm too stupid to handle more than 2 brackets")
                    else:
                        n1 = line.split('.Set')[0]
                        if n1 in vtkObjs.keys():
                            toSet = line.split('.Set')[1]

                            def set(objname, attr, val):
                                if objname in vtkObjs.keys():
                                    obj = vtkObjs[objname]
                                    if attr in obj.m_properties():
                                        setattr(obj, attr, val)
                                    else:
                                        print(obj.bl_idname + ' got no attributes' + attr + ' in this addon')
                                else:
                                    print(objname + ', missing corresponding node')

                            if 'To' in toSet:
                                if toSet.count('To') > 1:
                                    print(' "To" is not handled yet')
                                else:
                                    set(n1, 'e_' + toSet.split('To')[0],
                                        toSet.split('To')[1].replace('(', '').replace(')', ''))
                            elif 'On()' in toSet:
                                set(n1, 'm_' + toSet.split('On()')[0], True)
                            elif 'Off' in toSet:
                                set(n1, 'm_' + toSet.split('Off()')[0], False)
                            elif toSet.count('(') == 1 and toSet.split('(')[1].replace(')', '') != '':
                                try:
                                    set(n1, 'm_' + toSet.split('(')[0], eval(toSet.split('(')[1].replace(')', '')))
                                except:
                                    print(toSet + ' undefined argument')
                            else:
                                print('this "Set" has not been interpreted: ' + line)
    for i in range(len(linked)):
        linked[i].location = (i * 300, 0)

    tb = nodes.new('VTK2BlenderType')
    tb.location = (len(linked) * 300, 0)
    links.new(tb.inputs[0], linked[len(linked) - 1].outputs[0])

# ---------------------------------------------------------------------------------
# Arrage tree operator
# ---------------------------------------------------------------------------------


def x_behind_nodes(node):
    max_behind = 0
    for input in node.inputs:
        for link in input.links:
            in_node = link.from_node
            behind_in_node = x_behind_nodes(in_node)
            if behind_in_node + 1 > max_behind:
                max_behind = behind_in_node + 1
    return max_behind


def arrange_height(node, x_spacing, y_spacing, initial_y=0, initial_x=0):
    total_height = 0
    for output in node.outputs:
        for link in output.links:
            out_node = link.to_node
            out_block_height = arrange_height(out_node,
                                              x_spacing,
                                              y_spacing,
                                              initial_y-total_height,
                                              initial_x+node.width+x_spacing)
            total_height += out_block_height
    k = node.dimensions[0] / node.width  # node.height doesnt work
    height = node.dimensions[1] / k  # node height
    if height > total_height:
        total_height = height + y_spacing
    node.location = initial_x, initial_y - total_height/2 + height/2
    return total_height


class NodeBlock:

    def __init__(self, node_start):
        self.nodes = []
        self.start = node_start
        self.add_from(node_start)

    def add_from(self, node):
        self.nodes.append(node)
        for output in node.outputs:
            for i, link in enumerate(output.links):
                if link.to_node not in self.nodes:
                    self.add_from(link.to_node)
        for input in node.inputs:
            for i, link in enumerate(input.links):
                if link.from_node not in self.nodes:
                    self.add_from(link.from_node)


class VTKArrangeTree(bpy.types.Operator):
    bl_idname = "vtk.arrange_tree"
    bl_label = "arrange_tree"

    def has_input(self, node):
        """ true if node has at least one input linked """
        for input in node.inputs:
            if len(input.links) > 0:
                return True
        return False

    def execute(self, context):
        tree = context.space_data.node_tree
        node_blocks = []   # nodes with no connections in input
        x_spacing = context.scene.vtk_arrange_x_spacing
        y_spacing = context.scene.vtk_arrange_y_spacing
        i = 0
        for node in tree.nodes:
            if not self.has_input(node):
                flag = True
                for nb in node_blocks:
                    if node in nb.nodes:
                        flag = False
                        break
                if flag: node_blocks.append(NodeBlock(node))
        h = 0
        for nb in node_blocks:
            h -= arrange_height(nb.start, x_spacing, y_spacing, h)
        return {'FINISHED'}


core.add_ui_class(VTKArrangeTree)
