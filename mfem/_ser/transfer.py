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
    from . import _transfer
else:
    import _transfer

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _transfer.SWIG_PyInstanceMethod_New
_swig_new_static_method = _transfer.SWIG_PyStaticMethod_New

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

import mfem._ser.operators
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.array
import mfem._ser.fespace
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.matrix
import mfem._ser.symmat
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
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
import mfem._ser.bilininteg
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
class GridTransfer(object):
    r"""Proxy of C++ mfem::GridTransfer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _transfer.delete_GridTransfer

    def SetOperatorType(self, type):
        r"""SetOperatorType(GridTransfer self, mfem::Operator::Type type)"""
        return _transfer.GridTransfer_SetOperatorType(self, type)
    SetOperatorType = _swig_new_instance_method(_transfer.GridTransfer_SetOperatorType)

    def ForwardOperator(self):
        r"""ForwardOperator(GridTransfer self) -> Operator"""
        return _transfer.GridTransfer_ForwardOperator(self)
    ForwardOperator = _swig_new_instance_method(_transfer.GridTransfer_ForwardOperator)

    def BackwardOperator(self):
        r"""BackwardOperator(GridTransfer self) -> Operator"""
        return _transfer.GridTransfer_BackwardOperator(self)
    BackwardOperator = _swig_new_instance_method(_transfer.GridTransfer_BackwardOperator)

    def TrueForwardOperator(self):
        r"""TrueForwardOperator(GridTransfer self) -> Operator"""
        return _transfer.GridTransfer_TrueForwardOperator(self)
    TrueForwardOperator = _swig_new_instance_method(_transfer.GridTransfer_TrueForwardOperator)

    def TrueBackwardOperator(self):
        r"""TrueBackwardOperator(GridTransfer self) -> Operator"""
        return _transfer.GridTransfer_TrueBackwardOperator(self)
    TrueBackwardOperator = _swig_new_instance_method(_transfer.GridTransfer_TrueBackwardOperator)

# Register GridTransfer in _transfer:
_transfer.GridTransfer_swigregister(GridTransfer)

class InterpolationGridTransfer(GridTransfer):
    r"""Proxy of C++ mfem::InterpolationGridTransfer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, coarse_fes, fine_fes):
        r"""__init__(InterpolationGridTransfer self, FiniteElementSpace coarse_fes, FiniteElementSpace fine_fes) -> InterpolationGridTransfer"""
        _transfer.InterpolationGridTransfer_swiginit(self, _transfer.new_InterpolationGridTransfer(coarse_fes, fine_fes))
    __swig_destroy__ = _transfer.delete_InterpolationGridTransfer

    def SetMassIntegrator(self, mass_integ_, own_mass_integ_=True):
        r"""SetMassIntegrator(InterpolationGridTransfer self, BilinearFormIntegrator mass_integ_, bool own_mass_integ_=True)"""
        return _transfer.InterpolationGridTransfer_SetMassIntegrator(self, mass_integ_, own_mass_integ_)
    SetMassIntegrator = _swig_new_instance_method(_transfer.InterpolationGridTransfer_SetMassIntegrator)

    def ForwardOperator(self):
        r"""ForwardOperator(InterpolationGridTransfer self) -> Operator"""
        return _transfer.InterpolationGridTransfer_ForwardOperator(self)
    ForwardOperator = _swig_new_instance_method(_transfer.InterpolationGridTransfer_ForwardOperator)

    def BackwardOperator(self):
        r"""BackwardOperator(InterpolationGridTransfer self) -> Operator"""
        return _transfer.InterpolationGridTransfer_BackwardOperator(self)
    BackwardOperator = _swig_new_instance_method(_transfer.InterpolationGridTransfer_BackwardOperator)

# Register InterpolationGridTransfer in _transfer:
_transfer.InterpolationGridTransfer_swigregister(InterpolationGridTransfer)

class L2ProjectionGridTransfer(GridTransfer):
    r"""Proxy of C++ mfem::L2ProjectionGridTransfer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, coarse_fes_, fine_fes_, force_l2_space_=False):
        r"""__init__(L2ProjectionGridTransfer self, FiniteElementSpace coarse_fes_, FiniteElementSpace fine_fes_, bool force_l2_space_=False) -> L2ProjectionGridTransfer"""
        _transfer.L2ProjectionGridTransfer_swiginit(self, _transfer.new_L2ProjectionGridTransfer(coarse_fes_, fine_fes_, force_l2_space_))
    __swig_destroy__ = _transfer.delete_L2ProjectionGridTransfer

    def ForwardOperator(self):
        r"""ForwardOperator(L2ProjectionGridTransfer self) -> Operator"""
        return _transfer.L2ProjectionGridTransfer_ForwardOperator(self)
    ForwardOperator = _swig_new_instance_method(_transfer.L2ProjectionGridTransfer_ForwardOperator)

    def BackwardOperator(self):
        r"""BackwardOperator(L2ProjectionGridTransfer self) -> Operator"""
        return _transfer.L2ProjectionGridTransfer_BackwardOperator(self)
    BackwardOperator = _swig_new_instance_method(_transfer.L2ProjectionGridTransfer_BackwardOperator)

# Register L2ProjectionGridTransfer in _transfer:
_transfer.L2ProjectionGridTransfer_swigregister(L2ProjectionGridTransfer)

class TransferOperator(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::TransferOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, lFESpace, hFESpace):
        r"""__init__(TransferOperator self, FiniteElementSpace lFESpace, FiniteElementSpace hFESpace) -> TransferOperator"""
        _transfer.TransferOperator_swiginit(self, _transfer.new_TransferOperator(lFESpace, hFESpace))
    __swig_destroy__ = _transfer.delete_TransferOperator

    def Mult(self, x, y):
        r"""Mult(TransferOperator self, Vector x, Vector y)"""
        return _transfer.TransferOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_transfer.TransferOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(TransferOperator self, Vector x, Vector y)"""
        return _transfer.TransferOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_transfer.TransferOperator_MultTranspose)

# Register TransferOperator in _transfer:
_transfer.TransferOperator_swigregister(TransferOperator)

class PRefinementTransferOperator(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::PRefinementTransferOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, lFESpace_, hFESpace_):
        r"""__init__(PRefinementTransferOperator self, FiniteElementSpace lFESpace_, FiniteElementSpace hFESpace_) -> PRefinementTransferOperator"""
        _transfer.PRefinementTransferOperator_swiginit(self, _transfer.new_PRefinementTransferOperator(lFESpace_, hFESpace_))
    __swig_destroy__ = _transfer.delete_PRefinementTransferOperator

    def Mult(self, x, y):
        r"""Mult(PRefinementTransferOperator self, Vector x, Vector y)"""
        return _transfer.PRefinementTransferOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_transfer.PRefinementTransferOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(PRefinementTransferOperator self, Vector x, Vector y)"""
        return _transfer.PRefinementTransferOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_transfer.PRefinementTransferOperator_MultTranspose)

# Register PRefinementTransferOperator in _transfer:
_transfer.PRefinementTransferOperator_swigregister(PRefinementTransferOperator)

class TensorProductPRefinementTransferOperator(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::TensorProductPRefinementTransferOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, lFESpace_, hFESpace_):
        r"""__init__(TensorProductPRefinementTransferOperator self, FiniteElementSpace lFESpace_, FiniteElementSpace hFESpace_) -> TensorProductPRefinementTransferOperator"""
        _transfer.TensorProductPRefinementTransferOperator_swiginit(self, _transfer.new_TensorProductPRefinementTransferOperator(lFESpace_, hFESpace_))
    __swig_destroy__ = _transfer.delete_TensorProductPRefinementTransferOperator

    def Mult(self, x, y):
        r"""Mult(TensorProductPRefinementTransferOperator self, Vector x, Vector y)"""
        return _transfer.TensorProductPRefinementTransferOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_transfer.TensorProductPRefinementTransferOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(TensorProductPRefinementTransferOperator self, Vector x, Vector y)"""
        return _transfer.TensorProductPRefinementTransferOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_transfer.TensorProductPRefinementTransferOperator_MultTranspose)

# Register TensorProductPRefinementTransferOperator in _transfer:
_transfer.TensorProductPRefinementTransferOperator_swigregister(TensorProductPRefinementTransferOperator)

class TrueTransferOperator(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::TrueTransferOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, lFESpace_, hFESpace_):
        r"""__init__(TrueTransferOperator self, FiniteElementSpace lFESpace_, FiniteElementSpace hFESpace_) -> TrueTransferOperator"""
        _transfer.TrueTransferOperator_swiginit(self, _transfer.new_TrueTransferOperator(lFESpace_, hFESpace_))
    __swig_destroy__ = _transfer.delete_TrueTransferOperator

    def Mult(self, x, y):
        r"""Mult(TrueTransferOperator self, Vector x, Vector y)"""
        return _transfer.TrueTransferOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_transfer.TrueTransferOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(TrueTransferOperator self, Vector x, Vector y)"""
        return _transfer.TrueTransferOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_transfer.TrueTransferOperator_MultTranspose)

# Register TrueTransferOperator in _transfer:
_transfer.TrueTransferOperator_swigregister(TrueTransferOperator)



