# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
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

MFEM_VERSION = _tmop_tools.MFEM_VERSION
MFEM_VERSION_STRING = _tmop_tools.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _tmop_tools.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _tmop_tools.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _tmop_tools.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _tmop_tools.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _tmop_tools.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _tmop_tools.MFEM_VERSION_PATCH
import mfem._par.tmop
import mfem._par.intrules
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.globals
import mfem._par.gridfunc
import mfem._par.vector
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.operators
import mfem._par.symmat
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
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
import mfem._par.fespace
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.std_vectors
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.bilinearform
import mfem._par.pbilinearform
import mfem._par.pfespace
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
import mfem._par.solvers
class AdvectorCG(mfem._par.tmop.AdaptivityEvaluator):
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

    def ComputeAtNewPosition(self, *args, **kwargs):
        r"""ComputeAtNewPosition(AdvectorCG self, Vector new_nodes, Vector new_field, int new_nodes_ordering=byNODES)"""
        return _tmop_tools.AdvectorCG_ComputeAtNewPosition(self, *args, **kwargs)
    ComputeAtNewPosition = _swig_new_instance_method(_tmop_tools.AdvectorCG_ComputeAtNewPosition)

    def SetMemoryType(self, mt):
        r"""SetMemoryType(AdvectorCG self, mfem::MemoryType mt)"""
        return _tmop_tools.AdvectorCG_SetMemoryType(self, mt)
    SetMemoryType = _swig_new_instance_method(_tmop_tools.AdvectorCG_SetMemoryType)
    __swig_destroy__ = _tmop_tools.delete_AdvectorCG

# Register AdvectorCG in _tmop_tools:
_tmop_tools.AdvectorCG_swigregister(AdvectorCG)
class SerialAdvectorCGOper(mfem._par.operators.TimeDependentOperator):
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
class ParAdvectorCGOper(mfem._par.operators.TimeDependentOperator):
    r"""Proxy of C++ mfem::ParAdvectorCGOper class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(ParAdvectorCGOper self, Vector x_start, GridFunction vel, ParFiniteElementSpace pfes, mfem::AssemblyLevel al=LEGACY, mfem::MemoryType mt=DEFAULT) -> ParAdvectorCGOper"""
        _tmop_tools.ParAdvectorCGOper_swiginit(self, _tmop_tools.new_ParAdvectorCGOper(*args, **kwargs))

    def Mult(self, ind, di_dt):
        r"""Mult(ParAdvectorCGOper self, Vector ind, Vector di_dt)"""
        return _tmop_tools.ParAdvectorCGOper_Mult(self, ind, di_dt)
    Mult = _swig_new_instance_method(_tmop_tools.ParAdvectorCGOper_Mult)
    __swig_destroy__ = _tmop_tools.delete_ParAdvectorCGOper

# Register ParAdvectorCGOper in _tmop_tools:
_tmop_tools.ParAdvectorCGOper_swigregister(ParAdvectorCGOper)
class TMOPNewtonSolver(mfem._par.solvers.LBFGSSolver):
    r"""Proxy of C++ mfem::TMOPNewtonSolver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(TMOPNewtonSolver self, MPI_Comm comm, IntegrationRule irule, int type=0) -> TMOPNewtonSolver
        __init__(TMOPNewtonSolver self, IntegrationRule irule, int type=0) -> TMOPNewtonSolver
        """
        _tmop_tools.TMOPNewtonSolver_swiginit(self, _tmop_tools.new_TMOPNewtonSolver(*args))

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

    def SetAdaptiveSurfaceFittingScalingFactor(self, factor):
        r"""SetAdaptiveSurfaceFittingScalingFactor(TMOPNewtonSolver self, double factor)"""
        return _tmop_tools.TMOPNewtonSolver_SetAdaptiveSurfaceFittingScalingFactor(self, factor)
    SetAdaptiveSurfaceFittingScalingFactor = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetAdaptiveSurfaceFittingScalingFactor)

    def SetAdaptiveSurfaceFittingRelativeChangeThreshold(self, threshold):
        r"""SetAdaptiveSurfaceFittingRelativeChangeThreshold(TMOPNewtonSolver self, double threshold)"""
        return _tmop_tools.TMOPNewtonSolver_SetAdaptiveSurfaceFittingRelativeChangeThreshold(self, threshold)
    SetAdaptiveSurfaceFittingRelativeChangeThreshold = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetAdaptiveSurfaceFittingRelativeChangeThreshold)

    def SetMaxNumberofIncrementsForAdaptiveFitting(self, count):
        r"""SetMaxNumberofIncrementsForAdaptiveFitting(TMOPNewtonSolver self, int count)"""
        return _tmop_tools.TMOPNewtonSolver_SetMaxNumberofIncrementsForAdaptiveFitting(self, count)
    SetMaxNumberofIncrementsForAdaptiveFitting = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetMaxNumberofIncrementsForAdaptiveFitting)

    def SetTerminationWithMaxSurfaceFittingError(self, max_error):
        r"""SetTerminationWithMaxSurfaceFittingError(TMOPNewtonSolver self, double max_error)"""
        return _tmop_tools.TMOPNewtonSolver_SetTerminationWithMaxSurfaceFittingError(self, max_error)
    SetTerminationWithMaxSurfaceFittingError = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetTerminationWithMaxSurfaceFittingError)

    def SetMinimumDeterminantThreshold(self, threshold):
        r"""SetMinimumDeterminantThreshold(TMOPNewtonSolver self, double threshold)"""
        return _tmop_tools.TMOPNewtonSolver_SetMinimumDeterminantThreshold(self, threshold)
    SetMinimumDeterminantThreshold = _swig_new_instance_method(_tmop_tools.TMOPNewtonSolver_SetMinimumDeterminantThreshold)

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

def vis_tmop_metric_p(order, qm, tc, pmesh, title, position):
    r"""vis_tmop_metric_p(int order, TMOP_QualityMetric qm, TargetConstructor tc, ParMesh pmesh, char * title, int position)"""
    return _tmop_tools.vis_tmop_metric_p(order, qm, tc, pmesh, title, position)
vis_tmop_metric_p = _tmop_tools.vis_tmop_metric_p
