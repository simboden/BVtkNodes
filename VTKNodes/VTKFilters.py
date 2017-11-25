from .core import *    
TYPENAMES =[]

#----------------------------------------------------------------   
class VTKImageGaussianSmooth(Node, VTKTreeNode):

    bl_idname = 'VTKImageGaussianSmoothType'
    bl_label  = 'vtkImageGaussianSmooth'

    m_RadiusFactor      = bpy.props.FloatProperty(name = 'RadiusFactor',      default=1.1 )
    m_StandardDeviation = bpy.props.FloatProperty(name = 'StandardDeviation', default=1.1 )

    def properties( self ):
        return [ 'm_RadiusFactor', 'm_StandardDeviation' ] 

    def init(self, context):
        self.width = 200
        self.inputs.new ('VTKImageDataSocketType', "in")
        self.outputs.new('VTKImageDataSocketType', "out")
        node_created( self )

CLASSES.append( VTKImageGaussianSmooth )
TYPENAMES.append( 'VTKImageGaussianSmoothType' )

#-------------------------------------------------------------    
class VTKContourFilter(Node, VTKTreeNode):

    bl_idname = 'VTKContourFilterType'
    bl_label  = 'vtkContourFilter'
    m_Value = bpy.props.FloatProperty( name="IsoValue", default=0)

    def properties(self):
        return ['m_Value']

    def init(self, context):
        self.width = 200
        self.inputs.new ('VTKImageDataSocketType', "in")
        self.outputs.new('VTKPolyDataSocketType',  "out")
        node_created( self )

    def apply_properties(self,vtkobj):
        vtkobj.SetValue(0, self.m_Value ) # non standard syntax

CLASSES.append( VTKContourFilter )  
TYPENAMES.append( 'VTKContourFilterType' )     

#-------------------------------------------------------------    
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory("filters", "filters", items=menu_items) )