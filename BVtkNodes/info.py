from  .core import *
TYPENAMES = []


# ----------------------------------------------------------------
class VTKInfoNode(Node, VTKNode):

    bl_idname = 'VTKInfoNodeType'
    bl_label  = 'Info'

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'],[],[],['output'])

    def update_cb(self):
        print('tree updated')

    def draw_buttons(self, context, layout):
        in_node, vtkobj = self.get_input_node('input')
        if not in_node:
            layout.label('Connect a node')
        elif not vtkobj:
            layout.label('Input has not vtkobj (try updating)')
        else:
            vtkobj = resolve_algorithm_output(vtkobj)
            if not vtkobj:
                return

            layout.label(vtkobj.__class__.__name__)

            layout.label('num pts: ' + str(vtkobj.GetNumberOfPoints()))
            if hasattr(vtkobj, 'GetNumberOfCells'):
                layout.label('num cells: ' + str(vtkobj.GetNumberOfCells()))
            if hasattr(vtkobj, 'GetBounds'):
                layout.label('x range: ' + str(vtkobj.GetBounds()[0])+' - '+str(vtkobj.GetBounds()[1]))
                layout.label('y range: ' + str(vtkobj.GetBounds()[2])+' - '+str(vtkobj.GetBounds()[3]))
                layout.label('z range: ' + str(vtkobj.GetBounds()[4])+' - '+str(vtkobj.GetBounds()[5]))
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
        row.operator("node.update", text="update").node_path = node_path(self)
        row.separator()
        row.separator()
        row.separator()
        row.separator()

    def apply_properties(self, vtkobj):
        pass

    def get_output(self, socketname):
        return self.get_input_node('input')[1]

add_class(VTKInfoNode)
TYPENAMES.append('VTKInfoNodeType')
# ----------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory("debug", "debug", items=menu_items) )
# ----------------------------------------------------------------
