# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _quadinterpolator_face
else:
    import _quadinterpolator_face

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _quadinterpolator_face.SWIG_PyInstanceMethod_New
_swig_new_static_method = _quadinterpolator_face.SWIG_PyStaticMethod_New

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
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.coefficient
import mfem._ser.symmat
import mfem._ser.eltrans
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.std_vectors
import mfem._ser.qspace
class FaceQuadratureInterpolator(object):
    r"""Proxy of C++ mfem::FaceQuadratureInterpolator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    VALUES = _quadinterpolator_face.FaceQuadratureInterpolator_VALUES
    
    DERIVATIVES = _quadinterpolator_face.FaceQuadratureInterpolator_DERIVATIVES
    
    DETERMINANTS = _quadinterpolator_face.FaceQuadratureInterpolator_DETERMINANTS
    
    NORMALS = _quadinterpolator_face.FaceQuadratureInterpolator_NORMALS
    

    def __init__(self, fes, ir, type):
        r"""__init__(FaceQuadratureInterpolator self, FiniteElementSpace fes, IntegrationRule ir, mfem::FaceType type) -> FaceQuadratureInterpolator"""
        _quadinterpolator_face.FaceQuadratureInterpolator_swiginit(self, _quadinterpolator_face.new_FaceQuadratureInterpolator(fes, ir, type))

    def DisableTensorProducts(self, disable=True):
        r"""DisableTensorProducts(FaceQuadratureInterpolator self, bool disable=True)"""
        return _quadinterpolator_face.FaceQuadratureInterpolator_DisableTensorProducts(self, disable)
    DisableTensorProducts = _swig_new_instance_method(_quadinterpolator_face.FaceQuadratureInterpolator_DisableTensorProducts)

    def GetOutputLayout(self):
        r"""GetOutputLayout(FaceQuadratureInterpolator self) -> mfem::QVectorLayout"""
        return _quadinterpolator_face.FaceQuadratureInterpolator_GetOutputLayout(self)
    GetOutputLayout = _swig_new_instance_method(_quadinterpolator_face.FaceQuadratureInterpolator_GetOutputLayout)

    def SetOutputLayout(self, layout):
        r"""SetOutputLayout(FaceQuadratureInterpolator self, mfem::QVectorLayout layout)"""
        return _quadinterpolator_face.FaceQuadratureInterpolator_SetOutputLayout(self, layout)
    SetOutputLayout = _swig_new_instance_method(_quadinterpolator_face.FaceQuadratureInterpolator_SetOutputLayout)

    def Mult(self, e_vec, eval_flags, q_val, q_der, q_det, q_nor):
        r"""Mult(FaceQuadratureInterpolator self, Vector e_vec, unsigned int eval_flags, Vector q_val, Vector q_der, Vector q_det, Vector q_nor)"""
        return _quadinterpolator_face.FaceQuadratureInterpolator_Mult(self, e_vec, eval_flags, q_val, q_der, q_det, q_nor)
    Mult = _swig_new_instance_method(_quadinterpolator_face.FaceQuadratureInterpolator_Mult)

    def Values(self, e_vec, q_val):
        r"""Values(FaceQuadratureInterpolator self, Vector e_vec, Vector q_val)"""
        return _quadinterpolator_face.FaceQuadratureInterpolator_Values(self, e_vec, q_val)
    Values = _swig_new_instance_method(_quadinterpolator_face.FaceQuadratureInterpolator_Values)
    __swig_destroy__ = _quadinterpolator_face.delete_FaceQuadratureInterpolator

# Register FaceQuadratureInterpolator in _quadinterpolator_face:
_quadinterpolator_face.FaceQuadratureInterpolator_swigregister(FaceQuadratureInterpolator)
