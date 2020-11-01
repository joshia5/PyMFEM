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
    from . import _estimators
else:
    import _estimators

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _estimators.SWIG_PyInstanceMethod_New
_swig_new_static_method = _estimators.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _estimators.MFEM_VERSION
MFEM_VERSION_STRING = _estimators.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _estimators.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _estimators.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _estimators.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _estimators.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _estimators.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _estimators.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _estimators.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _estimators.MFEM_INSTALL_DIR
MFEM_TIMER_TYPE = _estimators.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _estimators.MFEM_HYPRE_VERSION
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.operators
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilinearform
class AbstractErrorEstimator(object):
    r"""Proxy of C++ mfem::AbstractErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _estimators.delete_AbstractErrorEstimator

    def __init__(self):
        r"""__init__(AbstractErrorEstimator self) -> AbstractErrorEstimator"""
        _estimators.AbstractErrorEstimator_swiginit(self, _estimators.new_AbstractErrorEstimator())

# Register AbstractErrorEstimator in _estimators:
_estimators.AbstractErrorEstimator_swigregister(AbstractErrorEstimator)

class ErrorEstimator(AbstractErrorEstimator):
    r"""Proxy of C++ mfem::ErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetLocalErrors(self):
        r"""GetLocalErrors(ErrorEstimator self) -> Vector"""
        return _estimators.ErrorEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.ErrorEstimator_GetLocalErrors)

    def Reset(self):
        r"""Reset(ErrorEstimator self)"""
        return _estimators.ErrorEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.ErrorEstimator_Reset)
    __swig_destroy__ = _estimators.delete_ErrorEstimator

# Register ErrorEstimator in _estimators:
_estimators.ErrorEstimator_swigregister(ErrorEstimator)

class AnisotropicErrorEstimator(ErrorEstimator):
    r"""Proxy of C++ mfem::AnisotropicErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetAnisotropicFlags(self):
        r"""GetAnisotropicFlags(AnisotropicErrorEstimator self) -> intArray"""
        return _estimators.AnisotropicErrorEstimator_GetAnisotropicFlags(self)
    GetAnisotropicFlags = _swig_new_instance_method(_estimators.AnisotropicErrorEstimator_GetAnisotropicFlags)
    __swig_destroy__ = _estimators.delete_AnisotropicErrorEstimator

# Register AnisotropicErrorEstimator in _estimators:
_estimators.AnisotropicErrorEstimator_swigregister(AnisotropicErrorEstimator)

class ZienkiewiczZhuEstimator(AnisotropicErrorEstimator):
    r"""Proxy of C++ mfem::ZienkiewiczZhuEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def SetWithCoeff(self, w_coeff=True):
        r"""SetWithCoeff(ZienkiewiczZhuEstimator self, bool w_coeff=True)"""
        return _estimators.ZienkiewiczZhuEstimator_SetWithCoeff(self, w_coeff)
    SetWithCoeff = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_SetWithCoeff)

    def SetAnisotropic(self, aniso=True):
        r"""SetAnisotropic(ZienkiewiczZhuEstimator self, bool aniso=True)"""
        return _estimators.ZienkiewiczZhuEstimator_SetAnisotropic(self, aniso)
    SetAnisotropic = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_SetAnisotropic)

    def SetFluxAveraging(self, fa):
        r"""SetFluxAveraging(ZienkiewiczZhuEstimator self, int fa)"""
        return _estimators.ZienkiewiczZhuEstimator_SetFluxAveraging(self, fa)
    SetFluxAveraging = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_SetFluxAveraging)

    def GetTotalError(self):
        r"""GetTotalError(ZienkiewiczZhuEstimator self) -> double"""
        return _estimators.ZienkiewiczZhuEstimator_GetTotalError(self)
    GetTotalError = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_GetTotalError)

    def GetLocalErrors(self):
        r"""GetLocalErrors(ZienkiewiczZhuEstimator self) -> Vector"""
        return _estimators.ZienkiewiczZhuEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_GetLocalErrors)

    def GetAnisotropicFlags(self):
        r"""GetAnisotropicFlags(ZienkiewiczZhuEstimator self) -> intArray"""
        return _estimators.ZienkiewiczZhuEstimator_GetAnisotropicFlags(self)
    GetAnisotropicFlags = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_GetAnisotropicFlags)

    def Reset(self):
        r"""Reset(ZienkiewiczZhuEstimator self)"""
        return _estimators.ZienkiewiczZhuEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.ZienkiewiczZhuEstimator_Reset)
    __swig_destroy__ = _estimators.delete_ZienkiewiczZhuEstimator

    def __init__(self, integ, sol, flux_fes, own_flux_fes=False):
        r"""__init__(ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, GridFunction sol, FiniteElementSpace flux_fes, bool own_flux_fes=False) -> ZienkiewiczZhuEstimator"""

        if own_flux_fes: flux_fes.thisown=0


        _estimators.ZienkiewiczZhuEstimator_swiginit(self, _estimators.new_ZienkiewiczZhuEstimator(integ, sol, flux_fes, own_flux_fes))

# Register ZienkiewiczZhuEstimator in _estimators:
_estimators.ZienkiewiczZhuEstimator_swigregister(ZienkiewiczZhuEstimator)

class L2ZienkiewiczZhuEstimator(ErrorEstimator):
    r"""Proxy of C++ mfem::L2ZienkiewiczZhuEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def SetLocalErrorNormP(self, p):
        r"""SetLocalErrorNormP(L2ZienkiewiczZhuEstimator self, int p)"""
        return _estimators.L2ZienkiewiczZhuEstimator_SetLocalErrorNormP(self, p)
    SetLocalErrorNormP = _swig_new_instance_method(_estimators.L2ZienkiewiczZhuEstimator_SetLocalErrorNormP)

    def GetTotalError(self):
        r"""GetTotalError(L2ZienkiewiczZhuEstimator self) -> double"""
        return _estimators.L2ZienkiewiczZhuEstimator_GetTotalError(self)
    GetTotalError = _swig_new_instance_method(_estimators.L2ZienkiewiczZhuEstimator_GetTotalError)

    def GetLocalErrors(self):
        r"""GetLocalErrors(L2ZienkiewiczZhuEstimator self) -> Vector"""
        return _estimators.L2ZienkiewiczZhuEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.L2ZienkiewiczZhuEstimator_GetLocalErrors)

    def Reset(self):
        r"""Reset(L2ZienkiewiczZhuEstimator self)"""
        return _estimators.L2ZienkiewiczZhuEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.L2ZienkiewiczZhuEstimator_Reset)
    __swig_destroy__ = _estimators.delete_L2ZienkiewiczZhuEstimator

    def __init__(self, integ, sol, flux_fes, smooth_flux_fes, own_flux_fes=False):
        r"""__init__(L2ZienkiewiczZhuEstimator self, BilinearFormIntegrator integ, mfem::ParGridFunction & sol, mfem::ParFiniteElementSpace * flux_fes, mfem::ParFiniteElementSpace * smooth_flux_fes, bool own_flux_fes=False) -> L2ZienkiewiczZhuEstimator"""

        if own_flux_fes: flux_fes.thisown=0


        _estimators.L2ZienkiewiczZhuEstimator_swiginit(self, _estimators.new_L2ZienkiewiczZhuEstimator(integ, sol, flux_fes, smooth_flux_fes, own_flux_fes))

# Register L2ZienkiewiczZhuEstimator in _estimators:
_estimators.L2ZienkiewiczZhuEstimator_swigregister(L2ZienkiewiczZhuEstimator)

class LpErrorEstimator(ErrorEstimator):
    r"""Proxy of C++ mfem::LpErrorEstimator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(LpErrorEstimator self, int p, GridFunction sol) -> LpErrorEstimator
        __init__(LpErrorEstimator self, int p, Coefficient coef, GridFunction sol) -> LpErrorEstimator
        __init__(LpErrorEstimator self, int p, VectorCoefficient coef, GridFunction sol) -> LpErrorEstimator
        """
        _estimators.LpErrorEstimator_swiginit(self, _estimators.new_LpErrorEstimator(*args))

    def SetLocalErrorNormP(self, p):
        r"""SetLocalErrorNormP(LpErrorEstimator self, int p)"""
        return _estimators.LpErrorEstimator_SetLocalErrorNormP(self, p)
    SetLocalErrorNormP = _swig_new_instance_method(_estimators.LpErrorEstimator_SetLocalErrorNormP)

    def SetCoef(self, *args):
        r"""
        SetCoef(LpErrorEstimator self, Coefficient A)
        SetCoef(LpErrorEstimator self, VectorCoefficient A)
        """
        return _estimators.LpErrorEstimator_SetCoef(self, *args)
    SetCoef = _swig_new_instance_method(_estimators.LpErrorEstimator_SetCoef)

    def Reset(self):
        r"""Reset(LpErrorEstimator self)"""
        return _estimators.LpErrorEstimator_Reset(self)
    Reset = _swig_new_instance_method(_estimators.LpErrorEstimator_Reset)

    def GetLocalErrors(self):
        r"""GetLocalErrors(LpErrorEstimator self) -> Vector"""
        return _estimators.LpErrorEstimator_GetLocalErrors(self)
    GetLocalErrors = _swig_new_instance_method(_estimators.LpErrorEstimator_GetLocalErrors)
    __swig_destroy__ = _estimators.delete_LpErrorEstimator

# Register LpErrorEstimator in _estimators:
_estimators.LpErrorEstimator_swigregister(LpErrorEstimator)



