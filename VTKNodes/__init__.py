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
    print( 'import vtk done')
except: 
    pass

if 'vtk' not in globals() and 'vtk' not in locals():
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
from . import VTKConverters
from . import VTKSources
from . import VTKReaders
from . import VTKWriters
from . import VTKFilters
from . import VTKFilters1

if Reloading:
    import importlib
    importlib.reload(core)
    importlib.reload(VTKConverters)
    importlib.reload(VTKSources)
    importlib.reload(VTKReaders)
    importlib.reload(VTKWriters)
    importlib.reload(VTKFilters)
    importlib.reload(VTKFilters1)

#---------------------------------------------------------------------------------
# on_file_loaded
#---------------------------------------------------------------------------------
@persistent
def on_file_loaded(scene):
    ''' initialize cache after a blender file open '''
    core.init_cache()

#---------------------------------------------------------------------------------
# Registering
# CLASSES and CATEGORIES are defined in core and filled by all the VTKxxx files
#---------------------------------------------------------------------------------
def register():
    bpy.app.handlers.load_post.append(on_file_loaded)
    for c in core.CLASSES:
        bpy.utils.register_class(c)
    nodeitems_utils.register_node_categories("VTK_NODES", core.CATEGORIES )

def unregister():
    nodeitems_utils.unregister_node_categories("VTK_NODES" )
    for c in reversed(core.CLASSES):
        bpy.utils.unregister_class(c)
    bpy.app.handlers.load_post.remove(on_file_loaded)
            
