import logging
import bpy
import vtk
import functools
from . import core

l = logging.getLogger(__name__)

# TODO: Modify Global Time Keeper and remove these?
persistent_storage = {"nodes": {}}

# It is sometimes not possible to save instance variables in a class, which is why we use this node
class PersistentStorageUser:
    def free(self):
        if self.name in persistent_storage["nodes"]:
            del persistent_storage["nodes"][self.name]

    def get_persistent_storage(self):
        if self.name not in persistent_storage["nodes"]:
            persistent_storage["nodes"][self.name] = {}
        return persistent_storage["nodes"][self.name]


nodeMaxId: int = 0  # Maximum node id number. 0 means not assigned.
nodeIdMap: dict = {}  # node_id -> node
treeIdMap: dict = {}  # node_id -> node tree
vtkCache: dict = {}  # node_id -> VTK object


class BVTKCache:
    """Class for navigation between nodes and VTK objects.
    node_id property is used as key in map dictionaries.
    All VTK nodes must have an entry in the cache dictionaries.
    vtkCache entry can be None if there is no VTK object.
    """

    @classmethod
    def reset_cache(cls):
        """Create new empty node cache variables.
        """
        # Zero the map dictionaries
        global nodeMaxId, nodeIdMap, treeIdMap, vtkCache
        nodeMaxId = 0
        nodeIdMap = {}
        treeIdMap = {}
        vtkCache = {}

    @classmethod
    def add_new_node(cls, node):
        """Create VTK object for argument node and add mapping between node
        and VTK object.
        """
        if node.bl_label.startswith("vtk"):
            vtk_class = getattr(vtk, node.bl_label, None)
            if vtk_class is None:
                node.vtk_status = "none"
                l.error("Bad VTK class name " + node.bl_label)
                return
            vtk_obj = vtk_class()
            vtkCache[node] = vtk_obj
            nodeCache[vtk_obj] = node
            node.vtk_status = "uninitialized"
            l.debug("Created VTK object of type " + node.bl_label)
        else:
            node.vtk_status = "none"

    @classmethod
    def init_vtkobj(cls, node):
        """Instantiate the nodes vtkobj and store it in VTKCache.
        """
        global vtkCache

        # create the node vtk_obj if needed
        if node.bl_label.startswith("vtk"):
            vtk_class = getattr(vtk, node.bl_label, None)
            if vtk_class is None:
                l.error("bad classname " + node.bl_label)
                return
            vtkCache[node.node_id] = vtk_class()
            l.debug(
                "Created VTK object of type "
                + node.bl_label
                + ", id "
                + str(node.node_id)
            )
        else:
            vtkCache[node.node_id] = None

        # Rebuild from existing nodes
        bvtk_nodes = core.get_all_bvtk_nodes()

        for node in bvtk_nodes:
            # Uninitialized node, create VTK object
            if node.node_id == 0 or BVTKCache.get_vtk_obj(node.node_id) == None:
                vtk_obj = node.init_vtk()
                cls.map_node(node, vtk_obj)
            # Update nodeMaxId if needed, to avoid doubles
            if node.node_id > nodeMaxId:
                nodeMaxId = node.node_id

        # Force resetting of VTK connections
        for node in bvtk_nodes:
            node.connected_input_names = ""  # Reset namelist to force update
            node.update()

    @classmethod
    def update_all(cls):
        """Go through all nodes and update those that are not up-to-date.
        """
        bvtk_nodes = core.get_all_bvtk_nodes()
        for node in bvtk_nodes:
            if node.vtk_status != "up-to-date":
                node.update_vtk()

    @classmethod
    def map_node(cls, node, vtk_obj=None):
        """Assign node ID to node and add VTK object and mappings to cache.
        """
        global nodeMaxId, nodeIdMap, treeIdMap, vtkCache

        # node_id value 0 indicates a new node, for which a new number
        # is to be assigned. For existing nodes use old node_id number.
        if node.node_id == 0:
            nodeMaxId += 1
            node.node_id = nodeMaxId
        if node.node_id in vtkCache:
            raise ValueError(
                "Internal Error: Cache already contains node_id #%d" % node.node_id
            )
        vtkCache[node.node_id] = vtk_obj
        nodeIdMap[node.node_id] = node
        tree = node.id_data
        treeIdMap[node.node_id] = tree

        if node.node_id == nodeMaxId:
            l.debug("Mapped new node: %s, id #%d" % (node.name, node.node_id))
        else:
            l.debug("Remapped old node: %s, id #%d" % (node.name, node.node_id))

    @classmethod
    def unmap_node(cls, node):
        """Remove node from cache. To be called from node.free().
        Remove node from cache dictionaries.
        """
        global nodeIdMap, treeIdMap, vtkCache

        if node.node_id in nodeIdMap:
            del nodeIdMap[node.node_id]
        if node.node_id in treeIdMap:
            del treeIdMap[node.node_id]
        if node.node_id in vtkCache:
            del vtkCache[node.node_id]
        l.debug("Unmapped node: %s, id #%d" % (node.name, node.node_id))

    @classmethod
    def get_node(cls, node_id: int):
        """Get node corresponding to node_id.
        Called by Node Write and Edit/Save Custom Code.
        """
        global nodeIdMap

        if node_id in nodeIdMap:
            return nodeIdMap[node_id]
        else:
            raise Exception("not found node_id " + str(node_id))

    @classmethod
    def get_tree(cls, node_id: int):
        """Get node tree corresponding to node_id.
        Called by Node Write and Edit/Save Custom Code.
        """
        global treeIdMap

        if node_id in treeIdMap:
            return treeIdMap[node_id]
        else:
            raise Exception("not found node_id " + str(node_id))

    @classmethod
    def get_vtk_obj(cls, node_id: int):
        """Get the VTK object from vtkCache by node ID number.
        """
        global vtkCache

        if node_id in vtkCache:
            return vtkCache[node_id]
        return None

    @classmethod
    def vtk_obj_in_cache(cls, node_id: int):
        """Return True if an object (or None) is in cache.
        """
        global vtkCache

        if node_id in vtkCache:
            return True
        return False
