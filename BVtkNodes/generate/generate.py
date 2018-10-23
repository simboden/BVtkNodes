import sqlite3
import os
import os.path
from jinja2 import Template

TypeMap = {}
TypeMap['String']                               = 'StringProperty'
TypeMap['Bool']                                 = 'BoolProperty'
TypeMap['Enum']                                 = 'EnumProperty'
TypeMap['Int']                                  = 'IntProperty'
TypeMap['IntVector']                            = 'IntVectorProperty'
TypeMap['Float']                                = 'FloatProperty'
TypeMap['FloatVector']                          = 'FloatVectorProperty'


# Class:    id, banned, num_pi, name, num_in, num_out, ctype, grp, status, note, doc = c
# Property: id, class, banned, editable, name, args, value, type, size, items, note
def get_classes( group ):

    c_list = []
    conn = sqlite3.connect('vtkdb.sqlite')
    cursor = conn.cursor()
    #cursor.execute( "SELECT id,name FROM Class WHERE num_pi = 0 AND grp = (SELECT id FROM CGroup WHERE name=? ) ORDER BY name ", (group,) )
    cursor.execute( "SELECT id,name,num_in,num_out FROM Class WHERE grp = (SELECT id FROM CGroup WHERE name=? ) ORDER BY name ", (group,) )
    classes = cursor.fetchall()
    for c in classes:
        dic = { 'name':c[1], 'props':[], 'num_in':c[2], 'num_out':c[3], 'extra_connections':[] }
        cursor.execute( "SELECT name,(SELECT name FROM PType WHERE id=Property.type ),size,value,items,banned FROM Property WHERE class = ? ORDER by type,name", (c[0],) )
        props = cursor.fetchall()
        for p in props:

            pname  = p[0]
            ptype  = p[1]
            psize  = p[2]
            value  = p[3]
            items  = p[4]
            banned = p[5]


            if banned == 1:
                continue  # skip banned properties
            
            if items:
                items = [ x[1] for x in eval(items) ]

            if not ptype in TypeMap:
                dic['extra_connections'].append(pname)
                continue # not a property

            ptype = TypeMap[ ptype ]

            if ptype == 'StringProperty' or ptype == 'EnumProperty':
                value = '"'+value+'"'
                value = value.replace('""""', '""')
                value = value.replace('"""', '""')
                if value.startswith("\n") or value.startswith("\\n"):
                    value = " "

            if ptype == 'BoolProperty' and value != "True" and value != "False":
                if value[0]!=0:
                    value = "True"
                else:
                    value = "False"
                
            if pname == 'ReadFromInputString':
                value = 'False'

            # clamp functions taking strings and returning numbers
            def clamp_int( value ):
                return  max(min( int(value), 1000000000), -1000000000)
            def clamp_float( value ):
                return  max(min( float(value), 1e30), -1e30)


            if ptype == 'IntProperty':
                value = str( clamp_int( value ) )
            if ptype == 'FloatProperty':
                value = str( clamp_float( value ) )
            if ptype == 'IntVectorProperty':
                list = eval(value)
                value = str( [ clamp_int(x) for x in list ] )
            if ptype == 'FloatVectorProperty':
                list = eval(value)
                value = str( [ clamp_float(x) for x in list ] )

            dic['props'].append( { 'name':pname, 'type':ptype, 'size':psize, 'value':value, 'items':items } )
            
        c_list.append(dic)
    conn.close()
    return c_list



node_template = '''from .core import *    
TYPENAMES = []
{% for C in CLASSES %}
#--------------------------------------------------------------
class VTK{{C.NAME}}(Node, {{BASE}}):

    bl_idname = 'VTK{{C.NAME}}Type'
    bl_label  = 'vtk{{C.NAME}}'
    {% for x in C.ENUM_ITEMS %}{{x}}
    {% endfor %}
    {% for x in C.PROPS  %}{{x.decl}}
    {% endfor %}
    b_properties = bpy.props.BoolVectorProperty(name="", size={{C.NP}}, get={{BASE}}.get_b, set={{BASE}}.set_b)
    
    def m_properties( self ):
        return [{% for x in C.PROPS %}'{{x.prefix}}{{x.name}}',{% endfor %}]
    def m_connections( self ):
        return {{C.CONNECTIONS}} 
    
add_class( VTK{{C.NAME}} )        
TYPENAMES.append('VTK{{C.NAME}}Type' )
{% endfor %}
#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( '{{MENU}}', '{{MENU}}', items=menu_items) )
'''
template = Template(node_template)


def generate( group ):

    classes = get_classes(group)
    
    DIC = { 'MENU':group.lower(), 'CLASSES':[], 'BASE':bases[group] }
    
    for c in classes:

        C = { 'NAME':c['name'], 'PROPS':[], 'ENUM_ITEMS':[], 'CONNECTIONS':((),(),(),()) }

        wm,wp = 0,0
        if len(c['props']):
            wn = max( [ len(p['name']) for p in c['props'] ])
            wp = max( [ len(p['type']) for p in c['props'] ])
            
        for p in c['props']:

            # some formatting is easier in python then in jinja
            name,ptype,value,size,items = p['name'], p['type'],p['value'],p['size'],p['items']


            if name == 'UTF8RecordDelimiters':
                value = '"\\n"'

            P = {'name':name }

            prefix = 'm_'
            items_arg = ''
            if items: # is an enum
                prefix = 'e_'
                items_arg =      ', items='+prefix+name+'_items'
                C['ENUM_ITEMS'].append( prefix+name+'_items=[ (x,x,x) for x in '+str(items)+']' )

            P['prefix']=prefix

            if size == 1:
                size = ''
            else:
                size = ', size='+ str(size)

            if ptype == 'StringProperty' and 'FileName' in name :
                items_arg = ", subtype='FILE_PATH'"

            P['decl'] = "{}{} = bpy.props.{}( name={} default={}{}{} )".format(
                prefix,
                name.ljust(wn),
                ptype.ljust(wp),
                ( "'"+name+"'," ).ljust(wn+3),
                value,
                size,
                items_arg
            )
            C['PROPS'].append(P)

        num_in  = c['num_in']
        if num_in == 1:
            input_ports = ['input']
        else:
            input_ports = ['input '+str(i) for i in range(num_in) ]

        num_out = c['num_out']
        if num_out == 1:
            output_ports = ['output']
        else:
            output_ports = ['output '+str(i) for i in range(num_out) ]

        extra_inputs = c['extra_connections']
        extra_outputs = []
        if group not in ['Source','Reader','Writer','Filter','Filter1','Filter2']:
            extra_outputs = ['self']
        C['CONNECTIONS'] = str( (input_ports, output_ports, extra_inputs, extra_outputs) )


        C['NP'] = max( 1, len(C['PROPS']) )

        if C['NP'] > 32:  # blender BoolArray max size is 32
            print( C['NAME'], 'skipped: too many properties (', C['NP'], ')' )
        else:
            DIC['CLASSES'].append(C)


    text = template.render( DIC )
    f = open( filenames[group], 'w')
    f.write(text)
    f.close()


bases = { 'Source':        'VTKNode',
          'Reader':        'VTKNode',
          'Writer':        'VTKNode',
          'Filter':        'VTKNode',
          'Filter1':       'VTKNode',
          'Filter2':       'VTKNode',
          'Transform':     'VTKNode',
          'ImplicitFunc':  'VTKNode',
          'ParametricFunc':'VTKNode',
          'Integrator':    'VTKNode',
          }

filenames = { 'Source':         'gen_VTKSources.py',
              'Reader':         'gen_VTKReaders.py',
              'Writer':         'gen_VTKWriters.py',
              'Filter' :        'gen_VTKFilters.py',
              'Filter1':        'gen_VTKFilters1.py',
              'Filter2':        'gen_VTKFilters2.py',
              'Transform':      'gen_VTKTransform.py',
              'ImplicitFunc':   'gen_VTKImplicitFunc.py',
              'ParametricFunc': 'gen_VTKParametricFunc.py',
              'Integrator':     'gen_VTKIntegrator.py',
}

generate('Source')
generate('Reader')
generate('Writer')
generate('Filter1')
generate('Filter2')
generate('Filter')
generate('Transform')
generate('ImplicitFunc')
generate('ParametricFunc')
generate('Integrator')

print('\ndone')


