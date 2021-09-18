from .core import l # Import logging
import time
import vtk
import bpy
import os
from .core import b_path

# -----------------------------------------------------------------------------
# Vtk logs
# -----------------------------------------------------------------------------

out = vtk.vtkFileOutputWindow()
b_dir = b_path.rsplit(os.sep, 1)[0]
logfile = os.path.join(b_dir, 'vtklog.txt')
open(logfile, 'w').write('')
out.SetFileName(logfile)
vtk.vtkOutputWindow.SetInstance(out)

last_log = '' # Current log file contents

def log_check():
    '''Saves current log file contents. This function is to be called
    before executing more code that could generate errors, so that
    only latest error messages can be shown to user
    '''
    global last_log
    last_log = open(logfile, 'r').read()


def log_show():
    '''Shows log text of only latest operation'''
    logs = open(logfile, 'r').read()
    logs = logs.replace(last_log, '', 1) # Remove old log text
    if logs:
        def draw(self, context):
            layout = self.layout
            for line in logs.split('\n'):
                if line:
                    row = layout.row()
                    row.label(text=line)

        bpy.context.window_manager.popup_menu(draw, 'vtk:', 'INFO')
