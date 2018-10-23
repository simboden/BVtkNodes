from .core import *
from . import favorites_data

favorites = favorites_data.favorites # must be an array of (node.bl_idname, node.bl_label) tuples
favorites_file = favorites_data.__file__

# ---------------------------------------------------------------------------------
# Favorites panel
# ---------------------------------------------------------------------------------

class VTKFavoritesPanel(bpy.types.Panel):
    """Information about active node's vtk object"""
    bl_label = 'Favorites'
    bl_idname = 'vtk_favorites'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'  # 'UI'
    bl_category = 'favorites'

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'VTKTreeType'

    def draw(self, context):
        global favorites
        active_node = context.active_node
        layout = self.layout
        if active_node:
            add = layout.operator('vtk.update_favorites', icon='ZOOMIN', text=active_node.bl_label)
            add.label = active_node.bl_label
            add.type = active_node.bl_idname
            layout.separator()
        for f in favorites:
            row = layout.row(align=True)
            remove = row.operator('vtk.update_favorites', icon='PANEL_CLOSE', text='')
            remove.label = f[1]
            remove.type = f[0]
            remove.remove = True
            op = row.operator('node.add_node', text=f[1])
            op.type = f[0]
            op.use_transform = True


add_ui_class(VTKFavoritesPanel)

# ---------------------------------------------------------------------------------
# Update favorite op
# ---------------------------------------------------------------------------------


class VTKUpdateFavorites(bpy.types.Operator):
    bl_idname = 'vtk.update_favorites'
    bl_label = 'add/remove favorites'

    remove = bpy.props.BoolProperty(default=False)
    label = bpy.props.StringProperty()
    type = bpy.props.StringProperty()

    def execute(self, context):
        global favorites
        global favorites_file
        fav = (self.type, self.label)
        if self.remove:
            favorites.remove(fav)
        else:
            if fav in favorites:
                self.report({'INFO'}, 'Already in favorites')
                return {'FINISHED'}
            favorites.append(fav)
        open(favorites_file, 'w').write('favorites = ' + repr(favorites).replace('),', '),\n'))
        self.remove = False
        return {'FINISHED'}


add_ui_class(VTKUpdateFavorites)
