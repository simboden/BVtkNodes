.. _development:

Development
===============================
BVTK is an open-source project that relies on and is happy for any contributions from the community.
If you want to start in helping to develop and improve BVTK, feel free to head over to the github repository at `https://github.com/tkeskita/BVtkNodes <https://github.com/tkeskita/BVtkNodes>`_.

Testing
---------------------------
BVTK now supports a testing framework that should help in checking new updates and finding bugs.

Executing the Tests
*************
* First, make sure that BVTK is correctly installed by running one of the examples in the examples folder. (See :ref:`general_installation`)
* Set your environment variable *BLENDER_PATH* to the blender executable that you want to test and make sure that you can access it through the console you are using to run the tests.
* Run ``python test/test_main.py`` with a python environment that has the numpy package and (optionally) pyvista (best installed using pip).

The tests should now run and you should see an output similar to the following

.. code-block:: bash

    ........
    ----------------------------------------------------------------------
    Ran 8 tests in 36.380s

    OK

.. note::
    The mentioned python environment can even be the python environment of Blender, which already has the numpy package by default.
    This environment can be accessed as described in :ref:`vtk_installation`.


Writing new Tests
*************

BVTK is currently not extensively tested and would benefit from additional tests.
Any new features should also include at least one test that checks if the new features are working as expected.

Each test consists of a .blend file for the initial state, a .json file that defines the BVTK Node Tree and (optionally) a python script that is executed inside Blender.
If no script is provided, a standard script is called that just executes the tree once (through the Update All node if present) and checks for any errors.
Most of the tests use `test_template.blend` and a custom json file for the node tree, which is easier to maintain, as discussed `here <https://github.com/tkeskita/BVtkNodes/pull/57>`_.
See :ref:`Tree <json_importexport>` on how to create the JSON file from an existing node tree.

``BVTKMainExamples`` in test/test_main.py lists all json files with their corresponding python scripts and executes all of them as follows:
* Blender is called with the ``--python [script] --background --python-exit-code 1 -- -j [json file] [additional parameters]`` flag
* The provided python script is executed. Note that you can use some utility functions from test_blender_script.py that already parses the additional parameters and can create the BVTK tree.
* (Optional) If no script was provided, the standard script test/test_blender_script.py will be called, which loads the JSON file, searches for the Update All node inside the tree and executes it. 
* After execution, Blender exits

The test is assumed to be successful if the return code of Blender is equal to zero. 
Exceptions in the script, or custom assertions will return a different return code.
It is also possible to write the data to a file and later load and compare it to a reference in test_main.py (see test_glyphs_and_writers).
Alternatively, you can directly compare the data inside the script that is executed in Blender (see test_global_time_keeper).


