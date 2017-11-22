import vtk

hidden = [
'Debug',
'Modified Time',
'Reference Count',
'Registered Events',
'Executive',
'ErrorCode',
'Information',
'AbortExecute',
'Progress',
'Progress Text',
'Output Points Precision',

'File Type',
'Header',
'ReadFromInputString',
'Input String',
'Input String',
'Input String Length',
'Scalars Name',
'ReadAllScalars',
'Vectors Name',
'ReadAllVectors',
'Normals Name',
'ReadAllNormals',
'Tensors Name',
'ReadAllTensors',
'Texture Coordinates Name',
'ReadAllTCoords',
'Lookup Table Name',
'ReadAllColorScalars',
'Field Data Name',
'ReadAllFields',
'InputStringLength',

'Compute Gradients',
'Contour Values',
'Use Scalar Tree',
'Scalar Tree',
'Locator',
'Precision of the output points',

'NumberOfThreads',
'EnableSMP',
'GlobalDefaultEnableSMP',
'MinimumPieceSize',
'DesiredBytesPerPiece',
'SplitMode',
'Dimensionality',

]

def print_o(o):

    m = str(o).split('\n')
    m = [ x.split(':')[0].strip() for x in m ] 
    m = [ x for x in m if not x in hidden and x != '' ]
    print( '------------------------\n' + '\n'.join(m) )


#print_o( vtk.vtkConeSource() )
#print_o( vtk.vtkStructuredPointsReader() )
#print_o( vtk.vtkContourFilter() )
#print_o( vtk.vtkImageGaussianSmooth() )

print_o( vtk.vtkCubeSource() )
print_o( vtk.vtkPlaneSource() )
print_o( vtk.vtkArrowSource() )
print_o( vtk.vtkSphereSource() )

'''
------------------------
vtkConeSource (0x2ad1da0)
Resolution
Height
Radius
Capping
Center
Direction
------------------------
vtkStructuredPointsReader (0x2c73630)
File Name                                << remove space
------------------------
vtkContourFilter (0x2c79a10)
Compute Normals
Compute Scalars
Value 0                                  << remove 0
------------------------
vtkImageGaussianSmooth (0x2befc60)
RadiusFactors
StandardDeviations
'''

