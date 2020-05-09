.. _ug_nodes:

Node Examples for Unstructured Grids
====================================

Here are listed various node setups used for processing unstructured
grid (*vtkUnstructuredGrid*) data composed of 3D cells. Examples below
utilize the *cubeflow* OpenFOAM dataset located in *examples_data*
folder of the add-on sources.

Set Up Reader
-------------

Here is a typical start node setup to read data, select time, select
the correct data block and finally info node to see information about
data read in:

* Add *vtkOpenFOAMReader* - Select *case.foam* file located at the
  *cubeflow* directory to *FileName* field.
* Add *Time Selector* node and connect it
* Add *Multi Block Leaf* node and connect it
* Add *Info* node and connect it
* Press *Update* button on *Info* node to update pipeline

When data is read in correctly, the *Info* node shows number of
points/cells, and fields read in. Set *Time Step* value to **5** in
*Time Selector* node either manually or by changing frame number in
Blender Timeline Editor.

.. image:: images/ug_reader_nodesetup.png

You need to select correct reader node depending on your data type. Note
that you may need to adjust reader settings and/or add *Custom Code*
to some readers, depending on your case and data.

* *vtkXMLUnstructuredGridReader* for **.vtu** files
* *vtkPolyDataReader* for some **.vtk** files

The following node setups assume that the input of the first node is
connected to some data source which produces *vtkUnstructuredGrid*
with data for 3D cells, such as the output of *Multi Block Leaf* node
in example above.


Extract Boundary Surfaces
-------------------------

*vtkGeometryFilter* followed by *VTK To Blender* extracts all boundary
surfaces.

.. image:: images/ug_boundary_nodesetup.png

If you want to extract a single boundary patch for OpenFOAM case, you
need to

* Add **EnableAllPatchArrays()** Custom Code to *vtkOpenFOAMReader*
* Add two *Multi Block Leaf* nodes in series to select patches and the
  wanted patch, before connecting to *vtkGeometryFilter*.

.. image:: images/ug_extract_boundary_patch_nodesetup.png


Calculations Using Field Data
-----------------------------

TODO

* Vector magnitude

* Vector component


Cutting Field Data
------------------

TODO, vtkCutter in kitchen example


Vector Glyphs
-------------

TODO, vtkGlyph3D in kitchen example


Contours
--------

TODO


Stream Tracers
--------------

TODO
