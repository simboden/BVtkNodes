from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKArrayDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKArrayDataWriterType'
    bl_label  = 'vtkArrayDataWriter'
    
    m_Binary              = bpy.props.BoolProperty  ( name='Binary',              default=0 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=False )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    
    def m_properties( self ):
        return ['m_Binary','m_WriteToOutputString','m_FileName',]
    
CLASSES.append  ( VTKArrayDataWriter )        
TYPENAMES.append('VTKArrayDataWriterType' )

#--------------------------------------------------------------
class VTKArrayWriter(Node, VTKReaderNode):

    bl_idname = 'VTKArrayWriterType'
    bl_label  = 'vtkArrayWriter'
    
    m_Binary              = bpy.props.BoolProperty  ( name='Binary',              default=0 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=False )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    
    def m_properties( self ):
        return ['m_Binary','m_WriteToOutputString','m_FileName',]
    
CLASSES.append  ( VTKArrayWriter )        
TYPENAMES.append('VTKArrayWriterType' )

#--------------------------------------------------------------
class VTKBMPWriter(Node, VTKReaderNode):

    bl_idname = 'VTKBMPWriterType'
    bl_label  = 'vtkBMPWriter'
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    
CLASSES.append  ( VTKBMPWriter )        
TYPENAMES.append('VTKBMPWriterType' )

#--------------------------------------------------------------
class VTKBYUWriter(Node, VTKReaderNode):

    bl_idname = 'VTKBYUWriterType'
    bl_label  = 'vtkBYUWriter'
    
    m_WriteDisplacement    = bpy.props.BoolProperty  ( name='WriteDisplacement',    default=1 )
    m_WriteScalar          = bpy.props.BoolProperty  ( name='WriteScalar',          default=1 )
    m_WriteTexture         = bpy.props.BoolProperty  ( name='WriteTexture',         default=1 )
    m_DisplacementFileName = bpy.props.StringProperty( name='DisplacementFileName', default="" )
    m_GeometryFileName     = bpy.props.StringProperty( name='GeometryFileName',     default="" )
    m_ScalarFileName       = bpy.props.StringProperty( name='ScalarFileName',       default="" )
    m_TextureFileName      = bpy.props.StringProperty( name='TextureFileName',      default="" )
    
    def m_properties( self ):
        return ['m_WriteDisplacement','m_WriteScalar','m_WriteTexture','m_DisplacementFileName','m_GeometryFileName','m_ScalarFileName','m_TextureFileName',]
    
CLASSES.append  ( VTKBYUWriter )        
TYPENAMES.append('VTKBYUWriterType' )

#--------------------------------------------------------------
class VTKCompositeDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKCompositeDataWriterType'
    bl_label  = 'vtkCompositeDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKCompositeDataWriter )        
TYPENAMES.append('VTKCompositeDataWriterType' )

#--------------------------------------------------------------
class VTKDICOMWriter(Node, VTKReaderNode):

    bl_idname = 'VTKDICOMWriterType'
    bl_label  = 'vtkDICOMWriter'
    e_FileSliceOrder_items=[ (x,x,x) for x in ['RHR', 'LHR', 'Same', 'Reverse']]
    e_MemoryRowOrder_items=[ (x,x,x) for x in ['FileNative', 'TopDown', 'BottomUp']]
    
    m_Streaming          = bpy.props.BoolProperty  ( name='Streaming',          default=0 )
    m_TimeAsVector       = bpy.props.BoolProperty  ( name='TimeAsVector',       default=0 )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_ImageType          = bpy.props.StringProperty( name='ImageType',          default="DERIVED/SECONDARY/OTHER" )
    m_SeriesDescription  = bpy.props.StringProperty( name='SeriesDescription',  default="" )
    m_TransferSyntaxUID  = bpy.props.StringProperty( name='TransferSyntaxUID',  default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_TimeDimension      = bpy.props.IntProperty   ( name='TimeDimension',      default=0 )
    m_RescaleIntercept   = bpy.props.FloatProperty ( name='RescaleIntercept',   default=0.0 )
    m_RescaleSlope       = bpy.props.FloatProperty ( name='RescaleSlope',       default=1.0 )
    m_TimeSpacing        = bpy.props.FloatProperty ( name='TimeSpacing',        default=1.0 )
    e_FileSliceOrder     = bpy.props.EnumProperty  ( name='FileSliceOrder',     default="RHR", items=e_FileSliceOrder_items )
    e_MemoryRowOrder     = bpy.props.EnumProperty  ( name='MemoryRowOrder',     default="BottomUp", items=e_MemoryRowOrder_items )
    
    def m_properties( self ):
        return ['m_Streaming','m_TimeAsVector','m_FileName','m_FilePattern','m_FilePrefix','m_ImageType','m_SeriesDescription','m_TransferSyntaxUID','m_FileDimensionality','m_TimeDimension','m_RescaleIntercept','m_RescaleSlope','m_TimeSpacing','e_FileSliceOrder','e_MemoryRowOrder',]
    
CLASSES.append  ( VTKDICOMWriter )        
TYPENAMES.append('VTKDICOMWriterType' )

#--------------------------------------------------------------
class VTKDIMACSGraphWriter(Node, VTKReaderNode):

    bl_idname = 'VTKDIMACSGraphWriterType'
    bl_label  = 'vtkDIMACSGraphWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKDIMACSGraphWriter )        
TYPENAMES.append('VTKDIMACSGraphWriterType' )

#--------------------------------------------------------------
class VTKDataObjectWriter(Node, VTKReaderNode):

    bl_idname = 'VTKDataObjectWriterType'
    bl_label  = 'vtkDataObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteToOutputString','m_FieldDataName','m_FileName','m_Header','e_FileType',]
    
CLASSES.append  ( VTKDataObjectWriter )        
TYPENAMES.append('VTKDataObjectWriterType' )

#--------------------------------------------------------------
class VTKDataSetWriter(Node, VTKReaderNode):

    bl_idname = 'VTKDataSetWriterType'
    bl_label  = 'vtkDataSetWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKDataSetWriter )        
TYPENAMES.append('VTKDataSetWriterType' )

#--------------------------------------------------------------
class VTKDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKDataWriterType'
    bl_label  = 'vtkDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKDataWriter )        
TYPENAMES.append('VTKDataWriterType' )

#--------------------------------------------------------------
class VTKDelimitedTextWriter(Node, VTKReaderNode):

    bl_idname = 'VTKDelimitedTextWriterType'
    bl_label  = 'vtkDelimitedTextWriter'
    
    m_UseStringDelimiter  = bpy.props.BoolProperty  ( name='UseStringDelimiter',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=False )
    m_FieldDelimiter      = bpy.props.StringProperty( name='FieldDelimiter',      default="," )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_StringDelimiter     = bpy.props.StringProperty( name='StringDelimiter',     default="" )
    
    def m_properties( self ):
        return ['m_UseStringDelimiter','m_WriteToOutputString','m_FieldDelimiter','m_FileName','m_StringDelimiter',]
    
CLASSES.append  ( VTKDelimitedTextWriter )        
TYPENAMES.append('VTKDelimitedTextWriterType' )

#--------------------------------------------------------------
class VTKExodusIIWriter(Node, VTKReaderNode):

    bl_idname = 'VTKExodusIIWriterType'
    bl_label  = 'vtkExodusIIWriter'
    
    m_IgnoreMetaDataWarning        = bpy.props.BoolProperty  ( name='IgnoreMetaDataWarning',        default=False )
    m_WriteAllTimeSteps            = bpy.props.BoolProperty  ( name='WriteAllTimeSteps',            default=0 )
    m_WriteOutBlockIdArray         = bpy.props.BoolProperty  ( name='WriteOutBlockIdArray',         default=0 )
    m_WriteOutGlobalElementIdArray = bpy.props.BoolProperty  ( name='WriteOutGlobalElementIdArray', default=0 )
    m_WriteOutGlobalNodeIdArray    = bpy.props.BoolProperty  ( name='WriteOutGlobalNodeIdArray',    default=0 )
    m_BlockIdArrayName             = bpy.props.StringProperty( name='BlockIdArrayName',             default="" )
    m_FileName                     = bpy.props.StringProperty( name='FileName',                     default="" )
    m_GhostLevel                   = bpy.props.IntProperty   ( name='GhostLevel',                   default=0 )
    m_StoreDoubles                 = bpy.props.IntProperty   ( name='StoreDoubles',                 default=-1 )
    
    def m_properties( self ):
        return ['m_IgnoreMetaDataWarning','m_WriteAllTimeSteps','m_WriteOutBlockIdArray','m_WriteOutGlobalElementIdArray','m_WriteOutGlobalNodeIdArray','m_BlockIdArrayName','m_FileName','m_GhostLevel','m_StoreDoubles',]
    
CLASSES.append  ( VTKExodusIIWriter )        
TYPENAMES.append('VTKExodusIIWriterType' )

#--------------------------------------------------------------
class VTKFacetWriter(Node, VTKReaderNode):

    bl_idname = 'VTKFacetWriterType'
    bl_label  = 'vtkFacetWriter'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKFacetWriter )        
TYPENAMES.append('VTKFacetWriterType' )

#--------------------------------------------------------------
class VTKGenericDataObjectWriter(Node, VTKReaderNode):

    bl_idname = 'VTKGenericDataObjectWriterType'
    bl_label  = 'vtkGenericDataObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKGenericDataObjectWriter )        
TYPENAMES.append('VTKGenericDataObjectWriterType' )

#--------------------------------------------------------------
class VTKGraphWriter(Node, VTKReaderNode):

    bl_idname = 'VTKGraphWriterType'
    bl_label  = 'vtkGraphWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKGraphWriter )        
TYPENAMES.append('VTKGraphWriterType' )

#--------------------------------------------------------------
class VTKHoudiniPolyDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKHoudiniPolyDataWriterType'
    bl_label  = 'vtkHoudiniPolyDataWriter'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKHoudiniPolyDataWriter )        
TYPENAMES.append('VTKHoudiniPolyDataWriterType' )

#--------------------------------------------------------------
class VTKIVWriter(Node, VTKReaderNode):

    bl_idname = 'VTKIVWriterType'
    bl_label  = 'vtkIVWriter'
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName',]
    
CLASSES.append  ( VTKIVWriter )        
TYPENAMES.append('VTKIVWriterType' )

#--------------------------------------------------------------
class VTKImageWriter(Node, VTKReaderNode):

    bl_idname = 'VTKImageWriterType'
    bl_label  = 'vtkImageWriter'
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    
CLASSES.append  ( VTKImageWriter )        
TYPENAMES.append('VTKImageWriterType' )

#--------------------------------------------------------------
class VTKJPEGWriter(Node, VTKReaderNode):

    bl_idname = 'VTKJPEGWriterType'
    bl_label  = 'vtkJPEGWriter'
    
    m_Progressive        = bpy.props.BoolProperty  ( name='Progressive',        default=1 )
    m_WriteToMemory      = bpy.props.BoolProperty  ( name='WriteToMemory',      default=0 )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_Quality            = bpy.props.IntProperty   ( name='Quality',            default=95 )
    
    def m_properties( self ):
        return ['m_Progressive','m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_Quality',]
    
CLASSES.append  ( VTKJPEGWriter )        
TYPENAMES.append('VTKJPEGWriterType' )

#--------------------------------------------------------------
class VTKJSONImageWriter(Node, VTKReaderNode):

    bl_idname = 'VTKJSONImageWriterType'
    bl_label  = 'vtkJSONImageWriter'
    
    m_ArrayName = bpy.props.StringProperty( name='ArrayName', default="" )
    m_FileName  = bpy.props.StringProperty( name='FileName',  default="" )
    m_Slice     = bpy.props.IntProperty   ( name='Slice',     default=-1 )
    
    def m_properties( self ):
        return ['m_ArrayName','m_FileName','m_Slice',]
    
CLASSES.append  ( VTKJSONImageWriter )        
TYPENAMES.append('VTKJSONImageWriterType' )

#--------------------------------------------------------------
class VTKJavaScriptDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKJavaScriptDataWriterType'
    bl_label  = 'vtkJavaScriptDataWriter'
    
    m_IncludeFieldNames = bpy.props.BoolProperty  ( name='IncludeFieldNames', default=True )
    m_FileName          = bpy.props.StringProperty( name='FileName',          default="" )
    m_VariableName      = bpy.props.StringProperty( name='VariableName',      default="data" )
    
    def m_properties( self ):
        return ['m_IncludeFieldNames','m_FileName','m_VariableName',]
    
CLASSES.append  ( VTKJavaScriptDataWriter )        
TYPENAMES.append('VTKJavaScriptDataWriterType' )

#--------------------------------------------------------------
class VTKMCubesWriter(Node, VTKReaderNode):

    bl_idname = 'VTKMCubesWriterType'
    bl_label  = 'vtkMCubesWriter'
    
    m_FileName       = bpy.props.StringProperty( name='FileName',       default="" )
    m_LimitsFileName = bpy.props.StringProperty( name='LimitsFileName', default="" )
    
    def m_properties( self ):
        return ['m_FileName','m_LimitsFileName',]
    
CLASSES.append  ( VTKMCubesWriter )        
TYPENAMES.append('VTKMCubesWriterType' )

#--------------------------------------------------------------
class VTKMINCImageWriter(Node, VTKReaderNode):

    bl_idname = 'VTKMINCImageWriterType'
    bl_label  = 'vtkMINCImageWriter'
    
    m_StrictValidation   = bpy.props.BoolProperty  ( name='StrictValidation',   default=1 )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_HistoryAddition    = bpy.props.StringProperty( name='HistoryAddition',    default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_RescaleIntercept   = bpy.props.FloatProperty ( name='RescaleIntercept',   default=0.0 )
    m_RescaleSlope       = bpy.props.FloatProperty ( name='RescaleSlope',       default=0.0 )
    
    def m_properties( self ):
        return ['m_StrictValidation','m_FileName','m_FilePattern','m_FilePrefix','m_HistoryAddition','m_FileDimensionality','m_RescaleIntercept','m_RescaleSlope',]
    
CLASSES.append  ( VTKMINCImageWriter )        
TYPENAMES.append('VTKMINCImageWriterType' )

#--------------------------------------------------------------
class VTKMNIObjectWriter(Node, VTKReaderNode):

    bl_idname = 'VTKMNIObjectWriterType'
    bl_label  = 'vtkMNIObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    e_FileType = bpy.props.EnumProperty  ( name='FileType', default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_FileName','e_FileType',]
    
CLASSES.append  ( VTKMNIObjectWriter )        
TYPENAMES.append('VTKMNIObjectWriterType' )

#--------------------------------------------------------------
class VTKMNITransformWriter(Node, VTKReaderNode):

    bl_idname = 'VTKMNITransformWriterType'
    bl_label  = 'vtkMNITransformWriter'
    
    m_Comments = bpy.props.StringProperty( name='Comments', default="" )
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    
    def m_properties( self ):
        return ['m_Comments','m_FileName',]
    
CLASSES.append  ( VTKMNITransformWriter )        
TYPENAMES.append('VTKMNITransformWriterType' )

#--------------------------------------------------------------
class VTKMetaImageWriter(Node, VTKReaderNode):

    bl_idname = 'VTKMetaImageWriterType'
    bl_label  = 'vtkMetaImageWriter'
    
    m_Compression        = bpy.props.BoolProperty  ( name='Compression',        default=True )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_RAWFileName        = bpy.props.StringProperty( name='RAWFileName',        default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    def m_properties( self ):
        return ['m_Compression','m_FileName','m_FilePattern','m_FilePrefix','m_RAWFileName','m_FileDimensionality',]
    
CLASSES.append  ( VTKMetaImageWriter )        
TYPENAMES.append('VTKMetaImageWriterType' )

#--------------------------------------------------------------
class VTKNIFTIImageWriter(Node, VTKReaderNode):

    bl_idname = 'VTKNIFTIImageWriterType'
    bl_label  = 'vtkNIFTIImageWriter'
    
    m_PlanarRGB          = bpy.props.BoolProperty  ( name='PlanarRGB',          default=False )
    m_Description        = bpy.props.StringProperty( name='Description',        default="VTK8.0.1" )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=3 )
    m_NIFTIVersion       = bpy.props.IntProperty   ( name='NIFTIVersion',       default=0 )
    m_TimeDimension      = bpy.props.IntProperty   ( name='TimeDimension',      default=0 )
    m_QFac               = bpy.props.FloatProperty ( name='QFac',               default=0.0 )
    m_RescaleIntercept   = bpy.props.FloatProperty ( name='RescaleIntercept',   default=0.0 )
    m_RescaleSlope       = bpy.props.FloatProperty ( name='RescaleSlope',       default=0.0 )
    m_TimeSpacing        = bpy.props.FloatProperty ( name='TimeSpacing',        default=1.0 )
    
    def m_properties( self ):
        return ['m_PlanarRGB','m_Description','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_NIFTIVersion','m_TimeDimension','m_QFac','m_RescaleIntercept','m_RescaleSlope','m_TimeSpacing',]
    
CLASSES.append  ( VTKNIFTIImageWriter )        
TYPENAMES.append('VTKNIFTIImageWriterType' )

#--------------------------------------------------------------
class VTKNIFTIWriter(Node, VTKReaderNode):

    bl_idname = 'VTKNIFTIWriterType'
    bl_label  = 'vtkNIFTIWriter'
    
    m_PlanarRGB          = bpy.props.BoolProperty  ( name='PlanarRGB',          default=False )
    m_Description        = bpy.props.StringProperty( name='Description',        default="" )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=3 )
    m_NIFTIVersion       = bpy.props.IntProperty   ( name='NIFTIVersion',       default=0 )
    m_TimeDimension      = bpy.props.IntProperty   ( name='TimeDimension',      default=0 )
    m_QFac               = bpy.props.FloatProperty ( name='QFac',               default=0.0 )
    m_RescaleIntercept   = bpy.props.FloatProperty ( name='RescaleIntercept',   default=0.0 )
    m_RescaleSlope       = bpy.props.FloatProperty ( name='RescaleSlope',       default=0.0 )
    m_TimeSpacing        = bpy.props.FloatProperty ( name='TimeSpacing',        default=1.0 )
    
    def m_properties( self ):
        return ['m_PlanarRGB','m_Description','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_NIFTIVersion','m_TimeDimension','m_QFac','m_RescaleIntercept','m_RescaleSlope','m_TimeSpacing',]
    
CLASSES.append  ( VTKNIFTIWriter )        
TYPENAMES.append('VTKNIFTIWriterType' )

#--------------------------------------------------------------
class VTKNewickTreeWriter(Node, VTKReaderNode):

    bl_idname = 'VTKNewickTreeWriterType'
    bl_label  = 'vtkNewickTreeWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_EdgeWeightArrayName = bpy.props.StringProperty( name='EdgeWeightArrayName', default="weight" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NodeNameArrayName   = bpy.props.StringProperty( name='NodeNameArrayName',   default="node name" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_EdgeWeightArrayName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NodeNameArrayName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKNewickTreeWriter )        
TYPENAMES.append('VTKNewickTreeWriterType' )

#--------------------------------------------------------------
class VTKOggTheoraWriter(Node, VTKReaderNode):

    bl_idname = 'VTKOggTheoraWriterType'
    bl_label  = 'vtkOggTheoraWriter'
    
    m_Subsampling = bpy.props.BoolProperty  ( name='Subsampling', default=0 )
    m_FileName    = bpy.props.StringProperty( name='FileName',    default="" )
    m_Quality     = bpy.props.IntProperty   ( name='Quality',     default=2 )
    m_Rate        = bpy.props.IntProperty   ( name='Rate',        default=25 )
    
    def m_properties( self ):
        return ['m_Subsampling','m_FileName','m_Quality','m_Rate',]
    
CLASSES.append  ( VTKOggTheoraWriter )        
TYPENAMES.append('VTKOggTheoraWriterType' )

#--------------------------------------------------------------
class VTKPDataSetWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPDataSetWriterType'
    bl_label  = 'vtkPDataSetWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_UseRelativeFileNames = bpy.props.BoolProperty  ( name='UseRelativeFileNames', default=1 )
    m_WriteArrayMetaData   = bpy.props.BoolProperty  ( name='WriteArrayMetaData',   default=True )
    m_WriteToOutputString  = bpy.props.BoolProperty  ( name='WriteToOutputString',  default=0 )
    m_EdgeFlagsName        = bpy.props.StringProperty( name='EdgeFlagsName',        default="" )
    m_FieldDataName        = bpy.props.StringProperty( name='FieldDataName',        default="FieldData" )
    m_FileName             = bpy.props.StringProperty( name='FileName',             default="" )
    m_FilePattern          = bpy.props.StringProperty( name='FilePattern',          default="%s.%d.vtk" )
    m_GlobalIdsName        = bpy.props.StringProperty( name='GlobalIdsName',        default="" )
    m_Header               = bpy.props.StringProperty( name='Header',               default="vtk output" )
    m_LookupTableName      = bpy.props.StringProperty( name='LookupTableName',      default="lookup_table" )
    m_NormalsName          = bpy.props.StringProperty( name='NormalsName',          default="" )
    m_PedigreeIdsName      = bpy.props.StringProperty( name='PedigreeIdsName',      default="" )
    m_ScalarsName          = bpy.props.StringProperty( name='ScalarsName',          default="" )
    m_TCoordsName          = bpy.props.StringProperty( name='TCoordsName',          default="" )
    m_TensorsName          = bpy.props.StringProperty( name='TensorsName',          default="" )
    m_VectorsName          = bpy.props.StringProperty( name='VectorsName',          default="" )
    m_EndPiece             = bpy.props.IntProperty   ( name='EndPiece',             default=0 )
    m_GhostLevel           = bpy.props.IntProperty   ( name='GhostLevel',           default=0 )
    m_NumberOfPieces       = bpy.props.IntProperty   ( name='NumberOfPieces',       default=1 )
    m_StartPiece           = bpy.props.IntProperty   ( name='StartPiece',           default=0 )
    e_FileType             = bpy.props.EnumProperty  ( name='FileType',             default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_UseRelativeFileNames','m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_FilePattern','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_StartPiece','e_FileType',]
    
CLASSES.append  ( VTKPDataSetWriter )        
TYPENAMES.append('VTKPDataSetWriterType' )

#--------------------------------------------------------------
class VTKPImageWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPImageWriterType'
    bl_label  = 'vtkPImageWriter'
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    m_MemoryLimit        = bpy.props.IntProperty   ( name='MemoryLimit',        default=1048576 )
    
    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_MemoryLimit',]
    
CLASSES.append  ( VTKPImageWriter )        
TYPENAMES.append('VTKPImageWriterType' )

#--------------------------------------------------------------
class VTKPLYWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPLYWriterType'
    bl_label  = 'vtkPLYWriter'
    e_ColorMode_items=[ (x,x,x) for x in ['Default', 'UniformCellColor', 'UniformPointColor', 'UniformColor', 'Off']]
    e_DataByteOrder_items=[ (x,x,x) for x in ['LittleEndian', 'BigEndian']]
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    e_TextureCoordinatesName_items=[ (x,x,x) for x in ['UV', 'TextureUV']]
    
    m_ArrayName              = bpy.props.StringProperty   ( name='ArrayName',              default="" )
    m_FileName               = bpy.props.StringProperty   ( name='FileName',               default="" )
    m_Component              = bpy.props.IntProperty      ( name='Component',              default=0 )
    e_ColorMode              = bpy.props.EnumProperty     ( name='ColorMode',              default="Default", items=e_ColorMode_items )
    e_DataByteOrder          = bpy.props.EnumProperty     ( name='DataByteOrder',          default="LittleEndian", items=e_DataByteOrder_items )
    e_FileType               = bpy.props.EnumProperty     ( name='FileType',               default="Binary", items=e_FileType_items )
    e_TextureCoordinatesName = bpy.props.EnumProperty     ( name='TextureCoordinatesName', default="UV", items=e_TextureCoordinatesName_items )
    m_Color                  = bpy.props.IntVectorProperty( name='Color',                  default=[255, 255, 255], size=3 )
    
    def m_properties( self ):
        return ['m_ArrayName','m_FileName','m_Component','e_ColorMode','e_DataByteOrder','e_FileType','e_TextureCoordinatesName','m_Color',]
    
CLASSES.append  ( VTKPLYWriter )        
TYPENAMES.append('VTKPLYWriterType' )

#--------------------------------------------------------------
class VTKPNGWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPNGWriterType'
    bl_label  = 'vtkPNGWriter'
    
    m_WriteToMemory      = bpy.props.BoolProperty  ( name='WriteToMemory',      default=0 )
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_CompressionLevel   = bpy.props.IntProperty   ( name='CompressionLevel',   default=5 )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    def m_properties( self ):
        return ['m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_CompressionLevel','m_FileDimensionality',]
    
CLASSES.append  ( VTKPNGWriter )        
TYPENAMES.append('VTKPNGWriterType' )

#--------------------------------------------------------------
class VTKPNMWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPNMWriterType'
    bl_label  = 'vtkPNMWriter'
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    
CLASSES.append  ( VTKPNMWriter )        
TYPENAMES.append('VTKPNMWriterType' )

#--------------------------------------------------------------
class VTKPhyloXMLTreeWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPhyloXMLTreeWriterType'
    bl_label  = 'vtkPhyloXMLTreeWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeWeightArrayName = bpy.props.StringProperty( name='EdgeWeightArrayName', default="weight" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_NodeNameArrayName   = bpy.props.StringProperty( name='NodeNameArrayName',   default="node name" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_EdgeWeightArrayName','m_FileName','m_NodeNameArrayName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKPhyloXMLTreeWriter )        
TYPENAMES.append('VTKPhyloXMLTreeWriterType' )

#--------------------------------------------------------------
class VTKPolyDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPolyDataWriterType'
    bl_label  = 'vtkPolyDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKPolyDataWriter )        
TYPENAMES.append('VTKPolyDataWriterType' )

#--------------------------------------------------------------
class VTKPostScriptWriter(Node, VTKReaderNode):

    bl_idname = 'VTKPostScriptWriterType'
    bl_label  = 'vtkPostScriptWriter'
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    
    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    
CLASSES.append  ( VTKPostScriptWriter )        
TYPENAMES.append('VTKPostScriptWriterType' )

#--------------------------------------------------------------
class VTKRectilinearGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKRectilinearGridWriterType'
    bl_label  = 'vtkRectilinearGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteExtent         = bpy.props.BoolProperty  ( name='WriteExtent',         default=False )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKRectilinearGridWriter )        
TYPENAMES.append('VTKRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKSTLWriter(Node, VTKReaderNode):

    bl_idname = 'VTKSTLWriterType'
    bl_label  = 'vtkSTLWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_FileName = bpy.props.StringProperty( name='FileName', default="" )
    m_Header   = bpy.props.StringProperty( name='Header',   default="Visualization Toolkit generated SLA File                                        " )
    e_FileType = bpy.props.EnumProperty  ( name='FileType', default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_FileName','m_Header','e_FileType',]
    
CLASSES.append  ( VTKSTLWriter )        
TYPENAMES.append('VTKSTLWriterType' )

#--------------------------------------------------------------
class VTKSimplePointsWriter(Node, VTKReaderNode):

    bl_idname = 'VTKSimplePointsWriterType'
    bl_label  = 'vtkSimplePointsWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    m_DecimalPrecision    = bpy.props.IntProperty   ( name='DecimalPrecision',    default=6 )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_DecimalPrecision','e_FileType',]
    
CLASSES.append  ( VTKSimplePointsWriter )        
TYPENAMES.append('VTKSimplePointsWriterType' )

#--------------------------------------------------------------
class VTKStructuredGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKStructuredGridWriterType'
    bl_label  = 'vtkStructuredGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteExtent         = bpy.props.BoolProperty  ( name='WriteExtent',         default=False )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKStructuredGridWriter )        
TYPENAMES.append('VTKStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKStructuredPointsWriter(Node, VTKReaderNode):

    bl_idname = 'VTKStructuredPointsWriterType'
    bl_label  = 'vtkStructuredPointsWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteExtent         = bpy.props.BoolProperty  ( name='WriteExtent',         default=False )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKStructuredPointsWriter )        
TYPENAMES.append('VTKStructuredPointsWriterType' )

#--------------------------------------------------------------
class VTKTIFFWriter(Node, VTKReaderNode):

    bl_idname = 'VTKTIFFWriterType'
    bl_label  = 'vtkTIFFWriter'
    e_Compression_items=[ (x,x,x) for x in ['NoCompression', 'PackBits', 'JPEG', 'Deflate', 'LZW']]
    
    m_FileName           = bpy.props.StringProperty( name='FileName',           default="" )
    m_FilePattern        = bpy.props.StringProperty( name='FilePattern',        default="%s.%d" )
    m_FilePrefix         = bpy.props.StringProperty( name='FilePrefix',         default="" )
    m_FileDimensionality = bpy.props.IntProperty   ( name='FileDimensionality', default=2 )
    e_Compression        = bpy.props.EnumProperty  ( name='Compression',        default="PackBits", items=e_Compression_items )
    
    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','e_Compression',]
    
CLASSES.append  ( VTKTIFFWriter )        
TYPENAMES.append('VTKTIFFWriterType' )

#--------------------------------------------------------------
class VTKTableWriter(Node, VTKReaderNode):

    bl_idname = 'VTKTableWriterType'
    bl_label  = 'vtkTableWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKTableWriter )        
TYPENAMES.append('VTKTableWriterType' )

#--------------------------------------------------------------
class VTKTreeWriter(Node, VTKReaderNode):

    bl_idname = 'VTKTreeWriterType'
    bl_label  = 'vtkTreeWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKTreeWriter )        
TYPENAMES.append('VTKTreeWriterType' )

#--------------------------------------------------------------
class VTKUnstructuredGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKUnstructuredGridWriterType'
    bl_label  = 'vtkUnstructuredGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData  = bpy.props.BoolProperty  ( name='WriteArrayMetaData',  default=True )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_EdgeFlagsName       = bpy.props.StringProperty( name='EdgeFlagsName',       default="" )
    m_FieldDataName       = bpy.props.StringProperty( name='FieldDataName',       default="FieldData" )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_GlobalIdsName       = bpy.props.StringProperty( name='GlobalIdsName',       default="" )
    m_Header              = bpy.props.StringProperty( name='Header',              default="vtk output" )
    m_LookupTableName     = bpy.props.StringProperty( name='LookupTableName',     default="lookup_table" )
    m_NormalsName         = bpy.props.StringProperty( name='NormalsName',         default="" )
    m_PedigreeIdsName     = bpy.props.StringProperty( name='PedigreeIdsName',     default="" )
    m_ScalarsName         = bpy.props.StringProperty( name='ScalarsName',         default="" )
    m_TCoordsName         = bpy.props.StringProperty( name='TCoordsName',         default="" )
    m_TensorsName         = bpy.props.StringProperty( name='TensorsName',         default="" )
    m_VectorsName         = bpy.props.StringProperty( name='VectorsName',         default="" )
    e_FileType            = bpy.props.EnumProperty  ( name='FileType',            default="ASCII", items=e_FileType_items )
    
    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','e_FileType',]
    
CLASSES.append  ( VTKUnstructuredGridWriter )        
TYPENAMES.append('VTKUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLDataSetWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLDataSetWriterType'
    bl_label  = 'vtkXMLDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLDataSetWriter )        
TYPENAMES.append('VTKXMLDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalBoxDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLHierarchicalBoxDataWriterType'
    bl_label  = 'vtkXMLHierarchicalBoxDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile       = bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLHierarchicalBoxDataWriter )        
TYPENAMES.append('VTKXMLHierarchicalBoxDataWriterType' )

#--------------------------------------------------------------
class VTKXMLHyperOctreeWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLHyperOctreeWriterType'
    bl_label  = 'vtkXMLHyperOctreeWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLHyperOctreeWriter )        
TYPENAMES.append('VTKXMLHyperOctreeWriterType' )

#--------------------------------------------------------------
class VTKXMLImageDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLImageDataWriterType'
    bl_label  = 'vtkXMLImageDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty     ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty     ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty   ( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty      ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty      ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty      ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty      ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece          = bpy.props.IntProperty      ( name='WritePiece',          default=-1 )
    e_ByteOrder           = bpy.props.EnumProperty     ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty     ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty     ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty     ( name='IdType',              default="Int64", items=e_IdType_items )
    m_WriteExtent         = bpy.props.IntVectorProperty( name='WriteExtent',         default=[0, -1, 0, -1, 0, -1], size=6 )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    
CLASSES.append  ( VTKXMLImageDataWriter )        
TYPENAMES.append('VTKXMLImageDataWriterType' )

#--------------------------------------------------------------
class VTKXMLMultiBlockDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLMultiBlockDataWriterType'
    bl_label  = 'vtkXMLMultiBlockDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile       = bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLMultiBlockDataWriter )        
TYPENAMES.append('VTKXMLMultiBlockDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPDataSetWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPDataSetWriterType'
    bl_label  = 'vtkXMLPDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_UseSubdirectory     = bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile    = bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece            = bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPDataSetWriter )        
TYPENAMES.append('VTKXMLPDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLPHierarchicalBoxDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPHierarchicalBoxDataWriterType'
    bl_label  = 'vtkXMLPHierarchicalBoxDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile       = bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPHierarchicalBoxDataWriter )        
TYPENAMES.append('VTKXMLPHierarchicalBoxDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPImageDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPImageDataWriterType'
    bl_label  = 'vtkXMLPImageDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_UseSubdirectory     = bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile    = bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece            = bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPImageDataWriter )        
TYPENAMES.append('VTKXMLPImageDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPMultiBlockDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPMultiBlockDataWriterType'
    bl_label  = 'vtkXMLPMultiBlockDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    m_WriteMetaFile       = bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPMultiBlockDataWriter )        
TYPENAMES.append('VTKXMLPMultiBlockDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPPolyDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPPolyDataWriterType'
    bl_label  = 'vtkXMLPPolyDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_UseSubdirectory     = bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile    = bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece            = bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPPolyDataWriter )        
TYPENAMES.append('VTKXMLPPolyDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPRectilinearGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPRectilinearGridWriterType'
    bl_label  = 'vtkXMLPRectilinearGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_UseSubdirectory     = bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile    = bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece            = bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPRectilinearGridWriter )        
TYPENAMES.append('VTKXMLPRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPStructuredGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPStructuredGridWriterType'
    bl_label  = 'vtkXMLPStructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_UseSubdirectory     = bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile    = bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece            = bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPStructuredGridWriter )        
TYPENAMES.append('VTKXMLPStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPUniformGridAMRWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPUniformGridAMRWriterType'
    bl_label  = 'vtkXMLPUniformGridAMRWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile       = bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPUniformGridAMRWriter )        
TYPENAMES.append('VTKXMLPUniformGridAMRWriterType' )

#--------------------------------------------------------------
class VTKXMLPUnstructuredGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPUnstructuredGridWriterType'
    bl_label  = 'vtkXMLPUnstructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_UseSubdirectory     = bpy.props.BoolProperty  ( name='UseSubdirectory',     default=False )
    m_WriteSummaryFile    = bpy.props.BoolProperty  ( name='WriteSummaryFile',    default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_EndPiece            = bpy.props.IntProperty   ( name='EndPiece',            default=0 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_StartPiece          = bpy.props.IntProperty   ( name='StartPiece',          default=0 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteToOutputString','m_FileName','m_BlockSize','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPUnstructuredGridWriter )        
TYPENAMES.append('VTKXMLPUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPolyDataWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLPolyDataWriterType'
    bl_label  = 'vtkXMLPolyDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece          = bpy.props.IntProperty   ( name='WritePiece',          default=-1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLPolyDataWriter )        
TYPENAMES.append('VTKXMLPolyDataWriterType' )

#--------------------------------------------------------------
class VTKXMLRectilinearGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLRectilinearGridWriterType'
    bl_label  = 'vtkXMLRectilinearGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty     ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty     ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty   ( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty      ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty      ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty      ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty      ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece          = bpy.props.IntProperty      ( name='WritePiece',          default=-1 )
    e_ByteOrder           = bpy.props.EnumProperty     ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty     ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty     ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty     ( name='IdType',              default="Int64", items=e_IdType_items )
    m_WriteExtent         = bpy.props.IntVectorProperty( name='WriteExtent',         default=[0, -1, 0, -1, 0, -1], size=6 )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    
CLASSES.append  ( VTKXMLRectilinearGridWriter )        
TYPENAMES.append('VTKXMLRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKXMLStructuredGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLStructuredGridWriterType'
    bl_label  = 'vtkXMLStructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty     ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty     ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty   ( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty      ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty      ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty      ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty      ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece          = bpy.props.IntProperty      ( name='WritePiece',          default=-1 )
    e_ByteOrder           = bpy.props.EnumProperty     ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty     ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty     ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty     ( name='IdType',              default="Int64", items=e_IdType_items )
    m_WriteExtent         = bpy.props.IntVectorProperty( name='WriteExtent',         default=[0, -1, 0, -1, 0, -1], size=6 )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    
CLASSES.append  ( VTKXMLStructuredGridWriter )        
TYPENAMES.append('VTKXMLStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLUniformGridAMRWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLUniformGridAMRWriterType'
    bl_label  = 'vtkXMLUniformGridAMRWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WriteMetaFile       = bpy.props.IntProperty   ( name='WriteMetaFile',       default=1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLUniformGridAMRWriter )        
TYPENAMES.append('VTKXMLUniformGridAMRWriterType' )

#--------------------------------------------------------------
class VTKXMLUnstructuredGridWriter(Node, VTKReaderNode):

    bl_idname = 'VTKXMLUnstructuredGridWriterType'
    bl_label  = 'vtkXMLUnstructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData  = bpy.props.BoolProperty  ( name='EncodeAppendedData',  default=1 )
    m_WriteToOutputString = bpy.props.BoolProperty  ( name='WriteToOutputString', default=0 )
    m_FileName            = bpy.props.StringProperty( name='FileName',            default="" )
    m_BlockSize           = bpy.props.IntProperty   ( name='BlockSize',           default=32768 )
    m_GhostLevel          = bpy.props.IntProperty   ( name='GhostLevel',          default=0 )
    m_NumberOfPieces      = bpy.props.IntProperty   ( name='NumberOfPieces',      default=1 )
    m_NumberOfTimeSteps   = bpy.props.IntProperty   ( name='NumberOfTimeSteps',   default=1 )
    m_WritePiece          = bpy.props.IntProperty   ( name='WritePiece',          default=-1 )
    e_ByteOrder           = bpy.props.EnumProperty  ( name='ByteOrder',           default="LittleEndian", items=e_ByteOrder_items )
    e_DataMode            = bpy.props.EnumProperty  ( name='DataMode',            default="Appended", items=e_DataMode_items )
    e_HeaderType          = bpy.props.EnumProperty  ( name='HeaderType',          default="UInt32", items=e_HeaderType_items )
    e_IdType              = bpy.props.EnumProperty  ( name='IdType',              default="Int64", items=e_IdType_items )
    
    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteToOutputString','m_FileName','m_BlockSize','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    
CLASSES.append  ( VTKXMLUnstructuredGridWriter )        
TYPENAMES.append('VTKXMLUnstructuredGridWriterType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory( 'writer', 'writer', items=menu_items) )