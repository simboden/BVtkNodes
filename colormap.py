# -----------------------------------------------------------------------------
# Color map nodes and functions
# -----------------------------------------------------------------------------

from .core import *
from .cache import BVTKCache
import json
import os
import numpy as np
from .converters import get_vtk_array_data

current_dir = os.path.dirname(__file__)

with open(current_dir + '/colormaps/colormaps_hsv.json') as json_file:
    colormaps_hsv = json.load(json_file)

with open(current_dir + '/colormaps/colormaps_rgb.json') as json_file:
    colormaps_rgb = json.load(json_file)

def get_default_texture(name):
    '''Create and return a new color ramp BLEND type brush texture'''
    if name not in bpy.data.textures:
        tex = bpy.data.textures.new(name, 'BLEND')
    else:
        tex = bpy.data.textures[name]
    tex.use_color_ramp = True

    # Force saving of blend texture, so that ramp is correct when
    # blend file is loaded. TODO: Is there better way to fix this?
    tex.use_fake_user = True

    elements = tex.color_ramp.elements
    elements[0].color = (10 / 255, 10 / 255, 180 / 255, 1)
    elements[0].position = 0.05
    elements[1].color = (180 / 255, 10 / 255, 20 / 255, 1)
    elements[1].position = 0.95
    e = elements.new(0.425)
    e.color = (141 / 255, 176 / 255, 254 / 255, 1)
    e = elements.new(0.5)
    e.color = (221 / 255, 221 / 255, 221 / 255, 1)
    e = elements.new(0.575)
    e.color = (243 / 255, 148 / 255, 117 / 255, 1)
    return tex

def get_matplotlib_colormap(texture_name, cm_name, cm_nr_values):
    '''Create or modify a texture map according to the colormap given name'''
    if texture_name not in bpy.data.textures:
        tex = bpy.data.textures.new(texture_name, 'BLEND')
    else:
        tex = bpy.data.textures[texture_name]
    tex.use_color_ramp = True

    # Force saving of blend texture, so that ramp is correct when
    # blend file is loaded. TODO: Is there better way to fix this?
    tex.use_fake_user = True

    elements = tex.color_ramp.elements
    old_len = len(elements.items())

    #Fetch new colormap
    new_colors = np.array(colormaps_rgb[cm_name]).astype(np.float32)
    new_colors_nr = new_colors.shape[0]
    #Positions on the x-axis of the colors
    colors_cmap_x = np.linspace(0, 1, num=new_colors_nr)
    colors_x = np.linspace(0, 1, num=cm_nr_values+1)[:-1]
    real_colors_x = np.linspace(0, 1, num=cm_nr_values)
    #Interpolate to desired length
    new_colors_interp = np.stack([np.interp(real_colors_x, colors_cmap_x, new_colors[:, i]) for i in range(3)], axis=-1)
    new_colors_interp_w_alpha = np.concatenate([new_colors_interp, np.ones_like(new_colors_interp[:, :1])], axis=-1)

    #Delete old colors if too many
    [elements.remove(elements[0]) for i in range(old_len - cm_nr_values)]

    #Add new colors if too few
    [elements.new(colors_x[i]) for i in range(cm_nr_values - old_len)]

    elements.foreach_set('position', colors_x)
    elements.foreach_set('color', new_colors_interp_w_alpha.reshape([-1]))
    return tex



class BVTK_Node_ColorMapper(Node, BVTK_Node):
    '''BVTK Color Mapper Node'''
    bl_idname = 'BVTK_Node_ColorMapperType'
    bl_label  = 'Color Mapper'
    bl_description = 'Node which specifies the variable and value range for coloring of surfaces'

    my_texture_name: bpy.props.StringProperty(default="", name="Name of Blender Texture used for color information", update=BVTK_Node.outdate_vtk_status)
    lut: bpy.props.BoolProperty(default=False, name="Generate Scalar Bar", update=BVTK_Node.outdate_vtk_status) # Boolean to generate scalar bar
    height: bpy.props.FloatProperty(default=5.5, name="Scalar Bar Height", update=BVTK_Node.outdate_vtk_status)
    max: bpy.props.FloatProperty(default=0, update=BVTK_Node.outdate_vtk_status)
    min: bpy.props.FloatProperty(default=0, update=BVTK_Node.outdate_vtk_status)
    color_by: bpy.props.StringProperty(default="", name="Color By", update=BVTK_Node.outdate_vtk_status)
    auto_range: bpy.props.BoolProperty(default=True, name="Auto Range", update=BVTK_Node.outdate_vtk_status)


    def validate_and_update_values(self):
        '''Check that values entered in node are sane. Update range min and
        max if requested. Return error text if an error is found.
        '''
        if len(self.color_by) < 3:
            return "Error: Color By must start with 'P_' (for point data)\n" \
                + "or 'C_' (for cell data), followed by array name."

        type_letter = self.color_by[0]
        if type_letter in ('p', 'P'):
            array_type = 'Point data'
        elif type_letter in ('c', 'C'):
            array_type = 'Cell data'
        else:
            return "Error: Color By must start with 'P_' (for point data)\n" \
                + "or 'C_' (for cell data), followed by array name."

        array_name = self.color_by[2:]
        input_node, vtk_obj, vtk_connection = self.get_input_node_and_vtk_objects()
        vtk_output_obj = resolve_algorithm_output(vtk_connection)
        d = get_vtk_array_data(vtk_output_obj, array_name, type_letter)
        if not d:
            return "Error: " + array_type + " %r not found on input." % array_name

        # Update range
        if self.auto_range:
            range = d.GetRange()
            self.max = range[1]
            self.min = range[0]

        if self.min >= self.max:
            return "Error: Range min >= range max, can't unwrap."

        if len(self.inputs['lookuptable'].links) != 1:
            return "Error: No Color Ramp Node connected"

    def color_by_enum_generator(self, context=None):
        '''Enum list generator for color_by property.
        Generate array items available for coloring.
        '''

        items = [('None', 'Empty (clear value)', 'Empty (clear value)', ENUM_ICON, 0)]

        vtk_obj, vtk_connection = self.get_vtk_obj_and_connection()
        if vtk_connection:
            vtk_output_obj = resolve_algorithm_output(vtk_connection)
            if hasattr(vtk_output_obj, 'GetCellData'):
                c_data = vtk_output_obj.GetCellData()
                p_data = vtk_output_obj.GetPointData()
                c_descr = 'Color by cell data using '
                p_descr = 'Color by point data using '
                for i in range(p_data.GetNumberOfArrays()):
                    arr_name = str(p_data.GetArrayName(i))
                    items.append(('P_'+arr_name, arr_name, p_descr+arr_name+' array', 'VERTEXSEL', len(items)))
                for i in range(c_data.GetNumberOfArrays()):
                    arr_name = str(c_data.GetArrayName(i))
                    items.append(('C_'+arr_name, arr_name, c_descr+arr_name+' array', 'FACESEL', len(items)))
        return items

    def color_by_set_value(self, context=None):
        '''Set value of StringProprety using value from EnumProperty'''
        if self.color_by_enum == 'None':
            self.color_by = ""
        else:
            self.color_by = str(self.color_by_enum)

    color_by_enum: bpy.props.EnumProperty(items=color_by_enum_generator, update=color_by_set_value, name='Choices')

    def m_properties(self):
        return ['color_by', 'auto_range', 'lut', 'min', 'max', 'height']

    def m_connections(self):
        return (['input','lookuptable'],[],[],['output'])

    def apply_properties_special(self):
        '''Special apply properties function.
        '''
        vtk_obj, vtk_connection = self.get_vtk_obj_and_connection()

        if not vtk_obj:
            self.ui_message = 'Input has no VTK object'
            return 'error'
        if not vtk_connection:
            self.ui_message = 'Input has no VTK connection'
            return 'error'
        vtk_obj.Update()
        val = self.validate_and_update_values()
        if val:
            self.ui_message = val
            return 'error'
        return 'up-to-date'

    def get_texture(self):
        '''Dig up the texture from the Color Ramp node connected to lookuptable input.
        '''
        in_links = self.inputs['lookuptable'].links
        if len(in_links) > 0:
            return in_links[0].from_node.get_texture()
        if self.my_texture_name:
            if self.my_texture_name in bpy.data.textures:
                return bpy.data.textures[self.my_texture_name]
        new_texture = get_default_texture(self.name)
        self.my_texture_name = new_texture.name
        return new_texture

    def free(self):
        if self.my_texture_name:
            if self.my_texture_name in bpy.data.textures:
                bpy.data.textures.remove(bpy.data.textures[self.my_texture_name])
        BVTKCache.unmap_node(self)

    def draw_buttons_special(self, context, layout):
        layout.prop(self, 'lut')
        if self.lut:
            layout.prop(self, 'height')
        row = layout.row(align=True)
        row.prop(self, 'color_by')
        row.prop(self, 'color_by_enum', icon_only=True)

        layout.prop(self, 'auto_range')
        row = layout.row(align=True)
        row.enabled = not self.auto_range
        row.prop(self, 'min')
        row.prop(self, 'max')
        layout.separator()

    def init_vtk(self):
        self.vtk_status = 'out-of-date'
        vtk_obj = vtk.vtkPassThroughFilter() # Pass through all input to output
        return vtk_obj


class BVTK_Node_ColorRamp(Node, BVTK_Node):
    '''BVTK Color Ramp Node'''
    bl_idname = 'BVTK_Node_ColorRampType'
    bl_label  = 'Color Ramp'
    bl_description = 'Node for providing VTK Lookup Table for colors of a color palette'

    my_texture: bpy.props.StringProperty()

    def preset_name_from_ind(self, ind):
        return self.cm_preset_items[ind][0]

    def update_colorbar_preset(self, context):
        self.notify_downstream(vtk_status='out-of-date')
        # Custom color map will not be modified
        if self.cm_preset == 'custom':
            return
        new_texture = get_matplotlib_colormap(self.name, self.cm_preset, self.cm_nr_values)
        self.my_texture = new_texture.name

    def update_colorbar_nr(self, context):
        self.notify_downstream(vtk_status='out-of-date')
        # Custom color map will not be modified
        if self.cm_preset == 'custom':
            return
        self.update_colorbar_preset(context)

    cm_preset_items = [ (x,x,x) for x in ['custom'] + sorted(list(colormaps_rgb.keys()))]
    cm_preset: bpy.props.EnumProperty(name='Preset', default='custom', items=cm_preset_items, update=update_colorbar_preset)
    cm_nr_values: bpy.props.IntProperty(name='Number of Colors', default=8, max=32, min=2, update=update_colorbar_nr)
    b_properties: bpy.props.BoolVectorProperty(name="", size=32, get=BVTK_Node.get_b, set=BVTK_Node.set_b)

    def m_properties(self):
        return ['cm_preset', 'cm_nr_values']

    def m_connections(self):
        return ([],[],[],['lookupTable'])

    def copy_setup(self, node):
        '''Copy color ramp from argument node to self'''
        new_texture = get_default_texture(self.name)
        self.my_texture = new_texture.name
        old_texture = node.get_texture()
        if old_texture:
            elements = new_texture.color_ramp.elements
            new_elements = old_texture.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el.color
                    elements[i].position = new_el.position
                else:
                    e = elements.new(new_el.position)
                    e.color = new_el.color

    def get_texture(self):
        if self.my_texture not in bpy.data.textures.keys():
            return None
        return bpy.data.textures[self.my_texture]

    def free(self):
        if self.my_texture in bpy.data.textures:
            bpy.data.textures.remove(bpy.data.textures[self.my_texture])
        BVTKCache.unmap_node(self)

    def draw_buttons_special(self, context, layout):
        if self.my_texture in bpy.data.textures.keys():
            layout.template_color_ramp(bpy.data.textures[self.my_texture], "color_ramp", expand=False)
        row = layout.row()
        row.prop(self, 'cm_preset')
        row = layout.row()
        row.prop(self, 'cm_nr_values')

    def apply_properties_special(self):
        return 'up-to-date'

    def init_vtk(self):
        new_texture = get_default_texture(self.name)
        self.my_texture = new_texture.name
        lut = vtk.vtkLookupTable()
        lut.Build()
        return lut

    def special_properties(self):
        '''Make auto_update scanner notice changes in the color ramp'''
        raise Exception("Check is this needed any more")
        return self.export_properties()['elements']

    def export_properties(self):
        '''Export colormap properties. Called by export operator'''
        t = self.get_texture()
        if t:
            elements = t.color_ramp.elements
            e = [[[x for x in e.color], e.position] for e in elements]
        else:
            e = []
        return {'elements': e}

    def import_properties(self, dict):
        l.debug("importing colormap " + str(self.name))
        '''Import colormap properties. Called by import operator'''
        t = self.get_texture()
        new_elements = dict['elements']
        if t:
            elements = t.color_ramp.elements
            while len(elements) > len(new_elements):
                elements.remove(elements[0])
            for i, new_el in enumerate(new_elements):
                if i < len(elements):
                    elements[i].color = new_el[0]
                    elements[i].position = new_el[1]
                else:
                    e = elements.new(new_el[1])
                    e.color = new_el[0]


# Add classes and menu items
TYPENAMES = []
add_class(BVTK_Node_ColorMapper)
TYPENAMES.append('BVTK_Node_ColorMapperType')
add_class(BVTK_Node_ColorRamp)
TYPENAMES.append('BVTK_Node_ColorRampType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Color", "Color", items=menu_items))
