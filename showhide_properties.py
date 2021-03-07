from .core import l # Import logging
from . import core
import bpy
from .cache import BVTKCache

class BVTK_PT_ShowHide_Properties(bpy.types.Panel):
    '''BVTK Show/hide properties panel'''
    bl_label = 'Show/Hide Properties'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Properties'

    @classmethod
    def poll(cls, context):
        return  context.active_node is not None and \
                context.space_data.tree_type == 'BVTK_NodeTreeType' and \
                hasattr(context.active_node, 'b_properties')

    def draw(self, context):
        layout = self.layout
        active_node = context.active_node
        m_properties = context.active_node.m_properties()
        for i in range(len(m_properties)):
            row = layout.row()
            row.prop(active_node, 'b_properties', index=i)

            # There seems to be something strange with Python type annotations:
            # getattr does not find annotations, so here is workaround.
            # TODO: Is it a bug in Python 3.7.0? This is ugly.
            # prop_dict = getattr(core.CLASSES[active_node.bl_idname], m_properties[i])[1] # OLD
            mp = m_properties[i]
            if mp in core.CLASSES[active_node.bl_idname].__annotations__:
                prop_dict = core.CLASSES[active_node.bl_idname].__annotations__[mp][1]
                if 'name' in prop_dict:  # collection properties don't have name
                    row.label(text=prop_dict['name'])
                elif 'attr' in prop_dict:
                    row.label(text=prop_dict['attr'][2:]) # removing first chars 'm_'
                else:
                    l.error("Broken dict " + str(prop_dict))
        # Custom code editing operators
        row = layout.row()
        row.operator("node.bvtk_custom_code_edit", text="Edit Custom Code")
        row = layout.row()
        row.operator("node.bvtk_custom_code_save", text="Save Custom Code")


class BVTK_OT_Edit_Custom_Code(bpy.types.Operator):
    '''Edit Custom Code text string for Active Node in Text Editor'''
    bl_idname = "node.bvtk_custom_code_edit"
    bl_label = "Edit Custom Code"
    node_id: bpy.props.IntProperty(default=0) # Used to save node button press is from

    def execute(self, context):
        if self.node_id == 0: # Call from properities panel
            active_node = context.active_node
        else: # Call from node
            # Get node based on node_id tag and make it active
            BVTKCache.check_cache()
            active_node = BVTKCache.get_node(self.node_id)
            active_node.select = True
            
            nt = BVTKCache.get_tree(self.node_id)
            nt.nodes.active = active_node

        name = 'BVTK'
        if name not in bpy.data.texts.keys():
            text = bpy.data.texts.new(name)
        else:
            text = bpy.data.texts[name]
        text.from_string(active_node.custom_code)
        flag = True
        areas = context.screen.areas
        for area in areas:
            if area.type == 'TEXT_EDITOR':
                for space in area.spaces:
                    if space.type == 'TEXT_EDITOR':
                        if flag:
                            space.text = text
                            space.top = 0
                            flag = False
        self.report({'INFO'}, "Edit node %r " % active_node.name \
                    + "in text editor %r" % name)
        return {'FINISHED'}


class BVTK_OT_Save_Custom_Code(bpy.types.Operator):
    '''Save Custom Code text from Text Editor to Active Node'''
    bl_idname = "node.bvtk_custom_code_save"
    bl_label = "Save Custom Code"
    node_id: bpy.props.IntProperty(default=0) # Used to save node button press is from

    def execute(self, context):
        if self.node_id == 0: # Call from properities panel
            active_node = context.active_node
        else: # Call from node
            # Get node based on node_id tag and make it active
            BVTKCache.check_cache()
            active_node = BVTKCache.get_node(self.node_id)
            active_node.select = True
            
            nt = BVTKCache.get_tree(self.node_id)
            nt.nodes.active = active_node

        name = 'BVTK'
        if name not in bpy.data.texts.keys():
            self.report({'ERROR'}, "No %r text found in text editor!" % name)
            return {'FINISHED'}
        else:
            active_node.custom_code = bpy.data.texts[name].as_string()
        self.report({'INFO'}, "Saved Custom Code from %r" % name)
        return {'FINISHED'}


core.add_ui_class(BVTK_PT_ShowHide_Properties)
core.add_class(BVTK_OT_Edit_Custom_Code)
core.add_class(BVTK_OT_Save_Custom_Code)
