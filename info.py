from .core import l # Import logging
from .core import *

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

        vtk_obj = self.get_vtk_obj()
        vtk_obj.Update()
        vtk_output_obj = self.get_vtk_output_object()

        text += 'Type: ' + vtk_output_obj.__class__.__name__ + '\n'

        # Print block names for vtkMultiBlockDataSet
        if hasattr(vtk_output_obj, 'GetNumberOfBlocks'):
            for i in range(vtk_output_obj.GetNumberOfBlocks()):
                block = vtk_output_obj.GetBlock(i)
                if not hasattr(vtk_output_obj, "GetMetaData"):
                    text += "     Block " + str(i) + ": No meta data available\n"
                    continue
                meta_data = vtk_output_obj.GetMetaData(i)
                if not meta_data:
                    continue
                block_name = meta_data.Get(vtk.vtkCompositeDataSet.NAME())
                text += "     Block " + str(i) + ": %r" % block_name + " (" + \
                       (block.__class__.__name__ if block else "Empty Block") + ")\n"

        if hasattr(vtk_output_obj, 'GetNumberOfPoints'):
            text += 'Points: ' + str(vtk_output_obj.GetNumberOfPoints()) + '\n'
        if hasattr(vtk_output_obj, 'GetNumberOfCells'):
            text += 'Cells: ' + str(vtk_output_obj.GetNumberOfCells()) + '\n'
        if hasattr(vtk_output_obj, 'GetBounds'):
            # GetBounds() can fail, so use try-except for getting bounds
            try:
                bounds = vtk_output_obj.GetBounds()
                text += 'X range: ' + fs1.format(bounds[0]) + \
                    ' - ' + fs1.format(bounds[1]) + '\n'
                text += 'Y range: ' + fs1.format(bounds[2]) + \
                    ' - ' + fs1.format(bounds[3]) + '\n'
                text += 'Z range: ' + fs1.format(bounds[4]) + \
                    ' - ' + fs1.format(bounds[5]) + '\n'
            except:
                pass
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
        self.set_vtk_status('out-of-date')
        vtk_obj = vtk.vtkPassThroughFilter() # Pass through all input to output
        return vtk_obj

TYPENAMES = []
add_class(BVTK_Node_Info)
TYPENAMES.append('BVTK_Node_InfoType')

menu_items = [NodeItem(x) for x in TYPENAMES]
CATEGORIES.append(BVTK_NodeCategory("Debug", "Debug", items=menu_items))
