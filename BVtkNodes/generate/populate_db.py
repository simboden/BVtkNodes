#import vtk
from vtk_info import infos
from vtk_info import vtk
import sys
import os
import os.path
import sqlite3

filename = 'vtkdb.sqlite'
if os.path.exists(filename):
    os.remove(filename)

conn = sqlite3.connect(filename)
c = conn.cursor()

c.execute("CREATE TABLE CType  ( id INTEGER PRIMARY KEY, name TEXT );")
c.execute("CREATE TABLE CGroup ( id INTEGER PRIMARY KEY, name TEXT );")
c.execute("CREATE TABLE CStatus( id INTEGER PRIMARY KEY, name TEXT );")
c.execute("CREATE TABLE PType  ( id INTEGER PRIMARY KEY, name TEXT );")

c.execute("insert into CTYPE(name) values('Source');")
c.execute("insert into CTYPE(name) values('Reader');")
c.execute("insert into CTYPE(name) values('Writer');")
c.execute("insert into CTYPE(name) values('Mapper');")
c.execute("insert into CTYPE(name) values('Sink');")
c.execute("insert into CTYPE(name) values('Filter1');")
c.execute("insert into CTYPE(name) values('Filter2');")
c.execute("insert into CTYPE(name) values('Filter');")
c.execute("insert into CTYPE(name) values('Transform');")
c.execute("insert into CTYPE(name) values('ImplicitFunc');")
c.execute("insert into CTYPE(name) values('ParametricFunc');")
c.execute("insert into CTYPE(name) values('Integrator');")
c.execute("insert into CTYPE(name) values('Weird');")

c.execute("insert into CGroup(name) values('Source');")
c.execute("insert into CGroup(name) values('Reader');")
c.execute("insert into CGroup(name) values('Writer');")
c.execute("insert into CGroup(name) values('Mapper');")
c.execute("insert into CGroup(name) values('Sink');")
c.execute("insert into CGroup(name) values('Filter1');")
c.execute("insert into CGroup(name) values('Filter2');")
c.execute("insert into CGroup(name) values('Filter');")
c.execute("insert into CGroup(name) values('Transform');")
c.execute("insert into CGroup(name) values('ImplicitFunc');")
c.execute("insert into CGroup(name) values('ParametricFunc');")
c.execute("insert into CGroup(name) values('Integrator');")
c.execute("insert into CGroup(name) values('Weird');")

c.execute("insert into CStatus(name) values('todo');")
c.execute("insert into CStatus(name) values('working');")
c.execute("insert into CStatus(name) values('approved');")
c.execute("insert into CStatus(name) values('rejected');")

c.execute("insert into PType(name) values('Weird');")    
c.execute("insert into PType(name) values('Bool');")
c.execute("insert into PType(name) values('String');")
c.execute("insert into PType(name) values('Int');")
c.execute("insert into PType(name) values('Float');")
c.execute("insert into PType(name) values('Enum');")
c.execute("insert into PType(name) values('IntVector');")
c.execute("insert into PType(name) values('FloatVector');")
c.execute("insert into PType(name) values('Object-in');")  #9
c.execute("insert into PType(name) values('Object-out');") #10

c.execute('''CREATE TABLE Class
( 
id      INTEGER PRIMARY KEY,
banned  INTEGER, 
name    TEXT, 
num_in  INTEGER, 
num_out INTEGER, 
type    INTEGER,
grp     INTEGER, 
status  INTEGER, 
note    TEXT,
doc     TEXT, 
FOREIGN KEY(type)   REFERENCES CType(id),
FOREIGN KEY(grp)    REFERENCES CGroup(id),
FOREIGN KEY(status) REFERENCES CStatus(id)
);''')

#c.execute("insert into Class(name,doc,num_in,num_out,type,banned,grp,status,note) values('name','doc',0,0,1,1,1,1,'note');")

c.execute('''CREATE TABLE Property
( 
id       INTEGER PRIMARY KEY,
class    INTEGER, 
banned   INTEGER, 
editable INTEGER, 
name     TEXT, 
args     TEXT, 
value    TEXT, 
type     INTEGER, 
size     INTEGER, 
items    TEXT, 
note     TEXT,
FOREIGN KEY(class) REFERENCES Class(id), 
FOREIGN KEY(type)  REFERENCES PType(id)
);''')

#c.execute("insert into Property(name) values('Pollo');")

Source  = 1
Reader  = 2
Writer  = 3
Mapper  = 4
Sink    = 5
Filter1 = 6
Filter2 = 7
Filter  = 8
Transform       = 9
ImplicitFunc    = 10
ParametricFunc  = 11
Integrator      = 12
Weird           = 13

TypeMap = {}
TypeMap['bool']                                 = (2, 1 )
TypeMap['string']                               = (3, 1 )
TypeMap['int']                                  = (4, 1 )
TypeMap['float']                                = (5, 1 )
TypeMap['enum']                                 = (6, 1 )
TypeMap['int,int']                              = (7, 2 )
TypeMap['int,int,int']                          = (7, 3 )
TypeMap['int,int,int,int']                      = (7, 4 )
TypeMap['int,int,int,int,int']                  = (7, 5 )
TypeMap['int,int,int,int,int,int']              = (7, 6 )
TypeMap['float,float']                          = (8, 2 )
TypeMap['float,float,float']                    = (8, 3 )
TypeMap['float,float,float,float']              = (8, 4 )
TypeMap['float,float,float,float,float']        = (8, 5 )
TypeMap['float,float,float,float,float,float']  = (8, 6 )

cid = 0
for info in infos:

    cid += 1

    name     = info['name']
    num_in   = info['num_in']
    num_out  = info['num_out']
    out_type = info['out_type']
    props    = info['props']
    doc      = info['docs']

    cls = getattr( vtk, 'vtk'+name, None )
    if cls is None:
        print( "noclass" , name)
        continue

    ctype = Filter
    if issubclass(cls, vtk.vtkAbstractTransform):
        ctype = Transform
    elif issubclass(cls, vtk.vtkImplicitFunction):
        ctype = ImplicitFunc
    elif issubclass(cls, vtk.vtkParametricFunction):
        ctype = ParametricFunc
    elif issubclass(cls, vtk.vtkInitialValueProblemSolver):
        ctype = Integrator
    elif 'Reader' in name:
        ctype = Reader
    elif 'Writer' in name:
        ctype = Writer
    elif 'Mapper' in name:
        ctype = Mapper
    elif num_in == 0 and num_out == 0:
        ctype = Weird
    elif num_in == 0 and num_out == 1:
        ctype = Source
    elif num_in == 1 and num_out == 0:
        ctype = Sink
    elif num_in == 1 and num_out == 1:
        ctype = Filter1
    elif num_in == 2 and num_out == 1:
        ctype = Filter2

    grp      = ctype
    banned   = 0
    status   = 1 # todo
    note     = ""
    doc = doc.replace("'","")

    # if ctype > Filter:
    #     print( name, ctype )

    sql = "INSERT INTO Class(banned,name,num_in,num_out,type,grp,status,note,doc) VALUES("
    sql+= "{},'{}',{},{},{},{},{},'{}','{}');".format(banned,name,num_in,num_out,ctype,grp,status,note,doc)
    try:
        c.execute(sql);
    except:
        print('error -- sql=',sql)

    for p in props:
        pname  = p['name']
        args   = p['args']
        value  = p['value']
        items  = str(p['items']).replace("'",'"').replace('[]','')
        note   = p['note']

        ptype,size = 1,1
        if args in TypeMap:
            ptype, size = TypeMap[args]
        elif args.startswith('vtk') and ',' not in args:
            ptype = 10 # object -- assume out connection
            if 'optional' in note:
                ptype = 9 # object -- input connection
            
        banned = 0
        if 'mismatch' in note: banned = 1

        editable = 1
        #if 'optional' in note editable = 1

        sql = "INSERT INTO Property(class,banned,editable,name,args,value,type,size,items,note) VALUES("
        sql+= "{},{},{},'{}','{}','{}',{},{},'{}','{}');".format(cid,banned,editable,pname,args,value,ptype,size,items,note )
        try:
            c.execute(sql);
        except:
            print('error -- sql=',sql)

conn.commit()
conn.close()

print('db done')
