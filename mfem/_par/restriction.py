# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _restriction
else:
    import _restriction

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _restriction.SWIG_PyInstanceMethod_New
_swig_new_static_method = _restriction.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
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

import mfem._par.element
import mfem._par.globals
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.densemat
import mfem._par.vector
import mfem._par.operators
import mfem._par.matrix
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.handle
import mfem._par.hypre
import mfem._par.bilininteg
import mfem._par.linearform
L2FaceValues_SingleValued = _restriction.L2FaceValues_SingleValued

L2FaceValues_DoubleValued = _restriction.L2FaceValues_DoubleValued

class ElementRestriction(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::ElementRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3):
        r"""__init__(ElementRestriction self, FiniteElementSpace arg2, mfem::ElementDofOrdering arg3) -> ElementRestriction"""
        _restriction.ElementRestriction_swiginit(self, _restriction.new_ElementRestriction(arg2, arg3))

    def Mult(self, x, y):
        r"""Mult(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.ElementRestriction_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.ElementRestriction_MultTranspose)

    def MultUnsigned(self, x, y):
        r"""MultUnsigned(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultUnsigned(self, x, y)
    MultUnsigned = _swig_new_instance_method(_restriction.ElementRestriction_MultUnsigned)

    def MultTransposeUnsigned(self, x, y):
        r"""MultTransposeUnsigned(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultTransposeUnsigned(self, x, y)
    MultTransposeUnsigned = _swig_new_instance_method(_restriction.ElementRestriction_MultTransposeUnsigned)

    def BooleanMask(self, y):
        r"""BooleanMask(ElementRestriction self, Vector y)"""
        return _restriction.ElementRestriction_BooleanMask(self, y)
    BooleanMask = _swig_new_instance_method(_restriction.ElementRestriction_BooleanMask)

    def FillSparseMatrix(self, mat_ea, mat):
        r"""FillSparseMatrix(ElementRestriction self, Vector mat_ea, SparseMatrix mat)"""
        return _restriction.ElementRestriction_FillSparseMatrix(self, mat_ea, mat)
    FillSparseMatrix = _swig_new_instance_method(_restriction.ElementRestriction_FillSparseMatrix)

    def FillI(self, mat):
        r"""FillI(ElementRestriction self, SparseMatrix mat) -> int"""
        return _restriction.ElementRestriction_FillI(self, mat)
    FillI = _swig_new_instance_method(_restriction.ElementRestriction_FillI)

    def FillJAndData(self, ea_data, mat):
        r"""FillJAndData(ElementRestriction self, Vector ea_data, SparseMatrix mat)"""
        return _restriction.ElementRestriction_FillJAndData(self, ea_data, mat)
    FillJAndData = _swig_new_instance_method(_restriction.ElementRestriction_FillJAndData)
    __swig_destroy__ = _restriction.delete_ElementRestriction

# Register ElementRestriction in _restriction:
_restriction.ElementRestriction_swigregister(ElementRestriction)

class L2ElementRestriction(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::L2ElementRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2):
        r"""__init__(L2ElementRestriction self, FiniteElementSpace arg2) -> L2ElementRestriction"""
        _restriction.L2ElementRestriction_swiginit(self, _restriction.new_L2ElementRestriction(arg2))

    def Mult(self, x, y):
        r"""Mult(L2ElementRestriction self, Vector x, Vector y)"""
        return _restriction.L2ElementRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.L2ElementRestriction_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(L2ElementRestriction self, Vector x, Vector y)"""
        return _restriction.L2ElementRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.L2ElementRestriction_MultTranspose)

    def FillI(self, mat):
        r"""FillI(L2ElementRestriction self, SparseMatrix mat)"""
        return _restriction.L2ElementRestriction_FillI(self, mat)
    FillI = _swig_new_instance_method(_restriction.L2ElementRestriction_FillI)

    def FillJAndData(self, ea_data, mat):
        r"""FillJAndData(L2ElementRestriction self, Vector ea_data, SparseMatrix mat)"""
        return _restriction.L2ElementRestriction_FillJAndData(self, ea_data, mat)
    FillJAndData = _swig_new_instance_method(_restriction.L2ElementRestriction_FillJAndData)
    __swig_destroy__ = _restriction.delete_L2ElementRestriction

# Register L2ElementRestriction in _restriction:
_restriction.L2ElementRestriction_swigregister(L2ElementRestriction)

class H1FaceRestriction(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::H1FaceRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3, arg4):
        r"""__init__(H1FaceRestriction self, FiniteElementSpace arg2, mfem::ElementDofOrdering const arg3, mfem::FaceType const arg4) -> H1FaceRestriction"""
        _restriction.H1FaceRestriction_swiginit(self, _restriction.new_H1FaceRestriction(arg2, arg3, arg4))

    def Mult(self, x, y):
        r"""Mult(H1FaceRestriction self, Vector x, Vector y)"""
        return _restriction.H1FaceRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.H1FaceRestriction_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(H1FaceRestriction self, Vector x, Vector y)"""
        return _restriction.H1FaceRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.H1FaceRestriction_MultTranspose)
    __swig_destroy__ = _restriction.delete_H1FaceRestriction

# Register H1FaceRestriction in _restriction:
_restriction.H1FaceRestriction_swigregister(H1FaceRestriction)

class L2FaceRestriction(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::L2FaceRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""__init__(L2FaceRestriction self, FiniteElementSpace arg2, mfem::ElementDofOrdering const arg3, mfem::FaceType const arg4, mfem::L2FaceValues const m=DoubleValued) -> L2FaceRestriction"""
        _restriction.L2FaceRestriction_swiginit(self, _restriction.new_L2FaceRestriction(*args))

    def Mult(self, x, y):
        r"""Mult(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.L2FaceRestriction_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.L2FaceRestriction_MultTranspose)

    def FillI(self, mat, face_mat):
        r"""FillI(L2FaceRestriction self, SparseMatrix mat, SparseMatrix face_mat)"""
        return _restriction.L2FaceRestriction_FillI(self, mat, face_mat)
    FillI = _swig_new_instance_method(_restriction.L2FaceRestriction_FillI)

    def FillJAndData(self, ea_data, mat, face_mat):
        r"""FillJAndData(L2FaceRestriction self, Vector ea_data, SparseMatrix mat, SparseMatrix face_mat)"""
        return _restriction.L2FaceRestriction_FillJAndData(self, ea_data, mat, face_mat)
    FillJAndData = _swig_new_instance_method(_restriction.L2FaceRestriction_FillJAndData)

    def AddFaceMatricesToElementMatrices(self, fea_data, ea_data):
        r"""AddFaceMatricesToElementMatrices(L2FaceRestriction self, Vector fea_data, Vector ea_data)"""
        return _restriction.L2FaceRestriction_AddFaceMatricesToElementMatrices(self, fea_data, ea_data)
    AddFaceMatricesToElementMatrices = _swig_new_instance_method(_restriction.L2FaceRestriction_AddFaceMatricesToElementMatrices)
    __swig_destroy__ = _restriction.delete_L2FaceRestriction

# Register L2FaceRestriction in _restriction:
_restriction.L2FaceRestriction_swigregister(L2FaceRestriction)


def GetFaceDofs(dim, face_id, dof1d, faceMap):
    r"""GetFaceDofs(int const dim, int const face_id, int const dof1d, intArray faceMap)"""
    return _restriction.GetFaceDofs(dim, face_id, dof1d, faceMap)
GetFaceDofs = _restriction.GetFaceDofs

def ToLexOrdering(dim, face_id, size1d, index):
    r"""ToLexOrdering(int const dim, int const face_id, int const size1d, int const index) -> int"""
    return _restriction.ToLexOrdering(dim, face_id, size1d, index)
ToLexOrdering = _restriction.ToLexOrdering

def PermuteFaceL2(dim, face_id1, face_id2, orientation, size1d, index):
    r"""PermuteFaceL2(int const dim, int const face_id1, int const face_id2, int const orientation, int const size1d, int const index) -> int"""
    return _restriction.PermuteFaceL2(dim, face_id1, face_id2, orientation, size1d, index)
PermuteFaceL2 = _restriction.PermuteFaceL2


