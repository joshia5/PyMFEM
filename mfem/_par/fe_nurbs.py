# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _fe_nurbs
else:
    import _fe_nurbs

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _fe_nurbs.SWIG_PyInstanceMethod_New
_swig_new_static_method = _fe_nurbs.SWIG_PyStaticMethod_New

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

import mfem._par.fe_base
import mfem._par.intrules
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.globals
import mfem._par.geom
import mfem._par.densemat
import mfem._par.vector
import mfem._par.operators
import mfem._par.matrix
import mfem._par.element
import mfem._par.table
import mfem._par.hash
class NURBSFiniteElement(mfem._par.fe_base.ScalarFiniteElement):
    r"""Proxy of C++ mfem::NURBSFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Reset(self):
        r"""Reset(NURBSFiniteElement self)"""
        return _fe_nurbs.NURBSFiniteElement_Reset(self)
    Reset = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_Reset)

    def SetIJK(self, IJK):
        r"""SetIJK(NURBSFiniteElement self, int const * IJK)"""
        return _fe_nurbs.NURBSFiniteElement_SetIJK(self, IJK)
    SetIJK = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_SetIJK)

    def GetPatch(self):
        r"""GetPatch(NURBSFiniteElement self) -> int"""
        return _fe_nurbs.NURBSFiniteElement_GetPatch(self)
    GetPatch = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_GetPatch)

    def SetPatch(self, p):
        r"""SetPatch(NURBSFiniteElement self, int p)"""
        return _fe_nurbs.NURBSFiniteElement_SetPatch(self, p)
    SetPatch = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_SetPatch)

    def GetElement(self):
        r"""GetElement(NURBSFiniteElement self) -> int"""
        return _fe_nurbs.NURBSFiniteElement_GetElement(self)
    GetElement = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_GetElement)

    def SetElement(self, e):
        r"""SetElement(NURBSFiniteElement self, int e)"""
        return _fe_nurbs.NURBSFiniteElement_SetElement(self, e)
    SetElement = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_SetElement)

    def KnotVectors(self):
        r"""KnotVectors(NURBSFiniteElement self) -> mfem::Array< mfem::KnotVector const * > &"""
        return _fe_nurbs.NURBSFiniteElement_KnotVectors(self)
    KnotVectors = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_KnotVectors)

    def Weights(self):
        r"""Weights(NURBSFiniteElement self) -> Vector"""
        return _fe_nurbs.NURBSFiniteElement_Weights(self)
    Weights = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_Weights)

    def SetOrder(self):
        r"""SetOrder(NURBSFiniteElement self)"""
        return _fe_nurbs.NURBSFiniteElement_SetOrder(self)
    SetOrder = _swig_new_instance_method(_fe_nurbs.NURBSFiniteElement_SetOrder)
    __swig_destroy__ = _fe_nurbs.delete_NURBSFiniteElement

# Register NURBSFiniteElement in _fe_nurbs:
_fe_nurbs.NURBSFiniteElement_swigregister(NURBSFiniteElement)
class NURBS1DFiniteElement(NURBSFiniteElement):
    r"""Proxy of C++ mfem::NURBS1DFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(NURBS1DFiniteElement self, int p) -> NURBS1DFiniteElement"""
        _fe_nurbs.NURBS1DFiniteElement_swiginit(self, _fe_nurbs.new_NURBS1DFiniteElement(p))

    def SetOrder(self):
        r"""SetOrder(NURBS1DFiniteElement self)"""
        return _fe_nurbs.NURBS1DFiniteElement_SetOrder(self)
    SetOrder = _swig_new_instance_method(_fe_nurbs.NURBS1DFiniteElement_SetOrder)

    def CalcShape(self, ip, shape):
        r"""CalcShape(NURBS1DFiniteElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_nurbs.NURBS1DFiniteElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_nurbs.NURBS1DFiniteElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(NURBS1DFiniteElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_nurbs.NURBS1DFiniteElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_nurbs.NURBS1DFiniteElement_CalcDShape)

    def CalcHessian(self, ip, hessian):
        r"""CalcHessian(NURBS1DFiniteElement self, IntegrationPoint ip, DenseMatrix hessian)"""
        return _fe_nurbs.NURBS1DFiniteElement_CalcHessian(self, ip, hessian)
    CalcHessian = _swig_new_instance_method(_fe_nurbs.NURBS1DFiniteElement_CalcHessian)
    __swig_destroy__ = _fe_nurbs.delete_NURBS1DFiniteElement

# Register NURBS1DFiniteElement in _fe_nurbs:
_fe_nurbs.NURBS1DFiniteElement_swigregister(NURBS1DFiniteElement)
class NURBS2DFiniteElement(NURBSFiniteElement):
    r"""Proxy of C++ mfem::NURBS2DFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(NURBS2DFiniteElement self, int p) -> NURBS2DFiniteElement
        __init__(NURBS2DFiniteElement self, int px, int py) -> NURBS2DFiniteElement
        """
        _fe_nurbs.NURBS2DFiniteElement_swiginit(self, _fe_nurbs.new_NURBS2DFiniteElement(*args))

    def SetOrder(self):
        r"""SetOrder(NURBS2DFiniteElement self)"""
        return _fe_nurbs.NURBS2DFiniteElement_SetOrder(self)
    SetOrder = _swig_new_instance_method(_fe_nurbs.NURBS2DFiniteElement_SetOrder)

    def CalcShape(self, ip, shape):
        r"""CalcShape(NURBS2DFiniteElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_nurbs.NURBS2DFiniteElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_nurbs.NURBS2DFiniteElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(NURBS2DFiniteElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_nurbs.NURBS2DFiniteElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_nurbs.NURBS2DFiniteElement_CalcDShape)

    def CalcHessian(self, ip, hessian):
        r"""CalcHessian(NURBS2DFiniteElement self, IntegrationPoint ip, DenseMatrix hessian)"""
        return _fe_nurbs.NURBS2DFiniteElement_CalcHessian(self, ip, hessian)
    CalcHessian = _swig_new_instance_method(_fe_nurbs.NURBS2DFiniteElement_CalcHessian)
    __swig_destroy__ = _fe_nurbs.delete_NURBS2DFiniteElement

# Register NURBS2DFiniteElement in _fe_nurbs:
_fe_nurbs.NURBS2DFiniteElement_swigregister(NURBS2DFiniteElement)
class NURBS3DFiniteElement(NURBSFiniteElement):
    r"""Proxy of C++ mfem::NURBS3DFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(NURBS3DFiniteElement self, int p) -> NURBS3DFiniteElement
        __init__(NURBS3DFiniteElement self, int px, int py, int pz) -> NURBS3DFiniteElement
        """
        _fe_nurbs.NURBS3DFiniteElement_swiginit(self, _fe_nurbs.new_NURBS3DFiniteElement(*args))

    def SetOrder(self):
        r"""SetOrder(NURBS3DFiniteElement self)"""
        return _fe_nurbs.NURBS3DFiniteElement_SetOrder(self)
    SetOrder = _swig_new_instance_method(_fe_nurbs.NURBS3DFiniteElement_SetOrder)

    def CalcShape(self, ip, shape):
        r"""CalcShape(NURBS3DFiniteElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_nurbs.NURBS3DFiniteElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_nurbs.NURBS3DFiniteElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(NURBS3DFiniteElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_nurbs.NURBS3DFiniteElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_nurbs.NURBS3DFiniteElement_CalcDShape)

    def CalcHessian(self, ip, hessian):
        r"""CalcHessian(NURBS3DFiniteElement self, IntegrationPoint ip, DenseMatrix hessian)"""
        return _fe_nurbs.NURBS3DFiniteElement_CalcHessian(self, ip, hessian)
    CalcHessian = _swig_new_instance_method(_fe_nurbs.NURBS3DFiniteElement_CalcHessian)
    __swig_destroy__ = _fe_nurbs.delete_NURBS3DFiniteElement

# Register NURBS3DFiniteElement in _fe_nurbs:
_fe_nurbs.NURBS3DFiniteElement_swigregister(NURBS3DFiniteElement)
