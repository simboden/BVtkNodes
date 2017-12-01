from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKArrayDataReader(Node, VTKReaderNode):

    bl_idname = 'VTKArrayDataReaderType'
    bl_label  = 'vtkArrayDataReader'
    
    m_ReadFromInputString = bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_InputString         = bpy.props.StringProperty( name='InputString',         default="" )
    
    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_InputString',]
    
CLASSES.append  ( VTKArrayDataReader )        
TYPENAMES.append('VTKArrayDataReaderType' )

#--------------------------------------------------------------
class VTKArrayReader(Node, VTKReaderNode):

    bl_idname = 'VTKArrayReaderType'
    bl_label  = 'vtkArrayReader'
    
    m_ReadFromInputString = bpy.props.BoolProperty  ( name='ReadFromInputString', default=False )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_InputString         = bpy.props.StringProperty( name='InputString',         default="" )
    
    def m_properties( self ):
        return ['m_ReadFromInputString','m_FileName','m_InputString',]
    
CLASSES.append  ( VTKArrayReader )        
TYPENAMES.append('VTKArrayReaderType' )

#--------------------------------------------------------------
class VTKBMPReader(Node, VTKReaderNode):

    bl_idname = 'VTKBMPReaderType'
    bl_label  = 'vtkBMPReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_Allow8BitBMP             = bpy.props.BoolProperty       ( name='Allow8BitBMP',             default=0 )
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName          = bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                 = bpy.props.IntProperty        ( name='DataMask',                 default=0 )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                  = bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_Allow8BitBMP','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKBMPReader )        
TYPENAMES.append('VTKBMPReaderType' )

#--------------------------------------------------------------
class VTKBYUReader(Node, VTKReaderNode):

    bl_idname = 'VTKBYUReaderType'
    bl_label  = 'vtkBYUReader'
    
    m_ReadDisplacement     = bpy.props.BoolProperty  ( name='ReadDisplacement',     default=1 )
    m_ReadScalar           = bpy.props.BoolProperty  ( name='ReadScalar',           default=1 )
    m_ReadTexture          = bpy.props.BoolProperty  ( name='ReadTexture',          default=1 )
    m_DisplacementFileName = bpy.props.StringProperty( name='DisplacementFileName', default="" )
    m_FileName             = bpy.props.StringProperty( name='FileName',             default="" )
    m_GeometryFileName     = bpy.props.StringProperty( name='GeometryFileName',     default="" )
    m_ScalarFileName       = bpy.props.StringProperty( name='ScalarFileName',       default="" )
    m_TextureFileName      = bpy.props.StringProperty( name='TextureFileName',      default="" )
    m_PartNumber           = bpy.props.IntProperty   ( name='PartNumber',           default=0 )
    
    def m_properties( self ):
        return ['m_ReadDisplacement','m_ReadScalar','m_ReadTexture','m_DisplacementFileName','m_FileName','m_GeometryFileName','m_ScalarFileName','m_TextureFileName','m_PartNumber',]
    
CLASSES.append  ( VTKBYUReader )        
TYPENAMES.append('VTKBYUReaderType' )

#--------------------------------------------------------------
class VTKCMLMoleculeReader(Node, VTKReaderNode):

    bl_idname = 'VTKCMLMoleculeReaderType'
    bl_label  = 'vtkCMLMoleculeReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKCMLMoleculeReader )        
TYPENAMES.append('VTKCMLMoleculeReaderType' )

#--------------------------------------------------------------
class VTKCPExodusIIInSituReader(Node, VTKReaderNode):

    bl_idname = 'VTKCPExodusIIInSituReaderType'
    bl_label  = 'vtkCPExodusIIInSituReader'
    
    m_FileName        = bpy.props.StringProperty( name='FileName',        default="" )
    m_CurrentTimeStep = bpy.props.IntProperty   ( name='CurrentTimeStep', default=0 )
    
    def m_properties( self ):
        return ['m_FileName','m_CurrentTimeStep',]
    
CLASSES.append  ( VTKCPExodusIIInSituReader )        
TYPENAMES.append('VTKCPExodusIIInSituReaderType' )

#--------------------------------------------------------------
class VTKChacoGraphReader(Node, VTKReaderNode):

    bl_idname = 'VTKChacoGraphReaderType'
    bl_label  = 'vtkChacoGraphReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKChacoGraphReader )        
TYPENAMES.append('VTKChacoGraphReaderType' )

#--------------------------------------------------------------
class VTKChacoReader(Node, VTKReaderNode):

    bl_idname = 'VTKChacoReaderType'
    bl_label  = 'vtkChacoReader'
    
    m_GenerateEdgeWeightArrays     = bpy.props.BoolProperty  ( name='GenerateEdgeWeightArrays',     default=0 )
    m_GenerateGlobalElementIdArray = bpy.props.BoolProperty  ( name='GenerateGlobalElementIdArray', default=1 )
    m_GenerateGlobalNodeIdArray    = bpy.props.BoolProperty  ( name='GenerateGlobalNodeIdArray',    default=1 )
    m_GenerateVertexWeightArrays   = bpy.props.BoolProperty  ( name='GenerateVertexWeightArrays',   default=0 )
    m_BaseName                     = bpy.props.StringProperty( name='BaseName',                     default="" )
    
    def m_properties( self ):
        return ['m_GenerateEdgeWeightArrays','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateVertexWeightArrays','m_BaseName',]
    
CLASSES.append  ( VTKChacoReader )        
TYPENAMES.append('VTKChacoReaderType' )

#--------------------------------------------------------------
class VTKDEMReader(Node, VTKReaderNode):

    bl_idname = 'VTKDEMReaderType'
    bl_label  = 'vtkDEMReader'
    e_ElevationReference_items=[ (x,x,x) for x in ['SeaLevel', 'ElevationBounds']]
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    e_ElevationReference = bpy.props.EnumProperty  ( name='ElevationReference', default="ElevationBounds", items=e_ElevationReference_items )
    
    def m_properties( self ):
        return ['m_FileName','e_ElevationReference',]
    
CLASSES.append  ( VTKDEMReader )        
TYPENAMES.append('VTKDEMReaderType' )

#--------------------------------------------------------------
class VTKDICOMImageReader(Node, VTKReaderNode):

    bl_idname = 'VTKDICOMImageReaderType'
    bl_label  = 'vtkDICOMImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_DirectoryName            = bpy.props.StringProperty     ( name='DirectoryName',            default="" )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_DirectoryName','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKDICOMImageReader )        
TYPENAMES.append('VTKDICOMImageReaderType' )

#--------------------------------------------------------------
class VTKDICOMReader(Node, VTKReaderNode):

    bl_idname = 'VTKDICOMReaderType'
    bl_label  = 'vtkDICOMReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    e_MemoryRowOrder_items=[ (x,x,x) for x in ['FileNative', 'TopDown', 'BottomUp']]
    
    m_AutoRescale              = bpy.props.BoolProperty       ( name='AutoRescale',              default=1 )
    m_AutoYBRToRGB             = bpy.props.BoolProperty       ( name='AutoYBRToRGB',             default=1 )
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_OverrideCharacterSet     = bpy.props.BoolProperty       ( name='OverrideCharacterSet',     default=False )
    m_Sorting                  = bpy.props.BoolProperty       ( name='Sorting',                  default=1 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_TimeAsVector             = bpy.props.BoolProperty       ( name='TimeAsVector',             default=0 )
    m_DesiredStackID           = bpy.props.StringProperty     ( name='DesiredStackID',           default="" )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_DesiredTimeIndex         = bpy.props.IntProperty        ( name='DesiredTimeIndex',         default=-1 )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    m_OutputScalarType         = bpy.props.IntProperty        ( name='OutputScalarType',         default=-1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    e_MemoryRowOrder           = bpy.props.EnumProperty       ( name='MemoryRowOrder',           default="BottomUp", items=e_MemoryRowOrder_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_AutoRescale','m_AutoYBRToRGB','m_FileLowerLeft','m_OverrideCharacterSet','m_Sorting','m_SwapBytes','m_TimeAsVector','m_DesiredStackID','m_FileName','m_FilePattern','m_FilePrefix','m_DesiredTimeIndex','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_OutputScalarType','e_DataByteOrder','e_DataScalarType','e_MemoryRowOrder','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKDICOMReader )        
TYPENAMES.append('VTKDICOMReaderType' )

#--------------------------------------------------------------
class VTKDIMACSGraphReader(Node, VTKReaderNode):

    bl_idname = 'VTKDIMACSGraphReaderType'
    bl_label  = 'vtkDIMACSGraphReader'
    
    m_EdgeAttributeArrayName   = bpy.props.StringProperty( name='EdgeAttributeArrayName',   default="" )
    m_FileName                 = bpy.props.StringProperty( name='FileName',                 default="" )
    m_VertexAttributeArrayName = bpy.props.StringProperty( name='VertexAttributeArrayName', default="" )
    
    def m_properties( self ):
        return ['m_EdgeAttributeArrayName','m_FileName','m_VertexAttributeArrayName',]
    
CLASSES.append  ( VTKDIMACSGraphReader )        
TYPENAMES.append('VTKDIMACSGraphReaderType' )

#--------------------------------------------------------------
class VTKFacetReader(Node, VTKReaderNode):

    bl_idname = 'VTKFacetReaderType'
    bl_label  = 'vtkFacetReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKFacetReader )        
TYPENAMES.append('VTKFacetReaderType' )

#--------------------------------------------------------------
class VTKFixedWidthTextReader(Node, VTKReaderNode):

    bl_idname = 'VTKFixedWidthTextReaderType'
    bl_label  = 'vtkFixedWidthTextReader'
    
    m_HaveHeaders     = bpy.props.BoolProperty  ( name='HaveHeaders',     default=False )
    m_StripWhiteSpace = bpy.props.BoolProperty  ( name='StripWhiteSpace', default=False )
    m_FileName        = bpy.props.StringProperty( name='FileName',        default="" )
    m_FieldWidth      = bpy.props.IntProperty   ( name='FieldWidth',      default=10 )
    
    def m_properties( self ):
        return ['m_HaveHeaders','m_StripWhiteSpace','m_FileName','m_FieldWidth',]
    
CLASSES.append  ( VTKFixedWidthTextReader )        
TYPENAMES.append('VTKFixedWidthTextReaderType' )

#--------------------------------------------------------------
class VTKGAMBITReader(Node, VTKReaderNode):

    bl_idname = 'VTKGAMBITReaderType'
    bl_label  = 'vtkGAMBITReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKGAMBITReader )        
TYPENAMES.append('VTKGAMBITReaderType' )

#--------------------------------------------------------------
class VTKGESignaReader(Node, VTKReaderNode):

    bl_idname = 'VTKGESignaReaderType'
    bl_label  = 'vtkGESignaReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_Date                     = bpy.props.StringProperty     ( name='Date',                     default="" )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ImageNumber              = bpy.props.StringProperty     ( name='ImageNumber',              default="" )
    m_Modality                 = bpy.props.StringProperty     ( name='Modality',                 default="" )
    m_PatientID                = bpy.props.StringProperty     ( name='PatientID',                default="" )
    m_PatientName              = bpy.props.StringProperty     ( name='PatientName',              default="" )
    m_Series                   = bpy.props.StringProperty     ( name='Series',                   default="" )
    m_Study                    = bpy.props.StringProperty     ( name='Study',                    default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_Date','m_FileName','m_FilePattern','m_FilePrefix','m_ImageNumber','m_Modality','m_PatientID','m_PatientName','m_Series','m_Study','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKGESignaReader )        
TYPENAMES.append('VTKGESignaReaderType' )

#--------------------------------------------------------------
class VTKGaussianCubeReader(Node, VTKReaderNode):

    bl_idname = 'VTKGaussianCubeReaderType'
    bl_label  = 'vtkGaussianCubeReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    m_BScale   = bpy.props.FloatProperty ( name='BScale',   default=1.0 )
    m_HBScale  = bpy.props.FloatProperty ( name='HBScale',  default=1.0 )
    
    def m_properties( self ):
        return ['m_FileName','m_BScale','m_HBScale',]
    
CLASSES.append  ( VTKGaussianCubeReader )        
TYPENAMES.append('VTKGaussianCubeReaderType' )

#--------------------------------------------------------------
class VTKGaussianCubeReader2(Node, VTKReaderNode):

    bl_idname = 'VTKGaussianCubeReader2Type'
    bl_label  = 'vtkGaussianCubeReader2'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKGaussianCubeReader2 )        
TYPENAMES.append('VTKGaussianCubeReader2Type' )

#--------------------------------------------------------------
class VTKISIReader(Node, VTKReaderNode):

    bl_idname = 'VTKISIReaderType'
    bl_label  = 'vtkISIReader'
    
    m_Delimiter  = bpy.props.StringProperty( name='Delimiter',  default=";" )
    m_FileName   = bpy.props.StringProperty( name='FileName',   default="" )
    m_MaxRecords = bpy.props.IntProperty   ( name='MaxRecords', default=0 )
    
    def m_properties( self ):
        return ['m_Delimiter','m_FileName','m_MaxRecords',]
    
CLASSES.append  ( VTKISIReader )        
TYPENAMES.append('VTKISIReaderType' )

#--------------------------------------------------------------
class VTKImageReader(Node, VTKReaderNode):

    bl_idname = 'VTKImageReaderType'
    bl_label  = 'vtkImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName          = bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                 = bpy.props.IntProperty        ( name='DataMask',                 default=0 )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                  = bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKImageReader )        
TYPENAMES.append('VTKImageReaderType' )

#--------------------------------------------------------------
class VTKImageReader2(Node, VTKReaderNode):

    bl_idname = 'VTKImageReader2Type'
    bl_label  = 'vtkImageReader2'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKImageReader2 )        
TYPENAMES.append('VTKImageReader2Type' )

#--------------------------------------------------------------
class VTKJPEGReader(Node, VTKReaderNode):

    bl_idname = 'VTKJPEGReaderType'
    bl_label  = 'vtkJPEGReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKJPEGReader )        
TYPENAMES.append('VTKJPEGReaderType' )

#--------------------------------------------------------------
class VTKMCubesReader(Node, VTKReaderNode):

    bl_idname = 'VTKMCubesReaderType'
    bl_label  = 'vtkMCubesReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_FlipNormals    = bpy.props.BoolProperty  ( name='FlipNormals',    default=0 )
    m_Normals        = bpy.props.BoolProperty  ( name='Normals',        default=1 )
    m_SwapBytes      = bpy.props.BoolProperty  ( name='SwapBytes',      default=0 )
    m_FileName       = bpy.props.StringProperty( name='FileName',       default="" )
    m_LimitsFileName = bpy.props.StringProperty( name='LimitsFileName', default="" )
    m_HeaderSize     = bpy.props.IntProperty   ( name='HeaderSize',     default=0 )
    e_DataByteOrder  = bpy.props.EnumProperty  ( name='DataByteOrder',  default="BigEndian", items=e_DataByteOrder_items )
    
    def m_properties( self ):
        return ['m_FlipNormals','m_Normals','m_SwapBytes','m_FileName','m_LimitsFileName','m_HeaderSize','e_DataByteOrder',]
    
CLASSES.append  ( VTKMCubesReader )        
TYPENAMES.append('VTKMCubesReaderType' )

#--------------------------------------------------------------
class VTKMINCImageReader(Node, VTKReaderNode):

    bl_idname = 'VTKMINCImageReaderType'
    bl_label  = 'vtkMINCImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_RescaleRealValues        = bpy.props.BoolProperty       ( name='RescaleRealValues',        default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    m_TimeStep                 = bpy.props.IntProperty        ( name='TimeStep',                 default=0 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_RescaleRealValues','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_TimeStep','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKMINCImageReader )        
TYPENAMES.append('VTKMINCImageReaderType' )

#--------------------------------------------------------------
class VTKMNIObjectReader(Node, VTKReaderNode):

    bl_idname = 'VTKMNIObjectReaderType'
    bl_label  = 'vtkMNIObjectReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKMNIObjectReader )        
TYPENAMES.append('VTKMNIObjectReaderType' )

#--------------------------------------------------------------
class VTKMNITagPointReader(Node, VTKReaderNode):

    bl_idname = 'VTKMNITagPointReaderType'
    bl_label  = 'vtkMNITagPointReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKMNITagPointReader )        
TYPENAMES.append('VTKMNITagPointReaderType' )

#--------------------------------------------------------------
class VTKMNITransformReader(Node, VTKReaderNode):

    bl_idname = 'VTKMNITransformReaderType'
    bl_label  = 'vtkMNITransformReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKMNITransformReader )        
TYPENAMES.append('VTKMNITransformReaderType' )

#--------------------------------------------------------------
class VTKMRCReader(Node, VTKReaderNode):

    bl_idname = 'VTKMRCReaderType'
    bl_label  = 'vtkMRCReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKMRCReader )        
TYPENAMES.append('VTKMRCReaderType' )

#--------------------------------------------------------------
class VTKMedicalImageReader2(Node, VTKReaderNode):

    bl_idname = 'VTKMedicalImageReader2Type'
    bl_label  = 'vtkMedicalImageReader2'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_Date                     = bpy.props.StringProperty     ( name='Date',                     default="" )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ImageNumber              = bpy.props.StringProperty     ( name='ImageNumber',              default="" )
    m_Modality                 = bpy.props.StringProperty     ( name='Modality',                 default="" )
    m_PatientID                = bpy.props.StringProperty     ( name='PatientID',                default="" )
    m_PatientName              = bpy.props.StringProperty     ( name='PatientName',              default="" )
    m_Series                   = bpy.props.StringProperty     ( name='Series',                   default="" )
    m_Study                    = bpy.props.StringProperty     ( name='Study',                    default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_Date','m_FileName','m_FilePattern','m_FilePrefix','m_ImageNumber','m_Modality','m_PatientID','m_PatientName','m_Series','m_Study','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKMedicalImageReader2 )        
TYPENAMES.append('VTKMedicalImageReader2Type' )

#--------------------------------------------------------------
class VTKMetaImageReader(Node, VTKReaderNode):

    bl_idname = 'VTKMetaImageReaderType'
    bl_label  = 'vtkMetaImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=1 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKMetaImageReader )        
TYPENAMES.append('VTKMetaImageReaderType' )

#--------------------------------------------------------------
class VTKMultiBlockPLOT3DReader(Node, VTKReaderNode):

    bl_idname = 'VTKMultiBlockPLOT3DReaderType'
    bl_label  = 'vtkMultiBlockPLOT3DReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AutoDetectFormat       = bpy.props.BoolProperty  ( name='AutoDetectFormat',       default=0 )
    m_BinaryFile             = bpy.props.BoolProperty  ( name='BinaryFile',             default=1 )
    m_DoublePrecision        = bpy.props.BoolProperty  ( name='DoublePrecision',        default=0 )
    m_ForceRead              = bpy.props.BoolProperty  ( name='ForceRead',              default=0 )
    m_HasByteCount           = bpy.props.BoolProperty  ( name='HasByteCount',           default=0 )
    m_IBlanking              = bpy.props.BoolProperty  ( name='IBlanking',              default=0 )
    m_MultiGrid              = bpy.props.BoolProperty  ( name='MultiGrid',              default=0 )
    m_TwoDimensionalGeometry = bpy.props.BoolProperty  ( name='TwoDimensionalGeometry', default=0 )
    m_FileName               = bpy.props.StringProperty( name='FileName',               default="" )
    m_FunctionFileName       = bpy.props.StringProperty( name='FunctionFileName',       default="" )
    m_QFileName              = bpy.props.StringProperty( name='QFileName',              default="" )
    m_XYZFileName            = bpy.props.StringProperty( name='XYZFileName',            default="" )
    m_ScalarFunctionNumber   = bpy.props.IntProperty   ( name='ScalarFunctionNumber',   default=100 )
    m_VectorFunctionNumber   = bpy.props.IntProperty   ( name='VectorFunctionNumber',   default=202 )
    m_Gamma                  = bpy.props.FloatProperty ( name='Gamma',                  default=1.4 )
    m_R                      = bpy.props.FloatProperty ( name='R',                      default=1.0 )
    e_ByteOrder              = bpy.props.EnumProperty  ( name='ByteOrder',              default="BigEndian", items=e_ByteOrder_items )
    
    def m_properties( self ):
        return ['m_AutoDetectFormat','m_BinaryFile','m_DoublePrecision','m_ForceRead','m_HasByteCount','m_IBlanking','m_MultiGrid','m_TwoDimensionalGeometry','m_FileName','m_FunctionFileName','m_QFileName','m_XYZFileName','m_ScalarFunctionNumber','m_VectorFunctionNumber','m_Gamma','m_R','e_ByteOrder',]
    
CLASSES.append  ( VTKMultiBlockPLOT3DReader )        
TYPENAMES.append('VTKMultiBlockPLOT3DReaderType' )

#--------------------------------------------------------------
class VTKNIFTIImageReader(Node, VTKReaderNode):

    bl_idname = 'VTKNIFTIImageReaderType'
    bl_label  = 'vtkNIFTIImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_PlanarRGB                = bpy.props.BoolProperty       ( name='PlanarRGB',                default=False )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_TimeAsVector             = bpy.props.BoolProperty       ( name='TimeAsVector',             default=False )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_PlanarRGB','m_SwapBytes','m_TimeAsVector','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKNIFTIImageReader )        
TYPENAMES.append('VTKNIFTIImageReaderType' )

#--------------------------------------------------------------
class VTKNIFTIReader(Node, VTKReaderNode):

    bl_idname = 'VTKNIFTIReaderType'
    bl_label  = 'vtkNIFTIReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_PlanarRGB                = bpy.props.BoolProperty       ( name='PlanarRGB',                default=False )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_TimeAsVector             = bpy.props.BoolProperty       ( name='TimeAsVector',             default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_PlanarRGB','m_SwapBytes','m_TimeAsVector','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKNIFTIReader )        
TYPENAMES.append('VTKNIFTIReaderType' )

#--------------------------------------------------------------
class VTKNrrdReader(Node, VTKReaderNode):

    bl_idname = 'VTKNrrdReaderType'
    bl_label  = 'vtkNrrdReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName          = bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                 = bpy.props.IntProperty        ( name='DataMask',                 default=0 )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                  = bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKNrrdReader )        
TYPENAMES.append('VTKNrrdReaderType' )

#--------------------------------------------------------------
class VTKOBJReader(Node, VTKReaderNode):

    bl_idname = 'VTKOBJReaderType'
    bl_label  = 'vtkOBJReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKOBJReader )        
TYPENAMES.append('VTKOBJReaderType' )

#--------------------------------------------------------------
class VTKPChacoReader(Node, VTKReaderNode):

    bl_idname = 'VTKPChacoReaderType'
    bl_label  = 'vtkPChacoReader'
    
    m_GenerateEdgeWeightArrays     = bpy.props.BoolProperty  ( name='GenerateEdgeWeightArrays',     default=0 )
    m_GenerateGlobalElementIdArray = bpy.props.BoolProperty  ( name='GenerateGlobalElementIdArray', default=1 )
    m_GenerateGlobalNodeIdArray    = bpy.props.BoolProperty  ( name='GenerateGlobalNodeIdArray',    default=1 )
    m_GenerateVertexWeightArrays   = bpy.props.BoolProperty  ( name='GenerateVertexWeightArrays',   default=0 )
    m_BaseName                     = bpy.props.StringProperty( name='BaseName',                     default="" )
    
    def m_properties( self ):
        return ['m_GenerateEdgeWeightArrays','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateVertexWeightArrays','m_BaseName',]
    
CLASSES.append  ( VTKPChacoReader )        
TYPENAMES.append('VTKPChacoReaderType' )

#--------------------------------------------------------------
class VTKPDBReader(Node, VTKReaderNode):

    bl_idname = 'VTKPDBReaderType'
    bl_label  = 'vtkPDBReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    m_BScale   = bpy.props.FloatProperty ( name='BScale',   default=1.0 )
    m_HBScale  = bpy.props.FloatProperty ( name='HBScale',  default=1.0 )
    
    def m_properties( self ):
        return ['m_FileName','m_BScale','m_HBScale',]
    
CLASSES.append  ( VTKPDBReader )        
TYPENAMES.append('VTKPDBReaderType' )

#--------------------------------------------------------------
class VTKPDataSetReader(Node, VTKReaderNode):

    bl_idname = 'VTKPDataSetReaderType'
    bl_label  = 'vtkPDataSetReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKPDataSetReader )        
TYPENAMES.append('VTKPDataSetReaderType' )

#--------------------------------------------------------------
class VTKPLYReader(Node, VTKReaderNode):

    bl_idname = 'VTKPLYReaderType'
    bl_label  = 'vtkPLYReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKPLYReader )        
TYPENAMES.append('VTKPLYReaderType' )

#--------------------------------------------------------------
class VTKPNGReader(Node, VTKReaderNode):

    bl_idname = 'VTKPNGReaderType'
    bl_label  = 'vtkPNGReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_ReadSpacingFromFile      = bpy.props.BoolProperty       ( name='ReadSpacingFromFile',      default=False )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_ReadSpacingFromFile','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKPNGReader )        
TYPENAMES.append('VTKPNGReaderType' )

#--------------------------------------------------------------
class VTKPNMReader(Node, VTKReaderNode):

    bl_idname = 'VTKPNMReaderType'
    bl_label  = 'vtkPNMReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_ScalarArrayName          = bpy.props.StringProperty     ( name='ScalarArrayName',          default="ImageFile" )
    m_DataMask                 = bpy.props.IntProperty        ( name='DataMask',                 default=0 )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataVOI                  = bpy.props.IntVectorProperty  ( name='DataVOI',                  default=[0, 0, 0, 0, 0, 0], size=6 )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKPNMReader )        
TYPENAMES.append('VTKPNMReaderType' )

#--------------------------------------------------------------
class VTKPTSReader(Node, VTKReaderNode):

    bl_idname = 'VTKPTSReaderType'
    bl_label  = 'vtkPTSReader'
    
    m_CreateCells              = bpy.props.BoolProperty       ( name='CreateCells',              default=True )
    m_IncludeColorAndLuminance = bpy.props.BoolProperty       ( name='IncludeColorAndLuminance', default=True )
    m_LimitReadToBounds        = bpy.props.BoolProperty       ( name='LimitReadToBounds',        default=False )
    m_LimitToMaxNumberOfPoints = bpy.props.BoolProperty       ( name='LimitToMaxNumberOfPoints', default=False )
    m_OutputDataTypeIsDouble   = bpy.props.BoolProperty       ( name='OutputDataTypeIsDouble',   default=False )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_MaxNumberOfPoints        = bpy.props.IntProperty        ( name='MaxNumberOfPoints',        default=1000000 )
    m_ReadBounds               = bpy.props.FloatVectorProperty( name='ReadBounds',               default=(1e+299, -1e+299, 1e+299, -1e+299, 1e+299, -1e+299), size=6 )
    
    def m_properties( self ):
        return ['m_CreateCells','m_IncludeColorAndLuminance','m_LimitReadToBounds','m_LimitToMaxNumberOfPoints','m_OutputDataTypeIsDouble','m_FileName','m_MaxNumberOfPoints','m_ReadBounds',]
    
CLASSES.append  ( VTKPTSReader )        
TYPENAMES.append('VTKPTSReaderType' )

#--------------------------------------------------------------
class VTKParticleReader(Node, VTKReaderNode):

    bl_idname = 'VTKParticleReaderType'
    bl_label  = 'vtkParticleReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_FileType_items=[ (x,x,x) for x in ['Unknown', 'Text', 'Binary']]
    
    m_HasScalar     = bpy.props.BoolProperty  ( name='HasScalar',     default=1 )
    m_SwapBytes     = bpy.props.BoolProperty  ( name='SwapBytes',     default=0 )
    m_FileName      = bpy.props.StringProperty( name='FileName',      default="" )
    e_DataByteOrder = bpy.props.EnumProperty  ( name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items )
    e_FileType      = bpy.props.EnumProperty  ( name='FileType',      default="Unknown", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_HasScalar','m_SwapBytes','m_FileName','e_DataByteOrder','e_FileType',]
    
CLASSES.append  ( VTKParticleReader )        
TYPENAMES.append('VTKParticleReaderType' )

#--------------------------------------------------------------
class VTKPlot3DMetaReader(Node, VTKReaderNode):

    bl_idname = 'VTKPlot3DMetaReaderType'
    bl_label  = 'vtkPlot3DMetaReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKPlot3DMetaReader )        
TYPENAMES.append('VTKPlot3DMetaReaderType' )

#--------------------------------------------------------------
class VTKProStarReader(Node, VTKReaderNode):

    bl_idname = 'VTKProStarReaderType'
    bl_label  = 'vtkProStarReader'
    
    m_FileName    = bpy.props.StringProperty( name='FileName',    default="" )
    m_ScaleFactor = bpy.props.FloatProperty ( name='ScaleFactor', default=1.0 )
    
    def m_properties( self ):
        return ['m_FileName','m_ScaleFactor',]
    
CLASSES.append  ( VTKProStarReader )        
TYPENAMES.append('VTKProStarReaderType' )

#--------------------------------------------------------------
class VTKRISReader(Node, VTKReaderNode):

    bl_idname = 'VTKRISReaderType'
    bl_label  = 'vtkRISReader'
    
    m_Delimiter  = bpy.props.StringProperty( name='Delimiter',  default=";" )
    m_FileName   = bpy.props.StringProperty( name='FileName',   default="" )
    m_MaxRecords = bpy.props.IntProperty   ( name='MaxRecords', default=0 )
    
    def m_properties( self ):
        return ['m_Delimiter','m_FileName','m_MaxRecords',]
    
CLASSES.append  ( VTKRISReader )        
TYPENAMES.append('VTKRISReaderType' )

#--------------------------------------------------------------
class VTKSLACParticleReader(Node, VTKReaderNode):

    bl_idname = 'VTKSLACParticleReaderType'
    bl_label  = 'vtkSLACParticleReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKSLACParticleReader )        
TYPENAMES.append('VTKSLACParticleReaderType' )

#--------------------------------------------------------------
class VTKSLCReader(Node, VTKReaderNode):

    bl_idname = 'VTKSLCReaderType'
    bl_label  = 'vtkSLCReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKSLCReader )        
TYPENAMES.append('VTKSLCReaderType' )

#--------------------------------------------------------------
class VTKSTLReader(Node, VTKReaderNode):

    bl_idname = 'VTKSTLReaderType'
    bl_label  = 'vtkSTLReader'
    
    m_Merging    = bpy.props.BoolProperty  ( name='Merging',    default=1 )
    m_ScalarTags = bpy.props.BoolProperty  ( name='ScalarTags', default=0 )
    m_FileName   = bpy.props.StringProperty( name='FileName',   default="" )
    
    def m_properties( self ):
        return ['m_Merging','m_ScalarTags','m_FileName',]
    
CLASSES.append  ( VTKSTLReader )        
TYPENAMES.append('VTKSTLReaderType' )

#--------------------------------------------------------------
class VTKScancoCTReader(Node, VTKReaderNode):

    bl_idname = 'VTKScancoCTReaderType'
    bl_label  = 'vtkScancoCTReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=1 )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKScancoCTReader )        
TYPENAMES.append('VTKScancoCTReaderType' )

#--------------------------------------------------------------
class VTKSimplePointsReader(Node, VTKReaderNode):

    bl_idname = 'VTKSimplePointsReaderType'
    bl_label  = 'vtkSimplePointsReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKSimplePointsReader )        
TYPENAMES.append('VTKSimplePointsReaderType' )

#--------------------------------------------------------------
class VTKTIFFReader(Node, VTKReaderNode):

    bl_idname = 'VTKTIFFReaderType'
    bl_label  = 'vtkTIFFReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_FileLowerLeft            = bpy.props.BoolProperty       ( name='FileLowerLeft',            default=0 )
    m_OriginSpecifiedFlag      = bpy.props.BoolProperty       ( name='OriginSpecifiedFlag',      default=False )
    m_SpacingSpecifiedFlag     = bpy.props.BoolProperty       ( name='SpacingSpecifiedFlag',     default=False )
    m_SwapBytes                = bpy.props.BoolProperty       ( name='SwapBytes',                default=0 )
    m_FileName                 = bpy.props.StringProperty     ( name='FileName',                 default="" )
    m_FilePattern              = bpy.props.StringProperty     ( name='FilePattern',              default="%s.%d" )
    m_FilePrefix               = bpy.props.StringProperty     ( name='FilePrefix',               default="" )
    m_FileDimensionality       = bpy.props.IntProperty        ( name='FileDimensionality',       default=2 )
    m_FileNameSliceOffset      = bpy.props.IntProperty        ( name='FileNameSliceOffset',      default=0 )
    m_FileNameSliceSpacing     = bpy.props.IntProperty        ( name='FileNameSliceSpacing',     default=1 )
    m_HeaderSize               = bpy.props.IntProperty        ( name='HeaderSize',               default=0 )
    m_MemoryBufferLength       = bpy.props.IntProperty        ( name='MemoryBufferLength',       default=0 )
    m_NumberOfScalarComponents = bpy.props.IntProperty        ( name='NumberOfScalarComponents', default=1 )
    m_OrientationType          = bpy.props.IntProperty        ( name='OrientationType',          default=4 )
    e_DataByteOrder            = bpy.props.EnumProperty       ( name='DataByteOrder',            default="LittleEndian", items=e_DataByteOrder_items )
    e_DataScalarType           = bpy.props.EnumProperty       ( name='DataScalarType',           default="Short", items=e_DataScalarType_items )
    m_DataOrigin               = bpy.props.FloatVectorProperty( name='DataOrigin',               default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing              = bpy.props.FloatVectorProperty( name='DataSpacing',              default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_FileLowerLeft','m_OriginSpecifiedFlag','m_SpacingSpecifiedFlag','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_OrientationType','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKTIFFReader )        
TYPENAMES.append('VTKTIFFReaderType' )

#--------------------------------------------------------------
class VTKTecplotTableReader(Node, VTKReaderNode):

    bl_idname = 'VTKTecplotTableReaderType'
    bl_label  = 'vtkTecplotTableReader'
    
    m_GeneratePedigreeIds = bpy.props.BoolProperty  ( name='GeneratePedigreeIds', default=False )
    m_OutputPedigreeIds   = bpy.props.BoolProperty  ( name='OutputPedigreeIds',   default=False )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_PedigreeIdArrayName = bpy.props.StringProperty( name='PedigreeIdArrayName', default="id" )
    m_ColumnNamesOnLine   = bpy.props.IntProperty   ( name='ColumnNamesOnLine',   default=1 )
    m_HeaderLines         = bpy.props.IntProperty   ( name='HeaderLines',         default=2 )
    m_MaxRecords          = bpy.props.IntProperty   ( name='MaxRecords',          default=0 )
    m_SkipColumnNames     = bpy.props.IntProperty   ( name='SkipColumnNames',     default=1 )
    
    def m_properties( self ):
        return ['m_GeneratePedigreeIds','m_OutputPedigreeIds','m_FileName','m_PedigreeIdArrayName','m_ColumnNamesOnLine','m_HeaderLines','m_MaxRecords','m_SkipColumnNames',]
    
CLASSES.append  ( VTKTecplotTableReader )        
TYPENAMES.append('VTKTecplotTableReaderType' )

#--------------------------------------------------------------
class VTKTulipReader(Node, VTKReaderNode):

    bl_idname = 'VTKTulipReaderType'
    bl_label  = 'vtkTulipReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKTulipReader )        
TYPENAMES.append('VTKTulipReaderType' )

#--------------------------------------------------------------
class VTKUGFacetReader(Node, VTKReaderNode):

    bl_idname = 'VTKUGFacetReaderType'
    bl_label  = 'vtkUGFacetReader'
    
    m_Merging    = bpy.props.BoolProperty  ( name='Merging',    default=1 )
    m_FileName   = bpy.props.StringProperty( name='FileName',   default="" )
    m_PartNumber = bpy.props.IntProperty   ( name='PartNumber', default=-1 )
    
    def m_properties( self ):
        return ['m_Merging','m_FileName','m_PartNumber',]
    
CLASSES.append  ( VTKUGFacetReader )        
TYPENAMES.append('VTKUGFacetReaderType' )

#--------------------------------------------------------------
class VTKVASPAnimationReader(Node, VTKReaderNode):

    bl_idname = 'VTKVASPAnimationReaderType'
    bl_label  = 'vtkVASPAnimationReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKVASPAnimationReader )        
TYPENAMES.append('VTKVASPAnimationReaderType' )

#--------------------------------------------------------------
class VTKVASPTessellationReader(Node, VTKReaderNode):

    bl_idname = 'VTKVASPTessellationReaderType'
    bl_label  = 'vtkVASPTessellationReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKVASPTessellationReader )        
TYPENAMES.append('VTKVASPTessellationReaderType' )

#--------------------------------------------------------------
class VTKVolume16Reader(Node, VTKReaderNode):

    bl_idname = 'VTKVolume16ReaderType'
    bl_label  = 'vtkVolume16Reader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_SwapBytes      = bpy.props.BoolProperty       ( name='SwapBytes',      default=0 )
    m_FilePattern    = bpy.props.StringProperty     ( name='FilePattern',    default="%s.%d" )
    m_FilePrefix     = bpy.props.StringProperty     ( name='FilePrefix',     default="" )
    m_DataMask       = bpy.props.IntProperty        ( name='DataMask',       default=0 )
    m_HeaderSize     = bpy.props.IntProperty        ( name='HeaderSize',     default=0 )
    e_DataByteOrder  = bpy.props.EnumProperty       ( name='DataByteOrder',  default="LittleEndian", items=e_DataByteOrder_items )
    m_DataDimensions = bpy.props.IntVectorProperty  ( name='DataDimensions', default=[0, 0], size=2 )
    m_ImageRange     = bpy.props.IntVectorProperty  ( name='ImageRange',     default=[1, 1], size=2 )
    m_DataOrigin     = bpy.props.FloatVectorProperty( name='DataOrigin',     default=(0.0, 0.0, 0.0), size=3 )
    m_DataSpacing    = bpy.props.FloatVectorProperty( name='DataSpacing',    default=(1.0, 1.0, 1.0), size=3 )
    
    def m_properties( self ):
        return ['m_SwapBytes','m_FilePattern','m_FilePrefix','m_DataMask','m_HeaderSize','e_DataByteOrder','m_DataDimensions','m_ImageRange','m_DataOrigin','m_DataSpacing',]
    
CLASSES.append  ( VTKVolume16Reader )        
TYPENAMES.append('VTKVolume16ReaderType' )

#--------------------------------------------------------------
class VTKXGMLReader(Node, VTKReaderNode):

    bl_idname = 'VTKXGMLReaderType'
    bl_label  = 'vtkXGMLReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKXGMLReader )        
TYPENAMES.append('VTKXGMLReaderType' )

#--------------------------------------------------------------
class VTKXMLTreeReader(Node, VTKReaderNode):

    bl_idname = 'VTKXMLTreeReaderType'
    bl_label  = 'vtkXMLTreeReader'
    
    m_GenerateEdgePedigreeIds   = bpy.props.BoolProperty  ( name='GenerateEdgePedigreeIds',   default=True )
    m_GenerateVertexPedigreeIds = bpy.props.BoolProperty  ( name='GenerateVertexPedigreeIds', default=True )
    m_MaskArrays                = bpy.props.BoolProperty  ( name='MaskArrays',                default=False )
    m_ReadCharData              = bpy.props.BoolProperty  ( name='ReadCharData',              default=False )
    m_ReadTagName               = bpy.props.BoolProperty  ( name='ReadTagName',               default=True )
    m_EdgePedigreeIdArrayName   = bpy.props.StringProperty( name='EdgePedigreeIdArrayName',   default="edge id" )
    m_FileName                  = bpy.props.StringProperty( name='FileName',                  default="" )
    m_VertexPedigreeIdArrayName = bpy.props.StringProperty( name='VertexPedigreeIdArrayName', default="vertex id" )
    m_XMLString                 = bpy.props.StringProperty( name='XMLString',                 default="" )
    
    def m_properties( self ):
        return ['m_GenerateEdgePedigreeIds','m_GenerateVertexPedigreeIds','m_MaskArrays','m_ReadCharData','m_ReadTagName','m_EdgePedigreeIdArrayName','m_FileName','m_VertexPedigreeIdArrayName','m_XMLString',]
    
CLASSES.append  ( VTKXMLTreeReader )        
TYPENAMES.append('VTKXMLTreeReaderType' )

#--------------------------------------------------------------
class VTKXYZMolReader(Node, VTKReaderNode):

    bl_idname = 'VTKXYZMolReaderType'
    bl_label  = 'vtkXYZMolReader'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    m_TimeStep = bpy.props.IntProperty   ( name='TimeStep', default=0 )
    m_BScale   = bpy.props.FloatProperty ( name='BScale',   default=1.0 )
    m_HBScale  = bpy.props.FloatProperty ( name='HBScale',  default=1.0 )
    
    def m_properties( self ):
        return ['m_FileName','m_TimeStep','m_BScale','m_HBScale',]
    
CLASSES.append  ( VTKXYZMolReader )        
TYPENAMES.append('VTKXYZMolReaderType' )

#--------------------------------------------------------------
class VTKXYZMolReader2(Node, VTKReaderNode):

    bl_idname = 'VTKXYZMolReader2Type'
    bl_label  = 'vtkXYZMolReader2'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKXYZMolReader2 )        
TYPENAMES.append('VTKXYZMolReader2Type' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( 'reader', 'reader', items=menu_items) )