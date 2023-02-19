import bpy
import bpy.utils.previews
from .core import *
from .cache import BVTKCache

# -----------------------------------------------------------------------------
# Debug panel and node documentation panel (information about
# active node's vtk object)
# -----------------------------------------------------------------------------
class BVTK_PT_Inspect(bpy.types.Panel):
    """Panel for operators which printing information about active node's
    VTK object
    """

    bl_label = "Inspect"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Inspect"

    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "BVTK_NodeTreeType"

    def draw(self, context):
        layout = self.layout
        from . import bl_info

        layout.label(
            text="BVTKNodes version: " + ".".join(str(i) for i in bl_info["version"])
        )
        layout.label(text="VTK version: " + vtk.vtkVersion().GetVTKVersion())

        layout.label(text="Update Mode:")
        layout.prop(context.scene.bvtknodes_settings, "update_mode", text="")
        layout.separator()

        active_node = context.active_node
        if not active_node:
            return None
        layout.operator("node.bvtk_node_update").node_path = node_path(active_node)

        vtkobj = active_node.get_vtk_obj()
        if vtkobj:
            column = layout.column(align=True)
            o = column.operator("node.bvtk_set_text_editor", text="Documentation")
            o.print = 0
            o = column.operator("node.bvtk_set_text_editor", text="Node Status")
            o.print = 1
            o = column.operator("node.bvtk_set_text_editor", text="Output Status")
            o.print = 2
            o = column.operator(
                "node.bvtk_open_website", text=" Online Documentation", icon="WORLD"
            )
            o.href = "https://www.vtk.org/doc/nightly/html/class{}.html".format(
                active_node.bl_label
            )
        else:
            layout.label(text="No active VTK node to inspect")


# -----------------------------------------------------------------------------
# Function to add buttons to Python Console header
# -----------------------------------------------------------------------------
def draw_console_header(self, context):
    node_tree = None
    for area in context.screen.areas:
        if area.type == "NODE_EDITOR":
            for space in area.spaces:
                if space.type == "NODE_EDITOR":
                    node_tree = space.node_tree.name

    if node_tree:
        self.layout.separator()
        row = self.layout.row(align=True)
        o = row.operator("console.insert", text="Get Node")
        o.text = "x=bpy.data.node_groups['" + node_tree + "'].nodes.active"
        o = row.operator("console.insert", text="Get VTK Object")
        o.text = (
            "x=bpy.data.node_groups['" + node_tree + "'].nodes.active.get_vtk_obj()"
        )
        o = row.operator("console.insert", text="Get Node Output")
        o.text = (
            "x=bpy.data.node_groups['"
            + node_tree
            + "'].nodes.active.get_vtk_obj().GetOutput()"
        )


# -----------------------------------------------------------------------------
# Operators
# -----------------------------------------------------------------------------
class BVTK_OT_SetTextEditor(bpy.types.Operator):
    """Add node info to the text editor"""

    bl_idname = "node.bvtk_set_text_editor"
    bl_label = "Print info (BVTK in text editor)"

    # 0 to print doc, 1 to print node status, 2 to print outputs status
    print: bpy.props.IntProperty(default=0)

    def execute(self, context):
        active_node = context.active_node
        vtkobj = active_node.get_vtk_obj()
        classname = vtkobj.__class__.__name__
        if self.print == 0:
            inner = self.text_block("DOCUMENTATION " + classname, str(vtkobj.__doc__))
        if self.print == 1:
            inner = self.text_block(classname, str(vtkobj))
        if self.print == 2:
            socketnames = active_node.get_output_socket_names()
            inner = ""
            for socketname in socketnames:
                vtk_output_obj = active_node.get_vtk_output_object(socketname)
                inner += self.text_block(socketname, str(vtk_output_obj))
        text = self.get_text("BVTK", inner)
        flag = True
        areas = context.screen.areas
        for area in areas:
            if area.type == "TEXT_EDITOR":
                for space in area.spaces:
                    if space.type == "TEXT_EDITOR":
                        if flag:
                            space.text = text
                            space.top = 0
                            flag = False
        if flag:
            self.report({"INFO"}, "See 'BVTK' in the text editor")
        return {"FINISHED"}

    def get_text(self, name, inner):
        """Get text object"""
        if name not in bpy.data.texts.keys():
            text = bpy.data.texts.new(name)
        else:
            text = bpy.data.texts[name]
        text.from_string(inner)
        return text

    def text_block(self, title, content):
        """Pretty print text content with title"""
        s = "-" * 50 + "\n" + title + "\n" + "-" * 50 + "\n" + content + "\n"
        if content == "None":
            s += "\n\n"
        return s


class BVTK_OT_OpenWebsite(bpy.types.Operator):
    bl_idname = "node.bvtk_open_website"
    bl_label = "Open Web Browser"
    bl_description = "Open web site in web browser"

    href: bpy.props.StringProperty()

    def execute(self, context):
        import webbrowser

        webbrowser.open(self.href)
        return {"FINISHED"}


# Register classes
add_ui_class(BVTK_PT_Inspect)
add_ui_class(BVTK_OT_SetTextEditor)
add_ui_class(BVTK_OT_OpenWebsite)
