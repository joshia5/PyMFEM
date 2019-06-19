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
        mname = '.'.join((pkg, '_bilinearform')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_bilinearform')
    _bilinearform = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_bilinearform', [dirname(__file__)])
        except ImportError:
            import _bilinearform
            return _bilinearform
        try:
            _mod = imp.load_module('_bilinearform', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _bilinearform = swig_import_helper()
    del swig_import_helper
else:
    import _bilinearform
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
        this = _bilinearform.new_intp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _bilinearform.delete_intp
    __del__ = lambda self: None

    def assign(self, value):
        return _bilinearform.intp_assign(self, value)

    def value(self):
        return _bilinearform.intp_value(self)

    def cast(self):
        return _bilinearform.intp_cast(self)
    if _newclass:
        frompointer = staticmethod(_bilinearform.intp_frompointer)
    else:
        frompointer = _bilinearform.intp_frompointer
intp_swigregister = _bilinearform.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t):
    return _bilinearform.intp_frompointer(t)
intp_frompointer = _bilinearform.intp_frompointer

class doublep(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doublep, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doublep, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _bilinearform.new_doublep()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _bilinearform.delete_doublep
    __del__ = lambda self: None

    def assign(self, value):
        return _bilinearform.doublep_assign(self, value)

    def value(self):
        return _bilinearform.doublep_value(self)

    def cast(self):
        return _bilinearform.doublep_cast(self)
    if _newclass:
        frompointer = staticmethod(_bilinearform.doublep_frompointer)
    else:
        frompointer = _bilinearform.doublep_frompointer
doublep_swigregister = _bilinearform.doublep_swigregister
doublep_swigregister(doublep)

def doublep_frompointer(t):
    return _bilinearform.doublep_frompointer(t)
doublep_frompointer = _bilinearform.doublep_frompointer

import mfem._ser.mem_manager
import mfem._ser.array
import mfem._ser.ostream_typemap
import mfem._ser.fespace
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.mesh
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.bilininteg
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.linearform
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.vertex
import mfem._ser.handle
AssemblyLevel_FULL = _bilinearform.AssemblyLevel_FULL
AssemblyLevel_ELEMENT = _bilinearform.AssemblyLevel_ELEMENT
AssemblyLevel_PARTIAL = _bilinearform.AssemblyLevel_PARTIAL
AssemblyLevel_NONE = _bilinearform.AssemblyLevel_NONE
class BilinearForm(mfem._ser.matrix.Matrix):
    """Proxy of C++ mfem::BilinearForm class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.matrix.Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BilinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.matrix.Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BilinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::BilinearForm self) -> BilinearForm
        __init__(mfem::BilinearForm self, FiniteElementSpace f) -> BilinearForm
        __init__(mfem::BilinearForm self, FiniteElementSpace f, BilinearForm bf, int ps=0) -> BilinearForm
        __init__(mfem::BilinearForm self, FiniteElementSpace f, BilinearForm bf) -> BilinearForm
        """
        if self.__class__ == BilinearForm:
            _self = None
        else:
            _self = self
        this = _bilinearform.new_BilinearForm(_self, *args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Size(self):
        """Size(BilinearForm self) -> int"""
        return _bilinearform.BilinearForm_Size(self)


    def SetAssemblyLevel(self, assembly_level):
        """SetAssemblyLevel(BilinearForm self, mfem::AssemblyLevel assembly_level)"""
        return _bilinearform.BilinearForm_SetAssemblyLevel(self, assembly_level)


    def EnableStaticCondensation(self):
        """EnableStaticCondensation(BilinearForm self)"""
        return _bilinearform.BilinearForm_EnableStaticCondensation(self)


    def StaticCondensationIsEnabled(self):
        """StaticCondensationIsEnabled(BilinearForm self) -> bool"""
        return _bilinearform.BilinearForm_StaticCondensationIsEnabled(self)


    def SCFESpace(self):
        """SCFESpace(BilinearForm self) -> FiniteElementSpace"""
        return _bilinearform.BilinearForm_SCFESpace(self)


    def EnableHybridization(self, constr_space, constr_integ, ess_tdof_list):
        """EnableHybridization(BilinearForm self, FiniteElementSpace constr_space, BilinearFormIntegrator constr_integ, intArray ess_tdof_list)"""
        val = _bilinearform.BilinearForm_EnableHybridization(self, constr_space, constr_integ, ess_tdof_list)

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(constr_integ)
        constr_integ.thisown = 0


        return val


    def UsePrecomputedSparsity(self, ps=1):
        """
        UsePrecomputedSparsity(BilinearForm self, int ps=1)
        UsePrecomputedSparsity(BilinearForm self)
        """
        return _bilinearform.BilinearForm_UsePrecomputedSparsity(self, ps)


    def UseSparsity(self, *args):
        """
        UseSparsity(BilinearForm self, int * I, int * J, bool isSorted)
        UseSparsity(BilinearForm self, SparseMatrix A)
        """
        return _bilinearform.BilinearForm_UseSparsity(self, *args)


    def AllocateMatrix(self):
        """AllocateMatrix(BilinearForm self)"""
        return _bilinearform.BilinearForm_AllocateMatrix(self)


    def GetDBFI(self):
        """GetDBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetDBFI(self)


    def GetBBFI(self):
        """GetBBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetBBFI(self)


    def GetBBFI_Marker(self):
        """GetBBFI_Marker(BilinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _bilinearform.BilinearForm_GetBBFI_Marker(self)


    def GetFBFI(self):
        """GetFBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetFBFI(self)


    def GetBFBFI(self):
        """GetBFBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetBFBFI(self)


    def GetBFBFI_Marker(self):
        """GetBFBFI_Marker(BilinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _bilinearform.BilinearForm_GetBFBFI_Marker(self)


    def __call__(self, i, j):
        """__call__(BilinearForm self, int i, int j) -> double const &"""
        return _bilinearform.BilinearForm___call__(self, i, j)


    def Elem(self, *args):
        """
        Elem(BilinearForm self, int i, int j) -> double
        Elem(BilinearForm self, int i, int j) -> double const &
        """
        return _bilinearform.BilinearForm_Elem(self, *args)


    def Mult(self, x, y):
        """Mult(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_Mult(self, x, y)


    def FullMult(self, x, y):
        """FullMult(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_FullMult(self, x, y)


    def AddMult(self, x, y, a=1.0):
        """
        AddMult(BilinearForm self, Vector x, Vector y, double const a=1.0)
        AddMult(BilinearForm self, Vector x, Vector y)
        """
        return _bilinearform.BilinearForm_AddMult(self, x, y, a)


    def FullAddMult(self, x, y):
        """FullAddMult(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_FullAddMult(self, x, y)


    def AddMultTranspose(self, x, y, a=1.0):
        """
        AddMultTranspose(BilinearForm self, Vector x, Vector y, double const a=1.0)
        AddMultTranspose(BilinearForm self, Vector x, Vector y)
        """
        return _bilinearform.BilinearForm_AddMultTranspose(self, x, y, a)


    def FullAddMultTranspose(self, x, y):
        """FullAddMultTranspose(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_FullAddMultTranspose(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_MultTranspose(self, x, y)


    def InnerProduct(self, x, y):
        """InnerProduct(BilinearForm self, Vector x, Vector y) -> double"""
        return _bilinearform.BilinearForm_InnerProduct(self, x, y)


    def Inverse(self):
        """Inverse(BilinearForm self) -> MatrixInverse"""
        return _bilinearform.BilinearForm_Inverse(self)


    def Finalize(self, skip_zeros=1):
        """
        Finalize(BilinearForm self, int skip_zeros=1)
        Finalize(BilinearForm self)
        """
        return _bilinearform.BilinearForm_Finalize(self, skip_zeros)


    def SpMat(self, *args):
        """
        SpMat(BilinearForm self) -> SparseMatrix
        SpMat(BilinearForm self) -> SparseMatrix
        """
        val = _bilinearform.BilinearForm_SpMat(self, *args)

        if not hasattr(self, "_spmat"): self._spmat = []
        self._spmat.append(val)
        val.thisown=0 


        return val


    def LoseMat(self):
        """LoseMat(BilinearForm self) -> SparseMatrix"""
        return _bilinearform.BilinearForm_LoseMat(self)


    def SpMatElim(self, *args):
        """
        SpMatElim(BilinearForm self) -> SparseMatrix
        SpMatElim(BilinearForm self) -> SparseMatrix
        """
        return _bilinearform.BilinearForm_SpMatElim(self, *args)


    def AddDomainIntegrator(self, bfi):
        """AddDomainIntegrator(BilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddDomainIntegrator(self, bfi)


    def AddBoundaryIntegrator(self, *args):
        """
        AddBoundaryIntegrator(BilinearForm self, BilinearFormIntegrator bfi)
        AddBoundaryIntegrator(BilinearForm self, BilinearFormIntegrator bfi, intArray bdr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        bfi = args[0]	     
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddBoundaryIntegrator(self, *args)


    def AddInteriorFaceIntegrator(self, bfi):
        """AddInteriorFaceIntegrator(BilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddInteriorFaceIntegrator(self, bfi)


    def AddBdrFaceIntegrator(self, *args):
        """
        AddBdrFaceIntegrator(BilinearForm self, BilinearFormIntegrator bfi)
        AddBdrFaceIntegrator(BilinearForm self, BilinearFormIntegrator bfi, intArray bdr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        bfi = args[0]
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddBdrFaceIntegrator(self, *args)


    def Assemble(self, skip_zeros=1):
        """
        Assemble(BilinearForm self, int skip_zeros=1)
        Assemble(BilinearForm self)
        """
        return _bilinearform.BilinearForm_Assemble(self, skip_zeros)


    def GetProlongation(self):
        """GetProlongation(BilinearForm self) -> Operator"""
        return _bilinearform.BilinearForm_GetProlongation(self)


    def GetRestriction(self):
        """GetRestriction(BilinearForm self) -> Operator"""
        return _bilinearform.BilinearForm_GetRestriction(self)


    def FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior=0):
        """
        FormLinearSystem(BilinearForm self, intArray ess_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B, int copy_interior=0)
        FormLinearSystem(BilinearForm self, intArray ess_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B)
        """
        return _bilinearform.BilinearForm_FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior)


    def FormSystemMatrix(self, ess_tdof_list, A):
        """FormSystemMatrix(BilinearForm self, intArray ess_tdof_list, OperatorHandle A)"""
        return _bilinearform.BilinearForm_FormSystemMatrix(self, ess_tdof_list, A)


    def RecoverFEMSolution(self, X, b, x):
        """RecoverFEMSolution(BilinearForm self, Vector X, Vector b, Vector x)"""
        return _bilinearform.BilinearForm_RecoverFEMSolution(self, X, b, x)


    def ComputeElementMatrices(self):
        """ComputeElementMatrices(BilinearForm self)"""
        return _bilinearform.BilinearForm_ComputeElementMatrices(self)


    def FreeElementMatrices(self):
        """FreeElementMatrices(BilinearForm self)"""
        return _bilinearform.BilinearForm_FreeElementMatrices(self)


    def ComputeElementMatrix(self, i, elmat):
        """ComputeElementMatrix(BilinearForm self, int i, DenseMatrix elmat)"""
        return _bilinearform.BilinearForm_ComputeElementMatrix(self, i, elmat)


    def AssembleElementMatrix(self, i, elmat, vdofs, skip_zeros=1):
        """
        AssembleElementMatrix(BilinearForm self, int i, DenseMatrix elmat, intArray vdofs, int skip_zeros=1)
        AssembleElementMatrix(BilinearForm self, int i, DenseMatrix elmat, intArray vdofs)
        """
        return _bilinearform.BilinearForm_AssembleElementMatrix(self, i, elmat, vdofs, skip_zeros)


    def AssembleBdrElementMatrix(self, i, elmat, vdofs, skip_zeros=1):
        """
        AssembleBdrElementMatrix(BilinearForm self, int i, DenseMatrix elmat, intArray vdofs, int skip_zeros=1)
        AssembleBdrElementMatrix(BilinearForm self, int i, DenseMatrix elmat, intArray vdofs)
        """
        return _bilinearform.BilinearForm_AssembleBdrElementMatrix(self, i, elmat, vdofs, skip_zeros)


    def EliminateEssentialBC(self, *args):
        """
        EliminateEssentialBC(BilinearForm self, intArray bdr_attr_is_ess, Vector sol, Vector rhs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateEssentialBC(BilinearForm self, intArray bdr_attr_is_ess, Vector sol, Vector rhs)
        EliminateEssentialBC(BilinearForm self, intArray bdr_attr_is_ess, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateEssentialBC(BilinearForm self, intArray bdr_attr_is_ess)
        """
        return _bilinearform.BilinearForm_EliminateEssentialBC(self, *args)


    def EliminateEssentialBCDiag(self, bdr_attr_is_ess, value):
        """EliminateEssentialBCDiag(BilinearForm self, intArray bdr_attr_is_ess, double value)"""
        return _bilinearform.BilinearForm_EliminateEssentialBCDiag(self, bdr_attr_is_ess, value)


    def EliminateVDofs(self, *args):
        """
        EliminateVDofs(BilinearForm self, intArray vdofs, Vector sol, Vector rhs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateVDofs(BilinearForm self, intArray vdofs, Vector sol, Vector rhs)
        EliminateVDofs(BilinearForm self, intArray vdofs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateVDofs(BilinearForm self, intArray vdofs)
        """
        return _bilinearform.BilinearForm_EliminateVDofs(self, *args)


    def EliminateEssentialBCFromDofs(self, *args):
        """
        EliminateEssentialBCFromDofs(BilinearForm self, intArray ess_dofs, Vector sol, Vector rhs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateEssentialBCFromDofs(BilinearForm self, intArray ess_dofs, Vector sol, Vector rhs)
        EliminateEssentialBCFromDofs(BilinearForm self, intArray ess_dofs, mfem::Matrix::DiagonalPolicy dpolicy)
        EliminateEssentialBCFromDofs(BilinearForm self, intArray ess_dofs)
        """
        return _bilinearform.BilinearForm_EliminateEssentialBCFromDofs(self, *args)


    def EliminateEssentialBCFromDofsDiag(self, ess_dofs, value):
        """EliminateEssentialBCFromDofsDiag(BilinearForm self, intArray ess_dofs, double value)"""
        return _bilinearform.BilinearForm_EliminateEssentialBCFromDofsDiag(self, ess_dofs, value)


    def EliminateVDofsInRHS(self, vdofs, x, b):
        """EliminateVDofsInRHS(BilinearForm self, intArray vdofs, Vector x, Vector b)"""
        return _bilinearform.BilinearForm_EliminateVDofsInRHS(self, vdofs, x, b)


    def FullInnerProduct(self, x, y):
        """FullInnerProduct(BilinearForm self, Vector x, Vector y) -> double"""
        return _bilinearform.BilinearForm_FullInnerProduct(self, x, y)


    def Update(self, nfes=None):
        """
        Update(BilinearForm self, FiniteElementSpace nfes=None)
        Update(BilinearForm self)
        """
        return _bilinearform.BilinearForm_Update(self, nfes)


    def GetFES(self):
        """GetFES(BilinearForm self) -> FiniteElementSpace"""
        return _bilinearform.BilinearForm_GetFES(self)


    def FESpace(self, *args):
        """
        FESpace(BilinearForm self) -> FiniteElementSpace
        FESpace(BilinearForm self) -> FiniteElementSpace
        """
        return _bilinearform.BilinearForm_FESpace(self, *args)


    def SetDiagonalPolicy(self, policy):
        """SetDiagonalPolicy(BilinearForm self, mfem::Matrix::DiagonalPolicy policy)"""
        return _bilinearform.BilinearForm_SetDiagonalPolicy(self, policy)

    __swig_destroy__ = _bilinearform.delete_BilinearForm
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _bilinearform.disown_BilinearForm(self)
        return weakref_proxy(self)
BilinearForm_swigregister = _bilinearform.BilinearForm_swigregister
BilinearForm_swigregister(BilinearForm)

class MixedBilinearForm(mfem._ser.matrix.Matrix):
    """Proxy of C++ mfem::MixedBilinearForm class."""

    __swig_setmethods__ = {}
    for _s in [mfem._ser.matrix.Matrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MixedBilinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._ser.matrix.Matrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, MixedBilinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::MixedBilinearForm self, FiniteElementSpace tr_fes, FiniteElementSpace te_fes) -> MixedBilinearForm
        __init__(mfem::MixedBilinearForm self, FiniteElementSpace tr_fes, FiniteElementSpace te_fes, MixedBilinearForm mbf) -> MixedBilinearForm
        """
        this = _bilinearform.new_MixedBilinearForm(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Elem(self, *args):
        """
        Elem(MixedBilinearForm self, int i, int j) -> double
        Elem(MixedBilinearForm self, int i, int j) -> double const &
        """
        return _bilinearform.MixedBilinearForm_Elem(self, *args)


    def Mult(self, x, y):
        """Mult(MixedBilinearForm self, Vector x, Vector y)"""
        return _bilinearform.MixedBilinearForm_Mult(self, x, y)


    def AddMult(self, x, y, a=1.0):
        """
        AddMult(MixedBilinearForm self, Vector x, Vector y, double const a=1.0)
        AddMult(MixedBilinearForm self, Vector x, Vector y)
        """
        return _bilinearform.MixedBilinearForm_AddMult(self, x, y, a)


    def AddMultTranspose(self, x, y, a=1.0):
        """
        AddMultTranspose(MixedBilinearForm self, Vector x, Vector y, double const a=1.0)
        AddMultTranspose(MixedBilinearForm self, Vector x, Vector y)
        """
        return _bilinearform.MixedBilinearForm_AddMultTranspose(self, x, y, a)


    def MultTranspose(self, x, y):
        """MultTranspose(MixedBilinearForm self, Vector x, Vector y)"""
        return _bilinearform.MixedBilinearForm_MultTranspose(self, x, y)


    def Inverse(self):
        """Inverse(MixedBilinearForm self) -> MatrixInverse"""
        return _bilinearform.MixedBilinearForm_Inverse(self)


    def Finalize(self, skip_zeros=1):
        """
        Finalize(MixedBilinearForm self, int skip_zeros=1)
        Finalize(MixedBilinearForm self)
        """
        return _bilinearform.MixedBilinearForm_Finalize(self, skip_zeros)


    def GetBlocks(self, blocks):
        """GetBlocks(MixedBilinearForm self, mfem::Array2D< mfem::SparseMatrix * > & blocks)"""
        return _bilinearform.MixedBilinearForm_GetBlocks(self, blocks)


    def SpMat(self, *args):
        """
        SpMat(MixedBilinearForm self) -> SparseMatrix
        SpMat(MixedBilinearForm self) -> SparseMatrix
        """
        val = _bilinearform.MixedBilinearForm_SpMat(self, *args)

        if not hasattr(self, "_spmat"): self._spmat = []
        self._spmat.append(val)
        val.thisown=0 


        return val


    def LoseMat(self):
        """LoseMat(MixedBilinearForm self) -> SparseMatrix"""
        return _bilinearform.MixedBilinearForm_LoseMat(self)


    def AddDomainIntegrator(self, bfi):
        """AddDomainIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddDomainIntegrator(self, bfi)


    def AddBoundaryIntegrator(self, bfi):
        """AddBoundaryIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddBoundaryIntegrator(self, bfi)


    def AddTraceFaceIntegrator(self, bfi):
        """AddTraceFaceIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddTraceFaceIntegrator(self, bfi)


    def GetDBFI(self):
        """GetDBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetDBFI(self)


    def GetBBFI(self):
        """GetBBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetBBFI(self)


    def GetTFBFI(self):
        """GetTFBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetTFBFI(self)


    def Assemble(self, skip_zeros=1):
        """
        Assemble(MixedBilinearForm self, int skip_zeros=1)
        Assemble(MixedBilinearForm self)
        """
        return _bilinearform.MixedBilinearForm_Assemble(self, skip_zeros)


    def ConformingAssemble(self):
        """ConformingAssemble(MixedBilinearForm self)"""
        return _bilinearform.MixedBilinearForm_ConformingAssemble(self)


    def EliminateTrialDofs(self, bdr_attr_is_ess, sol, rhs):
        """EliminateTrialDofs(MixedBilinearForm self, intArray bdr_attr_is_ess, Vector sol, Vector rhs)"""
        return _bilinearform.MixedBilinearForm_EliminateTrialDofs(self, bdr_attr_is_ess, sol, rhs)


    def EliminateEssentialBCFromTrialDofs(self, marked_vdofs, sol, rhs):
        """EliminateEssentialBCFromTrialDofs(MixedBilinearForm self, intArray marked_vdofs, Vector sol, Vector rhs)"""
        return _bilinearform.MixedBilinearForm_EliminateEssentialBCFromTrialDofs(self, marked_vdofs, sol, rhs)


    def EliminateTestDofs(self, bdr_attr_is_ess):
        """EliminateTestDofs(MixedBilinearForm self, intArray bdr_attr_is_ess)"""
        return _bilinearform.MixedBilinearForm_EliminateTestDofs(self, bdr_attr_is_ess)


    def Update(self):
        """Update(MixedBilinearForm self)"""
        return _bilinearform.MixedBilinearForm_Update(self)

    __swig_destroy__ = _bilinearform.delete_MixedBilinearForm
    __del__ = lambda self: None
MixedBilinearForm_swigregister = _bilinearform.MixedBilinearForm_swigregister
MixedBilinearForm_swigregister(MixedBilinearForm)

class DiscreteLinearOperator(MixedBilinearForm):
    """Proxy of C++ mfem::DiscreteLinearOperator class."""

    __swig_setmethods__ = {}
    for _s in [MixedBilinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DiscreteLinearOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [MixedBilinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DiscreteLinearOperator, name)
    __repr__ = _swig_repr

    def __init__(self, domain_fes, range_fes):
        """__init__(mfem::DiscreteLinearOperator self, FiniteElementSpace domain_fes, FiniteElementSpace range_fes) -> DiscreteLinearOperator"""
        this = _bilinearform.new_DiscreteLinearOperator(domain_fes, range_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def AddDomainInterpolator(self, di):
        """AddDomainInterpolator(DiscreteLinearOperator self, DiscreteInterpolator di)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(di)
        di.thisown=0 


        return _bilinearform.DiscreteLinearOperator_AddDomainInterpolator(self, di)


    def AddTraceFaceInterpolator(self, di):
        """AddTraceFaceInterpolator(DiscreteLinearOperator self, DiscreteInterpolator di)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(di)
        di.thisown=0 


        return _bilinearform.DiscreteLinearOperator_AddTraceFaceInterpolator(self, di)


    def GetDI(self):
        """GetDI(DiscreteLinearOperator self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.DiscreteLinearOperator_GetDI(self)


    def Assemble(self, skip_zeros=1):
        """
        Assemble(DiscreteLinearOperator self, int skip_zeros=1)
        Assemble(DiscreteLinearOperator self)
        """
        return _bilinearform.DiscreteLinearOperator_Assemble(self, skip_zeros)

    __swig_destroy__ = _bilinearform.delete_DiscreteLinearOperator
    __del__ = lambda self: None
DiscreteLinearOperator_swigregister = _bilinearform.DiscreteLinearOperator_swigregister
DiscreteLinearOperator_swigregister(DiscreteLinearOperator)

# This file is compatible with both classic and new-style classes.


