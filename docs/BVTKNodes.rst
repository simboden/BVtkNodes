BVKTNodes Addon for Blender
===========================

Introduction
------------

`The Visualization Toolkit (VTK) <https://www.vtk.org/>`_ is an open
source library for scientific data processing and visualization.
BVTKNodes is an addon for 
`Blender (an open source 3D content creation and visualization tool) <https://www.blender.org/>`_.
This addon makes it possible to create and execute VTK pipelines
configured in Blender Node Editor, to produce surface mesh objects,
which can be then modified and visualized in Blender.

BVTKNodes provides Blender users access to data readers for many
scientific data formats, along with capability to convert VTK data
into a Blender mesh. For VTK users, the add-on provides access to high
quality and photorealistic rendering and many kinds of mesh editing tools.
The add-on was first presented at
`Blender Conference 2018 <https://www.youtube.com/watch?v=KcF4LBTTyvk>`_.
You can see more examples in
`a gallery thread on blenderartists <https://blenderartists.org/t/bvtknodes-gallery/1161079>`_.

.. image:: images/isosurfaces.png


Target Use and Users
--------------------

BVTKNodes integrates VTK's data processing capabilities with Blender's
powerful visualization features. It allows creation of photorealistic
images and animations from scientific data.

Use of BVTKNodes requires both Blender and VTK skills. User needs to
know at least Blender 3D Viewport, Node Editor, Materials, Lighting
and Rendering basics, as well as VTK (to the extent required by users'
specific case). If photorealistic rendering or specialized VTK
pipelines are not required, then it is suggested to use `Paraview
<https://www.paraview.org/>`_ instead.

To learn Blender, see resources at `blender.org <https://www.blender.org/>`_
, `Blender 2.8 fundamentals series in Youtube <https://www.youtube.com/playlist?list=PLa1F2ddGya_-UvuAqHAksYnB0qL9yWDO6>`_ and search for Blender tutorials on a topic.
To learn VTK, see `VTK wiki <https://vtk.org/Wiki/VTK/Learning_VTK>`_
and view `VTK discourse forum <https://discourse.vtk.org/>`_.


Technical Details and Limitations
---------------------------------

BVTKNodes is based on automatic generation of Blender Node classes
from VTK Python classes. Simply put, the addon makes VTK classes
available as nodes in Blender. A manually programmed node class can
supercede automatically generated code where needed. It is fairly easy
to upgrade/downgrade to another VTK version, including customized VTK
builds, so this makes BVTKNodes good for prototyping and testing of
VTK pipelines.

BVTKNodes includes many custom made nodes that make it possible to
access VTK time step data, multi block data, and to color surfaces
according to a customizable color ramp. For nodes which have not yet
been fully customized for use in Blender, it is possible to add Custom
Code for VTK objects. This is often needed, since many VTK objects
require custom input from user to work correctly.

.. warning::

   BVTKNodes is a
   `bleeding edge software <https://en.wikipedia.org/wiki/Bleeding_edge_technology>`_.
   Because both Blender and VTK are constantly evolving pieces of
   software, it is expected that customized parts in BVTKNodes can break
   when versions change. Many parts of the addon would benefit from further
   development. Addon is prone to crashing, and results should always be
   reviewed critically for bugs. There is no guarantee: you use the
   addon at your own risk.


Available Versions of BVTKNodes addon
-------------------------------------

1. `simboden/bvtknodes <https://github.com/simboden/BVtkNodes>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Original version of BVTKNodes for Blender version 2.79 using VTK 8.0.1.
This version was demonstrated in the
`Blender Conference 2018 presentation <https://www.youtube.com/watch?v=KcF4LBTTyvk>`_.

2. `tkeskita/bvtknodes <https://github.com/tkeskita/BVtkNodes>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Upgraded and developed version for Blender 2.80 (or newer) using VTK
8.1.2. Please use latest released version of Blender for this version.

.. note::
   
   This documentation corresponds to `tkeskita/bvtknodes <https://github.com/tkeskita/BVtkNodes>`_ version.

3. `esowc/sci_vis <https://github.com/esowc/sci_vis>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A recent, more developed version with new features for Blender 2.79b
using VTK 8.2.0. Old Blender version is used for stability and 
`animation features that are not yet working correctly in Blender 2.80 or newer <https://developer.blender.org/T66392>`_.


Installation of VTK for Blender
-------------------------------

BVTKNodes requires VTK to be available as a module in Blender's
Python environment. It is suggested to 
`install VTK into Blender Python via Pip <https://github.com/tkeskita/BVtkNodes/blob/master/pip_install_vtk.md>`_.

.. note::

   **Optional, for experts:** Another VTK version (7 or later) may be alternatively used, but
   this requires compilation of VTK. Details are beyond this document, but
   to summarize briefly: If another version is used, then
   generated class definitions (gen_VTK*.py files) should also be updated
   (by running populate_db.py and generate.py. Warning: Modifications may be
   required). If you want to compile custom VTK, please see
   `VTK building instructions for Linux <https://github.com/tkeskita/BVtkNodes/blob/master/build_vtk.md>`_.


Installation
------------

- Install Blender (if needed, see `instructions <https://docs.blender.org/manual/en/latest/getting_started/installing/index.html>`_).
- Install VTK to Blender Python as instructed above in `Installation of VTK for Blender`_.
- Download appropriate BVTKNodes add-on ZIP file (see options in `Available Versions of BVTKNodes addon`_). To download add-on from Github, Select “Clone or download”, then “Download ZIP”.
- Start Blender, go to “Edit” –> “Preferences” –> “Add-ons” –> “Install” –> open the add-on zip file.
- Activate the “BVTKNodes” add-on in Preferences by clicking on the checkbox. Add-on is located in Node category, "Community" level of Blender add-ons.
- **For Blender 2.79:** User Settings are located in File menu, and it is suggested to **Save User Settings** before closing settings.


Workspace Setup
---------------

BVTKNodes is used via **BVTK Node Editor** in Blender.
These instructions help you set up a default workspace in Blender for
BVTK (nodes), to make work easy.

- Start a new file in Blender (File --> New --> General).
- Delete default Cube object.
- Duplicate the "Default" Workspace (right-click --> Duplicate) and
  rename the new workspace (double-click on the name) to "BVTK".
- Split the 3D Viewport horizontally, and then vertically to create 3
  window areas.
- Change top area from top left corner into "BVTK Node Tree". If you
  don't have this option available, then there is something wrong in
  the installation.

  .. image:: images/editor_selection.png

- In BVTK Node Editor, click New to add a new node tree.
- Change one of the smaller areas into "Text Editor".
- In Text Editor, click on "New" and rename "Text" into "BVTK".
- Save this setup as a Blender file so that you can use it as a template
  when starting to process a new case.

.. figure:: images/workspace.png

   Example setup for BVTK workspace.


Simple Example: Human Head Visualization
----------------------------------------

Here are the steps to create the meshes for the example
shown in `Introduction`_. For other examples, see `Tree`_ tab below.

- The data file *head.vti* is located in *examples_data* folder in the
  sources. You can also
  `download head.vti from github <https://github.com/tkeskita/BVtkNodes/blob/master/examples_data/head.vti>`_.
- Create node setup as shown in the image in `Introduction`_. You can
  add nodes from Add menu or by shortcut key shift + A. Link nodes by
  dragging from connectors to another connector.
- Set **FileName** in *vtkXMLImageDataReader* node by clicking on the
  folder icon and select *head.vti* file.
- In *vtkContourFilter* node click plus icon to add a contour value,
  then set the value.
- In *VTK To Blender* node, add name to mesh object, set **Generate
  Material** on, and run **Update**. A mesh object should now appear
  in the 3D viewport. Repeat this for the other *VTK To Blender Node*.
- At this point, BVTKNodes should have created two (overlapping) mesh
  objects, which are shown in the Blender Properties Editor.
- Save Blender file.

In practice this is the end of the BVTKNodes part. The rest of the
visualization includes steps in Blender: moving of objects, creation
of background plane object for visualization, setting up camera,
setting up lighting and world backround, modification of materials for
objects, modify settings for rendering engine, rendering of image,
possibly composition and finally saving of image file. To learn about
those, it is suggested to search for Blender tutorials on-line.


Tabs in BVTK Node Editor
------------------------

Tabs are located in the Sidebar of the BVTK Node Editor. You can hide
and view the Sidebar by pressing "N" key while hovering mouse over the
BVTK Node Editor. Note: Some tabs become visible only after you select
a node in the node tree. The properties and operations shown in tabs
will affect the active node.

Item, Tool and View Tabs
^^^^^^^^^^^^^^^^^^^^^^^^

These tabs are just default Blender tabs, which show node properties, node tools and view.

Properties
^^^^^^^^^^

- **Show/Hide Properties** shows list of VTK object boolean properties,
  which can be hidden or shown in the node based on this setting.
- **Edit Custom Code** operator copies node's custom code into BVTK
  Text Block in Text Editor, where it is possible to add code,
  which will be run, line by line, for the VTK object represented
  by this node when the node is updated.
- **Save Custom Code** operator saves the text from the BVTK Text Block
  into custom code storage string of the active node. Custom Code will be
  shown in the node if there is any saved to it.

Inspect
^^^^^^^

This tab contains tools for debugging and information.

- Inspect tab shows the VTK version at the top.
- **Update Object** operator will call Update() for the VTK object
  represented by this node.
- **Documentation** will show doc string of the VTK object in the
  BVTK Text Block in the Text Editor.
- **Node Status** will show status of the VTK object in the
  BVTK Text Block in the Text Editor.
- **Output Status** will show status of the VTK object in the
  BVTK Text Block in the Text Editor.
- **Online Documentation** will open up web browser showing the
  Doxygen generated documentation for the very latest nightly
  version of VTK. Warning: Documentation may not exactly match
  the version of VTK used in BVTKNodes!

Favorites
^^^^^^^^^

This tab lists favorite nodes. You can delete and add nodes for eay
access here.

Tree
^^^^

Node tree related operations.

- **Export JSON** exports the current node tree as JSON file.
- **Import JSON** imports the current node tree as JSON file.
- **Arrange** will try to arrange node tree for a clean view.
  Warning: Does not work well for complex node trees.
- **Examples** contains a selection of example node trees you can
  try out.


Special Nodes
-------------

VTK To Blender
^^^^^^^^^^^^^^

This is the main node, which converts VTK mesh data into Blender mesh.

- **Name** specifies the object and mesh names for the Blender object
  which will be created. Note: Any pre-existing mesh will be deleted
  upon update.
- **Auto update**: If enabled, the node tree will be updated immediately
  whenever a value in a node is changed. If not enabled, the user must
  run **Update** operator manually to update Blender object and mesh
  after changes.
- **Smooth** will set surface normal smoothing on for the mesh if enabled.
- **Generate Material** will generate an white diffuse default
  material and assign it to this object. Warning: Any existing
  material is overwritten if enabled.
- **Update** executes the node pipeline connected to this node.

Info
^^^^

Info node shows information about the VTK pipeline, and is useful for
VTK debugging purposes. It is best to try to use this node whenever
uncertain of what the current VTK pipeline contains. Currently
it shows:

- Type of VTK data.
- Number of points and cells in VTK data.
  *Note:* "cell" in VTK terminology can refer to a face or a 3D cell.
- X, Y and Z coordinate ranges of the data.
- Point and cell data (with names and value ranges) included in the
  pipeline.

Color Mapper
^^^^^^^^^^^^

This node is used to assign color to mesh data. You will see the colors
in Blender 3D Viewport when Shading mode is set to either **Material
Preview** or **Rendered**.

- **Input** connector is connected to a VTK pipeline
- **lookuptable** connector should be connected to a *Color Ramp* node,
  which specifies the colors for the value range.
- **Generate scalar bar** will generate a color legend object to the
  Blender scene. Warning: This feature is not working currently well.
  Alternative for this is to prepare a separate color legend image in an
  image manipulation program and composite that on top of the result
  images.
- **color bar** selects the variable according to which coloring is
  carried out.
- **Automatic range** if enabled, will udate the value ranges
  automatically.
- **min** and **max** specify the value range.
- **output** connector should be attached to a *VTK To Blender* node.

Multi Block Leaf
^^^^^^^^^^^^^^^^

This node allows you to filter to a single data set, when the input is
of type *vtkMultiBlockDataSet*. This is often required prior to
processing of a specific array data when a VTK Reader provides
multi block data.

Time Selector
^^^^^^^^^^^^^

This node can be connected immediately after a VTK Reader node to
control which time point of transient (time dependent) data is to be
processed.

Note: Time can be controlled via Blender Timeline Editor. If frame in
the Timeline is changed, the Time Step in the Time Selector node is
automatically updated to correspond that frame number. This allows
rendering of animations directly from Blender.

Note 2: If the VTK Reader is not aware of time data, and if File Name
of the Reader node contains integers at the end of the File Name, then
the integer part of the File Name is updated to correspond to Timeline
frame number. This allows animation of time series data for readers
that are not aware of time (e.g. vtkPolyDataReader, which can read
point and surface data from .vtk files).


Other Resources
---------------

- There are some examples in `Blenderartists BVTKNodes gallery discussion thread <https://blenderartists.org/t/bvtknodes-gallery/1161079/21>`_.

- You are free to ask and give advice for specific use cases at `github issues page <https://github.com/tkeskita/BVtkNodes/issues>`_.


Special Use Cases
-----------------

TODO. Here will be added documentation about various specific node
pipelines to achieve .
