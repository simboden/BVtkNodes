import time
import vtk
import bpy
from .core import b_path


def SetColor(node, color):
    node.color = color


def UpdateObj(node, vtkobj):
    #time.sleep(1)
    node.apply_properties(vtkobj)
    node.apply_inputs(vtkobj)
    if hasattr(vtkobj, "Update"):
        vtkobj.Update()


def SetInputConnection(vtkobj, i, input_obj):
    #time.sleep(1)
    vtkobj.SetInputConnection(i, input_obj)


def SetInputObj(vtkobj, name, input_obj):
    #time.sleep(1)
    cmd = 'vtkobj.Set' + name + '( input_obj )'
    exec(cmd, globals(), locals())


def Update(node, cb, x=True):
    ''' updates all the pipeline entering node, then execute it '''
    #print('on_update')  # , node.name )
    if x: queue.add(log_check)
    ex_color = node.color.copy()
    inputs_color = 0.84, 0.84, 0.73
    execute_color = 0.85, 0.6, 0.2
    vtkobj = node.get_vtkobj()

    queue.add(SetColor, node, inputs_color)
    for input_node in node.input_nodes():
        Update(input_node, None, False)
    queue.add(SetColor, node, execute_color)
    if vtkobj:
        queue.add(UpdateObj, node, vtkobj)
    queue.add(SetColor, node, ex_color)
    if x:
        queue.add(SetColor, node, execute_color)
        queue.add(log_show)
        if cb:
            queue.add(cb)
        queue.add(SetColor, node, ex_color)
        bpy.ops.vtk.function_queue()



# ---------------------------------------------------------------------------------
#  function queue
# ---------------------------------------------------------------------------------


class FunctionsQueue:
    functions = []
    executed = []
    running = False
    i = 0

    def add(self, f, *args):
        if not self.running:
            self.functions.append((f, (a for a in args)))

    def next_function(self):
        i = self.i
        if i >= len(self.functions):
            self.running = False
            return
        f = self.functions[i]
        if i not in self.executed:
            try:
                f[0](*f[1])
            except Exception as e:
                print('------- exception occurred -------')
                print(e)
                print('----------------------------------')
            self.executed.append(i)
            self.i += 1

    def reset(self):
        self.functions = []
        self.executed = []
        self.running = False
        self.i = 0


queue = FunctionsQueue()


class VTKFunctionQueue(bpy.types.Operator):
    """Run functions separated in time by 1/100s"""
    bl_idname = "vtk.function_queue"
    bl_label = "Run functions"

    _timer = None

    def modal(self, context, event):
        global queue
        if not queue.running:
            self.cancel(context)
            return {'CANCELLED'}
        elif event.type == 'TIMER':
            queue.next_function()
        return {'PASS_THROUGH'}

    def execute(self, context):
        global queue
        if queue.running:
            return {'CANCELLED'}
        queue.running = True
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.01, context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        global queue
        queue.reset()
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


# ---------------------------------------------------------------------------------
#  update without queue
# ---------------------------------------------------------------------------------


def no_queue_update(node, cb, x=True):
    ''' updates all the pipeline entering node, then execute it '''
    #print('on_update')  # , node.name )
    vtkobj = node.get_vtkobj()
    for input_node in node.input_nodes():
        no_queue_update(input_node, None, False)
    if x:
        cb()
    else:
        if vtkobj:
            node.apply_properties(vtkobj)
            node.apply_inputs(vtkobj)
            if hasattr(vtkobj, "Update"):
                vtkobj.Update()


# ---------------------------------------------------------------------------------
# Vtk logs
# ---------------------------------------------------------------------------------


out = vtk.vtkFileOutputWindow()
logfile = b_path.rsplit('/', 1)[0]+'/vtklog.txt'
open(logfile, 'w').write('')
out.SetFileName(logfile)
vtk.vtkOutputWindow.SetInstance(out)
last_log = ''


def log_check():
    """ to call before executing code that could generate errors """
    global last_log
    last_log = open(logfile, 'r').read()


def log_show():
    """ to call after log has been check and code has been executed """
    logs = open(logfile, 'r').read()
    logs = logs.replace(last_log, '', 1)
    if logs:
        def draw(self, context):
            layout = self.layout
            for line in logs.split('\n'):
                if line:
                    row = layout.row()
                    row.label(line)

        bpy.context.window_manager.popup_menu(draw, 'vtk:', 'INFO')

