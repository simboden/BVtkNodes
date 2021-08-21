.. _development:

Development
===========
BVTKNodes is a community driven `open-source project <https://producingoss.com/>`_.
If you want to develop and improve BVTKNodes for everyone, please feel free to head over to `our current github repository <https://github.com/tkeskita/BVtkNodes>`_.

Terminology
-----------

- (BVTK) node = a Blender node object in BVTK node tree
- generated node = VTK node which has been automatically generated
- custom node = customized version of a generated node
- VTK node = a generated or a custom node which implements a VTK class
- special node = all other nodes in BVTK node tree
- socket = Blender socket in a node
- VTK object = instance of vtkObject class
- VTK connection = instance of vtkAlgorithmOutput class

BVTK Core
---------

The `tkeskita/bvtknodes <https://github.com/tkeskita/BVtkNodes>`_
version includes a modified core functionality for BVTK Nodes, which
allows custom functionality to be plugged in for custom nodes.
These can be used by adding special functions to nodes:

- **init_special()** - special function to run when node is created.
- **draw_buttons_special()** - special node UI contents.
- **init_vtk()** - creation and initialization of VTK object.
- **apply_inputs()** - update input connections to VTK object.
- **validate_and_update_values_special()** - optional node value
  validation and update routine.
- **apply_properties_special()** - special function to run for setting
  properties and update VTK object for special nodes.
- **get_vtk_output_object_special()** - special function to provide
  VTK output object for special nodes.

Please see current custom nodes located in `custom_nodes` folder in
the source for examples.

Testing Framework
-----------------
BVTKNodes includes a testing framework (located in the `test` directory) that should help with checking new updates and finding bugs.

Executing Tests
***************
* First, make sure that BVTKNodes is correctly installed (see :ref:`general_installation`) by running one of the examples located in the Tree Tab.
* Set environment variable *BLENDER_PATH* to the Blender executable that you want to test.
* Run ``python test/test_main.py`` with a Python environment that has NumPy (and optionally PyVista, best installed using pip) package installed.

Running the tests should result in an output similar to the following:

.. code-block:: bash

    ........
    ----------------------------------------------------------------------
    Ran 8 tests in 36.380s

    OK

.. note::
    Tests can be also run from Blender's Python environment (see :ref:`vtk_installation`).


Writing Tests
*************

BVTKNodes is currently not extensively tested and would benefit from additional tests.
Nonetheless, we hope that new features would include at least one test to check that the features are working as expected.

Typical test applies `test_template.blend` file which includes an empty node tree, and a JSON file that defines the node tree.
Optionally an additional Python script can be provided to run special commands.
If no additional script is provided, a general `test_blender_script.py` is called.
This script executes the tree once (using the `Update All` node, which must be present in the node tree) and checks for any errors.
For discussion about testing, please check `#57 <https://github.com/tkeskita/BVtkNodes/pull/57>`_.
See :ref:`Tree <json_importexport>` on how to create the JSON file from an existing node tree.

``BVTKMainExamples`` in `test_main.py` lists all JSON files with their corresponding Python scripts and executes them as follows:

* Blender is called with flags ``--python [script] --background --python-exit-code 1 -- -j [JSON file] [additional parameters]``.
* The Python script is executed. Note that you can use utility functions from `test_blender_script.py` for parsing additional parameters and to create the node tree.
* After execution, Blender exits.

The test is assumed successful if the return code of Blender is zero. 
Exceptions in the script, or custom assertions must return a different return code to indicate failure.
It is also possible to provide a small reference data file and compare test result to it (see the `test_glyphs_and_writers` test case).
Alternatively, you can compare the data directly inside the script (see the `test_global_time_keeper` test case).
Please try to keep test cases small, effective, and avoid binary files if possible.
