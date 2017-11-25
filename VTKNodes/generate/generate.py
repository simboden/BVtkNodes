import vtk
from jinja2 import Template

def ls( lst ):
    print( '\n'.join( sorted( lst ))) 

HiddenMethods = (
'AbortExecuteOff',
'AbortExecuteOn',
'AddObserver',
'BreakOnError',
'ComputeInputUpdateExtents',
'DebugOff',
'DebugOn',
'Delete',
'EnlargeOutputUpdateExtents',
'GetAbortExecute',
'GetAddressAsString',
'GetClassName',
'GetDebug',
'GetErrorCode',
'GetGlobalWarningDisplay',
'GetMTime',
'GetOutputIndex',
'GetProgress',
'GetProgressMaxValue',
'GetProgressText',
'GetReferenceCount',
'GetReleaseDataFlag',
'GlobalWarningDisplayOn',
'GlobalWarningDisplayOff',
'HasObserver',
'InRegisterLoop',
'InvokeEvent',
'IsA',
'IsTypeOf',
'New',
'NewInstance',
'PrintRevisions',
'PropagateUpdateExtent',
'Register',
'ReleaseDataFlagOff',
'ReleaseDataFlagOn',
'RemoveAllInputs',
'RemoveObserver',
'RemoveObservers',
'SetAbortExecute',
'SafeDownCast',
'SetDebug',
'SetEndMethod',
'SetGlobalWarningDisplay',
'SetProgress',
'SetProgress',
'SetProgressMethod',
'SetProgressText',
'SetReleaseDataFlag',
'SetReferenceCount',
'SetStartMethod',
'SqueezeInputArray',
'TriggerAsynchronousUpdate',
'UnRegister',
'UnRegisterAllOutputs',
'UpdateData',
'UpdateInformation',
'UpdateProgress',
'UpdateWholeExtent',

'GetUserTransformMatrixMTime',
'ReleaseGraphicsResources',
'RenderOpaqueGeometry',
'RenderTranslucentGeometry',

'ApplyProperties',
'ComputeMatrix',
'ShallowCopy',
)

HiddenProp = (
'ArrayComponent',
'ComputeGradients',
'ComputeNormals',
'ComputeScalars',
'Executive',
'GenerateTriangles',
'Information',
'InputConnection',
'InputDataObject',
'Locator',
'NumberOfContours',
'Output', ###
'OutputPointsPrecision',
'ProgressObserver',
'ScalarTree',
'UpdateExtent',
'UseScalarTree',
)

TypeMap = {}
TypeMap['string']                               = ('StringProperty',       1 )
TypeMap['bool']                                 = ('BoolProperty',         1 )
TypeMap['int']                                  = ('IntProperty',          1 )
TypeMap['int,int']                              = ('IntVectorProperty',    2 )
TypeMap['int,int,int']                          = ('IntVectorProperty',    3 )
TypeMap['float']                                = ('FloatProperty',        1 )
TypeMap['float,float']                          = ('FloatVectorProperty',  2 )
TypeMap['float,float,float']                    = ('FloatVectorProperty',  3 )
TypeMap['float,float,float,float,float,float']  = ('FloatVectorProperty',  6 )
TypeMap['enum']                                 = ('EnumProperty',         1 )

def find_properties( name ):
    print()
    print(name)

    # instantiate the class
    c = getattr( vtk, name )
    if c is None: return None
    o = c()

    # retrieve the interesting methods
    m = [ x for x in dir(o) if not x.startswith('__') and not x in HiddenMethods and not x[3:] in HiddenProp ]
    m.sort()

    # init our output
    props = {}
    props['NAME'  ] = name[3:]
    props['PROPS' ] = []

    # scan methods searching for properties
    for x in m:
        if x.startswith('Set') and 'Get'+x[3:] in m : # if method is a Setter and there is a matching Getter
            p = x[3:]
            setter = getattr(o, 'Set'+p )
            getter = getattr(o, 'Get'+p )

            # the first line in the method doc is the python-function-signature --- example: SetXXX(int) -- GetXXX()->int
            setter_doc = setter.__doc__.split('\n')[0]
            getter_doc = getter.__doc__.split('\n')[0]

            # extract the arguments.
            # sometime getter have no '->' - meaning that they return the value in the arguments,
            # in some case these properties are reduntant, so lets ignore them
            setter_arg = setter_doc.split('(')[1].replace(')','').replace(' ','')                      
            if '>' in getter_doc:
                getter_arg = getter_doc.split('>')[1].replace(')','').replace('(','').replace(' ','')  
            else:
                getter_arg = "none"

            # setter and getter args should match
            if setter_arg != getter_arg:
                print( 'ko ', p.ljust(30), setter_doc.ljust(50), getter_doc.ljust(50), 'arg mismatch')
            else:
                # if there are also the methods p+On and p+Off this property is a bool
                if p+'On' in m and p+'Off' in m :
                    setter_arg = 'bool'

                # if there are also methods Set+p+To+xxx this property is an Enum  (WIP)
                #q = 'Set'+p+'To'
                #p_items = [ y.replace(q,'') for y in m if y.startswith( q ) ]
                #if len(p_items):
                #    setter_arg = 'enum'

                if not setter_arg in TypeMap:
                    print( 'KO ', p.ljust(30), 'unknow arg type:', setter_arg  )
                else:
                    p_type, p_size = TypeMap[setter_arg]
                    p_value = str( getter() ) # get the default value by calling the getter
                    props['PROPS'].append( { 'name':p, 'type':p_type, 'value':p_value, 'size':p_size } )
                    print( '   ', p.ljust(30), setter_arg, p_value )
    return props


node_template = '''from .core import *    

class VTK{{NAME}}(Node, VTKTreeNode):

    bl_idname = 'VTK{{NAME}}Type'
    bl_label  = 'vtk{{NAME}}'
    
    {% for x in PROPS  %}{{x.decl}}
    {% endfor %}
    
    def properties( self ):
        return [ {% for x in PROPS %}'m_{{x.name}}', {% endfor %}]

    def init(self, context):
        self.width = 200
        self.outputs.new('VTKPolyDataSocketType', "out")
        node_created( self )
    
CLASSES.append( VTK{{NAME}} )        
TYPENAMES.append( 'VTK{{NAME}}Type' )
'''

template = Template(node_template)

def generate( name ):
    props = find_properties(name)

    # it is easier to format properties-decl in in python than in template

    wn = max( [ len(p['name']) for p in props['PROPS'] ])
    wp = max( [ len(p['type']) for p in props['PROPS'] ])
    for p in props['PROPS']:

        p_size  = ''
        if p['size']>1: p_size = ', size='+ str(p['size'])

        p['decl'] = "m_{} = bpy.props.{}( name={} default={}{} )".format(
            p['name'].ljust(wn),
            p['type'].ljust(wp),
            ( "'"+p['name']+"'," ).ljust(wn+3),
            p['value'],
            p_size
        )
    
    text = template.render( props )
    f = open('generated/VTK'+props['NAME']+'.py', 'w')
    f.write(text)
    f.close()

# descendant of vtkPolyDataSource, with Source in their name --- 0 Input, 1 vtkPolyData Output
names = [ 
'vtkArcSource',
'vtkArrowSource',
'vtkBoundedPointSource',
'vtkConeSource',
'vtkCubeSource',
'vtkCylinderSource',
'vtkDiskSource',
'vtkEarthSource',
'vtkEllipseArcSource',
#'vtkFrustumSource',            # property Planes: unknow arg type: vtkPlanes
'vtkGlobeSource',
'vtkGlyphSource2D',
'vtkLineSource',                # property Points non standard                               -- not needed, we have Point1 and Point2
#'vtkOutlineCornerSource',      # property Corner has the signature-string on multiple line, accept a tuple of 24 float
#'vtkOutlineSource',            # idem
#'vtkParametricFunctionSource', # ParametricFunction unknow arg type: vtkParametricFunction  -- a Source with an Input! --- LATER
'vtkPlaneSource',               # method GetResolution(x,y) -> None non standard -- no problem, we have GetResolutionX and GetResolutionY
'vtkPlatonicSolidSource',       # Type is a Combo
'vtkPointSource',               # property RendomSequence, expecting a vtkRandomSequence     -- not needed
#'vtkPolyLineSource',           # property Points, expecting a vtkPoints  --- it is feasible ....
'vtkRegularPolygonSource',
'vtkSectorSource',
'vtkSphereSource',
'vtkSuperquadricSource',
'vtkTessellatedBoxSource',
'vtkTextSource',
'vtkTexturedSphereSource',
#'vtkVolumeOutlineSource'        # property VolumeMapper, expecting a vtkVolumeMapper
]


for x in names:
    #find_properties(x)
    generate(x)

print('\ndone')


