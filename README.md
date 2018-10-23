# BVtkNodes 
BVtkNodes is a Blender Addon allowing to use VTK within Blender.

The Visualization Toolkit (VTK https://www.vtk.org/ ) is an open source library for scientific visualization developed by Kitware.
Paraview ( https://www.kitware.com/platforms ), VolView, 3DSlicer are some of the open source applications built on top of VTK.

In VTK the process of reading/transform/display data is accomplished by instantiating and connecting
among them a series of reader/filters/actors so it naturally fit the metaphor provided by the Blender Node Editor, 

### Goals:
provide a tools to quickly learn VTK and prototiping VTK pipelines.

Beside this, BVtkNodes shows that Blender and VTK can work togheter nicely :

BVTKNodes may provide Blender users with:
- a wide number of importers for different data format commonly used in scientific research
- features to process these data until they become surfaces that can be transformed in Blender meshes
- bidirectional transfering of ( specific type of ) data between Blender and VTK

Blender may provide VTK users with:
- high quality rendering
- mesh editing features of any kind

### Status:
Beta 

### Download
[BVtkNodes.zip]( http://github.com/simboden/BVtkNodes/blob/master/BVtkNodes.zip )
