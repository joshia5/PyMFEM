# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _fe_pos
else:
    import _fe_pos

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _fe_pos.SWIG_PyInstanceMethod_New
_swig_new_static_method = _fe_pos.SWIG_PyStaticMethod_New

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

import mfem._ser.fe_base
import mfem._ser.intrules
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.globals
import mfem._ser.geom
import mfem._ser.densemat
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
class PositiveFiniteElement(mfem._ser.fe_base.ScalarFiniteElement):
    r"""Proxy of C++ mfem::PositiveFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(PositiveFiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_pos.PositiveFiniteElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_pos.PositiveFiniteElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(PositiveFiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_pos.PositiveFiniteElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_pos.PositiveFiniteElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(PositiveFiniteElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_pos.PositiveFiniteElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_pos.PositiveFiniteElement_GetTransferMatrix)

    def Project(self, *args):
        r"""
        Project(PositiveFiniteElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(PositiveFiniteElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(PositiveFiniteElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_pos.PositiveFiniteElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_pos.PositiveFiniteElement_Project)
    __swig_destroy__ = _fe_pos.delete_PositiveFiniteElement

# Register PositiveFiniteElement in _fe_pos:
_fe_pos.PositiveFiniteElement_swigregister(PositiveFiniteElement)
class PositiveTensorFiniteElement(PositiveFiniteElement, mfem._ser.fe_base.TensorBasisElement):
    r"""Proxy of C++ mfem::PositiveTensorFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def GetDofToQuad(self, ir, mode):
        r"""GetDofToQuad(PositiveTensorFiniteElement self, IntegrationRule ir, mfem::DofToQuad::Mode mode) -> DofToQuad"""
        return _fe_pos.PositiveTensorFiniteElement_GetDofToQuad(self, ir, mode)
    GetDofToQuad = _swig_new_instance_method(_fe_pos.PositiveTensorFiniteElement_GetDofToQuad)

    def GetFaceMap(self, face_id, face_map):
        r"""GetFaceMap(PositiveTensorFiniteElement self, int const face_id, intArray face_map)"""
        return _fe_pos.PositiveTensorFiniteElement_GetFaceMap(self, face_id, face_map)
    GetFaceMap = _swig_new_instance_method(_fe_pos.PositiveTensorFiniteElement_GetFaceMap)
    __swig_destroy__ = _fe_pos.delete_PositiveTensorFiniteElement

# Register PositiveTensorFiniteElement in _fe_pos:
_fe_pos.PositiveTensorFiniteElement_swigregister(PositiveTensorFiniteElement)
class BiQuadPos2DFiniteElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::BiQuadPos2DFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(BiQuadPos2DFiniteElement self) -> BiQuadPos2DFiniteElement"""
        _fe_pos.BiQuadPos2DFiniteElement_swiginit(self, _fe_pos.new_BiQuadPos2DFiniteElement())

    def CalcShape(self, ip, shape):
        r"""CalcShape(BiQuadPos2DFiniteElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.BiQuadPos2DFiniteElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.BiQuadPos2DFiniteElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(BiQuadPos2DFiniteElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.BiQuadPos2DFiniteElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.BiQuadPos2DFiniteElement_CalcDShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(BiQuadPos2DFiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_pos.BiQuadPos2DFiniteElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_pos.BiQuadPos2DFiniteElement_GetLocalInterpolation)

    def Project(self, *args):
        r"""
        Project(BiQuadPos2DFiniteElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        Project(BiQuadPos2DFiniteElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(BiQuadPos2DFiniteElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        """
        return _fe_pos.BiQuadPos2DFiniteElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_pos.BiQuadPos2DFiniteElement_Project)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(BiQuadPos2DFiniteElement self, int vertex, Vector dofs)"""
        return _fe_pos.BiQuadPos2DFiniteElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.BiQuadPos2DFiniteElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_BiQuadPos2DFiniteElement

# Register BiQuadPos2DFiniteElement in _fe_pos:
_fe_pos.BiQuadPos2DFiniteElement_swigregister(BiQuadPos2DFiniteElement)
class QuadPos1DFiniteElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::QuadPos1DFiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(QuadPos1DFiniteElement self) -> QuadPos1DFiniteElement"""
        _fe_pos.QuadPos1DFiniteElement_swiginit(self, _fe_pos.new_QuadPos1DFiniteElement())

    def CalcShape(self, ip, shape):
        r"""CalcShape(QuadPos1DFiniteElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.QuadPos1DFiniteElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.QuadPos1DFiniteElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(QuadPos1DFiniteElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.QuadPos1DFiniteElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.QuadPos1DFiniteElement_CalcDShape)
    __swig_destroy__ = _fe_pos.delete_QuadPos1DFiniteElement

# Register QuadPos1DFiniteElement in _fe_pos:
_fe_pos.QuadPos1DFiniteElement_swigregister(QuadPos1DFiniteElement)
class H1Pos_SegmentElement(PositiveTensorFiniteElement):
    r"""Proxy of C++ mfem::H1Pos_SegmentElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(H1Pos_SegmentElement self, int const p) -> H1Pos_SegmentElement"""
        _fe_pos.H1Pos_SegmentElement_swiginit(self, _fe_pos.new_H1Pos_SegmentElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(H1Pos_SegmentElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.H1Pos_SegmentElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.H1Pos_SegmentElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(H1Pos_SegmentElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.H1Pos_SegmentElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.H1Pos_SegmentElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(H1Pos_SegmentElement self, int vertex, Vector dofs)"""
        return _fe_pos.H1Pos_SegmentElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.H1Pos_SegmentElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_H1Pos_SegmentElement

# Register H1Pos_SegmentElement in _fe_pos:
_fe_pos.H1Pos_SegmentElement_swigregister(H1Pos_SegmentElement)
class H1Pos_QuadrilateralElement(PositiveTensorFiniteElement):
    r"""Proxy of C++ mfem::H1Pos_QuadrilateralElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(H1Pos_QuadrilateralElement self, int const p) -> H1Pos_QuadrilateralElement"""
        _fe_pos.H1Pos_QuadrilateralElement_swiginit(self, _fe_pos.new_H1Pos_QuadrilateralElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(H1Pos_QuadrilateralElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.H1Pos_QuadrilateralElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.H1Pos_QuadrilateralElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(H1Pos_QuadrilateralElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.H1Pos_QuadrilateralElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.H1Pos_QuadrilateralElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(H1Pos_QuadrilateralElement self, int vertex, Vector dofs)"""
        return _fe_pos.H1Pos_QuadrilateralElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.H1Pos_QuadrilateralElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_H1Pos_QuadrilateralElement

# Register H1Pos_QuadrilateralElement in _fe_pos:
_fe_pos.H1Pos_QuadrilateralElement_swigregister(H1Pos_QuadrilateralElement)
class H1Pos_HexahedronElement(PositiveTensorFiniteElement):
    r"""Proxy of C++ mfem::H1Pos_HexahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(H1Pos_HexahedronElement self, int const p) -> H1Pos_HexahedronElement"""
        _fe_pos.H1Pos_HexahedronElement_swiginit(self, _fe_pos.new_H1Pos_HexahedronElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(H1Pos_HexahedronElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.H1Pos_HexahedronElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.H1Pos_HexahedronElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(H1Pos_HexahedronElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.H1Pos_HexahedronElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.H1Pos_HexahedronElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(H1Pos_HexahedronElement self, int vertex, Vector dofs)"""
        return _fe_pos.H1Pos_HexahedronElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.H1Pos_HexahedronElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_H1Pos_HexahedronElement

# Register H1Pos_HexahedronElement in _fe_pos:
_fe_pos.H1Pos_HexahedronElement_swigregister(H1Pos_HexahedronElement)
class H1Pos_TriangleElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::H1Pos_TriangleElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(H1Pos_TriangleElement self, int const p) -> H1Pos_TriangleElement"""
        _fe_pos.H1Pos_TriangleElement_swiginit(self, _fe_pos.new_H1Pos_TriangleElement(p))

    def CalcShape(self, *args):
        r"""
        CalcShape(H1Pos_TriangleElement self, int const p, double const x, double const y, double * shape)
        CalcShape(H1Pos_TriangleElement self, IntegrationPoint ip, Vector shape)
        """
        return _fe_pos.H1Pos_TriangleElement_CalcShape(self, *args)
    CalcShape = _swig_new_instance_method(_fe_pos.H1Pos_TriangleElement_CalcShape)

    def CalcDShape(self, *args):
        r"""
        CalcDShape(H1Pos_TriangleElement self, int const p, double const x, double const y, double * dshape_1d, double * dshape)
        CalcDShape(H1Pos_TriangleElement self, IntegrationPoint ip, DenseMatrix dshape)
        """
        return _fe_pos.H1Pos_TriangleElement_CalcDShape(self, *args)
    CalcDShape = _swig_new_instance_method(_fe_pos.H1Pos_TriangleElement_CalcDShape)
    __swig_destroy__ = _fe_pos.delete_H1Pos_TriangleElement

# Register H1Pos_TriangleElement in _fe_pos:
_fe_pos.H1Pos_TriangleElement_swigregister(H1Pos_TriangleElement)
class H1Pos_TetrahedronElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::H1Pos_TetrahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(H1Pos_TetrahedronElement self, int const p) -> H1Pos_TetrahedronElement"""
        _fe_pos.H1Pos_TetrahedronElement_swiginit(self, _fe_pos.new_H1Pos_TetrahedronElement(p))

    def CalcShape(self, *args):
        r"""
        CalcShape(H1Pos_TetrahedronElement self, int const p, double const x, double const y, double const z, double * shape)
        CalcShape(H1Pos_TetrahedronElement self, IntegrationPoint ip, Vector shape)
        """
        return _fe_pos.H1Pos_TetrahedronElement_CalcShape(self, *args)
    CalcShape = _swig_new_instance_method(_fe_pos.H1Pos_TetrahedronElement_CalcShape)

    def CalcDShape(self, *args):
        r"""
        CalcDShape(H1Pos_TetrahedronElement self, int const p, double const x, double const y, double const z, double * dshape_1d, double * dshape)
        CalcDShape(H1Pos_TetrahedronElement self, IntegrationPoint ip, DenseMatrix dshape)
        """
        return _fe_pos.H1Pos_TetrahedronElement_CalcDShape(self, *args)
    CalcDShape = _swig_new_instance_method(_fe_pos.H1Pos_TetrahedronElement_CalcDShape)
    __swig_destroy__ = _fe_pos.delete_H1Pos_TetrahedronElement

# Register H1Pos_TetrahedronElement in _fe_pos:
_fe_pos.H1Pos_TetrahedronElement_swigregister(H1Pos_TetrahedronElement)
class H1Pos_WedgeElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::H1Pos_WedgeElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(H1Pos_WedgeElement self, int const p) -> H1Pos_WedgeElement"""
        _fe_pos.H1Pos_WedgeElement_swiginit(self, _fe_pos.new_H1Pos_WedgeElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(H1Pos_WedgeElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.H1Pos_WedgeElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.H1Pos_WedgeElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(H1Pos_WedgeElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.H1Pos_WedgeElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.H1Pos_WedgeElement_CalcDShape)
    __swig_destroy__ = _fe_pos.delete_H1Pos_WedgeElement

# Register H1Pos_WedgeElement in _fe_pos:
_fe_pos.H1Pos_WedgeElement_swigregister(H1Pos_WedgeElement)
class L2Pos_SegmentElement(PositiveTensorFiniteElement):
    r"""Proxy of C++ mfem::L2Pos_SegmentElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(L2Pos_SegmentElement self, int const p) -> L2Pos_SegmentElement"""
        _fe_pos.L2Pos_SegmentElement_swiginit(self, _fe_pos.new_L2Pos_SegmentElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2Pos_SegmentElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.L2Pos_SegmentElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.L2Pos_SegmentElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2Pos_SegmentElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.L2Pos_SegmentElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.L2Pos_SegmentElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2Pos_SegmentElement self, int vertex, Vector dofs)"""
        return _fe_pos.L2Pos_SegmentElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.L2Pos_SegmentElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_L2Pos_SegmentElement

# Register L2Pos_SegmentElement in _fe_pos:
_fe_pos.L2Pos_SegmentElement_swigregister(L2Pos_SegmentElement)
class L2Pos_QuadrilateralElement(PositiveTensorFiniteElement):
    r"""Proxy of C++ mfem::L2Pos_QuadrilateralElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(L2Pos_QuadrilateralElement self, int const p) -> L2Pos_QuadrilateralElement"""
        _fe_pos.L2Pos_QuadrilateralElement_swiginit(self, _fe_pos.new_L2Pos_QuadrilateralElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2Pos_QuadrilateralElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.L2Pos_QuadrilateralElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.L2Pos_QuadrilateralElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2Pos_QuadrilateralElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.L2Pos_QuadrilateralElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.L2Pos_QuadrilateralElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2Pos_QuadrilateralElement self, int vertex, Vector dofs)"""
        return _fe_pos.L2Pos_QuadrilateralElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.L2Pos_QuadrilateralElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_L2Pos_QuadrilateralElement

# Register L2Pos_QuadrilateralElement in _fe_pos:
_fe_pos.L2Pos_QuadrilateralElement_swigregister(L2Pos_QuadrilateralElement)
class L2Pos_HexahedronElement(PositiveTensorFiniteElement):
    r"""Proxy of C++ mfem::L2Pos_HexahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(L2Pos_HexahedronElement self, int const p) -> L2Pos_HexahedronElement"""
        _fe_pos.L2Pos_HexahedronElement_swiginit(self, _fe_pos.new_L2Pos_HexahedronElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2Pos_HexahedronElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.L2Pos_HexahedronElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.L2Pos_HexahedronElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2Pos_HexahedronElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.L2Pos_HexahedronElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.L2Pos_HexahedronElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2Pos_HexahedronElement self, int vertex, Vector dofs)"""
        return _fe_pos.L2Pos_HexahedronElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.L2Pos_HexahedronElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_L2Pos_HexahedronElement

# Register L2Pos_HexahedronElement in _fe_pos:
_fe_pos.L2Pos_HexahedronElement_swigregister(L2Pos_HexahedronElement)
class L2Pos_TriangleElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::L2Pos_TriangleElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(L2Pos_TriangleElement self, int const p) -> L2Pos_TriangleElement"""
        _fe_pos.L2Pos_TriangleElement_swiginit(self, _fe_pos.new_L2Pos_TriangleElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2Pos_TriangleElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.L2Pos_TriangleElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.L2Pos_TriangleElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2Pos_TriangleElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.L2Pos_TriangleElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.L2Pos_TriangleElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2Pos_TriangleElement self, int vertex, Vector dofs)"""
        return _fe_pos.L2Pos_TriangleElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.L2Pos_TriangleElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_L2Pos_TriangleElement

# Register L2Pos_TriangleElement in _fe_pos:
_fe_pos.L2Pos_TriangleElement_swigregister(L2Pos_TriangleElement)
class L2Pos_TetrahedronElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::L2Pos_TetrahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(L2Pos_TetrahedronElement self, int const p) -> L2Pos_TetrahedronElement"""
        _fe_pos.L2Pos_TetrahedronElement_swiginit(self, _fe_pos.new_L2Pos_TetrahedronElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2Pos_TetrahedronElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.L2Pos_TetrahedronElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.L2Pos_TetrahedronElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2Pos_TetrahedronElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.L2Pos_TetrahedronElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.L2Pos_TetrahedronElement_CalcDShape)

    def ProjectDelta(self, vertex, dofs):
        r"""ProjectDelta(L2Pos_TetrahedronElement self, int vertex, Vector dofs)"""
        return _fe_pos.L2Pos_TetrahedronElement_ProjectDelta(self, vertex, dofs)
    ProjectDelta = _swig_new_instance_method(_fe_pos.L2Pos_TetrahedronElement_ProjectDelta)
    __swig_destroy__ = _fe_pos.delete_L2Pos_TetrahedronElement

# Register L2Pos_TetrahedronElement in _fe_pos:
_fe_pos.L2Pos_TetrahedronElement_swigregister(L2Pos_TetrahedronElement)
class L2Pos_WedgeElement(PositiveFiniteElement):
    r"""Proxy of C++ mfem::L2Pos_WedgeElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(L2Pos_WedgeElement self, int const p) -> L2Pos_WedgeElement"""
        _fe_pos.L2Pos_WedgeElement_swiginit(self, _fe_pos.new_L2Pos_WedgeElement(p))

    def CalcShape(self, ip, shape):
        r"""CalcShape(L2Pos_WedgeElement self, IntegrationPoint ip, Vector shape)"""
        return _fe_pos.L2Pos_WedgeElement_CalcShape(self, ip, shape)
    CalcShape = _swig_new_instance_method(_fe_pos.L2Pos_WedgeElement_CalcShape)

    def CalcDShape(self, ip, dshape):
        r"""CalcDShape(L2Pos_WedgeElement self, IntegrationPoint ip, DenseMatrix dshape)"""
        return _fe_pos.L2Pos_WedgeElement_CalcDShape(self, ip, dshape)
    CalcDShape = _swig_new_instance_method(_fe_pos.L2Pos_WedgeElement_CalcDShape)
    __swig_destroy__ = _fe_pos.delete_L2Pos_WedgeElement

# Register L2Pos_WedgeElement in _fe_pos:
_fe_pos.L2Pos_WedgeElement_swigregister(L2Pos_WedgeElement)
