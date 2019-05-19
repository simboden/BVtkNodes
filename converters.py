from .update import *
from .core import l # Import logging
from .core import *
import bmesh

# -----------------------------------------------------------------------------
# Converters from VTK to Blender
# -----------------------------------------------------------------------------

class BVTK_Node_VTKToBlender(Node, BVTK_Node):
    '''Convert output from VTK Node to Blender Mesh Object'''
    bl_idname = 'BVTK_Node_VTKToBlenderType' # type name
    bl_label  = 'VTK To Blender'  # label for nice name display

    m_Name: bpy.props.StringProperty(name='Name', default='mesh')
    smooth: bpy.props.BoolProperty(name='Smooth', default=False)
    generate_material: bpy.props.BoolProperty(name='Generate Material', default=False)

    def start_scan(self, context):
        if context:
            if self.auto_update:
                bpy.ops.node.bvtk_auto_update_scan(
                    node_name=self.name,
                    tree_name=context.space_data.node_tree.name)

    auto_update: bpy.props.BoolProperty(default=False, update=start_scan)

    def m_properties(self):
        return ['m_Name', 'smooth', 'generate_material']

    def m_connections(self):
        return ( ['input'],[],[],[] )

    def draw_buttons(self, context, layout):
        layout.prop(self, 'm_Name')
        layout.prop(self, 'auto_update', text='Auto update')
        layout.prop(self, 'smooth', text='Smooth')
        layout.prop(self, 'generate_material')
        layout.separator()
        layout.operator("node.bvtk_node_update", text="update").node_path = node_path(self)

    def update_cb(self):
        '''Update node'''
        input_node, vtkobj = self.get_input_node('input')
        ramp = None
        if input_node and input_node.bl_idname == 'BVTK_Node_ColorMapperType':
            ramp = input_node
            ramp.update()    # setting auto range
            input_node, vtkobj = input_node.get_input_node('input')
        if vtkobj:
            vtkobj = resolve_algorithm_output(vtkobj)
            vtkdata_to_blender(vtkobj, self.m_Name, ramp, self.smooth, self.generate_material)
            update_3d_view()

    def apply_properties(self, vtkobj):
        pass


def vtkdata_to_blender(data, name, ramp=None, smooth=False, generate_material=False):
    '''Convert VTK data to Blender mesh object, using optionally
    given color ramp and normal smoothing. Optionally generates default
    material, which includes also color information if ramp is given.
    '''
    if not data:
        l.error('no data!')
        return
    if issubclass(data.__class__, vtk.vtkImageData):
        imgdata_to_blender(data, name)
        return
    me, ob = mesh_and_object(name)
    if me.is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    err = 0 # Number of errors encountered
    bm = bmesh.new()
    # bm.from_mesh(me) # fill it in from a Mesh

    # Get vertices
    data_p = data.GetPoints()
    verts = [bm.verts.new(data_p.GetPoint(i)) for i in range(data.GetNumberOfPoints())]

    # Loop over cells to create edges and faces
    for i in range(data.GetNumberOfCells()):
        data_pi = data.GetCell(i).GetPointIds()
        # Error is raised if a face already exists. Count errors.
        try:
            face_verts = [verts[data_pi.GetId(x)] for x in range(data_pi.GetNumberOfIds())]
            if len(face_verts) == 2:
                e = bm.edges.new(face_verts)
            else:
                f = bm.faces.new(face_verts)
                f.smooth = smooth
        except:
            err += 1
    if err:
        l.error('number of errors: ' + str(err))

    # Set normals
    point_normals = data.GetPointData().GetNormals()
    cell_normals = data.GetCellData().GetNormals()
    if cell_normals:
        bm.faces.ensure_lookup_table()
        for i in range(len(bm.faces)):
            bm.faces[i].normal = cell_normals.GetTuple(i)
    if point_normals:
        for i in range(len(verts)):
            verts[i].normal = point_normals.GetTuple(i)

    # Set colors and color legend
    if ramp and ramp.color_by:
        texture = ramp.get_texture()
        l.debug("color_ramp is " + str(texture.color_ramp))
        if ramp.texture_type == 'IMAGE':
            image_width = 1000
            img = image_from_ramp(texture.color_ramp, texture.name, image_width)
            # TODO: Remove commented lines below
            # texture = get_item(bpy.data.textures, texture.name+'IMAGE', 'IMAGE')
            # texture.image = img
        # texture_material(me, 'VTK'+name, texture)

        # Color legend
        vrange = (ramp.min, ramp.max)
        if ramp.lut:
            create_lut(name, vrange, 6, texture, h=ramp.height)

        # Generate UV maps to get coloring either by points or faces
        bm.verts.index_update()
        bm.faces.index_update()
        if ramp.color_by[0] == 'P':
            bm = point_unwrap(bm, data, int(ramp.color_by[1:]), vrange)
        else:
            bm = face_unwrap(bm, data, int(ramp.color_by[1:]), vrange)

    # Generate default material if wanted
    if generate_material and ramp and ramp.color_by:
        create_material(ob, texture.name)
    elif generate_material:
        create_material(ob, None)

    bm.to_mesh(me)  # store bmesh to mesh

    l.info('conversion successful, verts = ' + str(len(verts)))

    #if (autoCenter):
    #    bpy.data.objects[me.name].select = True
    #    context.scene.objects.active = bpy.data.objects[me.name]
    #    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')


# -----------------------------------------------------------------------------
# Auto update scan functions
# -----------------------------------------------------------------------------

def map(node, pmap = None):
    '''Create node property map (pmap). The map represent the status
    (m_properties and inputs) of every preceding node connected
    to node.
    '''
    # {} map:        node name -> (nodeprops, nodeinputs)
    # {} nodeprops:  property name -> property value
    # {} nodeinputs: input name -> connected node name

    if not pmap:
        pmap = {}
    props = {}
    for prop in node.m_properties():
        val = getattr(node, prop)
        # Special for arrays. Any other type to include?
        if val.__class__.__name__ == 'bpy_prop_array':
            val = [x for x in val]
        props[prop] = val

    if hasattr(node, 'special_properties'):
        # you can add to a node a function called special_properties
        # to make auto update notice differences outside of m_properties
        props['special_properties'] = node.special_properties()

    links = {}
    for input in node.inputs:
        links[input.name] = ''
        for link in input.links:
            links[input.name] = link.from_node.name
            pmap = map(link.from_node, pmap)
    pmap[node.name] = (props, links)
    return pmap


def differences(map1, map2):
    '''Generate differences in properties and inputs of argument maps'''
    props = {}   # differences in properties
    inputs = {}  # differences in inputs
    for node in map1:
        nodeprops1, nodeinputs1 = map1[node]
        if node not in map2:
            props[node] = nodeprops1.keys()
            inputs[node] = nodeinputs1.keys()
        else:
            nodeprops2, nodeinputs2 = map2[node]
            props[node] = compare(nodeprops1, nodeprops2)
            if not props[node]:
                props.pop(node)
            inputs[node] = compare(nodeinputs1, nodeinputs2)
            if not inputs[node]:
                inputs.pop(node)
    return props, inputs


def compare(dict1, dict2):
    '''Compare two dictionaries. Return a list of mismatching keys'''
    diff = []
    for k in dict1:
        if k not in dict2:
            diff.append(k)
        else:
            val1 = dict1[k]
            val2 = dict2[k]
            if val1 != val2:
                diff.append(k)
    for k in dict2:
        if k not in dict1:
            diff.append(k)
    return diff


class BVTK_OT_AutoUpdateScan(bpy.types.Operator):
    '''BVTK Auto Update Scan'''
    bl_idname = "node.bvtk_auto_update_scan"
    bl_label = "Auto Update"

    _timer = None
    node_name: bpy.props.StringProperty()
    tree_name: bpy.props.StringProperty()

    def modal(self, context, event):
        if event.type == 'TIMER':
            if self.node_is_valid():
                actual_map = map(self.node)
                props, conn = differences(actual_map, self.last_map)
                if props or conn:
                    self.last_map = actual_map
                    check_cache()
                    try:
                        no_queue_update(self.node, self.node.update_cb)
                    except Exception as e:
                        l.error('ERROR UPDATING ' + str(e))
            else:
                self.cancel(context)
                return {'CANCELLED'}
        return {'PASS_THROUGH'}

    def node_is_valid(self):
        '''Node validity test. Return false if node has been deleted or auto
        update has been turned off.
        '''
        return self.node.name in self.tree and self.node.auto_update

    def execute(self, context):
        self.tree = bpy.data.node_groups[self.tree_name].nodes
        self.node = bpy.data.node_groups[self.tree_name].nodes[self.node_name]
        self.last_map = map(self.node)
        bpy.ops.node.bvtk_node_update(node_path=node_path(self.node))
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)



# -----------------------------------------------------------------------------
# Help functions
# -----------------------------------------------------------------------------


def mesh_and_object(name):
    '''Get mesh object and mesh'''
    me = get_item(bpy.data.meshes, name)
    ob = get_object(name, me)
    return me, ob


def get_item(data, *args):
    '''Get or create item with key args[0] from data'''
    item = data.get(args[0])
    if not item:
        item = data.new(*args)
    return item


def set_link(data, item):
    '''Link item to data'''
    if item.name not in data:
        data.link(item)


def get_object(name, data):
    '''Initialize mesh object name with data into current scene'''
    ob = get_item(bpy.data.objects, name, data)
    ob.data = data
    set_link(bpy.context.collection.objects, ob)
    return ob


def texture_material(me, name, texture=None, texturetype='IMAGE'):
    '''Get or create a material and link with given texture,
    then apply it to given object.
    '''
    # TODO: Remove this function after image textures work OK
    l.error("Blender 2.8 no longer supports brush textures to be used for texturing via mat.texture_slots, that was only for Blender Internal")
    return None, None

    if not texture:
        texture = get_item(bpy.data.textures, name, texturetype)
        texture.type = texturetype
    mat = get_item(bpy.data.materials, name)
    if mat.name not in me.materials:
        me.materials.append(mat)
    # Disable other textures
    for ts in mat.texture_slots:
        if ts:
            ts.use = False
    if texture.name not in mat.texture_slots:
        ts=mat.texture_slots.add()
        ts.texture = texture
        ts.texture_coords = 'UV'
    else:
        ts = mat.texture_slots[texture.name]
    ts.use = True

    return texture, mat

def create_material(ob, texture_name=None):
    '''Create default material for final output node mesh object.
    Add image coloring nodes if texture name is given.
    '''

    if ob.name in bpy.data.materials:
        mat = bpy.data.materials[ob.name]
    else:
        mat = bpy.data.materials.new(name=ob.name)
    if not mat.use_nodes:
        mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links

    # Delete existing nodes
    for i in nodes:
        nodes.remove(i)

    node1 = nodes.new('ShaderNodeOutputMaterial')
    node1.location = (300, 300)

    node2 = nodes.new('ShaderNodeBsdfPrincipled')
    node2.location = (0, 300)
    links.new(node2.outputs['BSDF'], node1.inputs['Surface'])

    # Add UV related nodes for colored materials
    if texture_name:
        node3 = nodes.new('ShaderNodeTexImage')
        node3.image = bpy.data.images[texture_name]
        node3.location = (-300, 300)
        links.new(node3.outputs['Color'], node2.inputs['Base Color'])

        node4 = nodes.new('ShaderNodeMapping')
        node4.location = (-700, 300)
        links.new(node4.outputs['Vector'], node3.inputs['Vector'])

        node5 = nodes.new('ShaderNodeTexCoord')
        node5.location = (-900, 300)
        links.new(node5.outputs['UV'], node4.inputs['Vector'])

    # Assign material
    if ob.data.materials:
        ob.data.materials[0] = mat
    else:
        ob.data.materials.append(mat)


def image_from_ramp(ramp, name, length):
    '''Create image (size 1 px) from color ramp'''
    # Blender requires minimum image height is 4 to show the image
    # TODO: Check if this is a Blender bug and report it.
    height = 4
    img = get_item(bpy.data.images, name, length, height)
    for j in range(length):
        for i,val in enumerate(ramp.evaluate(j/length)):
            for k in range(height):
                img.pixels[height*k*length + height*j + i] = val
        # TODO: Delete below
        #p.extend(ramp.evaluate(j/length))
    #img.pixels = p
    #return img


def face_unwrap(bm, data, array_index, vrange):
    '''Unwrap by cell data'''
    scalars=data.GetCellData().GetArray(array_index)
    if scalars is not None:
        min, max = vrange
        if max==min:
            l.error("can't unwrap -- values are constant -- range(" + str(min) + "," + str(max) + ")!")
            return bm
        uv_layer = bm.loops.layers.uv.verify()
        for face in bm.faces:
            for loop in face.loops:
                v = (scalars.GetValue(face.index) - min)/(max - min)
                v = min(0.999, max(0.001, v)) # Force value inside range
                loop[uv_layer].uv = (v, 0.5)
    return bm


def point_unwrap(bm, data, array_index, vrange):
    '''Unwrap by point data'''
    scalars=data.GetPointData().GetArray(array_index)
    if scalars is not None:
        min, max = vrange
        if max == min:
            l.error("can't unwrap -- values are constant -- range(" + str(min) + "," + str(max) + ")!")
            return bm
        uv_layer = bm.loops.layers.uv.verify()
        for face in bm.faces:
            for loop in face.loops:
                v = (scalars.GetValue(loop.vert.index) - min)/(max - min)
                v = min(0.999, max(0.001, v)) # Force value inside range
                loop[uv_layer].uv = (v, 0.5)
    return bm


# -----------------------------------------------------------------------------
# Color legend
# -----------------------------------------------------------------------------

def text(name, body):
    '''Get a text data block'''
    font = get_item(bpy.data.curves, name, 'FONT')
    ob = get_object(name, font)
    font.body = body
    return ob


def delete_texts(name):
    '''Delete text data block'''
    for ob in bpy.data.objects:
        if ob.name.startswith(name):
            curve = ob.data
            bpy.data.objects.remove(ob)
            bpy.data.curves.remove(curve)


def create_lut(name, vrange, n_div, texture, b=0.5, h=5.5, x=5, y=0, z=0, fontsize=0.35, roundto=2):
    '''Create value labels and color legends and add to current scene'''
    name = name + '_colormap'
    delete_texts(name + '_lab') # Delete old labels

    # Create plane and UVs
    plane = bmesh.new()
    plane.faces.new((
        plane.verts.new((0, 0, 0)),
        plane.verts.new((b, 0, 0)),
        plane.verts.new((b, 0, h)),
        plane.verts.new((0, 0, h)),
    ))
    uv_layer = plane.loops.layers.uv.verify()
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 1)
    plane.faces[0].loops[1][uv_layer].uv = (0, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 0)
    plane.faces[0].loops[3][uv_layer].uv = (1, 1)
    me, ob = mesh_and_object(name)
    plane.to_mesh(me)
    ob.location = x,y,z
    #texture_material(me, name, texture)

    # Calculate label interval
    min, max = vrange
    if min > max or h <= 0:
        l.error('vrange maximum greater than minimum')
        return
    import math
    idealspace = (max-min)/(h)
    exponent = math.floor(math.log10(idealspace))
    mantissa = idealspace/(10**exponent)
    if mantissa < 2.5:
        step = 10 ** exponent
    elif mantissa < 7.5:
        step = 5*10**exponent
    else:
        step = 10*10**exponent
    start = math.ceil(min/step)*step
    delta = max-min
    if step>delta:
        return
    starth = (h*(start-min))/delta
    steph = (h*step)/delta

    # Add labels as texts
    for i in range(int(math.floor((max-start)/step))+1):
        t = text(name+'_lab'+str(i), '{:.15}'.format(start+i*step))
        t.data.size = fontsize
        t.rotation_mode = 'XYZ'
        t.rotation_euler = (1.5707963705062866, 0.0, 0.0)
        t.location = b+b/5, 0, starth+steph*i
        t.parent = ob


# -----------------------------------------------------------------------------
#  Image data conversion
# -----------------------------------------------------------------------------

def imgdata_to_blender(data, name):
    '''Convert vtkImageData to a Blender image'''

    wm = bpy.context.window_manager
    scalars = data.GetPointData().GetScalars()

    # Generate image data to img
    dim = data.GetDimensions()
    z = 0
    wm.progress_begin(0, 100)
    if name in bpy.data.images:
        bpy.data.images.remove(bpy.data.images[name])
    img = bpy.data.images.new(name, dim[0], dim[1])
    l = scalars.GetNumberOfTuples()
    p = []
    prog = 0
    l_prog = 1
    for j in range(l):
        t = scalars.GetTuple(j)
        if len(t) == 1:
            p.extend([t[0] / 255, t[0] / 255, t[0] / 255, 1])
        else:
            alpha = 1 if len(t)<4 else t[3]/255
            p.extend([t[0]/255, t[1]/255, t[2]/255, alpha])

        prog = int(j/l*100)
        if prog != l_prog:
            l_prog = prog
            wm.progress_update(prog)
            l.debug('Converting to img: ' + str(prog) + '%')
    img.pixels = p
    wm.progress_end()
    l.info('Image data conversion succesful, num pixels = ' + str(l))

    # Create plane mesh with UVs to show the image
    spacing = data.GetSpacing()
    x = dim[0] * spacing[0]
    y = dim[1] * spacing[0]
    plane = bmesh.new()
    plane.faces.new((
        plane.verts.new((0, 0, 0)),
        plane.verts.new((x, 0, 0)),
        plane.verts.new((x, y, 0)),
        plane.verts.new((0, y, 0)),
    ))
    uv_layer = plane.loops.layers.uv.verify()
    plane.faces.ensure_lookup_table()
    plane.faces[0].loops[0][uv_layer].uv = (0, 0)
    plane.faces[0].loops[1][uv_layer].uv = (1, 0)
    plane.faces[0].loops[2][uv_layer].uv = (1, 1)
    plane.faces[0].loops[3][uv_layer].uv = (0, 1)
    me, ob = mesh_and_object(name)
    ob.location = data.GetOrigin()
    plane.to_mesh(me)
    #tex, mat = texture_material(me, 'VTK' + name)
    #mat.use_shadeless = True
    #tex.image = img


class BVTK_OT_NodeUpdate(bpy.types.Operator):
    '''Node Update Operator'''
    bl_idname = "node.bvtk_node_update"
    bl_label = "Update Node"

    node_path: bpy.props.StringProperty()
    use_queue: bpy.props.BoolProperty(default = True)

    def execute(self, context):
        check_cache()
        node = eval(self.node_path)
        if node:
            l.debug('Updating from node: '+ node.name)
            if self.use_queue:
                Update(node, node.update_cb)
            else:
                no_queue_update(node, node.update_cb)
        self.use_queue = True
        return {'FINISHED'}


# Add classes and menu items
TYPENAMES = []
add_class(BVTK_Node_VTKToBlender)
TYPENAMES.append('BVTK_Node_VTKToBlenderType')
menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Converters", "Converters", items=menu_items))

add_class(BVTK_OT_NodeUpdate)
add_ui_class(BVTK_OT_AutoUpdateScan)
add_ui_class(BVTK_OT_FunctionQueue) # CHECKME: Why does this not work in update.py?

