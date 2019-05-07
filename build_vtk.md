# Compile a VTK compatible with Blender 

These are the steps that worked for me with VTK8 and Blender 2.79 on Ubuntu 16.04 LTS.
I wasnt't able to do the same thing on OSX, and I haven't tried yet on Windows (sorry)
I'll update this page as soon as I have more results.    

In short you have to compile Python that matches the one in Blender, 
then compile VTK and its python bindings using the your version of Python, 
lastly you need to configure the environment so that the various libraries can be found from Blender.


find out which version of python is blender using
```
run blender, create a py-console, 
> import sys 
> sys.version
'3.5.3 (default, May 18 2017, 14:40:48) \n[GCC 5.4.1 20161019]'
```

download and compile python
```
> wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
> tar -xvzf Python-3.5.3.tgz
> cd python-sources
> ./configure --prefix=../install --with-computed-gotos --with-pymalloc [--enable-shared or --enable_framework on osx ]
```
the last three options should build python matching the way it is built for blender 
```
> make -j 4
> make install
> cd ../install/bin 
> python
Python 3.5.3 (default, Nov  3 2017, 17:31:29) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
```
download and compile vtk using the previous python.   
prepare the following folders:
```
xxx/VTK8-py353/src -- explode the vtk source here
xxx/VTK8-py353/build
xxx/VTK8-py353/install
```
run cmake-gui, and set src and build dir,   
press configure
```
set CMAKE_BUILD_TYPE = Release
set INSTALL_PREFIX= xxx/VTK8-py353/install
set module_vtkImagingOpenGL2 = on
set module_vtkPython = on
set module_vtkWrappingPythonCore= on
```
press configure
```
set PYTHON/PYTHON_INCLUDE_DIR = your_python_install_dir/include
set PYTHON/PYTHON_LIB_DIR =  your_python_install_dir/lib
set VTK/VTK_PYTHON_VERSION = 3
set VTK/VTK_WRAP_PYTHON  = on

> cp xxx/PY353/include/python3.5m/patchlevel.h  xxx/PY353/install/include/patchlevel.h
```
press generate
```
> export PYTHONPATH= xxx/PY353/install/lib/python3.5:$PYTHONPATH
> export LD_LIBRARY_PATH= xxx/PY353/install/lib:$LD_LIBRARY_PATH
> cd ../build
> make 
> make install
```
configure the environment
```
> export PYTHONPATH= xxx/VTK/install/site-packages:$PYTHONPATH
> export LD_LIBRARY_PATH= xxx/VTK/install/lib:$LD_LIBRARY_PATH
```
test it:       
Run Blender, open the python console 
```
> import vtk
> dir(vtk)
[ ‘DC’… ….. 'vtkZLibDataCompressor' ]
```
