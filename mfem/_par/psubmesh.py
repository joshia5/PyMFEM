# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _psubmesh
else:
    import _psubmesh

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _psubmesh.SWIG_PyInstanceMethod_New
_swig_new_static_method = _psubmesh.SWIG_PyStaticMethod_New

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

import mfem._par.submesh
import mfem._par.mesh
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.globals
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
import mfem._par.transfermap
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
import mfem._par.pgridfunc
import mfem._par.pfespace
import mfem._par.ptransfermap
class ParSubMesh(mfem._par.pmesh.ParMesh):
    r"""Proxy of C++ mfem::ParSubMesh class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    @staticmethod
    def CreateFromDomain(parent, domain_attributes):
        r"""CreateFromDomain(ParMesh parent, intArray domain_attributes) -> ParSubMesh"""
        return _psubmesh.ParSubMesh_CreateFromDomain(parent, domain_attributes)
    CreateFromDomain = _swig_new_static_method(_psubmesh.ParSubMesh_CreateFromDomain)

    @staticmethod
    def CreateFromBoundary(parent, boundary_attributes):
        r"""CreateFromBoundary(ParMesh parent, intArray boundary_attributes) -> ParSubMesh"""
        return _psubmesh.ParSubMesh_CreateFromBoundary(parent, boundary_attributes)
    CreateFromBoundary = _swig_new_static_method(_psubmesh.ParSubMesh_CreateFromBoundary)

    def GetParent(self):
        r"""GetParent(ParSubMesh self) -> ParMesh"""
        return _psubmesh.ParSubMesh_GetParent(self)
    GetParent = _swig_new_instance_method(_psubmesh.ParSubMesh_GetParent)

    def GetFrom(self):
        r"""GetFrom(ParSubMesh self) -> mfem::SubMesh::From"""
        return _psubmesh.ParSubMesh_GetFrom(self)
    GetFrom = _swig_new_instance_method(_psubmesh.ParSubMesh_GetFrom)

    def GetParentElementIDMap(self):
        r"""GetParentElementIDMap(ParSubMesh self) -> intArray"""
        return _psubmesh.ParSubMesh_GetParentElementIDMap(self)
    GetParentElementIDMap = _swig_new_instance_method(_psubmesh.ParSubMesh_GetParentElementIDMap)

    def GetParentVertexIDMap(self):
        r"""GetParentVertexIDMap(ParSubMesh self) -> intArray"""
        return _psubmesh.ParSubMesh_GetParentVertexIDMap(self)
    GetParentVertexIDMap = _swig_new_instance_method(_psubmesh.ParSubMesh_GetParentVertexIDMap)

    def GetParentFaceIDMap(self):
        r"""GetParentFaceIDMap(ParSubMesh self) -> intArray"""
        return _psubmesh.ParSubMesh_GetParentFaceIDMap(self)
    GetParentFaceIDMap = _swig_new_instance_method(_psubmesh.ParSubMesh_GetParentFaceIDMap)

    def GetParentToSubMeshFaceIDMap(self):
        r"""GetParentToSubMeshFaceIDMap(ParSubMesh self) -> intArray"""
        return _psubmesh.ParSubMesh_GetParentToSubMeshFaceIDMap(self)
    GetParentToSubMeshFaceIDMap = _swig_new_instance_method(_psubmesh.ParSubMesh_GetParentToSubMeshFaceIDMap)

    @staticmethod
    def Transfer(src, dst):
        r"""Transfer(ParGridFunction src, ParGridFunction dst)"""
        return _psubmesh.ParSubMesh_Transfer(src, dst)
    Transfer = _swig_new_static_method(_psubmesh.ParSubMesh_Transfer)

    @staticmethod
    def CreateTransferMap(src, dst):
        r"""CreateTransferMap(ParGridFunction src, ParGridFunction dst) -> ParTransferMap"""
        return _psubmesh.ParSubMesh_CreateTransferMap(src, dst)
    CreateTransferMap = _swig_new_static_method(_psubmesh.ParSubMesh_CreateTransferMap)

    @staticmethod
    def IsParSubMesh(m):
        r"""IsParSubMesh(ParMesh m) -> bool"""
        return _psubmesh.ParSubMesh_IsParSubMesh(m)
    IsParSubMesh = _swig_new_static_method(_psubmesh.ParSubMesh_IsParSubMesh)
    __swig_destroy__ = _psubmesh.delete_ParSubMesh

# Register ParSubMesh in _psubmesh:
_psubmesh.ParSubMesh_swigregister(ParSubMesh)

