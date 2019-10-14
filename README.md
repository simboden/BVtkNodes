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
[presented at Blender Conference 2018](https://www.youtube.com/watch?v=KcF4LBTTyvk).

<p align="center">
<img src="isosurfaces.jpg">
</p>

### Information

- **Tested version**: Blender version 2.80 and VTK library version 8.1.2.
- **License**: [GPL v3](http://www.gnu.org/licenses/quick-guide-gplv3.html)
- **Contributors**: Silvano Imboden (s.imboden@cineca.it), Lorenzo Celli,
  Paul McManus, Tuomo Keskitalo

### Prerequisites

BVTKNodes add-on has been tested with Blender version 2.80,
VTK version 8.1.2 and VTK python wrappers
compatible with the Python version used in Blender.
Easiest way is to
[Install VTK into Blender Python via Pip](./pip_install_vtk.md)
which currently installs VTK version 8.1.2.
Another VTK version (7 or later) may be alternatively used, if generated class
definitions (gen_VTK*.py files) are also updated (by running
populate_db.py and generate.py. Warning: Modifications may be
required).
If you want to compile custom VTK, please see
[VTK building instructions for Linux](./build_vtk.md).

### Installation

- Add-on code is available at
  https://github.com/tkeskita/BVtkNodes. To download add-on from
  Github, Select “Clone or download”, then “Download ZIP”.
- Start Blender, go to “Edit” –> “Preferences” –> “Add-ons” –> “Install” –> open the add-on zip file.
- Activate the “BVTKNodes” add-on in Preferences. Add-on is located in
  Node category, Testing level of Blender add-ons.


