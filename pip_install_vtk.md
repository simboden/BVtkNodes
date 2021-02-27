# Installation of VTK in Blender 2.8x Python via Pip 

Replace x in the version number with the correct number you are using

# On Windows

Run CMD.EXE as administrator and run commands
```
cd C:\Program Files\Blender Foundation\Blender\2.8x\python\bin
python.exe -m ensurepip
python.exe -m pip install vtk==9.0.1
```
or if you need to install newest (possibly unsupported) version of vtk, replace last command with
```
python.exe -m pip install vtk
```

# On Linux

Run on normal terminal commands
```
cd /path/to/blender-2.8x/2.8x/python/bin
./python3.7m -m ensurepip
./python3.7m -m pip install vtk==9.0.1
```
or if you need to install newest (possibly unsupported) version of vtk, replace last command with
```
./python3.7m -m pip install vtk
```

# Testing

You can test if VTK is found in 
[Blender Python Console](https://docs.blender.org/manual/en/latest/editors/python_console.html)
(by default located in the Scripting 
[workspace](https://docs.blender.org/manual/en/latest/interface/window_system/workspaces.html)
) with commands

```
import vtk
vtk.vtkVersion().GetVTKVersion()
```

which should return VTK version number that was installed.
