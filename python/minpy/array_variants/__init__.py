#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ..utils import common
from . import numpy
from . import mxnet

class FunctionType(common.AutoNumber):
    """Enumeration of types of functions.

    Semantically this is different from :class:`..array.ArrayType`,
    but for now one data type corresponds to one function type.
    """
    NUMPY = ()
    MXNET = ()

class ArrayType(common.AutoNumber):
    """Enumeration of types of arrays."""
    NUMPY = ()
    MXNET = ()

variants = {
        'numpy': (ArrayType.NUMPY, FunctionType.NUMPY),
        #'mxnet': (ArrayType.MXNET, FunctionType.MXNET)
        }

allowed_types = {
        'numpy': numpy.allowed_types,
        'mxnet': mxnet.allowed_types
}