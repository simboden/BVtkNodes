from .core import *    

class VTK2Blender(Node, VTKTreeNode):

    bl_idname = 'VTK2BlenderType' # type name
    bl_label  = 'ToBlender'       # label for nice name display 
    m_Name = bpy.props.StringProperty( name="Name", default="mesh")

    def properties():
        return ['m_Name']

    def init(self, context):
        self.width = 150
        self.inputs.new('VTKPolyDataSocketType', "in")
        node_created( self )

    def draw_buttons(self, context, layout):
        layout.prop(self, "m_Name")
        layout.operator("node.update", text="update").node_id = self.node_id
        #layout.operator("node.print").node_id = self.node_id

    def apply_properties(self, vtkobj):
        pass

CLASSES.append  (  VTK2Blender )        
TYPENAMES.append( 'VTK2BlenderType' )