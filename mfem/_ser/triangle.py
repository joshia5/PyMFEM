# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _triangle
else:
    import _triangle

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _triangle.SWIG_PyInstanceMethod_New
_swig_new_static_method = _triangle.SWIG_PyStaticMethod_New

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

import mfem._ser.fe
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.globals
import mfem._ser.vector
import mfem._ser.geom
import mfem._ser.intrules
import mfem._ser.densemat
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.sparsemat
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
class Triangle(mfem._ser.element.Element):
    r"""Proxy of C++ mfem::Triangle class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(Triangle self) -> Triangle
        __init__(Triangle self, int const * ind, int attr=1) -> Triangle
        __init__(Triangle self, int ind1, int ind2, int ind3, int attr=1) -> Triangle
        """
        _triangle.Triangle_swiginit(self, _triangle.new_Triangle(*args))

    def GetType(self):
        r"""GetType(Triangle self) -> mfem::Element::Type"""
        return _triangle.Triangle_GetType(self)
    GetType = _swig_new_instance_method(_triangle.Triangle_GetType)

    def NeedRefinement(self, v_to_v):
        r"""NeedRefinement(Triangle self, mfem::HashTable< mfem::Hashed2 > & v_to_v) -> int"""
        return _triangle.Triangle_NeedRefinement(self, v_to_v)
    NeedRefinement = _swig_new_instance_method(_triangle.Triangle_NeedRefinement)

    def SetVertices(self, ind):
        r"""SetVertices(Triangle self, int const * ind)"""
        return _triangle.Triangle_SetVertices(self, ind)
    SetVertices = _swig_new_instance_method(_triangle.Triangle_SetVertices)

    def MarkEdge(self, *args):
        r"""
        MarkEdge(Triangle self, DenseMatrix pmat)
        MarkEdge(Triangle self, int * indices, DSTable v_to_v, int const * length)
        MarkEdge(Triangle self, DSTable v_to_v, int const * length)
        """
        return _triangle.Triangle_MarkEdge(self, *args)
    MarkEdge = _swig_new_instance_method(_triangle.Triangle_MarkEdge)

    def ResetTransform(self, tr):
        r"""ResetTransform(Triangle self, int tr)"""
        return _triangle.Triangle_ResetTransform(self, tr)
    ResetTransform = _swig_new_instance_method(_triangle.Triangle_ResetTransform)

    def GetTransform(self):
        r"""GetTransform(Triangle self) -> unsigned int"""
        return _triangle.Triangle_GetTransform(self)
    GetTransform = _swig_new_instance_method(_triangle.Triangle_GetTransform)

    def PushTransform(self, tr):
        r"""PushTransform(Triangle self, int tr)"""
        return _triangle.Triangle_PushTransform(self, tr)
    PushTransform = _swig_new_instance_method(_triangle.Triangle_PushTransform)

    @staticmethod
    def GetPointMatrix(transform, pm):
        r"""GetPointMatrix(unsigned int transform, DenseMatrix pm)"""
        return _triangle.Triangle_GetPointMatrix(transform, pm)
    GetPointMatrix = _swig_new_static_method(_triangle.Triangle_GetPointMatrix)

    def GetVertices(self, *args):
        r"""
        GetVertices(Triangle self, intArray v)
        GetVertices(Triangle self) -> int *
        """
        return _triangle.Triangle_GetVertices(self, *args)
    GetVertices = _swig_new_instance_method(_triangle.Triangle_GetVertices)

    def GetNVertices(self):
        r"""GetNVertices(Triangle self) -> int"""
        return _triangle.Triangle_GetNVertices(self)
    GetNVertices = _swig_new_instance_method(_triangle.Triangle_GetNVertices)

    def GetNEdges(self):
        r"""GetNEdges(Triangle self) -> int"""
        return _triangle.Triangle_GetNEdges(self)
    GetNEdges = _swig_new_instance_method(_triangle.Triangle_GetNEdges)

    def GetEdgeVertices(self, ei):
        r"""GetEdgeVertices(Triangle self, int ei) -> int const *"""
        return _triangle.Triangle_GetEdgeVertices(self, ei)
    GetEdgeVertices = _swig_new_instance_method(_triangle.Triangle_GetEdgeVertices)

    def GetNFaces(self, *args):
        r"""
        GetNFaces(Triangle self, int & nFaceVertices) -> int
        GetNFaces(Triangle self) -> int
        """

        if len(args) == 1:
             import warnings
             warnings.warn("Triangle::GetNFaces(int & nFaceVertices) is deprecated is deprecated",
         	              DeprecationWarning,)


        return _triangle.Triangle_GetNFaces(self, *args)


    def GetNFaceVertices(self, arg2):
        r"""GetNFaceVertices(Triangle self, int arg2) -> int"""
        return _triangle.Triangle_GetNFaceVertices(self, arg2)
    GetNFaceVertices = _swig_new_instance_method(_triangle.Triangle_GetNFaceVertices)

    def GetFaceVertices(self, fi):
        r"""GetFaceVertices(Triangle self, int fi) -> int const *"""
        return _triangle.Triangle_GetFaceVertices(self, fi)
    GetFaceVertices = _swig_new_instance_method(_triangle.Triangle_GetFaceVertices)

    def Duplicate(self, m):
        r"""Duplicate(Triangle self, mfem::Mesh * m) -> Element"""
        return _triangle.Triangle_Duplicate(self, m)
    Duplicate = _swig_new_instance_method(_triangle.Triangle_Duplicate)
    __swig_destroy__ = _triangle.delete_Triangle

# Register Triangle in _triangle:
_triangle.Triangle_swigregister(Triangle)

cvar = _triangle.cvar

