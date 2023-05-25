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

import mfem._par.fe
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.globals
import mfem._par.vector
import mfem._par.geom
import mfem._par.intrules
import mfem._par.densemat
import mfem._par.operators
import mfem._par.matrix
import mfem._par.sparsemat
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.symmat
import mfem._par.eltrans
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
import mfem._par.qspace
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
