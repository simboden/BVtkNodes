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

SocketMap = {}
SocketMap['vtkPolyData' ]         = 'VTKPolyDataSocketType'
SocketMap['vtkImageData']         = 'VTKImageDataSocketType'
SocketMap['vtkStructuredPoints']  = 'VTKImageDataSocketType'
SocketMap['vtkDataSet']           = 'VTKImageDataSocketType'


def find_properties( name ):
    print()
    print(name)

    # instantiate the class
    c = getattr( vtk, name )
    if c is None: return None
    o = c()

    # init our output
    props = {}
    props['NAME'  ]      = name[3:]
    props['PROPS' ]      = []
    props['ENUM_ITEMS' ] = []
    props['INPUTS' ]     = []
    props['OUTPUTS' ]    = []

    # info about connectivity
    if 'GetNumberOfInputPorts' in dir(o):
        print( '   ', 'Inputs'.ljust(30), o.GetNumberOfInputPorts() )

    if 'GetNumberOfOutputPorts' in dir(o):
        print( '   ', 'Outputs'.ljust(30), o.GetNumberOfOutputPorts() )

    got_port = 'GetOutputPort' in dir(o)
    got_out  = 'GetOutput' in dir(o)
    out_type = None
    if got_out and got_port:
        met = getattr( o, 'GetOutput' )
        out_type = met.__doc__.split('\n')[0].split('>')[1].strip()

    if out_type not in SocketMap:
        print( 'KO ', 'OutType'.ljust(30), 'unknow socket type:', out_type  )
    else:
        print( '   ', 'OutType'.ljust(30), out_type )
        props['OUTPUTS' ].append( SocketMap[out_type] )

    # retrieve the interesting methods
    m = [ x for x in dir(o) if not x.startswith('__') and not x in HiddenMethods and not x[3:] in HiddenProp ]
    m.sort()


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
                p_value = str( getter() ) # get the default value by calling the getter
                
                # if there are also the methods p+On and p+Off this property is a bool
                if p+'On' in m and p+'Off' in m :
                    setter_arg = 'bool'

                # if there are also methods Set+p+To+xxx this property is an Enum  (WIP)
                q = 'Set'+p+'To'
                names = [ y.replace(q,'') for y in m if y.startswith( q ) ]
                p_items = [] # enum-names ordered by their value --- or nothing
                if len(names):
                    setter_arg = 'enum'
                    # retrieve the numerical value matching the enum-names
                    for y in names:
                        getattr(o,q+y)()                # call Set+p+To+y()
                        p_items.append( (getter(), y) ) # retrieve its value calling Get+p()
                    p_items.sort()
                    p_value = "'"+(p_items[ int(p_value) ][1])+"'" # translate p_value to enum_name
                    p_items = str([ y[1] for y in p_items ]) # drop values, keep the order, transform in string

                # check if the type of the property is recognized
                if not setter_arg in TypeMap:
                    print( 'KO ', p.ljust(30), 'unknow arg type:', setter_arg  )
                else:
                    p_type, p_size = TypeMap[setter_arg]
                    
                    props['PROPS'].append( { 'name':p, 'type':p_type, 'value':p_value, 'size':p_size, 'items':p_items } )

                    if not p_items: p_items='' # just for the printout
                    print( '   ', p.ljust(30), setter_arg, p_value, p_items )
    return props


node_template = '''from .core import *    
TYPENAMES = []
{% for C in CLASSES %}
#--------------------------------------------------------------
class VTK{{C.NAME}}(Node, VTKTreeNode):

    bl_idname = 'VTK{{C.NAME}}Type'
    bl_label  = 'vtk{{C.NAME}}'

    {% for x in C.ENUM_ITEMS %}{{x}}
    {% endfor %}
    {% for x in C.PROPS  %}{{x.decl}}
    {% endfor %}
    def m_properties( self ):
        return [{% for x in C.PROPS %}'{{x.prefix}}{{x.name}}',{% endfor %}]
        
    def m_outputs(self):
        return [ {% for x in C.OUTPUTS %}'{{x}}',{% endfor %}]
    
CLASSES.append  ( VTK{{C.NAME}} )        
TYPENAMES.append('VTK{{C.NAME}}Type' )
{% endfor %}
#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( '{{MENU}}', '{{MENU}}', items=menu_items) )
'''

template = Template(node_template)

def generate( module, classes ):

    DIC = {}
    DIC['MENU']    = module.lower().replace('vtk','')
    DIC['CLASSES'] = []
    
    for name in classes:
        props = find_properties(name)

        wn = max( [ len(p['name']) for p in props['PROPS'] ])
        wp = max( [ len(p['type']) for p in props['PROPS'] ])
        for p in props['PROPS']:

            # some formatting is easier in python then in jinja
            name,ptype,value,size,items = p['name'],p['type'],p['value'],p['size'],p['items']

            prefix = 'm_'
            items_arg = ''
            if items: # is an enum
                prefix = 'e_'
                items_arg =      ', items='+prefix+name+'_items'
                props['ENUM_ITEMS'].append( prefix+name+'_items=[ (x,x,x) for x in '+items+']' )
            p['prefix']=prefix

            if size == 1:
                size = ''
            else:
                size = ', size='+ str(size)
            
            p['decl'] = "{}{} = bpy.props.{}( name={} default={}{}{} )".format(
                prefix,
                name.ljust(wn),
                ptype.ljust(wp),
                ( "'"+name+"'," ).ljust(wn+3),
                value,
                size,
                items_arg
            )

        DIC['CLASSES'].append(props)
    
    text = template.render( DIC )
    f = open( '../'+module+'.py', 'w')
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

generate('VTKSources', names )

print('\ndone')


