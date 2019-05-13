from .core import l # Import logging
from . import core
import bpy

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

core.add_ui_class(BVTK_PT_ShowHide_Properties)
