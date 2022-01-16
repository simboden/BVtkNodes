#Dependencies in pip
$PWD/blender/2.93/python/bin/python3.9 -m ensurepip
$PWD/blender/2.93/python/bin/python3.9 -m pip install --upgrade pip
$PWD/blender/2.93/python/bin/python3.9 -m pip install vtk==9.1.0 pyvista

#Disable vtkRenderingMatplotlib
sed -i 's/from\ \.vtkRenderingMatplotlib\ import/\#from\ \.vtkRenderingMatplotlib\ import/g' $PWD/blender/2.93/python/lib/python3.9/site-packages/vtkmodules/all.py

#Install the addon
mkdir $PWD/blender/2.93/scripts/addons/BVtkNodes
unzip BVtkNodes.zip -d $PWD/blender/2.93/scripts/addons/BVtkNodes
