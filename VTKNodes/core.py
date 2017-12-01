# <pep8 compliant>
#---------------------------------------------------------------------------------
# MODULES IMPORT
#---------------------------------------------------------------------------------
import bpy
from   bpy.types import NodeTree, Node, NodeSocket
import nodeitems_utils
from   nodeitems_utils import NodeCategory, NodeItem
import vtk
    
#---------------------------------------------------------------------------------
# Cache
#---------------------------------------------------------------------------------
NodesMaxId = 1   # 0 means invalid
NodesMap   = {}  # node_id -> node
VTKCache   = {}  # node_id -> vtkobj

def node_created(node):
    ''' to be called from node.init().
    give the node a unique node_id
    add it in NodesMap
    instantiate its vtkobj and store it in VTKCache 
    ''' 
    global NodesMaxId, NodesMap, VTKCache  
    node.node_id = NodesMaxId
    NodesMaxId += 1
    NodesMap[node.node_id] = node
    VTKCache[node.node_id] = None

    if node.bl_label.startswith('vtk'):
        vtk_class = getattr( vtk, node.bl_label, None )
        if vtk_class is None:
            print("VTKNodeData: - bad classname", node.bl_label ) 
            return
        VTKCache[node.node_id] = vtk_class() # make an instance of node.vtk_class

    print( "node_created", node.bl_label, node.node_id )

def node_deleted(node):
    ''' to be called from node.free().
    remove node from NodesMap and its vtkobj from VTKCache ''' 
    global NodesMap, VTKCache  
    if node.node_id in NodesMap:
        del NodesMap[node.node_id]

    if node.node_id in VTKCache:
        obj = VTKCache[node.node_id]
        if obj: 
            obj.UnRegister(obj)  # vtkObjects have no Delete in Python -- maybe is not needed
        del VTKCache[node.node_id]
    print( "node_deleted", node.bl_label, node.node_id )

def get_node( node_id ):
    ''' to be called form operators
    retrieve the node with the given node_id.'''
    node = NodesMap.get(node_id)
    if node is None:
        print( "get_node - node not found, node_id=", node_id )
    return node

def get_vtkobj(node):
    ''' get the vtk-object associated to a node'''
    if node is None :
        print( "get_vtkobj - bad node" )
        return None 
    if not node.node_id in VTKCache:
        print( "get_vtkobj - node_id not in cache", node.node_id )
        return None 
    return VTKCache[node.node_id]

def init_cache():
    global NodesMaxId, NodesMap, VTKCache  
    print( "init_cache")
    NodesMaxId = 1
    NodesMap   = {}
    VTKCache   = {}
    for nt in bpy.data.node_groups:
        if nt.bl_idname == "VTKTreeType":
            for n in nt.nodes:
                node_created(n)
    print_nodes()

def check_cache():
    ''' called by all operators.
    if an operator is called a button exist, 
    if at the same time NodesMaxId == 1
    this mean that the Cache is out of sinc (this happen after reloading addons). 
    We must rebuild the cache, and the operator must be interrupted.
    ( the next try will work )
    ''' 
    if NodesMaxId > 1:
        return True
    else:        
        init_cache()
        return False #- abort operator -- user may retry

#---------------------------------------------------------------------------------
# OperatorNodeUpdate 
#---------------------------------------------------------------------------------
class OperatorNodeUpdate(bpy.types.Operator):
    
    bl_idname = "node.update"
    bl_label  = "update"
    node_id = bpy.props.IntProperty()
 
    def execute(self, context):
        if check_cache():
            node = get_node(self.node_id)
            if node:
                on_update(node) 
        return{'FINISHED'}    

#---------------------------------------------------------------------------------
# OperatorFileChoose
#---------------------------------------------------------------------------------
class OperatorFileChoose(bpy.types.Operator):
    bl_idname = "node.filechoose"
    bl_label = "choose file"
    node_id  = bpy.props.IntProperty()
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        if check_cache():
            node = get_node( self.node_id )
            if node: node.on_filename( self.filepath )
        return{'FINISHED'}    
    
#---------------------------------------------------------------------------------
# OperatorPrint
#---------------------------------------------------------------------------------
class OperatorPrint(bpy.types.Operator):
    bl_idname = "node.print"
    bl_label  = "print"
    node_id   = bpy.props.IntProperty()

    def execute(self, context):
        if check_cache():
            node = get_node( self.node_id )
            if node is None:
                print("OperatorPrint -- no node", self.node_id)
            else:
                print("=====PRINT NODE", node.name, "id=", node.node_id)
                print( node.get_vtkobj() )
                print("=====")
        return{'FINISHED'}    
    
#---------------------------------------------------------------------------------
# VTKTree
#---------------------------------------------------------------------------------
class VTKTree(NodeTree):
    '''vtk nodes'''             # description string - used for tooltip
    bl_idname = 'VTKTreeType'   # typename string - defaults to class name
    bl_label  = 'VTK'           # label
    bl_icon   = 'COLOR_RED'     # icon

#---------------------------------------------------------------------------------
# Custom socket type
#---------------------------------------------------------------------------------
class VTKPolyDataSocket(NodeSocket):
    '''VTKPolyDataSocket'''             # description / tooltip
    bl_idname = 'VTKPolyDataSocketType' # typename 
    bl_label  = 'vtkPolyData Socket'    # label
    
    def draw(self, context, layout, node, text):
        layout.label(text)

    def draw_color(self, context, node):
        return (1.0, 0.4, 0.216, 0.5)


class VTKImageDataSocket(NodeSocket):
    '''VTKImageDataSocket'''             # description / tooltip
    bl_idname = 'VTKImageDataSocketType' # typename 
    bl_label  = 'vtkImageData Socket'    # label
    
    def draw(self, context, layout, node, text):
        layout.label(text)

    def draw_color(self, context, node):
        return (0.4, 1.0, 0.216, 0.5)

#---------------------------------------------------------------------------------
# base class for all VTKNodes
#---------------------------------------------------------------------------------
class VTKTreeNode:

    node_id   = bpy.props.IntProperty( default=0 )

    @classmethod
    def poll(cls, ntree): # required
        return ntree.bl_idname == 'VTKTreeNodeType' # ??

    def free(self):
        node_deleted( self )

    def get_input_node(self):
        if not "in" in self.inputs:
            return None
        if not self.inputs["in"].is_linked:
            print( self.name, 'get_input_node --- no input')
            return None
        input_node = self.inputs["in"].links[0].from_node
        if input_node is None:
            print( self.name, 'get_input_node --- no input node')
            return None
        return input_node

    def get_vtkobj(self): # just a shortcut 
        return get_vtkobj( self ) 

    def draw_buttons(self, context, layout):
        for x in self.m_properties() :
            layout.prop(self, x )
        #layout.operator("node.print").node_id = self.node_id

    def copy(self, node):
        for x in self.m_properties() :
            exec(  'self.'+x+'=node.'+x, globals(), locals() )

    def apply_properties(self,vtkobj):
        for x in self.m_properties() :
            if x.startswith('e_'):
                value = getattr( self, x )
                cmd = 'vtkobj.Set'+x[2:]+'To'+value+'()'
            else:
                cmd = 'vtkobj.Set'+x[2:]+'(self.'+x+')'
            exec(  cmd, globals(), locals() ) 

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )

    def on_filename( self, filepath ):
        self.m_FilePath = filepath
        self.m_FileName = filepath.split('/')[-1]
        
                
#---------------------------------------------------------------------------------
class VTKReaderNode(VTKTreeNode):

    m_FilePath = bpy.props.StringProperty(              default="" )
    m_FileName = bpy.props.StringProperty( name='File', default="" )

    def draw_buttons(self, context, layout):
        for x in self.m_properties() :
            if x == 'm_FileName':
               layout.prop(self, "m_FileName") 
               layout.operator("node.filechoose" ).node_id = self.node_id
            else:
                layout.prop(self, x )

    def copy(self, node):
        for x in self.m_properties() :
            if x == 'm_FileName':
                self.m_FilePath = node.m_FilePath
                self.m_FileName = node.m_FileName
            else:
                exec(  'self.'+x+'=node.'+x, globals(), locals() )

    def apply_properties(self,vtkobj):
        for x in self.m_properties() :
            if x == 'm_FileName':
                vtkobj.SetFileName( self.m_FilePath )
                continue
            elif x.startswith('e_'):
                value = getattr( self, x )
                cmd = 'vtkobj.Set'+x[2:]+'To'+value+'()'
            else:
                cmd = 'vtkobj.Set'+x[2:]+'(self.'+x+')'
            exec(  cmd, globals(), locals() ) 

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )

    def on_filename( self, filepath ):
        self.m_FilePath = filepath
        self.m_FileName = filepath.split('/')[-1]
        

#---------------------------------------------------------------------------------
class VTKWriterNode(VTKTreeNode):

    m_FilePath = bpy.props.StringProperty(              default="" )
    m_FileName = bpy.props.StringProperty( name='File', default="" )

    def draw_buttons(self, context, layout):
        for x in self.m_properties() :
            if x == 'm_FileName':
               layout.prop(self, "m_FileName") 
               layout.operator("node.filechoose" ).node_id = self.node_id
            else:
                layout.prop(self, x )

    def copy(self, node):
        for x in self.m_properties() :
            if x == 'm_FileName':
                self.m_FilePath = node.m_FilePath
                self.m_FileName = node.m_FileName
            else:
                exec(  'self.'+x+'=node.'+x, globals(), locals() )

    def apply_properties(self,vtkobj):
        for x in self.m_properties() :
            if x == 'm_FileName':
                vtkobj.SetFileName( self.m_FilePath )
                continue
            elif x.startswith('e_'):
                value = getattr( self, x )
                cmd = 'vtkobj.Set'+x[2:]+'To'+value+'()'
            else:
                cmd = 'vtkobj.Set'+x[2:]+'(self.'+x+')'
            exec(  cmd, globals(), locals() ) 

    def init(self, context):
        self.width = 200
        self.inputs.new('VTKPolyDataSocketType', "in")
        node_created( self )

    def on_filename( self, filepath ):
        self.m_FilePath = filepath
        self.m_FileName = filepath.split('/')[-1]

#---------------------------------------------------------------------------------
class VTKFilter1Node(VTKTreeNode):

    def init(self, context):
        self.width = 200
        self.inputs.new( 'VTKPolyDataSocketType', "in")
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )


#---------------------------------------------------------------------------------
# on_update 
#---------------------------------------------------------------------------------
def on_update( node ):
    ''' updates all the pipeline entering node, then execute it '''  
    print( 'on_update', node.name )

    input_node = node.get_input_node()
    vtkobj = get_vtkobj( node )
    in_obj = None

    #print('vtkobj', not vtkobj     is None)
    #print('in_nod', not input_node is None)

    if input_node:
        on_update(input_node)
        in_obj = get_vtkobj( input_node )
        if vtkobj:
            if in_obj:
                vtkobj.SetInputConnection( in_obj.GetOutputPort() )
            else:
                vtkobj.SetInputConnection( 0 )        

    #print('in_obj', not in_obj is None)

    if node.bl_idname == "VTK2BlenderType":
        if in_obj:
            vtkdata_to_blender( in_obj.GetOutput(), node.m_Name )
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
    else:
        if vtkobj:
            node.apply_properties( vtkobj )
            vtkobj.Update()

#---------------------------------------------------------------------------------
# Registering
#---------------------------------------------------------------------------------
CLASSES = [ 
    VTKTree,
    OperatorNodeUpdate,
    OperatorFileChoose,
    OperatorPrint,
    VTKPolyDataSocket,
    VTKImageDataSocket,
    ]

#---------------------------------------------------------------------------------
# VTKNodeCategory
#---------------------------------------------------------------------------------
class VTKNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'VTKTreeType'

CATEGORIES = []            

#---------------------------------------------------------------------------------
# vtkdata_to_blender
#---------------------------------------------------------------------------------
def vtkdata_to_blender( data, name ):
    ''' convert the given vtkdata 
        creating or overwriting a blender object named "name" '''
    import bmesh

    me = bpy.data.meshes.get(name)
    if me is None:
        me = bpy.data.meshes.new(name)

    ob = bpy.data.objects.get(name)
    if ob is None:
        ob = bpy.data.objects.new( name, me )
        bpy.context.scene.objects.link(ob)     

    if data:
        err = 0
        bm = bmesh.new() # create an empty BMesh
        #bm.from_mesh(me) # fill it in from a Mesh
        data_p = data.GetPoints()
        verts = [ bm.verts.new( data_p.GetPoint(i) ) for i in range(data.GetNumberOfPoints())]    
        for i in range( data.GetNumberOfCells() ):
            data_pi = data.GetCell(i).GetPointIds()
            try:
                # it complains if a face is already existing
                bm.faces.new( [ verts[data_pi.GetId(x)] for x in range(data_pi.GetNumberOfIds()) ] )
            except:
                err += 1
        if err:
            print( 'num err', err )

        bm.to_mesh(me) # store bmesh to mesh
        print('vtkdata_to_blender -- ok!  -- num verts =', len(verts) )
    else:
        print('vtkdata_to_blender -- no data!')
    return ob

#---------------------------------------------------------------------------------
# debug utilities
#---------------------------------------------------------------------------------
def ls(o):
    print('\n'.join(sorted(dir(o))))

def print_cls(obj):
    print( "------------------------------" )
    print( "Class =",obj.__class__.__name__ )
    print( "------------------------------" )
    for m in sorted(dir(obj)):
        if not m.startswith('__'):
            attr = getattr(obj,m)
            rep = str(attr)
            if len(rep) > 100:
                rep = rep[:100] + '  [...]'
            print (m.ljust(30),"=",rep )

def print_nodes(): 
    print( "########################")
    for nt in bpy.data.node_groups:
        if nt.bl_idname == "VTKTreeType":
            print( "## tree", nt.name)
            for n in nt.nodes:
                if get_vtkobj(n) is None:
                    x = "vtkObj:NO"
                else:
                    x = 'vtkobj:ok'
                print( "##    node", n.node_id, n.name.ljust(30,'.'), x )
    print( "########################")



