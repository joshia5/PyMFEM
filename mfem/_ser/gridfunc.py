# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_gridfunc')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_gridfunc')
    _gridfunc = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gridfunc', [dirname(__file__)])
        except ImportError:
            import _gridfunc
            return _gridfunc
        try:
            _mod = imp.load_module('_gridfunc', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _gridfunc = swig_import_helper()
    del swig_import_helper
else:
    import _gridfunc
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _gridfunc.new_intp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gridfunc.delete_intp
    __del__ = lambda self: None

    def assign(self, value):
        return _gridfunc.intp_assign(self, value)

    def value(self):
        return _gridfunc.intp_value(self)

    def cast(self):
        return _gridfunc.intp_cast(self)
    if _newclass:
        frompointer = staticmethod(_gridfunc.intp_frompointer)
    else:
        frompointer = _gridfunc.intp_frompointer
intp_swigregister = _gridfunc.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t):
    return _gridfunc.intp_frompointer(t)
intp_frompointer = _gridfunc.intp_frompointer

class doublep(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doublep, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doublep, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _gridfunc.new_doublep()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gridfunc.delete_doublep
    __del__ = lambda self: None

    def assign(self, value):
        return _gridfunc.doublep_assign(self, value)

    def value(self):
        return _gridfunc.doublep_value(self)

    def cast(self):
        return _gridfunc.doublep_cast(self)
    if _newclass:
        frompointer = staticmethod(_gridfunc.doublep_frompointer)
    else:
        frompointer = _gridfunc.doublep_frompointer
doublep_swigregister = _gridfunc.doublep_swigregister
doublep_swigregister(doublep)

def doublep_frompointer(t):
    return _gridfunc.doublep_frompointer(t)
doublep_frompointer = _gridfunc.doublep_frompointer

import mfem._ser.array
import mfem._ser.ostream_typemap
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.mesh
import mfem._ser.ncmesh
import mfem._ser.element
import mfem._ser.geom
import mfem._ser.table
import mfem._ser.vertex
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.handle
import mfem._ser.bilininteg
import mfem._ser.linearform
class GridFunction(mfem._ser.vector.Vector):
    """Proxy of C++ mfem::GridFunction class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.vector.Vector]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GridFunction, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.vector.Vector]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GridFunction, name)
    __repr__ = _swig_repr

    def MakeOwner(self, _fec):
        """MakeOwner(GridFunction self, FiniteElementCollection _fec)"""
        return _gridfunc.GridFunction_MakeOwner(self, _fec)


    def OwnFEC(self):
        """OwnFEC(GridFunction self) -> FiniteElementCollection"""
        return _gridfunc.GridFunction_OwnFEC(self)


    def VectorDim(self):
        """VectorDim(GridFunction self) -> int"""
        return _gridfunc.GridFunction_VectorDim(self)


    def GetTrueVector(self, *args):
        """
        GetTrueVector(GridFunction self) -> Vector
        GetTrueVector(GridFunction self) -> Vector
        """
        return _gridfunc.GridFunction_GetTrueVector(self, *args)


    def GetTrueDofs(self, tv):
        """GetTrueDofs(GridFunction self, Vector tv)"""
        return _gridfunc.GridFunction_GetTrueDofs(self, tv)


    def SetTrueVector(self):
        """SetTrueVector(GridFunction self)"""
        return _gridfunc.GridFunction_SetTrueVector(self)


    def SetFromTrueDofs(self, tv):
        """SetFromTrueDofs(GridFunction self, Vector tv)"""
        return _gridfunc.GridFunction_SetFromTrueDofs(self, tv)


    def SetFromTrueVector(self):
        """SetFromTrueVector(GridFunction self)"""
        return _gridfunc.GridFunction_SetFromTrueVector(self)


    def GetValue(self, i, ip, vdim=1):
        """
        GetValue(GridFunction self, int i, IntegrationPoint ip, int vdim=1) -> double
        GetValue(GridFunction self, int i, IntegrationPoint ip) -> double
        """
        return _gridfunc.GridFunction_GetValue(self, i, ip, vdim)


    def GetVectorValue(self, i, ip, val):
        """GetVectorValue(GridFunction self, int i, IntegrationPoint ip, Vector val)"""
        return _gridfunc.GridFunction_GetVectorValue(self, i, ip, val)


    def GetValues(self, *args):
        """
        GetValues(GridFunction self, int i, IntegrationRule ir, Vector vals, int vdim=1)
        GetValues(GridFunction self, int i, IntegrationRule ir, Vector vals)
        GetValues(GridFunction self, int i, IntegrationRule ir, Vector vals, DenseMatrix tr, int vdim=1)
        GetValues(GridFunction self, int i, IntegrationRule ir, Vector vals, DenseMatrix tr)
        """
        return _gridfunc.GridFunction_GetValues(self, *args)


    def GetFaceValues(self, i, side, ir, vals, tr, vdim=1):
        """
        GetFaceValues(GridFunction self, int i, int side, IntegrationRule ir, Vector vals, DenseMatrix tr, int vdim=1) -> int
        GetFaceValues(GridFunction self, int i, int side, IntegrationRule ir, Vector vals, DenseMatrix tr) -> int
        """
        return _gridfunc.GridFunction_GetFaceValues(self, i, side, ir, vals, tr, vdim)


    def GetVectorValues(self, *args):
        """
        GetVectorValues(GridFunction self, ElementTransformation T, IntegrationRule ir, DenseMatrix vals)
        GetVectorValues(GridFunction self, int i, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr)
        """
        return _gridfunc.GridFunction_GetVectorValues(self, *args)


    def GetFaceVectorValues(self, i, side, ir, vals, tr):
        """GetFaceVectorValues(GridFunction self, int i, int side, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr) -> int"""
        return _gridfunc.GridFunction_GetFaceVectorValues(self, i, side, ir, vals, tr)


    def GetValuesFrom(self, orig_func):
        """GetValuesFrom(GridFunction self, GridFunction orig_func)"""
        return _gridfunc.GridFunction_GetValuesFrom(self, orig_func)


    def GetBdrValuesFrom(self, orig_func):
        """GetBdrValuesFrom(GridFunction self, GridFunction orig_func)"""
        return _gridfunc.GridFunction_GetBdrValuesFrom(self, orig_func)


    def GetVectorFieldValues(self, i, ir, vals, tr, comp=0):
        """
        GetVectorFieldValues(GridFunction self, int i, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr, int comp=0)
        GetVectorFieldValues(GridFunction self, int i, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr)
        """
        return _gridfunc.GridFunction_GetVectorFieldValues(self, i, ir, vals, tr, comp)


    def ReorderByNodes(self):
        """ReorderByNodes(GridFunction self)"""
        return _gridfunc.GridFunction_ReorderByNodes(self)


    def GetNodalValues(self, *args):
        '''
        GetNodalValues(i)   ->   GetNodalValues(vector, vdim)
        GetNodalValues(i, array<dobule>, vdim)
        '''
        from .vector import Vector
        if len(args) == 1:
            vec = Vector()
            _gridfunc.GridFunction_GetNodalValues(self, vec, args[0])
            vec.thisown = 0
            return vec.GetDataArray()
        else:
            return _gridfunc.GridFunction_GetNodalValues(self, *args)



    def GetVectorFieldNodalValues(self, val, comp):
        """GetVectorFieldNodalValues(GridFunction self, Vector val, int comp)"""
        return _gridfunc.GridFunction_GetVectorFieldNodalValues(self, val, comp)


    def ProjectVectorFieldOn(self, vec_field, comp=0):
        """
        ProjectVectorFieldOn(GridFunction self, GridFunction vec_field, int comp=0)
        ProjectVectorFieldOn(GridFunction self, GridFunction vec_field)
        """
        return _gridfunc.GridFunction_ProjectVectorFieldOn(self, vec_field, comp)


    def GetDerivative(self, comp, der_comp, der):
        """GetDerivative(GridFunction self, int comp, int der_comp, GridFunction der)"""
        return _gridfunc.GridFunction_GetDerivative(self, comp, der_comp, der)


    def GetDivergence(self, tr):
        """GetDivergence(GridFunction self, ElementTransformation tr) -> double"""
        return _gridfunc.GridFunction_GetDivergence(self, tr)


    def GetCurl(self, tr, curl):
        """GetCurl(GridFunction self, ElementTransformation tr, Vector curl)"""
        return _gridfunc.GridFunction_GetCurl(self, tr, curl)


    def GetGradient(self, tr, grad):
        """GetGradient(GridFunction self, ElementTransformation tr, Vector grad)"""
        return _gridfunc.GridFunction_GetGradient(self, tr, grad)


    def GetGradients(self, *args):
        """
        GetGradients(GridFunction self, ElementTransformation tr, IntegrationRule ir, DenseMatrix grad)
        GetGradients(GridFunction self, int const elem, IntegrationRule ir, DenseMatrix grad)
        """
        return _gridfunc.GridFunction_GetGradients(self, *args)


    def GetVectorGradient(self, tr, grad):
        """GetVectorGradient(GridFunction self, ElementTransformation tr, DenseMatrix grad)"""
        return _gridfunc.GridFunction_GetVectorGradient(self, tr, grad)


    def GetElementAverages(self, avgs):
        """GetElementAverages(GridFunction self, GridFunction avgs)"""
        return _gridfunc.GridFunction_GetElementAverages(self, avgs)


    def ImposeBounds(self, *args):
        """
        ImposeBounds(GridFunction self, int i, Vector weights, Vector _lo, Vector _hi)
        ImposeBounds(GridFunction self, int i, Vector weights, double _min=0.0, double _max)
        ImposeBounds(GridFunction self, int i, Vector weights, double _min=0.0)
        ImposeBounds(GridFunction self, int i, Vector weights)
        """
        return _gridfunc.GridFunction_ImposeBounds(self, *args)


    def ProjectGridFunction(self, src):
        """ProjectGridFunction(GridFunction self, GridFunction src)"""
        return _gridfunc.GridFunction_ProjectGridFunction(self, src)


    def ProjectCoefficient(self, *args):
        """
        ProjectCoefficient(GridFunction self, Coefficient coeff)
        ProjectCoefficient(GridFunction self, Coefficient coeff, intArray dofs, int vd=0)
        ProjectCoefficient(GridFunction self, Coefficient coeff, intArray dofs)
        ProjectCoefficient(GridFunction self, VectorCoefficient vcoeff)
        ProjectCoefficient(GridFunction self, VectorCoefficient vcoeff, intArray dofs)
        ProjectCoefficient(GridFunction self, mfem::Coefficient *[] coeff)
        """
        return _gridfunc.GridFunction_ProjectCoefficient(self, *args)

    ARITHMETIC = _gridfunc.GridFunction_ARITHMETIC
    HARMONIC = _gridfunc.GridFunction_HARMONIC

    def ProjectDiscCoefficient(self, *args):
        """
        ProjectDiscCoefficient(GridFunction self, VectorCoefficient coeff)
        ProjectDiscCoefficient(GridFunction self, Coefficient coeff, mfem::GridFunction::AvgType type)
        ProjectDiscCoefficient(GridFunction self, VectorCoefficient coeff, mfem::GridFunction::AvgType type)
        """
        return _gridfunc.GridFunction_ProjectDiscCoefficient(self, *args)


    def ProjectBdrCoefficient(self, *args):
        """
        ProjectBdrCoefficient(GridFunction self, Coefficient coeff, intArray attr)
        ProjectBdrCoefficient(GridFunction self, VectorCoefficient vcoeff, intArray attr)
        ProjectBdrCoefficient(GridFunction self, mfem::Coefficient *[] coeff, intArray attr)
        """
        return _gridfunc.GridFunction_ProjectBdrCoefficient(self, *args)


    def ProjectBdrCoefficientNormal(self, vcoeff, bdr_attr):
        """ProjectBdrCoefficientNormal(GridFunction self, VectorCoefficient vcoeff, intArray bdr_attr)"""
        return _gridfunc.GridFunction_ProjectBdrCoefficientNormal(self, vcoeff, bdr_attr)


    def ProjectBdrCoefficientTangent(self, vcoeff, bdr_attr):
        """ProjectBdrCoefficientTangent(GridFunction self, VectorCoefficient vcoeff, intArray bdr_attr)"""
        return _gridfunc.GridFunction_ProjectBdrCoefficientTangent(self, vcoeff, bdr_attr)


    def ComputeL2Error(self, *args):
        """
        ComputeL2Error(GridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(GridFunction self, Coefficient exsol) -> double
        ComputeL2Error(GridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(GridFunction self, mfem::Coefficient *[] exsol) -> double
        ComputeL2Error(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0, intArray elems=None) -> double
        ComputeL2Error(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(GridFunction self, VectorCoefficient exsol) -> double
        """
        return _gridfunc.GridFunction_ComputeL2Error(self, *args)


    def ComputeH1Error(self, exsol, exgrad, ell_coef, Nu, norm_type):
        """ComputeH1Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, Coefficient ell_coef, double Nu, int norm_type) -> double"""
        return _gridfunc.GridFunction_ComputeH1Error(self, exsol, exgrad, ell_coef, Nu, norm_type)


    def ComputeMaxError(self, *args):
        """
        ComputeMaxError(GridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(GridFunction self, Coefficient exsol) -> double
        ComputeMaxError(GridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(GridFunction self, mfem::Coefficient *[] exsol) -> double
        ComputeMaxError(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(GridFunction self, VectorCoefficient exsol) -> double
        """
        return _gridfunc.GridFunction_ComputeMaxError(self, *args)


    def ComputeW11Error(self, exsol, exgrad, norm_type, elems=None, irs=0):
        """
        ComputeW11Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, int norm_type, intArray elems=None, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeW11Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, int norm_type, intArray elems=None) -> double
        ComputeW11Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, int norm_type) -> double
        """
        return _gridfunc.GridFunction_ComputeW11Error(self, exsol, exgrad, norm_type, elems, irs)


    def ComputeL1Error(self, *args):
        """
        ComputeL1Error(GridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL1Error(GridFunction self, Coefficient exsol) -> double
        ComputeL1Error(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL1Error(GridFunction self, VectorCoefficient exsol) -> double
        """
        return _gridfunc.GridFunction_ComputeL1Error(self, *args)


    def ComputeLpError(self, *args):
        """
        ComputeLpError(GridFunction self, double const p, Coefficient exsol, Coefficient weight=None, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeLpError(GridFunction self, double const p, Coefficient exsol, Coefficient weight=None) -> double
        ComputeLpError(GridFunction self, double const p, Coefficient exsol) -> double
        ComputeLpError(GridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None, VectorCoefficient v_weight=None, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeLpError(GridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None, VectorCoefficient v_weight=None) -> double
        ComputeLpError(GridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None) -> double
        ComputeLpError(GridFunction self, double const p, VectorCoefficient exsol) -> double
        """
        return _gridfunc.GridFunction_ComputeLpError(self, *args)


    def ComputeElementLpErrors(self, *args):
        """
        ComputeElementLpErrors(GridFunction self, double const p, Coefficient exsol, GridFunction error, Coefficient weight=None, mfem::IntegrationRule const *[] irs=0)
        ComputeElementLpErrors(GridFunction self, double const p, Coefficient exsol, GridFunction error, Coefficient weight=None)
        ComputeElementLpErrors(GridFunction self, double const p, Coefficient exsol, GridFunction error)
        ComputeElementLpErrors(GridFunction self, double const p, VectorCoefficient exsol, GridFunction error, Coefficient weight=None, VectorCoefficient v_weight=None, mfem::IntegrationRule const *[] irs=0)
        ComputeElementLpErrors(GridFunction self, double const p, VectorCoefficient exsol, GridFunction error, Coefficient weight=None, VectorCoefficient v_weight=None)
        ComputeElementLpErrors(GridFunction self, double const p, VectorCoefficient exsol, GridFunction error, Coefficient weight=None)
        ComputeElementLpErrors(GridFunction self, double const p, VectorCoefficient exsol, GridFunction error)
        """
        return _gridfunc.GridFunction_ComputeElementLpErrors(self, *args)


    def ComputeElementL1Errors(self, *args):
        """
        ComputeElementL1Errors(GridFunction self, Coefficient exsol, GridFunction error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementL1Errors(GridFunction self, Coefficient exsol, GridFunction error)
        ComputeElementL1Errors(GridFunction self, VectorCoefficient exsol, GridFunction error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementL1Errors(GridFunction self, VectorCoefficient exsol, GridFunction error)
        """
        return _gridfunc.GridFunction_ComputeElementL1Errors(self, *args)


    def ComputeElementL2Errors(self, *args):
        """
        ComputeElementL2Errors(GridFunction self, Coefficient exsol, GridFunction error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementL2Errors(GridFunction self, Coefficient exsol, GridFunction error)
        ComputeElementL2Errors(GridFunction self, VectorCoefficient exsol, GridFunction error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementL2Errors(GridFunction self, VectorCoefficient exsol, GridFunction error)
        """
        return _gridfunc.GridFunction_ComputeElementL2Errors(self, *args)


    def ComputeElementMaxErrors(self, *args):
        """
        ComputeElementMaxErrors(GridFunction self, Coefficient exsol, GridFunction error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementMaxErrors(GridFunction self, Coefficient exsol, GridFunction error)
        ComputeElementMaxErrors(GridFunction self, VectorCoefficient exsol, GridFunction error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementMaxErrors(GridFunction self, VectorCoefficient exsol, GridFunction error)
        """
        return _gridfunc.GridFunction_ComputeElementMaxErrors(self, *args)


    def ComputeFlux(self, blfi, flux, wcoef=1, subdomain=-1):
        """
        ComputeFlux(GridFunction self, BilinearFormIntegrator blfi, GridFunction flux, int wcoef=1, int subdomain=-1)
        ComputeFlux(GridFunction self, BilinearFormIntegrator blfi, GridFunction flux, int wcoef=1)
        ComputeFlux(GridFunction self, BilinearFormIntegrator blfi, GridFunction flux)
        """
        return _gridfunc.GridFunction_ComputeFlux(self, blfi, flux, wcoef, subdomain)


    def Assign(self, *args):
        """
        Assign(GridFunction self, GridFunction rhs) -> GridFunction
        Assign(GridFunction self, double value) -> GridFunction
        Assign(GridFunction self, Vector v) -> GridFunction
        """
        return _gridfunc.GridFunction_Assign(self, *args)


    def Update(self):
        """Update(GridFunction self)"""
        return _gridfunc.GridFunction_Update(self)


    def FESpace(self, *args):
        """
        FESpace(GridFunction self) -> FiniteElementSpace
        FESpace(GridFunction self) -> FiniteElementSpace
        """
        return _gridfunc.GridFunction_FESpace(self, *args)


    def SetSpace(self, f):
        """SetSpace(GridFunction self, FiniteElementSpace f)"""
        return _gridfunc.GridFunction_SetSpace(self, f)


    def MakeRef(self, *args):
        """
        MakeRef(GridFunction self, FiniteElementSpace f, double * v)
        MakeRef(GridFunction self, FiniteElementSpace f, Vector v, int v_offset)
        """
        return _gridfunc.GridFunction_MakeRef(self, *args)


    def MakeTRef(self, *args):
        """
        MakeTRef(GridFunction self, FiniteElementSpace f, double * tv)
        MakeTRef(GridFunction self, FiniteElementSpace f, Vector tv, int tv_offset)
        """
        return _gridfunc.GridFunction_MakeTRef(self, *args)


    def Save(self, out):
        """Save(GridFunction self, std::ostream & out)"""
        return _gridfunc.GridFunction_Save(self, out)


    def SaveVTK(self, out, field_name, ref):
        """SaveVTK(GridFunction self, std::ostream & out, std::string const & field_name, int ref)"""
        return _gridfunc.GridFunction_SaveVTK(self, out, field_name, ref)


    def SaveSTL(self, out, TimesToRefine=1):
        """
        SaveSTL(GridFunction self, std::ostream & out, int TimesToRefine=1)
        SaveSTL(GridFunction self, std::ostream & out)
        """
        return _gridfunc.GridFunction_SaveSTL(self, out, TimesToRefine)

    __swig_destroy__ = _gridfunc.delete_GridFunction
    __del__ = lambda self: None

    def __init__(self, *args):
        """
        __init__(mfem::GridFunction self) -> GridFunction
        __init__(mfem::GridFunction self, GridFunction orig) -> GridFunction
        __init__(mfem::GridFunction self, FiniteElementSpace f) -> GridFunction
        __init__(mfem::GridFunction self, FiniteElementSpace f, double * data) -> GridFunction
        __init__(mfem::GridFunction self, Mesh m, std::istream & input) -> GridFunction
        __init__(mfem::GridFunction self, Mesh m, mfem::GridFunction *[] gf_array, int num_pieces) -> GridFunction
        __init__(mfem::GridFunction self, Mesh m, char const * grid_file) -> GridFunction
        __init__(mfem::GridFunction self, FiniteElementSpace fes, Vector v, int offset) -> GridFunction
        """
        this = _gridfunc.new_GridFunction(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SaveToFile(self, gf_file, precision):
        """SaveToFile(GridFunction self, char const * gf_file, int const precision)"""
        return _gridfunc.GridFunction_SaveToFile(self, gf_file, precision)


    def iadd(self, c):
        """iadd(GridFunction self, GridFunction c) -> GridFunction"""
        return _gridfunc.GridFunction_iadd(self, c)


    def isub(self, *args):
        """
        isub(GridFunction self, GridFunction c) -> GridFunction
        isub(GridFunction self, double c) -> GridFunction
        """
        return _gridfunc.GridFunction_isub(self, *args)


    def imul(self, c):
        """imul(GridFunction self, double c) -> GridFunction"""
        return _gridfunc.GridFunction_imul(self, c)


    def idiv(self, c):
        """idiv(GridFunction self, double c) -> GridFunction"""
        return _gridfunc.GridFunction_idiv(self, c)

GridFunction_swigregister = _gridfunc.GridFunction_swigregister
GridFunction_swigregister(GridFunction)

class QuadratureFunction(mfem._ser.vector.Vector):
    """Proxy of C++ mfem::QuadratureFunction class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.vector.Vector]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuadratureFunction, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.vector.Vector]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, QuadratureFunction, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::QuadratureFunction self) -> QuadratureFunction
        __init__(mfem::QuadratureFunction self, QuadratureFunction orig) -> QuadratureFunction
        __init__(mfem::QuadratureFunction self, QuadratureSpace qspace_, int vdim_=1) -> QuadratureFunction
        __init__(mfem::QuadratureFunction self, QuadratureSpace qspace_) -> QuadratureFunction
        __init__(mfem::QuadratureFunction self, QuadratureSpace qspace_, double * qf_data, int vdim_=1) -> QuadratureFunction
        __init__(mfem::QuadratureFunction self, QuadratureSpace qspace_, double * qf_data) -> QuadratureFunction
        __init__(mfem::QuadratureFunction self, Mesh mesh, std::istream & arg3) -> QuadratureFunction
        """
        this = _gridfunc.new_QuadratureFunction(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _gridfunc.delete_QuadratureFunction
    __del__ = lambda self: None

    def GetSpace(self):
        """GetSpace(QuadratureFunction self) -> QuadratureSpace"""
        return _gridfunc.QuadratureFunction_GetSpace(self)


    def SetSpace(self, *args):
        """
        SetSpace(QuadratureFunction self, QuadratureSpace qspace_, int vdim_=-1)
        SetSpace(QuadratureFunction self, QuadratureSpace qspace_)
        SetSpace(QuadratureFunction self, QuadratureSpace qspace_, double * qf_data, int vdim_=-1)
        SetSpace(QuadratureFunction self, QuadratureSpace qspace_, double * qf_data)
        """
        return _gridfunc.QuadratureFunction_SetSpace(self, *args)


    def GetVDim(self):
        """GetVDim(QuadratureFunction self) -> int"""
        return _gridfunc.QuadratureFunction_GetVDim(self)


    def SetVDim(self, vdim_):
        """SetVDim(QuadratureFunction self, int vdim_)"""
        return _gridfunc.QuadratureFunction_SetVDim(self, vdim_)


    def OwnsSpace(self):
        """OwnsSpace(QuadratureFunction self) -> bool"""
        return _gridfunc.QuadratureFunction_OwnsSpace(self)


    def SetOwnsSpace(self, own):
        """SetOwnsSpace(QuadratureFunction self, bool own)"""
        return _gridfunc.QuadratureFunction_SetOwnsSpace(self, own)


    def GetElementIntRule(self, idx):
        """GetElementIntRule(QuadratureFunction self, int idx) -> IntegrationRule"""
        return _gridfunc.QuadratureFunction_GetElementIntRule(self, idx)


    def GetElementValues(self, *args):
        """
        GetElementValues(QuadratureFunction self, int idx, Vector values)
        GetElementValues(QuadratureFunction self, int idx, Vector values)
        GetElementValues(QuadratureFunction self, int idx, DenseMatrix values)
        GetElementValues(QuadratureFunction self, int idx, DenseMatrix values)
        """
        return _gridfunc.QuadratureFunction_GetElementValues(self, *args)


    def Save(self, out):
        """Save(QuadratureFunction self, std::ostream & out)"""
        return _gridfunc.QuadratureFunction_Save(self, out)

QuadratureFunction_swigregister = _gridfunc.QuadratureFunction_swigregister
QuadratureFunction_swigregister(QuadratureFunction)


def __lshift__(*args):
    """
    __lshift__(std::ostream & out, Mesh mesh) -> std::ostream
    __lshift__(std::ostream & out, GridFunction sol) -> std::ostream
    __lshift__(std::ostream & out, QuadratureFunction qf) -> std::ostream &
    """
    return _gridfunc.__lshift__(*args)

def ZZErrorEstimator(blfi, u, flux, error_estimates, aniso_flags=None, with_subdomains=1):
    """
    ZZErrorEstimator(BilinearFormIntegrator blfi, GridFunction u, GridFunction flux, Vector error_estimates, intArray aniso_flags=None, int with_subdomains=1) -> double
    ZZErrorEstimator(BilinearFormIntegrator blfi, GridFunction u, GridFunction flux, Vector error_estimates, intArray aniso_flags=None) -> double
    ZZErrorEstimator(BilinearFormIntegrator blfi, GridFunction u, GridFunction flux, Vector error_estimates) -> double
    """
    return _gridfunc.ZZErrorEstimator(blfi, u, flux, error_estimates, aniso_flags, with_subdomains)

def ComputeElementLpDistance(p, i, gf1, gf2):
    """ComputeElementLpDistance(double p, int i, GridFunction gf1, GridFunction gf2) -> double"""
    return _gridfunc.ComputeElementLpDistance(p, i, gf1, gf2)
class ExtrudeCoefficient(mfem._ser.coefficient.Coefficient):
    """Proxy of C++ mfem::ExtrudeCoefficient class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.coefficient.Coefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ExtrudeCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.coefficient.Coefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ExtrudeCoefficient, name)
    __repr__ = _swig_repr

    def __init__(self, m, s, _n):
        """__init__(mfem::ExtrudeCoefficient self, Mesh m, Coefficient s, int _n) -> ExtrudeCoefficient"""
        this = _gridfunc.new_ExtrudeCoefficient(m, s, _n)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Eval(self, T, ip):
        """Eval(ExtrudeCoefficient self, ElementTransformation T, IntegrationPoint ip) -> double"""
        return _gridfunc.ExtrudeCoefficient_Eval(self, T, ip)

    __swig_destroy__ = _gridfunc.delete_ExtrudeCoefficient
    __del__ = lambda self: None
ExtrudeCoefficient_swigregister = _gridfunc.ExtrudeCoefficient_swigregister
ExtrudeCoefficient_swigregister(ExtrudeCoefficient)


def Extrude1DGridFunction(mesh, mesh2d, sol, ny):
    """Extrude1DGridFunction(Mesh mesh, Mesh mesh2d, GridFunction sol, int const ny) -> GridFunction"""
    return _gridfunc.Extrude1DGridFunction(mesh, mesh2d, sol, ny)

def __iadd__(self, v):
    ret = _gridfunc.GridFunction_iadd(self, v)
    ret.thisown = 0
    return self
def __isub__(self, v):
    ret = _gridfunc.GridFunction_isub(self, v)
    ret.thisown = 0
    return self
def __idiv__(self, v):
    ret = _gridfunc.GridFunction_idiv(self, v)
    ret.thisown = 0
    return self
def __imul__(self, v):
    ret = _gridfunc.GridFunction_imul(self, v)
    ret.thisown = 0
    return self

GridFunction.__iadd__  = __iadd__
GridFunction.__idiv__  = __idiv__
GridFunction.__isub__  = __isub__
GridFunction.__imul__  = __imul__      

# This file is compatible with both classic and new-style classes.


