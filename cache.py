import logging
import bpy
import vtk
import functools

l = logging.getLogger(__name__)

#last_update_id:dict = {} # node_id -> last update ID

#persistent_storage = {"nodes": {}}

#It is sometimes not possible to save instance variables in a class, which is why we use this node
class PersistentStorageUser():
    def free(self):
        if self.name in persistent_storage["nodes"]:
            del persistent_storage["nodes"][self.name]

    def get_persistent_storage(self):
        if self.name not in persistent_storage["nodes"]:
            persistent_storage["nodes"][self.name] = {}
        return persistent_storage["nodes"][self.name]

nodeMaxId:int = 0    # Maximum node id number. 0 means not assigned.
nodeIdMap:dict = {}  # node_id -> node
treeIdMap:dict = {}  # node_id -> node tree
vtkCache:dict = {}   # node_id -> VTK object


class BVTKCache:
    '''Class for navigation between nodes and VTK objects.
    node_id property is used as key in map dictionaries.
    All nodes should have an entry in the cache dictionaries.
    vtkCache entry can be None if there is no VTK object.
    '''

    @classmethod
    def init(cls):
        ''' Create cache.
        '''
        cls.rebuild_cache()

    @classmethod
    def rebuild_cache(cls):
        '''Rebuild Node cache and recreate VTK objects from current node
        trees.
        '''
<<<<<<< HEAD
        global nodeMaxId, nodesIdMap, vtkCache, last_update_id

        nodeMaxId = 1
        nodesIdMap = {}
=======
        # Zero the map dictionaries
        global nodeMaxId, nodeIdMap, treeIdMap, vtkCache
        nodeMaxId = 0
        nodeIdMap = {}
>>>>>>> WIP: Restore node_id, streamline cache, updates to node code
        treeIdMap = {}
        vtkCache = {}
<<<<<<< HEAD
        last_update_id = {}
        nodeCache = {}

    @classmethod
    def add_new_node(cls, node):
        '''Create VTK object for argument node and add mapping between node
        and VTK object.
        '''
        if node.bl_label.startswith('vtk'):
            vtk_class = getattr(vtk, node.bl_label, None)
            if vtk_class is None:
                node.vtk_status = 'none'
                l.error("Bad VTK class name " + node.bl_label)
                return
            vtk_obj = vtk_class()
            vtkCache[node] = vtk_obj
            nodeCache[vtk_obj] = node
            node.vtk_status = 'uninitialized'
            l.debug("Created VTK object of type " + node.bl_label)
        else:
            node.vtk_status = 'none'

    @classmethod
    def check_cache(cls):
        '''Rebuild Node Cache. Called by all operators. Cache is out of sync
        if an operator is called and at the same time NodesMaxId=1.
        This happens after reloading addons. Cache is rebuilt, and the
        operator must be interrupted, but the next operator call will work
        OK.
        '''
        # After F8 or FileOpen VTKCache is empty and NodesMaxId == 1
        # any previous node_id must be invalidated
        if nodeMaxId == 1:
            for nt in bpy.data.node_groups:
                if nt.bl_idname == 'BVTK_NodeTreeType':
                    for n in nt.nodes:
                        n.node_id = 0

        # For each node check if it has a node_id
        # and if it has a vtk_obj associated
        for nt in bpy.data.node_groups:
            if nt.bl_idname == 'BVTK_NodeTreeType':
                for n in nt.nodes:
                    if n.node_id == 0:
                        cls.map_node(n, tree=nt)
                    if cls.get_vtkobj(n) == None:
                        cls.init_vtkobj(n)

    @classmethod
    def update_necessary(cls, node, update_id):
        global last_update_id
        node_id = node.node_id
        return (not node_id in last_update_id or update_id != last_update_id[node_id])

    @classmethod
    def update_id(cls, node, update_iter):
        global last_update_id
        last_update_id[node.node_id] = update_iter

    @classmethod
    def init_vtkobj(cls, node):
        '''Instantiate the nodes vtkobj and store it in VTKCache.
        '''
        global vtkCache
        
        # create the node vtk_obj if needed
        if node.bl_label.startswith('vtk'):
            vtk_class = getattr(vtk, node.bl_label, None)
            if vtk_class is None:
                l.error("bad classname " + node.bl_label)
                return
            vtkCache[node.node_id] = vtk_class()
            l.debug("Created VTK object of type " + node.bl_label + ", id " + str(node.node_id))
        else:
            vtkCache[node.node_id] = None
=======

        # Rebuild from existing nodes
        for nodetree in bpy.data.node_groups:
            if nodetree.bl_idname != 'BVTK_NodeTreeType':
                continue
            for n in nodetree.nodes:
                # Uninitialized node
                if n.node_id == 0:
                    vtk_obj = n.init_vtk()
                    cls.map_node(n, vtk_obj)
                # Update nodeMaxId if needed
                elif n.node_id > nodeMaxId:
                    nodeMaxId = n.node_id
>>>>>>> WIP: Restore node_id, streamline cache, updates to node code

    @classmethod
    def map_node(cls, node, vtk_obj=None):
        '''Assign node ID to node and add VTK object and mappings to cache.
        '''
        global nodeMaxId, nodeIdMap, treeIdMap, vtkCache

        nodeMaxId += 1
        node.node_id = nodeMaxId
        vtkCache[node.node_id] = vtk_obj
        nodeIdMap[node.node_id] = node
        tree = node.id_data
        treeIdMap[node.node_id] = tree
        l.debug("Mapped node: %s, id %d" % (node.name, node.node_id))

    @classmethod
    def unmap_node(cls, node):
        '''Remove node from cache. To be called from node.free().
        Remove node from cache dictionaries.
        '''
        global nodeIdMap, treeIdMap, vtkCache

        if node.node_id in nodeIdMap:
            del nodeIdMap[node.node_id]
        if node.node_id in treeIdMap:
            del treeIdMap[node.node_id]
        if node.node_id in vtkCache:
            del vtkCache[node.node_id]
        l.debug("Unmapped node: %s, id %d" % (node.name, node.node_id))

    @classmethod
    def get_node(cls, node_id:int):
        '''Get node corresponding to node_id.
        Called by BVTK_OT_NodeWrite.
        '''
        global nodeIdMap

        if node_id in nodeIdMap:
            return nodeIdMap[node_id]
        else:
            raise Exception("not found node_id " + str(node_id))

    @classmethod
    def get_tree(cls, node_id:int):
        '''Get node tree corresponding to node_id.
        Called in BVTK_OT_Edit_Custom_Code.
        '''
        global treeIdMap

        if node_id in treeIdMap:
            return treeIdMap[node_id]
        else:
            raise Exception("not found node_id " + str(node_id))

    @classmethod
    def get_vtk_obj(cls, node_id:int):
        '''Get the VTK object from vtkCache by node ID number.
        '''
        global vtkCache

        if node_id in vtkCache:
            return vtkCache[node_id]
        else:
            raise Exception("not found node_id:" + str(node_id))
