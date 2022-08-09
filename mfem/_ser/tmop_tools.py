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
    from . import _tmop_tools
else:
    import _tmop_tools

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _tmop_tools.SWIG_PyInstanceMethod_New
_swig_new_static_method = _tmop_tools.SWIG_PyStaticMethod_New

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

import mfem._ser.tmop
import mfem._ser.intrules
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.gridfunc
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.symmat
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
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.std_vectors
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.bilinearform
import mfem._ser.solvers
class AdvectorCG(mfem._ser.tmop.AdaptivityEvaluator):
    r"""Proxy of C++ mfem::AdvectorCG class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(AdvectorCG self, mfem::AssemblyLevel al=LEGACY, double timestep_scale=0.5) -> AdvectorCG"""
        _tmop_tools.AdvectorCG_swiginit(self, _tmop_tools.new_AdvectorCG(*args, **kwargs))

    def SetInitialField(self, init_nodes, init_field):
        r"""SetInitialField(AdvectorCG self, Vector init_nodes, Vector init_field)"""
        return _tmop_tools.AdvectorCG_SetInitialField(self, init_nodes, init_field)
    SetInitialField = _swig_new_instance_method(_tmop_tools.AdvectorCG_SetInitialField)

    def ComputeAtNewPosition(self, new_nodes, new_field):
        r"""ComputeAtNewPosition(AdvectorCG self, Vector new_nodes, Vector new_field)"""
        return _tmop_tools.AdvectorCG_ComputeAtNewPosition(self, new_nodes, new_field)
    ComputeAtNewPosition = _swig_new_instance_method(_tmop_tools.AdvectorCG_ComputeAtNewPosition)

    def SetMemoryType(self, mt):
        r"""SetMemoryType(AdvectorCG self, mfem::MemoryType mt)"""
        return _tmop_tools.AdvectorCG_SetMemoryType(self, mt)
    SetMemoryType = _swig_new_instance_method(_tmop_tools.AdvectorCG_SetMemoryType)
    __swig_destroy__ = _tmop_tools.delete_AdvectorCG

# Register AdvectorCG in _tmop_tools:
_tmop_tools.AdvectorCG_swigregister(AdvectorCG)

class InterpolatorFP(mfem._ser.tmop.AdaptivityEvaluator):
    r"""Proxy of C++ mfem::InterpolatorFP class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(InterpolatorFP self) -> InterpolatorFP"""
        _tmop_tools.InterpolatorFP_swiginit(self, _tmop_tools.new_InterpolatorFP())

    def SetInitialField(self, init_nodes, init_field):
        r"""SetInitialField(InterpolatorFP self, Vector init_nodes, Vector init_field)"""
        return _tmop_tools.InterpolatorFP_SetInitialField(self, init_nodes, init_field)
    SetInitialField = _swig_new_instance_method(_tmop_tools.InterpolatorFP_SetInitialField)

    def ComputeAtNewPosition(self, new_nodes, new_field):
        r"""ComputeAtNewPosition(InterpolatorFP self, Vector new_nodes, Vector new_field)"""
        return _tmop_tools.InterpolatorFP_ComputeAtNewPosition(self, new_nodes, new_field)
    ComputeAtNewPosition = _swig_new_instance_method(_tmop_tools.InterpolatorFP_ComputeAtNewPosition)
    __swig_destroy__ = _tmop_tools.delete_InterpolatorFP

# Register InterpolatorFP in _tmop_tools:
_tmop_tools.InterpolatorFP_swigregister(InterpolatorFP)

class SerialAdvectorCGOper(mfem._ser.operators.TimeDependentOperator):
    r"""Proxy of C++ mfem::SerialAdvectorCGOper class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(SerialAdvectorCGOper self, Vector x_start, GridFunction vel, FiniteElementSpace fes, mfem::AssemblyLevel al=LEGACY) -> SerialAdvectorCGOper"""
        _tmop_tools.SerialAdvectorCGOper_swiginit(self, _tmop_tools.new_SerialAdvectorCGOper(*args, **kwargs))

    def Mult(self, ind, di_dt):
        r"""Mult(SerialAdvectorCGOper self, Vector ind, Vector di_dt)"""
        return _tmop_tools.SerialAdvectorCGOper_Mult(self, ind, di_dt)
    Mult = _swig_new_instance_method(_tmop_tools.SerialAdvectorCGOper_Mult)
    __swig_destroy__ = _tmop_tools.delete_SerialAdvectorCGOper

# Register SerialAdvectorCGOper in _tmop_tools:
_tmop_tools.SerialAdvectorCGOper_swigregister(SerialAdvectorCGOper)

class TMOPNewtonSolver(mfem._ser.solvers.LBFGSSolver):
    r"""Proxy of C++ mfem::TMOPNewtonSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, irule, type=0):
        r"""__init__(TMOPNewtonSolver self, IntegrationRule irule, int type=0) -> TMOPNewtonSolver"""
        _tmop_tools.TMOPNewtonSolver_swiginit(self, _tmop_tools.new_TMOPNewtonSolver(irule, type))

    def SetIntegrationRules(self, irules, order):
        r"""SetIntegrationRules(TMOPNewtonSolver self, IntegrationRules irules, int order)"""
        return _tmop_tools.TMOPNewtonSolver_SetIntegrationRules(self, irules, order)
    SetIntegrationRules = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetIntegrationRules)

    def SetMinDetPtr(self, md_ptr):
        r"""SetMinDetPtr(TMOPNewtonSolver self, double * md_ptr)"""
        return _tmop_tools.TMOPNewtonSolver_SetMinDetPtr(self, md_ptr)
    SetMinDetPtr = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetMinDetPtr)

    def SetTempMemoryType(self, mt):
        r"""SetTempMemoryType(TMOPNewtonSolver self, mfem::MemoryType mt)"""
        return _tmop_tools.TMOPNewtonSolver_SetTempMemoryType(self, mt)
    SetTempMemoryType = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetTempMemoryType)

    def ComputeScalingFactor(self, x, b):
        r"""ComputeScalingFactor(TMOPNewtonSolver self, Vector x, Vector b) -> double"""
        return _tmop_tools.TMOPNewtonSolver_ComputeScalingFactor(self, x, b)
    ComputeScalingFactor = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_ComputeScalingFactor)

    def ProcessNewState(self, x):
        r"""ProcessNewState(TMOPNewtonSolver self, Vector x)"""
        return _tmop_tools.TMOPNewtonSolver_ProcessNewState(self, x)
    ProcessNewState = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_ProcessNewState)

    def EnableAdaptiveSurfaceFitting(self):
        r"""EnableAdaptiveSurfaceFitting(TMOPNewtonSolver self)"""
        return _tmop_tools.TMOPNewtonSolver_EnableAdaptiveSurfaceFitting(self)
    EnableAdaptiveSurfaceFitting = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_EnableAdaptiveSurfaceFitting)

    def SetTerminationWithMaxSurfaceFittingError(self, max_error):
        r"""SetTerminationWithMaxSurfaceFittingError(TMOPNewtonSolver self, double max_error)"""
        return _tmop_tools.TMOPNewtonSolver_SetTerminationWithMaxSurfaceFittingError(self, max_error)
    SetTerminationWithMaxSurfaceFittingError = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetTerminationWithMaxSurfaceFittingError)

    def Mult(self, b, x):
        r"""Mult(TMOPNewtonSolver self, Vector b, Vector x)"""
        return _tmop_tools.TMOPNewtonSolver_Mult(self, b, x)
    Mult = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_Mult)

    def SetSolver(self, solver):
        r"""SetSolver(TMOPNewtonSolver self, Solver solver)"""
        return _tmop_tools.TMOPNewtonSolver_SetSolver(self, solver)
    SetSolver = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetSolver)

    def SetPreconditioner(self, pr):
        r"""SetPreconditioner(TMOPNewtonSolver self, Solver pr)"""
        return _tmop_tools.TMOPNewtonSolver_SetPreconditioner(self, pr)
    SetPreconditioner = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetPreconditioner)
    __swig_destroy__ = _tmop_tools.delete_TMOPNewtonSolver

# Register TMOPNewtonSolver in _tmop_tools:
_tmop_tools.TMOPNewtonSolver_swigregister(TMOPNewtonSolver)


def vis_tmop_metric_s(order, qm, tc, pmesh, title, position):
    r"""vis_tmop_metric_s(int order, TMOP_QualityMetric qm, TargetConstructor tc, Mesh pmesh, char * title, int position)"""
    return _tmop_tools.vis_tmop_metric_s(order, qm, tc, pmesh, title, position)
vis_tmop_metric_s = _tmop_tools.vis_tmop_metric_s


