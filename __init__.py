# <pep8 compliant>

#---------------------------------------------------------------------------------
# ADDON HEADER SECTION
#---------------------------------------------------------------------------------

bl_info = {
    "name": "BVTKNodes, Blender VTK Nodes",
    "author": "Silvano Imboden, Lorenzo Celli, Paul McManus, Tuomo Keskitalo",
    "version": (0, 1),
    "blender": (2, 79,  0),
    "location": "Node Editor > Use Nodes > VTK > New NodeTree",
    "description": "Create and execute VTK pipelines in Blender Node Editor",
    "warning": "Experimental. Requires custom installation of VTK library",
    "wiki_url": "https://github.com/tkeskita/BVtkNodes",
    "tracker_url": "https://github.com/tkeskita/BVtkNodes/issues",
    "support": 'COMMUNITY',
    "category": "Node",
    }

# tkeskita OPEN ISSUES
# - generate/vtk_info_modified.py is not used, can it be deleted?
#
# tkeskita TODO list:
# - replace all prints with Python logging
#

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

# Import VTK Python module
try:
    import vtk
except:
    pass

try:
    dir(vtk)
except:
    message = '''
    BVTKNodes add-on failed to access the VTK library. You must
    compile and install Python library corresponding to the Python
    library version used by Blender, and then compile and install
    VTK on top of it. Finally you must customize environment variables
    to use the compiled Python library before starting Blender.
    Please refer to BVTKNodes documentation for help.
    '''
    l.error(message)
    raise Exception(message)

l.info("Loaded VTK version: " + vtk.vtkVersion().GetVTKVersion())
l.info("VTK base path: " + vtk.__file__)

need_reloading = "bpy" in locals()

import bpy
from   bpy.app.handlers import persistent
import nodeitems_utils
from   nodeitems_utils import NodeItem

from . import core
from . import b_properties
from . import showhide_properties
from . import inspect
from . import favorites
from . import tree
from . import colormap
from . import customfilter
from . import info
from . import update
from . import converters

from . import VTKSources
from . import VTKReaders
from . import VTKWriters
from . import VTKFilters

from . import VTKOthers

if need_reloading:
    import importlib

    importlib.reload(update)
    importlib.reload(core)
    importlib.reload(b_properties)
    importlib.reload(showhide_properties)
    importlib.reload(tree)
    importlib.reload(inspect)
    importlib.reload(colormap)
    importlib.reload(customfilter)
    importlib.reload(info)
    importlib.reload(favorites_data)
    importlib.reload(favorites)
    importlib.reload(converters)

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

@persistent
def on_file_loaded(scene):
    '''Initialize cache after a blender file open'''
    core.init_cache()


@persistent
def on_frame_change(scene):
    '''Update nodes after frame changes by updating all VTK to Blender nodes'''
    for node_group in bpy.data.node_groups:
        for node in node_group.nodes:
            if node.bl_idname == 'BVTK_Node_VTKToBlenderType':
                update.no_queue_update(node, node.update_cb)


def custom_register_node_categories():
    '''Custom registering of node categories to prevent node categories to
    be shown on the tool-shelf
    '''

    identifier = "VTK_NODES"
    cat_list = core.CATEGORIES

    if identifier in nodeitems_utils._node_categories:
        raise KeyError("Node categories list '%s' already registered" % identifier)
        return

    def draw_node_item(self, context):
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            item.draw(item, col, context)

    def draw_add_menu(self, context):
        layout = self.layout
        for cat in cat_list:
            if cat.poll(context):
                layout.menu("NODE_MT_category_%s" % cat.identifier)

    menu_types = []
    for cat in cat_list:
        menu_type = type(\
            "NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
                "bl_space_type": 'NODE_EDITOR',
                "bl_label": cat.name,
                "category": cat,
                "poll": cat.poll,
                "draw": draw_node_item,
            })
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)

    nodeitems_utils._node_categories[identifier] = \
        (cat_list, draw_add_menu, menu_types, []) # , panel_types)


def register():
    '''Register function. CLASSES and CATEGORIES are defined in core.py and
    filled in all the gen_VTK*.py and VTK*.py files
    '''
    bpy.app.handlers.load_post.append(on_file_loaded)
    bpy.app.handlers.frame_change_post.append(on_frame_change)
    core.check_b_properties() # delayed to here to allow class overriding
    for c in core.UI_CLASSES:
        try:
            bpy.utils.register_class(c)
        except:
            l.critical('error registering ', c)
    for c in sorted(core.CLASSES.keys()):
        try:
            bpy.utils.register_class(core.CLASSES[c])
        except:
            l.critical('error registering ', c)
    custom_register_node_categories()

def unregister():
    nodeitems_utils.unregister_node_categories("VTK_NODES")
    for c in reversed(sorted(core.CLASSES.keys())):
        bpy.utils.unregister_class(core.CLASSES[c])
    for c in reversed(core.UI_CLASSES):
        bpy.utils.unregister_class(c)
    bpy.app.handlers.load_post.remove(on_file_loaded)
    bpy.app.handlers.frame_change_post.remove(on_frame_change)
            
