# <pep8 compliant>

#---------------------------------------------------------------------------------
# ADDON HEADER SECTION
#---------------------------------------------------------------------------------

bl_info = {
    "name": "VTK nodes",
    "author": "Silvano Imboden",
    "version": (0, 0),
    "blender": (2, 79,  0),
    "location": "node editor > Add > Mesh > New Object",
    "description": "create and execute VTK pipelines",
    "warning": "",
    "wiki_url": "",
    "category": "Node",
    }

#---------------------------------------------------------------------------------
# MODULES IMPORT
#---------------------------------------------------------------------------------
try:
    print( 'import vtk begin, please wait')
    import vtk
    #from .vtk_patch import vtk
    print( 'import vtk done')
except:
    print('====error importing vtk')
    pass

# if 'vtk' not in globals() and 'vtk' not in locals():
#     message = '''\n\n
#     The VTKNodes addon depends on the vtk library.
#     Unfortunately the Blender build you are using does not have access to this library.
#     Please install vtk, and ensure that the blender python is able to import it.\n'''
#     raise Exception(message)

try:
    dir(vtk)
except:
    message = '''\n\n
    The VTKNodes addon depends on the vtk library.
    Unfortunately the Blender build you are using does not have access to this library.
    Please install vtk, and ensure that the blender python is able to import it.\n'''
    raise Exception(message)


Reloading = "bpy" in locals()

import bpy
from   bpy.app.handlers import persistent
import nodeitems_utils
from   nodeitems_utils import NodeItem

from . import core
from . import b_properties
from . import b_panel
from . import inspect
from . import favorites
from . import examples
from . import colormap
from . import customfilter
from . import info
from . import update

from . import VTKConverters
from . import VTKSources
from . import VTKReaders
from . import VTKWriters
from . import VTKFilters
from . import VTKOthers

if Reloading:
    import importlib

    #importlib.reload(vtk_patch)
    importlib.reload(update)
    importlib.reload(core)
    importlib.reload(b_properties)
    importlib.reload(b_panel)
    importlib.reload(examples)
    importlib.reload(inspect)
    importlib.reload(colormap)
    importlib.reload(customfilter)
    importlib.reload(info)
    importlib.reload(favorites_data)
    importlib.reload(favorites)

    importlib.reload(VTKConverters)

    importlib.reload(gen_VTKSources)
    importlib.reload(VTKSources)

    importlib.reload(gen_VTKReaders)
    importlib.reload(VTKReaders)

    importlib.reload(gen_VTKWriters)
    importlib.reload(VTKWriters)
    
    importlib.reload(gen_VTKFilters1)
    importlib.reload(gen_VTKFilters2)
    importlib.reload(gen_VTKFilters)
    importlib.reload(VTKFilters)

    importlib.reload(gen_VTKTransform)
    importlib.reload(gen_VTKImplicitFunc)
    importlib.reload(gen_VTKParametricFunc)
    importlib.reload(gen_VTKIntegrator)
    importlib.reload(VTKOthers)

#---------------------------------------------------------------------------------
# on_file_loaded
#---------------------------------------------------------------------------------
@persistent
def on_file_loaded(scene):
    ''' initialize cache after a blender file open '''
    core.init_cache()

#---------------------------------------------------------------------------------
# on_frame_change
#---------------------------------------------------------------------------------
@persistent
def on_frame_change(scene):
    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            if node.bl_idname == 'VTK2BlenderType':
                update.no_queue_update(node, node.update_cb)

#---------------------------------------------------------------------------------
# Custom register_node_categories
# prevent the node categories to be shown on the tool-shelf
#---------------------------------------------------------------------------------
def custom_register_node_categories(identifier, cat_list):
    if identifier in nodeitems_utils._node_categories:
        raise KeyError("Node categories list '%s' already registered" % identifier)
        return

    def draw_node_item(self, context):
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            item.draw(item, col, context)

    menu_types = []

    for cat in cat_list:
        menu_type = type("NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
            "bl_space_type": 'NODE_EDITOR',
            "bl_label": cat.name,
            "category": cat,
            "poll": cat.poll,
            "draw": draw_node_item,
            })

        menu_types.append(menu_type)

        bpy.utils.register_class(menu_type)

    def draw_add_menu(self, context):
        layout = self.layout

        for cat in cat_list:
            if cat.poll(context):
                layout.menu("NODE_MT_category_%s" % cat.identifier)

    nodeitems_utils._node_categories[identifier] = (cat_list, draw_add_menu, menu_types, [])#, panel_types)

#---------------------------------------------------------------------------------
# Used for debugging
#---------------------------------------------------------------------------------

bpy.types.Scene.vtk_debug = bpy.props.IntProperty(default=50, subtype='PERCENTAGE', min=0, max=100)

#---------------------------------------------------------------------------------
# Registering
# CLASSES and CATEGORIES are defined in core and filled by all the VTKxxx files
#---------------------------------------------------------------------------------
def register():
    bpy.app.handlers.load_post.append(on_file_loaded)
    bpy.app.handlers.frame_change_post.append(on_frame_change)
    core.check_b_properties() # delayed to deal with overloading
    for c in core.UI_CLASSES:
        try:
            bpy.utils.register_class(c)
        except:
            print('error registering ', c)
    for c in sorted(core.CLASSES.keys()):
        try:
            bpy.utils.register_class(core.CLASSES[c])
        except:
            print( 'error registering ', c)
    custom_register_node_categories("VTK_NODES", core.CATEGORIES )

def unregister():
    nodeitems_utils.unregister_node_categories("VTK_NODES")
    for c in reversed(sorted(core.CLASSES.keys())):
        bpy.utils.unregister_class(core.CLASSES[c])
    for c in reversed(core.UI_CLASSES):
        bpy.utils.unregister_class(c)
    bpy.app.handlers.load_post.remove(on_file_loaded)
    bpy.app.handlers.frame_change_post.remove(on_frame_change)
            
