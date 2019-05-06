from . import core
import bpy

class BVTK_PT_ShowHide_Properties_Panel(bpy.types.Panel):
    '''BVTK Show/hide properties panel'''
    bl_label = 'Show/Hide Properties'
    bl_idname = 'BVTK_PT_Panel'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = 'properties'

    @classmethod
    def poll(cls, context):
        return  context.active_node is not None and \
                context.space_data.tree_type == 'VTKTreeType' and \
                hasattr(context.active_node, 'b_properties')

    def draw(self, context):
        layout = self.layout
        active_node = context.active_node
        m_properties = context.active_node.m_properties()
        for i in range(len(m_properties)):
            row = layout.row()
            row.prop(active_node, 'b_properties', index=i)
            prop_dict = getattr(core.CLASSES[active_node.bl_idname], m_properties[i])[1]
            if 'name' in prop_dict:  # collection properties don't have name
                row.label(prop_dict['name'])
            elif 'attr' in prop_dict:
                row.label(prop_dict['attr'][2:]) # removing first chars 'm_'


core.add_ui_class(BVTK_PT_ShowHide_Properties_Panel)
