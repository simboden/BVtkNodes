from .core import *    

class VTKImageGaussianSmooth(Node, VTKTreeNode):

    bl_idname = 'VTKImageGaussianSmoothType'
    bl_label  = 'vtkImageGaussianSmooth'

    m_RadiusFactor      = bpy.props.FloatProperty(name = 'RadiusFactor',      default=1.1 )
    m_StandardDeviation = bpy.props.FloatProperty(name = 'StandardDeviation', default=1.1 )

    def properties( self ):
        return [ 'm_RadiusFactor', 'm_StandardDeviation' ] 

    def init(self, context):
        self.width = 200
        self.inputs.new ('VTKPolyDataSocketType', "in")
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )

CLASSES.append( VTKImageGaussianSmooth )
TYPENAMES.append( 'VTKImageGaussianSmoothType' )

