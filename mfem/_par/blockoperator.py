# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _blockoperator
else:
    import _blockoperator

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _blockoperator.SWIG_PyInstanceMethod_New
_swig_new_static_method = _blockoperator.SWIG_PyStaticMethod_New

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

import mfem._par.array
import mfem._par.mem_manager
import mfem._par.globals
import mfem._par.vector
import mfem._par.operators

def Opr2BlockOpr(op):
    r"""Opr2BlockOpr(Operator op) -> BlockOperator"""
    return _blockoperator.Opr2BlockOpr(op)
Opr2BlockOpr = _blockoperator.Opr2BlockOpr

def Opr2SparseMat(op):
    r"""Opr2SparseMat(Operator op) -> mfem::SparseMatrix *"""
    return _blockoperator.Opr2SparseMat(op)
Opr2SparseMat = _blockoperator.Opr2SparseMat

def Opr2HypreParMat(op):
    r"""Opr2HypreParMat(Operator op) -> mfem::HypreParMatrix *"""
    return _blockoperator.Opr2HypreParMat(op)
Opr2HypreParMat = _blockoperator.Opr2HypreParMat
class BlockOperator(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::BlockOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(BlockOperator self, intArray offsets) -> BlockOperator
        __init__(BlockOperator self, intArray row_offsets, intArray col_offsets) -> BlockOperator
        """
        _blockoperator.BlockOperator_swiginit(self, _blockoperator.new_BlockOperator(*args))

        from mfem.par import intArray  
        if len(args) == 1:
           if isinstance(args[0], intArray):
               self._offsets = args[0]
        if len(args) == 2:
           if (isinstance(args[0], intArray) and
               isinstance(args[1], intArray)):
               self._offsets = (args[0], args[1])




    def SetDiagonalBlock(self, iblock, op, c=1.0):
        r"""SetDiagonalBlock(BlockOperator self, int iblock, Operator op, double c=1.0)"""
        val = _blockoperator.BlockOperator_SetDiagonalBlock(self, iblock, op, c)

        if not hasattr(self, '_linked_op'):
           self._linked_op = {}
        self._linked_op[iblock, iblock] = op


        return val


    def SetBlock(self, iRow, iCol, op, c=1.0):
        r"""SetBlock(BlockOperator self, int iRow, int iCol, Operator op, double c=1.0)"""
        val = _blockoperator.BlockOperator_SetBlock(self, iRow, iCol, op, c)

        if not hasattr(self, '_linked_op'):
           self._linked_op = {}
        self._linked_op[iRow, iCol] = op


        return val


    def NumRowBlocks(self):
        r"""NumRowBlocks(BlockOperator self) -> int"""
        return _blockoperator.BlockOperator_NumRowBlocks(self)
    NumRowBlocks = _swig_new_instance_method(_blockoperator.BlockOperator_NumRowBlocks)

    def NumColBlocks(self):
        r"""NumColBlocks(BlockOperator self) -> int"""
        return _blockoperator.BlockOperator_NumColBlocks(self)
    NumColBlocks = _swig_new_instance_method(_blockoperator.BlockOperator_NumColBlocks)

    def IsZeroBlock(self, i, j):
        r"""IsZeroBlock(BlockOperator self, int i, int j) -> int"""
        return _blockoperator.BlockOperator_IsZeroBlock(self, i, j)
    IsZeroBlock = _swig_new_instance_method(_blockoperator.BlockOperator_IsZeroBlock)

    def GetBlock(self, *args):
        r"""
        GetBlock(BlockOperator self, int i, int j) -> Operator
        GetBlock(BlockOperator self, int i, int j) -> Operator
        """
        return _blockoperator.BlockOperator_GetBlock(self, *args)
    GetBlock = _swig_new_instance_method(_blockoperator.BlockOperator_GetBlock)

    def GetBlockCoef(self, i, j):
        r"""GetBlockCoef(BlockOperator self, int i, int j) -> double"""
        return _blockoperator.BlockOperator_GetBlockCoef(self, i, j)
    GetBlockCoef = _swig_new_instance_method(_blockoperator.BlockOperator_GetBlockCoef)

    def SetBlockCoef(self, i, j, c):
        r"""SetBlockCoef(BlockOperator self, int i, int j, double c)"""
        return _blockoperator.BlockOperator_SetBlockCoef(self, i, j, c)
    SetBlockCoef = _swig_new_instance_method(_blockoperator.BlockOperator_SetBlockCoef)

    def RowOffsets(self, *args):
        r"""
        RowOffsets(BlockOperator self) -> intArray
        RowOffsets(BlockOperator self) -> intArray
        """
        return _blockoperator.BlockOperator_RowOffsets(self, *args)
    RowOffsets = _swig_new_instance_method(_blockoperator.BlockOperator_RowOffsets)

    def ColOffsets(self, *args):
        r"""
        ColOffsets(BlockOperator self) -> intArray
        ColOffsets(BlockOperator self) -> intArray
        """
        return _blockoperator.BlockOperator_ColOffsets(self, *args)
    ColOffsets = _swig_new_instance_method(_blockoperator.BlockOperator_ColOffsets)

    def Mult(self, x, y):
        r"""Mult(BlockOperator self, Vector x, Vector y)"""
        return _blockoperator.BlockOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_blockoperator.BlockOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(BlockOperator self, Vector x, Vector y)"""
        return _blockoperator.BlockOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_blockoperator.BlockOperator_MultTranspose)
    __swig_destroy__ = _blockoperator.delete_BlockOperator
    owns_blocks = property(_blockoperator.BlockOperator_owns_blocks_get, _blockoperator.BlockOperator_owns_blocks_set, doc=r"""owns_blocks : int""")

    def GetType(self):
        r"""GetType(BlockOperator self) -> mfem::Operator::Type"""
        return _blockoperator.BlockOperator_GetType(self)
    GetType = _swig_new_instance_method(_blockoperator.BlockOperator_GetType)

# Register BlockOperator in _blockoperator:
_blockoperator.BlockOperator_swigregister(BlockOperator)
class BlockDiagonalPreconditioner(mfem._par.operators.Solver):
    r"""Proxy of C++ mfem::BlockDiagonalPreconditioner class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, offsets):
        r"""__init__(BlockDiagonalPreconditioner self, intArray offsets) -> BlockDiagonalPreconditioner"""
        _blockoperator.BlockDiagonalPreconditioner_swiginit(self, _blockoperator.new_BlockDiagonalPreconditioner(offsets))

        self._offsets = offsets




    def SetDiagonalBlock(self, iblock, op):
        r"""SetDiagonalBlock(BlockDiagonalPreconditioner self, int iblock, Operator op)"""
        val = _blockoperator.BlockDiagonalPreconditioner_SetDiagonalBlock(self, iblock, op)

        if not hasattr(self, '_linked_op'):
           self._linked_op = {}
        self._linked_op[iblock, iblock] = op


        return val


    def SetOperator(self, op):
        r"""SetOperator(BlockDiagonalPreconditioner self, Operator op)"""
        return _blockoperator.BlockDiagonalPreconditioner_SetOperator(self, op)
    SetOperator = _swig_new_instance_method(_blockoperator.BlockDiagonalPreconditioner_SetOperator)

    def NumBlocks(self):
        r"""NumBlocks(BlockDiagonalPreconditioner self) -> int"""
        return _blockoperator.BlockDiagonalPreconditioner_NumBlocks(self)
    NumBlocks = _swig_new_instance_method(_blockoperator.BlockDiagonalPreconditioner_NumBlocks)

    def GetDiagonalBlock(self, *args):
        r"""
        GetDiagonalBlock(BlockDiagonalPreconditioner self, int iblock) -> Operator
        GetDiagonalBlock(BlockDiagonalPreconditioner self, int iblock) -> Operator
        """
        return _blockoperator.BlockDiagonalPreconditioner_GetDiagonalBlock(self, *args)
    GetDiagonalBlock = _swig_new_instance_method(_blockoperator.BlockDiagonalPreconditioner_GetDiagonalBlock)

    def Offsets(self, *args):
        r"""
        Offsets(BlockDiagonalPreconditioner self) -> intArray
        Offsets(BlockDiagonalPreconditioner self) -> intArray
        """
        return _blockoperator.BlockDiagonalPreconditioner_Offsets(self, *args)
    Offsets = _swig_new_instance_method(_blockoperator.BlockDiagonalPreconditioner_Offsets)

    def Mult(self, x, y):
        r"""Mult(BlockDiagonalPreconditioner self, Vector x, Vector y)"""
        return _blockoperator.BlockDiagonalPreconditioner_Mult(self, x, y)
    Mult = _swig_new_instance_method(_blockoperator.BlockDiagonalPreconditioner_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(BlockDiagonalPreconditioner self, Vector x, Vector y)"""
        return _blockoperator.BlockDiagonalPreconditioner_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_blockoperator.BlockDiagonalPreconditioner_MultTranspose)
    __swig_destroy__ = _blockoperator.delete_BlockDiagonalPreconditioner
    owns_blocks = property(_blockoperator.BlockDiagonalPreconditioner_owns_blocks_get, _blockoperator.BlockDiagonalPreconditioner_owns_blocks_set, doc=r"""owns_blocks : int""")

# Register BlockDiagonalPreconditioner in _blockoperator:
_blockoperator.BlockDiagonalPreconditioner_swigregister(BlockDiagonalPreconditioner)
class BlockLowerTriangularPreconditioner(mfem._par.operators.Solver):
    r"""Proxy of C++ mfem::BlockLowerTriangularPreconditioner class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, offsets):
        r"""__init__(BlockLowerTriangularPreconditioner self, intArray offsets) -> BlockLowerTriangularPreconditioner"""
        _blockoperator.BlockLowerTriangularPreconditioner_swiginit(self, _blockoperator.new_BlockLowerTriangularPreconditioner(offsets))

        self._offsets = offsets




    def SetDiagonalBlock(self, iblock, op):
        r"""SetDiagonalBlock(BlockLowerTriangularPreconditioner self, int iblock, Operator op)"""
        val = _blockoperator.BlockLowerTriangularPreconditioner_SetDiagonalBlock(self, iblock, op)

        if not hasattr(self, '_linked_op'):
           self._linked_op = {}
        self._linked_op[iblock, iblock] = op


        return val


    def SetBlock(self, iRow, iCol, op):
        r"""SetBlock(BlockLowerTriangularPreconditioner self, int iRow, int iCol, Operator op)"""

        if not (iRow > iCol):
            raise ValueError("can not set upper triangle")


        val = _blockoperator.BlockLowerTriangularPreconditioner_SetBlock(self, iRow, iCol, op)

        if not hasattr(self, '_linked_op'):
           self._linked_op = {}

        self._linked_op[iRow, iCol] = op


        return val


    def SetOperator(self, op):
        r"""SetOperator(BlockLowerTriangularPreconditioner self, Operator op)"""
        return _blockoperator.BlockLowerTriangularPreconditioner_SetOperator(self, op)
    SetOperator = _swig_new_instance_method(_blockoperator.BlockLowerTriangularPreconditioner_SetOperator)

    def NumBlocks(self):
        r"""NumBlocks(BlockLowerTriangularPreconditioner self) -> int"""
        return _blockoperator.BlockLowerTriangularPreconditioner_NumBlocks(self)
    NumBlocks = _swig_new_instance_method(_blockoperator.BlockLowerTriangularPreconditioner_NumBlocks)

    def GetBlock(self, iblock, jblock):
        r"""GetBlock(BlockLowerTriangularPreconditioner self, int iblock, int jblock) -> Operator"""
        return _blockoperator.BlockLowerTriangularPreconditioner_GetBlock(self, iblock, jblock)
    GetBlock = _swig_new_instance_method(_blockoperator.BlockLowerTriangularPreconditioner_GetBlock)

    def Offsets(self):
        r"""Offsets(BlockLowerTriangularPreconditioner self) -> intArray"""
        return _blockoperator.BlockLowerTriangularPreconditioner_Offsets(self)
    Offsets = _swig_new_instance_method(_blockoperator.BlockLowerTriangularPreconditioner_Offsets)

    def Mult(self, x, y):
        r"""Mult(BlockLowerTriangularPreconditioner self, Vector x, Vector y)"""
        return _blockoperator.BlockLowerTriangularPreconditioner_Mult(self, x, y)
    Mult = _swig_new_instance_method(_blockoperator.BlockLowerTriangularPreconditioner_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(BlockLowerTriangularPreconditioner self, Vector x, Vector y)"""
        return _blockoperator.BlockLowerTriangularPreconditioner_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_blockoperator.BlockLowerTriangularPreconditioner_MultTranspose)
    __swig_destroy__ = _blockoperator.delete_BlockLowerTriangularPreconditioner
    owns_blocks = property(_blockoperator.BlockLowerTriangularPreconditioner_owns_blocks_get, _blockoperator.BlockLowerTriangularPreconditioner_owns_blocks_set, doc=r"""owns_blocks : int""")

# Register BlockLowerTriangularPreconditioner in _blockoperator:
_blockoperator.BlockLowerTriangularPreconditioner_swigregister(BlockLowerTriangularPreconditioner)

