from .core import *    

class VTKStructuredPointsReader(Node, VTKTreeNode):

    bl_idname = 'VTKStructuredPointsReaderType'
    bl_label  = 'vtkStructuredPointsReader'

    m_FilePath = bpy.props.StringProperty(              default="" )
    m_FileName = bpy.props.StringProperty( name='File', default="" )

    def properties():
        return ['m_FilePath', 'm_FileName']

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )

    def draw_buttons(self, context, layout):
        layout.prop(self, "m_FileName")
        layout.operator("node.filechoose" ).node_id = self.node_id
        layout.operator("node.print").node_id = self.node_id

    def on_filename( self, filepath ):
        self.m_FilePath = filepath
        self.m_FileName = filepath.split('/')[-1]

    def apply_properties(self, vtkobj):
        vtkobj.SetFileName( self.m_FilePath ) # non standard 

CLASSES.append(    VTKStructuredPointsReader )
TYPENAMES.append( 'VTKStructuredPointsReaderType' )
