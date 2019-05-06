# BVTKNodes 

[The Visualization Toolkit (VTK)](https://www.vtk.org/) is an open
source library for scientific data visualization. BVTKNodes is a
[Blender](https://www.blender.org/) addon to create and execute VTK
pipelines in Blender Node Editor. The add-on is based on automatic
generation of Blender Node classes from VTK Python classes. A manually
programmed node class can supercede automatically generated code where
needed.

BVTKNodes provides Blender users access to data readers for many
scientific data formats, along with capability to convert VTK data
into a Blender mesh. For VTK users, the add-on provides access to high
quality rendering and many kind of mesh editing tools. The add-on was
[presented at Blender Conference 2018](https://www.youtube.com/watch?v=KcF4LBTTyvk)

<p align="center">
<img src="isosurfaces.jpg">
</p>

### Information

**Note:** This repository is being updated, information may be partially out of date.

**Warning:** On-going code changes may result in incompatibility of
  previously saved files due to class name changes! I will remove this
  warning when renaming is complete.

- **Tested version**: Blender version 2.79b
  and VTK library version 8.2.0.
- **License**: [GPL v3](http://www.gnu.org/licenses/quick-guide-gplv3.html)
- **Contributors**: Silvano Imboden (s.imboden@cineca.it), Lorenzo Celli,
  Paul McManus, Tuomo Keskitalo

### Prerequisites

BVTKNodes add-on requires VTK version 8.2.0 and VTK python wrappers
compatible with the python version used in Blender.
Another VTK version (>7) may be alternatively used, if generated class
definitions (gen_VTK*.py files) are also updated (by running
populate_db.py and generate.py. Warning: Modifications may be
required).
See [VTK building instructions for Linux](./build_vtk.md).

### Installation

- Add-on code is available at
  https://github.com/tkeskita/BVtkNodes. To download add-on from
  Github, Select “Clone or download”, then “Download ZIP”.
- Start Blender, go to “File” –> “User Preferences” –> “Add-ons” –> “Install” –> open the add-on zip file.
- Activate the “BVTKNodes” add-on in Preferences. Add-on is located in
  Node category, Testing level of Blender add-ons.
- Click “Save Preferences” to autoload add-on every time Blender is started


