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
from   nodeitems_utils import NodeCategory, NodeItem

from . import core
from . import VTK2Blender
from . import VTKArrowSource
from . import VTKConeSource
from . import VTKCubeSource
from . import VTKPlaneSource
from . import VTKSphereSource
from . import VTKContourFilter
from . import VTKImageGaussianSmooth
from . import VTKStructuredPointsReader

if Reloading:
    import importlib
    importlib.reload(core)
    importlib.reload(VTK2Blender)
    importlib.reload(VTKArrowSource)
    importlib.reload(VTKConeSource)
    importlib.reload(VTKCubeSource)
    importlib.reload(VTKPlaneSource)
    importlib.reload(VTKSphereSource)
    importlib.reload(VTKContourFilter)
    importlib.reload(VTKImageGaussianSmooth)
    importlib.reload(VTKStructuredPointsReader)

#print( "###CLASSES",   core.CLASSES )
#print( "###TYPENAMES", core.TYPENAMES )

#---------------------------------------------------------------------------------
# on_file_loaded
#---------------------------------------------------------------------------------
@persistent
def on_file_loaded(scene):
    ''' initialize cache after a blender file open '''
    core.init_cache()

#---------------------------------------------------------------------------------
# VTKNodeCategory
#---------------------------------------------------------------------------------
class VTKNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'VTKTreeType'

menu_items = [ NodeItem(x) for x in core.TYPENAMES ] 
node_categories = [ VTKNodeCategory("ALL", "vtk nodes", items=menu_items) ]

#---------------------------------------------------------------------------------
# Registering
#---------------------------------------------------------------------------------
def register():
    bpy.app.handlers.load_post.append(on_file_loaded)
    for c in core.CLASSES:
        bpy.utils.register_class(c)
    nodeitems_utils.register_node_categories("VTK_NODES", node_categories)

def unregister():
    nodeitems_utils.unregister_node_categories("VTK_NODES")
    for c in reversed(core.CLASSES):
        bpy.utils.unregister_class(c)
    bpy.app.handlers.load_post.remove(on_file_loaded)
            

# if __name__ == "__main__":
#     register()

