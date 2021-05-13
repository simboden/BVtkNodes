from .core import l # Import logging
from .core import *
from .cache import BVTKCache

class BVTK_Node_Info(Node, BVTK_Node):
    '''BVTK Info Node'''
    bl_idname = 'BVTK_Node_InfoType'
    bl_label  = 'Info'

    def m_properties(self):
        return []

    def m_connections(self):
        return (['input'],['output'],[],[])

    def apply_properties_special(self):
        '''Special update function to generate info text from VTK objects
        '''
        text = ""
        fs1 = "{:.5g}"
        fs2 = '{k} [{i}] ({data_type_name}{n_comps}): \'{name}\': {range_text}'

        vtk_obj, vtk_connection = self.get_vtk_obj_and_connection()

        if not vtk_obj:
            self.ui_message = 'Input has no VTK object'
            return 'error'
        if not vtk_connection:
            self.ui_message = 'Input has no VTK connection'
            return 'error'
        num_missing_connections = len(self.get_input_socket_names()) - vtk_obj.GetTotalNumberOfInputConnections()
        if num_missing_connections > 0 :
            self.ui_message = "Missing %d input connection(s)" % num_missing_connections
            return 'error'

        vtk_obj.Update()
        vtk_output_obj = resolve_algorithm_output(vtk_connection)

        text += 'Type: ' + vtk_output_obj.__class__.__name__ + '\n'
        if hasattr(vtk_output_obj, 'GetNumberOfPoints'):
            text += 'Points: ' + str(vtk_output_obj.GetNumberOfPoints()) + '\n'
        if hasattr(vtk_output_obj, 'GetNumberOfCells'):
            text += 'Cells: ' + str(vtk_output_obj.GetNumberOfCells()) + '\n'
        if hasattr(vtk_output_obj, 'GetBounds'):
            text += 'X range: ' + fs1.format(vtk_output_obj.GetBounds()[0]) + \
                ' - ' + fs1.format(vtk_output_obj.GetBounds()[1]) + '\n'
            text += 'Y range: ' + fs1.format(vtk_output_obj.GetBounds()[2]) + \
                ' - ' + fs1.format(vtk_output_obj.GetBounds()[3]) + '\n'
            text += 'Z range: ' + fs1.format(vtk_output_obj.GetBounds()[4]) + \
                ' - ' + fs1.format(vtk_output_obj.GetBounds()[5]) + '\n'
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
                    text += 'Warning: Invalid array encountered, number ' + str(i) + '\n'

                range_text = ''
                for n in range(n_comps):
                    r = arr.GetRange(n)
                    range_text += '[' + fs1.format(r[0]) +', ' + fs1.format(r[1]) + ']  '
                    text += fs2.format(k=k, i=i, data_type_name=data_type_name,
                                       n_comps=n_comps, name=name, range_text=range_text)
                    text += '\n'
        self.ui_message = text
        return 'up-to-date'

    def init_vtk(self):
        self.vtk_status = 'out-of-date'
        vtk_obj = vtk.vtkPassThroughFilter() # Pass through all input to output
        return vtk_obj

TYPENAMES = []
add_class(BVTK_Node_Info)
TYPENAMES.append('BVTK_Node_InfoType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Debug", "Debug", items=menu_items))
