#import vtk
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
    cursor.execute( "SELECT id,name FROM Class WHERE num_pi = 0 AND grp = (SELECT id FROM CGroup WHERE name=? ) ORDER BY name ", (group,) )
    classes = cursor.fetchall()
    for c in classes:
        dic = { 'name':c[1], 'props':[] }
        cursor.execute( "SELECT name,(SELECT name FROM PType WHERE id=Property.type ),size,value,items FROM Property WHERE class = ? ORDER by type,name", (c[0],) )
        props = cursor.fetchall()
        for p in props:

            
            items = p[4] 
            if items:
                items = [ x[1] for x in eval(items) ]

            ptype = p[1]
            if not ptype in TypeMap:
                #print( 'bad ptype', ptype )
                continue
            ptype = TypeMap[ ptype ]

            value = p[3]
            if ptype == 'StringProperty' or ptype == 'EnumProperty':
                value = '"'+value+'"'
                value = value.replace('""""', '""')
                value = value.replace('"""', '""')

            if value.isdigit() and int(value) > 1e9:
                print(value)
                value = '0'

            if ptype == 'IntVectorProperty':
                def filter(x):
                    if x>1e9: return 0
                    return x
                value = str( [ filter(x) for x in eval(value) ] )
                
            dic['props'].append( { 'name':p[0], 'type':ptype, 'size':p[2], 'value':value, 'items':items } )
            
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
    def m_properties( self ):
        return [{% for x in C.PROPS %}'{{x.prefix}}{{x.name}}',{% endfor %}]
    
CLASSES.append  ( VTK{{C.NAME}} )        
TYPENAMES.append('VTK{{C.NAME}}Type' )
{% endfor %}
#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( '{{MENU}}', '{{MENU}}', items=menu_items) )
'''
template = Template(node_template)


def generate( group ):

    classes = get_classes(group)
    
    bases = { 'Source':'VTKTreeNode', 'Reader':'VTKReaderNode', 'Writer':'VTKReaderNode', 'Filter1':'VTKFilter1Node' }

    DIC = { 'MENU':group.lower(), 'CLASSES':[], 'BASE':bases[group] }
    
    for c in classes:

        C = { 'NAME':c['name'], 'PROPS':[], 'ENUM_ITEMS':[] }

        wm,wp = 0,0
        if len(c['props']):
            wn = max( [ len(p['name']) for p in c['props'] ])
            wp = max( [ len(p['type']) for p in c['props'] ])
            
        for p in c['props']:

            # some formatting is easier in python then in jinja
            name,ptype,value,size,items = p['name'], p['type'],p['value'],p['size'],p['items']
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

        DIC['CLASSES'].append(C)

    filename = { 'Source':'VTKSources.py', 'Reader':'VTKReaders.py','Writer':'VTKWriters.py','Filter1':'VTKFilters1.py' }
    
    text = template.render( DIC )
    f = open( '/home/simboden/Desktop/BVTK/GIT/VTKNodes/'+filename[group], 'w')
    f.write(text)
    f.close()


generate('Source')
generate('Reader')
generate('Writer')
generate('Filter1')


            
print('\ndone')


