# Installation of VTK in Blender 2.80 Python via Pip 

# On Windows

Run CMD.EXE as administrator and run commands
```
cd C:\Program Files\Blender Foundation\Blender\2.80\python\bin
python.exe -m ensurepip
python.exe -m pip install vtk
```

# On Linux

Run on normal terminal commands
```
cd /path/to/blender-2.80/2.80/python/bin
./python3.7m -m ensurepip
./python3.7m -m pip install vtk
```

# Testing

You can test if VTK is found in Blender Python Console with commands

```
import vtk
vtk.vtkVersion().GetVTKVersion()
```

which should return VTK version number that was installed.
