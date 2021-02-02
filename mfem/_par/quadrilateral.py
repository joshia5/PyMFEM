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
    from . import _quadrilateral
else:
    import _quadrilateral

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _quadrilateral.SWIG_PyInstanceMethod_New
_swig_new_static_method = _quadrilateral.SWIG_PyStaticMethod_New

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

import mfem._par.fe
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.geom
import mfem._par.intrules
import mfem._par.densemat
import mfem._par.operators
import mfem._par.matrix
import mfem._par.sparsemat
import mfem._par.element
import mfem._par.globals
import mfem._par.table
import mfem._par.hash
class Quadrilateral(mfem._par.element.Element):
    r"""Proxy of C++ mfem::Quadrilateral class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(Quadrilateral self) -> Quadrilateral
        __init__(Quadrilateral self, int const * ind, int attr=1) -> Quadrilateral
        __init__(Quadrilateral self, int ind1, int ind2, int ind3, int ind4, int attr=1) -> Quadrilateral
        """
        _quadrilateral.Quadrilateral_swiginit(self, _quadrilateral.new_Quadrilateral(*args))

    def GetType(self):
        r"""GetType(Quadrilateral self) -> mfem::Element::Type"""
        return _quadrilateral.Quadrilateral_GetType(self)
    GetType = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetType)

    def SetVertices(self, ind):
        r"""SetVertices(Quadrilateral self, int const * ind)"""
        return _quadrilateral.Quadrilateral_SetVertices(self, ind)
    SetVertices = _swig_new_instance_method(_quadrilateral.Quadrilateral_SetVertices)

    def GetVertices(self, *args):
        r"""
        GetVertices(Quadrilateral self, intArray v)
        GetVertices(Quadrilateral self) -> int *
        """
        return _quadrilateral.Quadrilateral_GetVertices(self, *args)
    GetVertices = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetVertices)

    def GetNVertices(self):
        r"""GetNVertices(Quadrilateral self) -> int"""
        return _quadrilateral.Quadrilateral_GetNVertices(self)
    GetNVertices = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetNVertices)

    def GetNEdges(self):
        r"""GetNEdges(Quadrilateral self) -> int"""
        return _quadrilateral.Quadrilateral_GetNEdges(self)
    GetNEdges = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetNEdges)

    def GetEdgeVertices(self, ei):
        r"""GetEdgeVertices(Quadrilateral self, int ei) -> int const *"""
        return _quadrilateral.Quadrilateral_GetEdgeVertices(self, ei)
    GetEdgeVertices = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetEdgeVertices)

    def GetNFaces(self, *args):
        r"""
        GetNFaces(Quadrilateral self, int & nFaceVertices) -> int
        GetNFaces(Quadrilateral self) -> int
        """

        if len(args) == 1:
             import warnings
             warnings.warn("Quadrilateral::GetNFaces(int & nFaceVertices) is deprecated is deprecated",
         	              DeprecationWarning,)


        return _quadrilateral.Quadrilateral_GetNFaces(self, *args)


    def GetNFaceVertices(self, arg2):
        r"""GetNFaceVertices(Quadrilateral self, int arg2) -> int"""
        return _quadrilateral.Quadrilateral_GetNFaceVertices(self, arg2)
    GetNFaceVertices = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetNFaceVertices)

    def GetFaceVertices(self, fi):
        r"""GetFaceVertices(Quadrilateral self, int fi) -> int const *"""
        return _quadrilateral.Quadrilateral_GetFaceVertices(self, fi)
    GetFaceVertices = _swig_new_instance_method(_quadrilateral.Quadrilateral_GetFaceVertices)

    def Duplicate(self, m):
        r"""Duplicate(Quadrilateral self, mfem::Mesh * m) -> Element"""
        return _quadrilateral.Quadrilateral_Duplicate(self, m)
    Duplicate = _swig_new_instance_method(_quadrilateral.Quadrilateral_Duplicate)
    __swig_destroy__ = _quadrilateral.delete_Quadrilateral

# Register Quadrilateral in _quadrilateral:
_quadrilateral.Quadrilateral_swigregister(Quadrilateral)


cvar = _quadrilateral.cvar

