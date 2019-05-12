from .core import l # Import logging
from .core import *

class BVTK_Node_Info(Node, BVTK_Node):
    '''BVTK Info Node'''
    bl_idname = 'BVTK_Node_InfoType'
    bl_label  = 'Info'

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'],[],[],['output'])

    def update_cb(self):
        l.debug('tree updated')

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label(text='Connect a node')
        elif not vtkobj:
            layout.label(text='Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return

            layout.label(text=vtkobj.__class__.__name__)

            layout.label(text='num pts: ' + str(vtkobj.GetNumberOfPoints()))
            if hasattr(vtkobj, 'GetNumberOfCells'):
                layout.label(text='num cells: ' + str(vtkobj.GetNumberOfCells()))
            if hasattr(vtkobj, 'GetBounds'):
                layout.label(text='x range: ' + str(vtkobj.GetBounds()[0])+' - '+str(vtkobj.GetBounds()[1]))
                layout.label(text='y range: ' + str(vtkobj.GetBounds()[2])+' - '+str(vtkobj.GetBounds()[3]))
                layout.label(text='z range: ' + str(vtkobj.GetBounds()[4])+' - '+str(vtkobj.GetBounds()[5]))
            data = {}
            if hasattr(vtkobj, 'GetPointData'):
                data['Point data'] = vtkobj.GetPointData()
            if hasattr(vtkobj, 'GetCellData'):
                data['Cell data'] = vtkobj.GetCellData()
            if hasattr(vtkobj, 'GetFieldData'):
                data['Field data'] = vtkobj.GetFieldData()
            for k in data:
                d = data[k]
                for i in range(d.GetNumberOfArrays()):
                    arr = d.GetArray(i)
                    r = arr.GetRange()
                    name = arr.GetName()
                    row = layout.row()
                    row.label(k+':'+str(i)+': '+name+' max:'+str(r[0])+' min:'+str(r[1]))

        layout.separator()
        row = layout.row()
        row.separator()
        row.separator()
        row.separator()
        row.separator()
        row.operator("node.bvtk_node_update", text="update").node_path = node_path(self)
        row.separator()
        row.separator()
        row.separator()
        row.separator()

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        return self.get_input_node('input')[1]

TYPENAMES = []
add_class(BVTK_Node_Info)
TYPENAMES.append('BVTK_Node_InfoType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Debug", "Debug", items=menu_items))
