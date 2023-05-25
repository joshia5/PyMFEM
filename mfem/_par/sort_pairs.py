# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sort_pairs
else:
    import _sort_pairs

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _sort_pairs.SWIG_PyInstanceMethod_New
_swig_new_static_method = _sort_pairs.SWIG_PyStaticMethod_New

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


class intintintTriple(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    one = property(_sort_pairs.intintintTriple_one_get, _sort_pairs.intintintTriple_one_set)
    two = property(_sort_pairs.intintintTriple_two_get, _sort_pairs.intintintTriple_two_set)
    three = property(_sort_pairs.intintintTriple_three_get, _sort_pairs.intintintTriple_three_set)

    def __init__(self, *args):
        _sort_pairs.intintintTriple_swiginit(self, _sort_pairs.new_intintintTriple(*args))
    __swig_destroy__ = _sort_pairs.delete_intintintTriple

# Register intintintTriple in _sort_pairs:
_sort_pairs.intintintTriple_swigregister(intintintTriple)
