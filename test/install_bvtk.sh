#Dependencies in pip
$PWD/blender/2.83/python/bin/python3.7m -m ensurepip
$PWD/blender/2.83/python/bin/python3.7m -m pip install --upgrade pip
$PWD/blender/2.83/python/bin/python3.7m -m pip install vtk==9.0.1 pyvista

#Install the addon
mkdir $PWD/blender/2.83/scripts/addons/BVtkNodes
unzip BVtkNodes.zip -d $PWD/blender/2.83/scripts/addons/BVtkNodes