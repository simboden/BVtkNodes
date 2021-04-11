from .core import l # Import logging
from .core import *
from .cache import BVTKCache

class BVTK_Node_Info(Node, BVTK_Node):
    '''BVTK Info Node'''
    bl_idname = 'BVTK_Node_InfoType'
    bl_label  = 'Info'

    arr_string = '{k} [{i}] ({data_type_name}{n_comps}): \'{name}\': {range_text}'

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'],[],[],['output'])

    def draw_buttons(self, context, layout):
        # Debug
        row = layout.row()
        row.label(text="node_id #%d: %r" % (self.node_id, str(self.vtk_status)))

        fs="{:.5g}" # Format string
        in_node, vtk_obj, vtk_connection = self.get_input_node_and_vtk_objects('input')
        if not in_node:
            layout.label(text='No node connected to input')
        elif not vtk_obj:
            layout.label(text='Input has no VTK object')
        elif not vtk_connection:
            layout.label(text='Input has no VTK connection')
        else:
            vtk_output_obj = resolve_algorithm_output(vtk_connection)
            layout.label(text='Type: ' + vtk_output_obj.__class__.__name__)
            if hasattr(vtk_output_obj, 'GetNumberOfPoints'):
                layout.label(text='Points: ' + str(vtk_output_obj.GetNumberOfPoints()))
            if hasattr(vtk_output_obj, 'GetNumberOfCells'):
                layout.label(text='Cells: ' + str(vtk_output_obj.GetNumberOfCells()))
            if hasattr(vtk_output_obj, 'GetBounds'):
                layout.label(text='X range: ' + fs.format(vtk_output_obj.GetBounds()[0]) + \
                             ' - ' + fs.format(vtk_output_obj.GetBounds()[1]))
                layout.label(text='Y range: ' + fs.format(vtk_output_obj.GetBounds()[2]) + \
                             ' - ' + fs.format(vtk_output_obj.GetBounds()[3]))
                layout.label(text='Z range: ' + fs.format(vtk_output_obj.GetBounds()[4]) + \
                             ' - ' + fs.format(vtk_output_obj.GetBounds()[5]))
            data = {}
            if hasattr(vtk_output_obj, 'GetPointData'):
                data['Point data'] = vtk_output_obj.GetPointData()
            if hasattr(vtk_output_obj, 'GetCellData'):
                data['Cell data'] = vtk_output_obj.GetCellData()
            if hasattr(vtk_output_obj, 'GetFieldData'):
                data['Field data'] = vtk_output_obj.GetFieldData()
            for k in data:
                d = data[k]
                for i in range(d.GetNumberOfArrays()):
                    arr = d.GetArray(i)
                    data_type_name = arr.GetDataTypeAsString()
                    n_comps = arr.GetNumberOfComponents()
                    name = arr.GetName()
                        
                    if name is None or data_type_name is None or n_comps is None:
                        l.warning("Invalid array encountered...")

                    range_text = ''
                    for n in range(n_comps):
                        r = arr.GetRange(n)
                        range_text += '[' + fs.format(r[0]) +', ' + fs.format(r[1]) + ']  '
                    row = layout.row()
                    row.label(text = self.arr_string.format(k=k, i=i, data_type_name=data_type_name,
                                                            n_comps=n_comps, name=name, range_text=range_text))

        layout.separator()
        row = layout.row()
        row.operator("node.bvtk_node_update").node_path = node_path(self)

    def init_vtk(self):
        return None

    def apply_inputs(self):
        # Assign upstream VTK object to this node's VTK object to provide output
        upstream_node, dummy = self.get_input_node_and_socketname()
        upstream_vtk_obj = BVTKCache.get_vtk_obj(upstream_node.node_id)
        BVTKCache.map_node(self, upstream_vtk_obj)

    def apply_properties(self):
        return None

TYPENAMES = []
add_class(BVTK_Node_Info)
TYPENAMES.append('BVTK_Node_InfoType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Debug", "Debug", items=menu_items))
