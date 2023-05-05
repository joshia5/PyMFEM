# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _datacollection
else:
    import _datacollection

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _datacollection.SWIG_PyInstanceMethod_New
_swig_new_static_method = _datacollection.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

MFEM_VERSION = _datacollection.MFEM_VERSION
MFEM_VERSION_STRING = _datacollection.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _datacollection.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _datacollection.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _datacollection.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _datacollection.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _datacollection.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _datacollection.MFEM_VERSION_PATCH
import mfem._par.globals
import mfem._par.mesh
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.element
import mfem._par.densemat
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.symmat
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.std_vectors
import mfem._par.pgridfunc
import mfem._par.pfespace
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class DataCollection(object):
    r"""Proxy of C++ mfem::DataCollection class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SERIAL_FORMAT = _datacollection.DataCollection_SERIAL_FORMAT
    
    PARALLEL_FORMAT = _datacollection.DataCollection_PARALLEL_FORMAT
    

    def __init__(self, collection_name, mesh_=None):
        r"""__init__(DataCollection self, std::string const & collection_name, Mesh mesh_=None) -> DataCollection"""
        _datacollection.DataCollection_swiginit(self, _datacollection.new_DataCollection(collection_name, mesh_))

    def RegisterField(self, field_name, gf):
        r"""RegisterField(DataCollection self, std::string const & field_name, GridFunction gf)"""
        return _datacollection.DataCollection_RegisterField(self, field_name, gf)
    RegisterField = _swig_new_instance_method(_datacollection.DataCollection_RegisterField)

    def DeregisterField(self, field_name):
        r"""DeregisterField(DataCollection self, std::string const & field_name)"""
        return _datacollection.DataCollection_DeregisterField(self, field_name)
    DeregisterField = _swig_new_instance_method(_datacollection.DataCollection_DeregisterField)

    def RegisterQField(self, q_field_name, qf):
        r"""RegisterQField(DataCollection self, std::string const & q_field_name, mfem::QuadratureFunction * qf)"""
        return _datacollection.DataCollection_RegisterQField(self, q_field_name, qf)
    RegisterQField = _swig_new_instance_method(_datacollection.DataCollection_RegisterQField)

    def DeregisterQField(self, field_name):
        r"""DeregisterQField(DataCollection self, std::string const & field_name)"""
        return _datacollection.DataCollection_DeregisterQField(self, field_name)
    DeregisterQField = _swig_new_instance_method(_datacollection.DataCollection_DeregisterQField)

    def HasField(self, field_name):
        r"""HasField(DataCollection self, std::string const & field_name) -> bool"""
        return _datacollection.DataCollection_HasField(self, field_name)
    HasField = _swig_new_instance_method(_datacollection.DataCollection_HasField)

    def GetField(self, field_name):
        r"""GetField(DataCollection self, std::string const & field_name) -> GridFunction"""
        return _datacollection.DataCollection_GetField(self, field_name)
    GetField = _swig_new_instance_method(_datacollection.DataCollection_GetField)

    def GetComm(self):
        r"""GetComm(DataCollection self) -> MPI_Comm"""
        return _datacollection.DataCollection_GetComm(self)
    GetComm = _swig_new_instance_method(_datacollection.DataCollection_GetComm)

    def GetParField(self, field_name):
        r"""GetParField(DataCollection self, std::string const & field_name) -> ParGridFunction"""
        return _datacollection.DataCollection_GetParField(self, field_name)
    GetParField = _swig_new_instance_method(_datacollection.DataCollection_GetParField)

    def HasQField(self, q_field_name):
        r"""HasQField(DataCollection self, std::string const & q_field_name) -> bool"""
        return _datacollection.DataCollection_HasQField(self, q_field_name)
    HasQField = _swig_new_instance_method(_datacollection.DataCollection_HasQField)

    def GetQField(self, q_field_name):
        r"""GetQField(DataCollection self, std::string const & q_field_name) -> mfem::QuadratureFunction *"""
        return _datacollection.DataCollection_GetQField(self, q_field_name)
    GetQField = _swig_new_instance_method(_datacollection.DataCollection_GetQField)

    def GetFieldMap(self):
        r"""GetFieldMap(DataCollection self) -> mfem::DataCollection::FieldMapType const &"""
        return _datacollection.DataCollection_GetFieldMap(self)
    GetFieldMap = _swig_new_instance_method(_datacollection.DataCollection_GetFieldMap)

    def GetQFieldMap(self):
        r"""GetQFieldMap(DataCollection self) -> mfem::DataCollection::QFieldMapType const &"""
        return _datacollection.DataCollection_GetQFieldMap(self)
    GetQFieldMap = _swig_new_instance_method(_datacollection.DataCollection_GetQFieldMap)

    def GetMesh(self):
        r"""GetMesh(DataCollection self) -> Mesh"""
        return _datacollection.DataCollection_GetMesh(self)
    GetMesh = _swig_new_instance_method(_datacollection.DataCollection_GetMesh)

    def SetMesh(self, *args):
        r"""
        SetMesh(DataCollection self, Mesh new_mesh)
        SetMesh(DataCollection self, MPI_Comm comm, Mesh new_mesh)
        """
        return _datacollection.DataCollection_SetMesh(self, *args)
    SetMesh = _swig_new_instance_method(_datacollection.DataCollection_SetMesh)

    def SetCycle(self, c):
        r"""SetCycle(DataCollection self, int c)"""
        return _datacollection.DataCollection_SetCycle(self, c)
    SetCycle = _swig_new_instance_method(_datacollection.DataCollection_SetCycle)

    def SetTime(self, t):
        r"""SetTime(DataCollection self, double t)"""
        return _datacollection.DataCollection_SetTime(self, t)
    SetTime = _swig_new_instance_method(_datacollection.DataCollection_SetTime)

    def SetTimeStep(self, ts):
        r"""SetTimeStep(DataCollection self, double ts)"""
        return _datacollection.DataCollection_SetTimeStep(self, ts)
    SetTimeStep = _swig_new_instance_method(_datacollection.DataCollection_SetTimeStep)

    def GetCycle(self):
        r"""GetCycle(DataCollection self) -> int"""
        return _datacollection.DataCollection_GetCycle(self)
    GetCycle = _swig_new_instance_method(_datacollection.DataCollection_GetCycle)

    def GetTime(self):
        r"""GetTime(DataCollection self) -> double"""
        return _datacollection.DataCollection_GetTime(self)
    GetTime = _swig_new_instance_method(_datacollection.DataCollection_GetTime)

    def GetTimeStep(self):
        r"""GetTimeStep(DataCollection self) -> double"""
        return _datacollection.DataCollection_GetTimeStep(self)
    GetTimeStep = _swig_new_instance_method(_datacollection.DataCollection_GetTimeStep)

    def GetCollectionName(self):
        r"""GetCollectionName(DataCollection self) -> std::string const &"""
        return _datacollection.DataCollection_GetCollectionName(self)
    GetCollectionName = _swig_new_instance_method(_datacollection.DataCollection_GetCollectionName)

    def SetOwnData(self, o):
        r"""SetOwnData(DataCollection self, bool o)"""
        return _datacollection.DataCollection_SetOwnData(self, o)
    SetOwnData = _swig_new_instance_method(_datacollection.DataCollection_SetOwnData)

    def SetPrecision(self, prec):
        r"""SetPrecision(DataCollection self, int prec)"""
        return _datacollection.DataCollection_SetPrecision(self, prec)
    SetPrecision = _swig_new_instance_method(_datacollection.DataCollection_SetPrecision)

    def SetPadDigits(self, digits):
        r"""SetPadDigits(DataCollection self, int digits)"""
        return _datacollection.DataCollection_SetPadDigits(self, digits)
    SetPadDigits = _swig_new_instance_method(_datacollection.DataCollection_SetPadDigits)

    def SetPadDigitsCycle(self, digits):
        r"""SetPadDigitsCycle(DataCollection self, int digits)"""
        return _datacollection.DataCollection_SetPadDigitsCycle(self, digits)
    SetPadDigitsCycle = _swig_new_instance_method(_datacollection.DataCollection_SetPadDigitsCycle)

    def SetPadDigitsRank(self, digits):
        r"""SetPadDigitsRank(DataCollection self, int digits)"""
        return _datacollection.DataCollection_SetPadDigitsRank(self, digits)
    SetPadDigitsRank = _swig_new_instance_method(_datacollection.DataCollection_SetPadDigitsRank)

    def SetFormat(self, fmt):
        r"""SetFormat(DataCollection self, int fmt)"""
        return _datacollection.DataCollection_SetFormat(self, fmt)
    SetFormat = _swig_new_instance_method(_datacollection.DataCollection_SetFormat)

    def SetCompression(self, comp):
        r"""SetCompression(DataCollection self, bool comp)"""
        return _datacollection.DataCollection_SetCompression(self, comp)
    SetCompression = _swig_new_instance_method(_datacollection.DataCollection_SetCompression)

    def SetPrefixPath(self, prefix):
        r"""SetPrefixPath(DataCollection self, std::string const & prefix)"""
        return _datacollection.DataCollection_SetPrefixPath(self, prefix)
    SetPrefixPath = _swig_new_instance_method(_datacollection.DataCollection_SetPrefixPath)

    def GetPrefixPath(self):
        r"""GetPrefixPath(DataCollection self) -> std::string const &"""
        return _datacollection.DataCollection_GetPrefixPath(self)
    GetPrefixPath = _swig_new_instance_method(_datacollection.DataCollection_GetPrefixPath)

    def Save(self):
        r"""Save(DataCollection self)"""
        return _datacollection.DataCollection_Save(self)
    Save = _swig_new_instance_method(_datacollection.DataCollection_Save)

    def SaveMesh(self):
        r"""SaveMesh(DataCollection self)"""
        return _datacollection.DataCollection_SaveMesh(self)
    SaveMesh = _swig_new_instance_method(_datacollection.DataCollection_SaveMesh)

    def SaveField(self, field_name):
        r"""SaveField(DataCollection self, std::string const & field_name)"""
        return _datacollection.DataCollection_SaveField(self, field_name)
    SaveField = _swig_new_instance_method(_datacollection.DataCollection_SaveField)

    def SaveQField(self, q_field_name):
        r"""SaveQField(DataCollection self, std::string const & q_field_name)"""
        return _datacollection.DataCollection_SaveQField(self, q_field_name)
    SaveQField = _swig_new_instance_method(_datacollection.DataCollection_SaveQField)

    def Load(self, cycle_=0):
        r"""Load(DataCollection self, int cycle_=0)"""
        return _datacollection.DataCollection_Load(self, cycle_)
    Load = _swig_new_instance_method(_datacollection.DataCollection_Load)
    __swig_destroy__ = _datacollection.delete_DataCollection
    NO_ERROR = _datacollection.DataCollection_NO_ERROR
    
    No_Error = _datacollection.DataCollection_No_Error
    
    READ_ERROR = _datacollection.DataCollection_READ_ERROR
    
    WRITE_ERROR = _datacollection.DataCollection_WRITE_ERROR
    

    def Error(self):
        r"""Error(DataCollection self) -> int"""
        return _datacollection.DataCollection_Error(self)
    Error = _swig_new_instance_method(_datacollection.DataCollection_Error)

    def ResetError(self, *args, **kwargs):
        r"""ResetError(DataCollection self, int err_state=No_Error)"""
        return _datacollection.DataCollection_ResetError(self, *args, **kwargs)
    ResetError = _swig_new_instance_method(_datacollection.DataCollection_ResetError)

# Register DataCollection in _datacollection:
_datacollection.DataCollection_swigregister(DataCollection)
class VisItFieldInfo(object):
    r"""Proxy of C++ mfem::VisItFieldInfo class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    association = property(_datacollection.VisItFieldInfo_association_get, _datacollection.VisItFieldInfo_association_set, doc=r"""association : std::string""")
    num_components = property(_datacollection.VisItFieldInfo_num_components_get, _datacollection.VisItFieldInfo_num_components_set, doc=r"""num_components : int""")
    lod = property(_datacollection.VisItFieldInfo_lod_get, _datacollection.VisItFieldInfo_lod_set, doc=r"""lod : int""")

    def __init__(self, *args):
        r"""
        __init__(VisItFieldInfo self) -> VisItFieldInfo
        __init__(VisItFieldInfo self, std::string association_, int num_components_, int lod_=1) -> VisItFieldInfo
        """
        _datacollection.VisItFieldInfo_swiginit(self, _datacollection.new_VisItFieldInfo(*args))
    __swig_destroy__ = _datacollection.delete_VisItFieldInfo

# Register VisItFieldInfo in _datacollection:
_datacollection.VisItFieldInfo_swigregister(VisItFieldInfo)
class VisItDataCollection(DataCollection):
    r"""Proxy of C++ mfem::VisItDataCollection class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(VisItDataCollection self, std::string const & collection_name, Mesh mesh_=None) -> VisItDataCollection
        __init__(VisItDataCollection self, MPI_Comm comm, std::string const & collection_name, Mesh mesh_=None) -> VisItDataCollection
        """
        _datacollection.VisItDataCollection_swiginit(self, _datacollection.new_VisItDataCollection(*args))

    def SetMesh(self, *args):
        r"""
        SetMesh(VisItDataCollection self, Mesh new_mesh)
        SetMesh(VisItDataCollection self, MPI_Comm comm, Mesh new_mesh)
        """
        return _datacollection.VisItDataCollection_SetMesh(self, *args)
    SetMesh = _swig_new_instance_method(_datacollection.VisItDataCollection_SetMesh)

    def RegisterField(self, field_name, gf):
        r"""RegisterField(VisItDataCollection self, std::string const & field_name, GridFunction gf)"""
        return _datacollection.VisItDataCollection_RegisterField(self, field_name, gf)
    RegisterField = _swig_new_instance_method(_datacollection.VisItDataCollection_RegisterField)

    def RegisterQField(self, q_field_name, qf):
        r"""RegisterQField(VisItDataCollection self, std::string const & q_field_name, mfem::QuadratureFunction * qf)"""
        return _datacollection.VisItDataCollection_RegisterQField(self, q_field_name, qf)
    RegisterQField = _swig_new_instance_method(_datacollection.VisItDataCollection_RegisterQField)

    def SetPadDigits(self, digits):
        r"""SetPadDigits(VisItDataCollection self, int digits)"""
        return _datacollection.VisItDataCollection_SetPadDigits(self, digits)
    SetPadDigits = _swig_new_instance_method(_datacollection.VisItDataCollection_SetPadDigits)

    def SetLevelsOfDetail(self, levels_of_detail):
        r"""SetLevelsOfDetail(VisItDataCollection self, int levels_of_detail)"""
        return _datacollection.VisItDataCollection_SetLevelsOfDetail(self, levels_of_detail)
    SetLevelsOfDetail = _swig_new_instance_method(_datacollection.VisItDataCollection_SetLevelsOfDetail)

    def SetMaxLevelsOfDetail(self, max_levels_of_detail):
        r"""SetMaxLevelsOfDetail(VisItDataCollection self, int max_levels_of_detail)"""
        return _datacollection.VisItDataCollection_SetMaxLevelsOfDetail(self, max_levels_of_detail)
    SetMaxLevelsOfDetail = _swig_new_instance_method(_datacollection.VisItDataCollection_SetMaxLevelsOfDetail)

    def DeleteAll(self):
        r"""DeleteAll(VisItDataCollection self)"""
        return _datacollection.VisItDataCollection_DeleteAll(self)
    DeleteAll = _swig_new_instance_method(_datacollection.VisItDataCollection_DeleteAll)

    def Save(self):
        r"""Save(VisItDataCollection self)"""
        return _datacollection.VisItDataCollection_Save(self)
    Save = _swig_new_instance_method(_datacollection.VisItDataCollection_Save)

    def SaveRootFile(self):
        r"""SaveRootFile(VisItDataCollection self)"""
        return _datacollection.VisItDataCollection_SaveRootFile(self)
    SaveRootFile = _swig_new_instance_method(_datacollection.VisItDataCollection_SaveRootFile)

    def Load(self, cycle_=0):
        r"""Load(VisItDataCollection self, int cycle_=0)"""
        return _datacollection.VisItDataCollection_Load(self, cycle_)
    Load = _swig_new_instance_method(_datacollection.VisItDataCollection_Load)
    __swig_destroy__ = _datacollection.delete_VisItDataCollection

# Register VisItDataCollection in _datacollection:
_datacollection.VisItDataCollection_swigregister(VisItDataCollection)
class ParaViewDataCollection(DataCollection):
    r"""Proxy of C++ mfem::ParaViewDataCollection class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, collection_name, mesh_=None):
        r"""__init__(ParaViewDataCollection self, std::string const & collection_name, Mesh mesh_=None) -> ParaViewDataCollection"""
        _datacollection.ParaViewDataCollection_swiginit(self, _datacollection.new_ParaViewDataCollection(collection_name, mesh_))

    def SetLevelsOfDetail(self, levels_of_detail_):
        r"""SetLevelsOfDetail(ParaViewDataCollection self, int levels_of_detail_)"""
        return _datacollection.ParaViewDataCollection_SetLevelsOfDetail(self, levels_of_detail_)
    SetLevelsOfDetail = _swig_new_instance_method(_datacollection.ParaViewDataCollection_SetLevelsOfDetail)

    def Save(self):
        r"""Save(ParaViewDataCollection self)"""
        return _datacollection.ParaViewDataCollection_Save(self)
    Save = _swig_new_instance_method(_datacollection.ParaViewDataCollection_Save)

    def SetDataFormat(self, fmt):
        r"""SetDataFormat(ParaViewDataCollection self, mfem::VTKFormat fmt)"""
        return _datacollection.ParaViewDataCollection_SetDataFormat(self, fmt)
    SetDataFormat = _swig_new_instance_method(_datacollection.ParaViewDataCollection_SetDataFormat)

    def SetCompressionLevel(self, compression_level_):
        r"""SetCompressionLevel(ParaViewDataCollection self, int compression_level_)"""
        return _datacollection.ParaViewDataCollection_SetCompressionLevel(self, compression_level_)
    SetCompressionLevel = _swig_new_instance_method(_datacollection.ParaViewDataCollection_SetCompressionLevel)

    def SetCompression(self, compression_):
        r"""SetCompression(ParaViewDataCollection self, bool compression_)"""
        return _datacollection.ParaViewDataCollection_SetCompression(self, compression_)
    SetCompression = _swig_new_instance_method(_datacollection.ParaViewDataCollection_SetCompression)

    def IsBinaryFormat(self):
        r"""IsBinaryFormat(ParaViewDataCollection self) -> bool"""
        return _datacollection.ParaViewDataCollection_IsBinaryFormat(self)
    IsBinaryFormat = _swig_new_instance_method(_datacollection.ParaViewDataCollection_IsBinaryFormat)

    def SetHighOrderOutput(self, high_order_output_):
        r"""SetHighOrderOutput(ParaViewDataCollection self, bool high_order_output_)"""
        return _datacollection.ParaViewDataCollection_SetHighOrderOutput(self, high_order_output_)
    SetHighOrderOutput = _swig_new_instance_method(_datacollection.ParaViewDataCollection_SetHighOrderOutput)

    def UseRestartMode(self, restart_mode_):
        r"""UseRestartMode(ParaViewDataCollection self, bool restart_mode_)"""
        return _datacollection.ParaViewDataCollection_UseRestartMode(self, restart_mode_)
    UseRestartMode = _swig_new_instance_method(_datacollection.ParaViewDataCollection_UseRestartMode)

    def Load(self, cycle_=0):
        r"""Load(ParaViewDataCollection self, int cycle_=0)"""
        return _datacollection.ParaViewDataCollection_Load(self, cycle_)
    Load = _swig_new_instance_method(_datacollection.ParaViewDataCollection_Load)
    __swig_destroy__ = _datacollection.delete_ParaViewDataCollection

# Register ParaViewDataCollection in _datacollection:
_datacollection.ParaViewDataCollection_swigregister(ParaViewDataCollection)

