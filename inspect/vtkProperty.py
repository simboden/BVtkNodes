"""
vtkObjProperties take a vtkObject and return its properties, classified as follows:

   Bool:   -- SetXXX, GetXXX, XXXOn, XXXOff method exist  --- to be mapped with a checkbox
   SetGet  -- SetXXX taking 'y1', GetXXX returning 'y2' methods exist, and y1 and y2 match and are not vtkDataObject --- to be mapped to an entry
   Radio   -- SetXXX, GetXXX, SetXXXToY1, SetXXXToY2, ... method exist --- to be mapped to a radio
   Conn    -- like SetGet but connectiong vtkDataObject --- this form the connection
   MConn   -- multiple connection: SetInput(x,1),  SetInput(x,2), ....
   Cmd     -- all the remaining method --- when taking 0 arguments can be mapped to a button 

USAGE:
    o = vtk.vtkActor()
    p = vtkObjProperties(o)
    p.Print()

NOTE:
  converted from python 2 --- may be improved a lot
"""

#from vtkProxy import *
import vtk
import re

#---------------------------------------------------------
DEBUG=0
def debug (msg):
    if DEBUG:
        print(msg)
        
#---------------------------------------------------------
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

#---------------------------------------------------------

def lm( vtkobj ):
    op = vtkObjProperties( vtkobj)
    op.Print()

#---------------------------------------------------------
class vtkObjProperties:
    def __init__(self,vtkObj):

        self.MET    = {} # method name -> arguments number
        self.BOOL   = {} # SetX,GetX,XOn,XOff 
        self.SETGET = {} # SetX,GetX
        self.SETTO  = {} # SetX,GetX,SetXToY1,SetXToY2,...
        self.CONN   = {} # SetGet that form pipeline connections
        self.MCONN  = {} # SetGet that form multiple connections
        self.CMD    = {} # all the rest
        self.vtkObj = vtkObj
        self.Parse()
        
    def GetDoc(self,m):
        return getattr(self.vtkObj,m).__doc__.splitlines()[0].split('.')[1].strip()

    def GetSignature(self,m):
        return self.GetDoc(m)[len(m):]

    def GetArg(self,m):
        return self.GetDoc(m).split('(')[1].split(')')[0].strip()

    def GetRet(self,m):
        doc = self.GetDoc(m)
        n = doc.count('>')
        if n == 0:
            return ''
        elif n == 1:
            ret = doc.split('>')[1].strip()
            if ret[0:1] == '(':
                ret = ret[1:]
            if ret[-1:] == ')':
                ret = ret[:-1]
            return ret
        else:
            debug('invalid doc:' + doc)
            return ''

    def Parse(self):
        global HiddenMethods
        # fill MET [name]->(arg,ret)
        debug('######################################')
        debug('parsing a:'+self.vtkObj.__class__.__name__  )
        debug('######################################')
        for m in dir(self.vtkObj): #self.vtkObj.__methods__:
            # removing methods to be hidden
            if m[:2] == '__':
                continue
            if m in HiddenMethods:
                continue
            if m[-8:] == 'MinValue' or m[-8:] == 'MaxValue':
                continue
            # get the command
            cm = getattr(self.vtkObj,m)
            # get the first line of the doc
            doc = cm.__doc__
            if doc is None:
                continue
            doc = doc.splitlines()[0]
            # check that doc has 'V.' 
            if doc[:2] != 'V.':
                debug('no V. in doc:' + doc)
                continue
            # do argument count
            arg = doc.split('(')[1].split(')')[0].strip()
            if arg == '':
                argc = 0
            else:
                argc = 1 + arg.count(',')
             # insert in the table
            self.MET[m]= argc
            #print m,'--',argc

        debug('done loading MET')
        # separate the Boolean
        for m in list(self.MET.keys()):
            if m[-2:] == 'On':
                m2 = m[:-2]+'Off'
                m3 = 'Set' + m[:-2]
                m4 = 'Get' + m[:-2]
                if m2 in self.MET and m3 in self.MET and m4 in self.MET:
                    # non controllo gli argomenti - speriamo bene 
                    del self.MET[m]
                    del self.MET[m2]
                    del self.MET[m3]
                    del self.MET[m4]
                    self.BOOL[m[:-2]] = ''
                    #print m,m2,m3,m4,'-> Bool ',m[:-2]

        debug('done loading BOOL')
        # separate the SetGet - the Get must have 0 arguments
        for m in list(self.MET.keys()):
            if m[:3] == 'Set':
                m2 = 'Get'+ m[3:]
                if m2 in self.MET:
                    if self.MET[m2] == 0:
                        del self.MET[m]
                        del self.MET[m2]
                        self.SETGET[m[3:]] = self.GetArg(m)
                        if self.GetArg(m) != self.GetRet(m2):
                            debug( m+' args = '+self.GetArg(m)+' DIFFERENT FROM '+m2+' ret = '+self.GetRet(m2))
                        #print m,m2,'-> SetGet ',m[3:]
        debug('done loading SETGET')
        # separate the radio
        # there must be SetXxxToYyy and there must be SetGet (TODO: SetGet should be optional)
        # there may be  GetXxxAsString
        rex = re.compile('^Set(.*)To')
        for m in list(self.MET.keys()):
            mat = rex.match(m)
            if mat != None and m in self.MET and self.MET[m] == 0:
                xxx = mat.group(1)
                if xxx in self.SETGET:
                    del self.SETGET[xxx]
                    if 'Get'+xxx+'AsString' in self.MET:
                        values = 'AsString',
                        del self.MET['Get'+xxx+'AsString']
                    else:
                        values = ()
                    prefix = 'Set'+xxx+'To'
                    prefix_len = len(prefix)
                    rex2 = re.compile('^'+prefix)
                    for met in list(self.MET.keys()):
                        if rex2.match(met) != None and self.MET[met] == 0:
                            values += met[prefix_len:],
                            del self.MET[met]
                    self.SETTO[xxx] = values
                    #print xxx,values
        debug('done loading SETTO')

        # searching methods that form connections
        rex = re.compile('vtk')
        for m in list(self.SETGET.keys()):
            doc = self.GetDoc('Set'+ m)
            doc2 = self.GetDoc('Get'+ m)
            if rex.search(doc+doc2) != None:
                s_arg = self.GetArg('Set'+m)
                g_ret = self.GetRet('Get'+m)
                if s_arg != g_ret:
                    debug( 'Set'+m+' args = '+s_arg+' DIFFERENT FROM Get'+m+' ret = '+g_ret)
                del self.SETGET[m]
                self.CONN[m] = s_arg
        debug('done loading CONN')
        
        # multiple connections:
        # we have a SETGET xxxNumberOfyyy and exist a pair of methods
        # Getyyy(int)->vtkObj, Setyyy(vtkobj,i)
        # ----- but the Glyph dont have a Setyyy(vtkobj,i) - :-(
        # - todo

        # multiple values: ( e.g. vtkContur::SetValue(int,float)  )
        # - todo 

        # the remainig unclassified methods become CMD
        for m in list(self.MET.keys()):
            self.CMD[m] = self.GetSignature(m)
            del self.MET[m]

        self.bool = list(self.BOOL.keys())
        self.bool.sort()

        self.setget = list(self.SETGET.keys())
        self.setget.sort()
        
        self.radio = list(self.SETTO.keys())
        self.radio.sort()
        
        self.conn = list(self.CONN.keys())
        self.conn.sort()
        
        self.cmd = list(self.CMD.keys())
        self.cmd.sort()
        
    def Print(self):
        
        j = 26
        print( '----------------------------------------------' )
        print( 'Property for ',self.vtkObj.__class__.__name__  )
        print()

        for m in self.bool: 
            print( 'bool....' + m)
        
        if len(self.setget): print()
        for m in self.setget: 
            print( 'setget..' + m.ljust(j,'.') + self.SETGET[m] )

        if len(self.radio): print()
        for m in self.radio: 
            print( 'radio...' + m.ljust(j,'.') + repr( self.SETTO[m] ).replace("'","").replace(", ", " ").replace("(", "").replace(")", "").replace("AsString", "*") )

        if len(self.conn): print()
        for m in self.conn: 
            print( 'conn....' + m.ljust(j,'.') + self.CONN[m] )

        if len(self.cmd): print
        for m in self.cmd: 
            print( 'cmd.....' + m.ljust(j,'.') + self.CMD[m] )
        print()
        
    def Print2(self):
        
        j = 26
        print( '############################################' )
        print( 'Property for ',self.vtkObj.__class__.__name__  )   

        lst = self.BOOL.keys()
        lst.sort()
        if len(lst): print( 'BOOL')
        for m in lst: 
            print(  '...' +m )
        
        lst = self.SETGET.keys()
        lst.sort()
        if len(lst): print( 'SETGET')
        for m in lst: 
            print( '...' +m.ljust(j,'.') + self.SETGET[m]  )

        lst = self.SETTO.keys()
        lst.sort()
        if len(lst): print( 'RADIO' )
        for m in lst: 
            print( '...' +m.rjust(j,'.') + self.SETTO[m] )

        lst = self.CONN.keys()
        lst.sort()
        if len(lst): print( 'CONN' )
        for m in lst: 
            print( '...' +m.ljust(j,'.') + self.CONN[m] )

        lst = self.CMD.keys()
        lst.sort()
        if len(lst): print( 'CMD' )
        for m in lst: 
            print( '...' + m.ljust(j,'.') + self.CMD[m] )


    def Anchestor(cls):

        """ take a vtk class, return the list of anchestor """
        c = cls
        l = []
        l.append(c.__name__)
        t = c.__bases__  # probably doesn't work anymore -- but anchestor are reported in __doc__
        while len(t):
                c = t[0]
                l.append(c.__name__)
                t = c.__bases__
        return l

#---------------------------------------------------------------------------

if __name__ == '__main__':
    #o = vtk.vtkActor()
    #p = vtkObjProperties(o)
    #p.Print()
    
    #o = vtk.vtkContourFilter()
    #p = vtkObjProperties(o)
    #p.Print()

    #o = vtk.vtkGlyph3D()
    #p = vtkObjProperties(o)
    #p.Print()

    #raw_input()

    lm( vtk.vtkStructuredPointsReader() )
    lm( vtk.vtkContourFilter() )
    lm( vtk.vtkImageGaussianSmooth )
