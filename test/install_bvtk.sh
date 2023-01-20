#Dependencies in pip
$PWD/blender/3.3/python/bin/python3.10 -m ensurepip
$PWD/blender/3.3/python/bin/python3.10 -m pip install --upgrade pip
$PWD/blender/3.3/python/bin/python3.10 -m pip install vtk==9.2.2 pyvista

#Disable vtkRenderingMatplotlib
sed -i 's/from\ \.vtkRenderingMatplotlib\ import/\#from\ \.vtkRenderingMatplotlib\ import/g' $PWD/blender/3.3/python/lib/python3.10/site-packages/vtkmodules/all.py

#Install the addon
mkdir $PWD/blender/3.3/scripts/addons/BVtkNodes
unzip BVtkNodes.zip -d $PWD/blender/3.3/scripts/addons/BVtkNodes
