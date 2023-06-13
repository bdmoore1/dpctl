#                      Data Parallel Control (dpctl)
#
# Copyright 2020-2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    **Data Parallel Tensor Collection** is a collection of tensor
    implementations that implement Python data API
    (https://data-apis.github.io/array-api/latest/) standard.

"""

from dpctl.tensor._copy_utils import asnumpy, astype, copy, from_numpy, to_numpy
from dpctl.tensor._ctors import (
    arange,
    asarray,
    empty,
    empty_like,
    eye,
    full,
    full_like,
    linspace,
    meshgrid,
    ones,
    ones_like,
    tril,
    triu,
    zeros,
    zeros_like,
)
from dpctl.tensor._data_types import (
    bool,
    complex64,
    complex128,
    dtype,
    float16,
    float32,
    float64,
    int8,
    int16,
    int32,
    int64,
    isdtype,
    uint8,
    uint16,
    uint32,
    uint64,
)
from dpctl.tensor._device import Device
from dpctl.tensor._dlpack import from_dlpack
from dpctl.tensor._indexing_functions import extract, nonzero, place, put, take
from dpctl.tensor._manipulation_functions import (
    broadcast_arrays,
    broadcast_to,
    can_cast,
    concat,
    expand_dims,
    finfo,
    flip,
    iinfo,
    moveaxis,
    permute_dims,
    result_type,
    roll,
    squeeze,
    stack,
    swapaxes,
    unstack,
)
from dpctl.tensor._print import (
    get_print_options,
    print_options,
    set_print_options,
    usm_ndarray_repr,
    usm_ndarray_str,
)
from dpctl.tensor._reshape import reshape
from dpctl.tensor._search_functions import where
from dpctl.tensor._usmarray import usm_ndarray
from dpctl.tensor._utility_functions import all, any

from ._constants import e, inf, nan, newaxis, pi
from ._elementwise_funcs import (
    abs,
    add,
    conj,
    cos,
    divide,
    equal,
    exp,
    expm1,
    floor_divide,
    greater,
    greater_equal,
    imag,
    isfinite,
    isinf,
    isnan,
    less,
    less_equal,
    log,
    log1p,
    multiply,
    not_equal,
    proj,
    real,
    sin,
    sqrt,
    subtract,
)
from ._reduction import sum

__all__ = [
    "Device",
    "usm_ndarray",
    "arange",
    "asarray",
    "astype",
    "copy",
    "empty",
    "zeros",
    "ones",
    "full",
    "eye",
    "linspace",
    "empty_like",
    "zeros_like",
    "ones_like",
    "full_like",
    "flip",
    "reshape",
    "roll",
    "concat",
    "stack",
    "broadcast_arrays",
    "broadcast_to",
    "expand_dims",
    "permute_dims",
    "squeeze",
    "take",
    "put",
    "extract",
    "place",
    "nonzero",
    "from_numpy",
    "to_numpy",
    "asnumpy",
    "from_dlpack",
    "tril",
    "triu",
    "where",
    "all",
    "any",
    "dtype",
    "isdtype",
    "bool",
    "int8",
    "uint8",
    "int16",
    "uint16",
    "int32",
    "uint32",
    "int64",
    "uint64",
    "float16",
    "float32",
    "float64",
    "complex64",
    "complex128",
    "iinfo",
    "finfo",
    "unstack",
    "moveaxis",
    "swapaxes",
    "can_cast",
    "result_type",
    "meshgrid",
    "get_print_options",
    "set_print_options",
    "print_options",
    "usm_ndarray_repr",
    "usm_ndarray_str",
    "newaxis",
    "e",
    "pi",
    "nan",
    "inf",
    "abs",
    "add",
    "conj",
    "cos",
    "exp",
    "expm1",
    "greater",
    "greater_equal",
    "imag",
    "isinf",
    "isnan",
    "isfinite",
    "less",
    "less_equal",
    "log",
    "log1p",
    "proj",
    "real",
    "sin",
    "sqrt",
    "divide",
    "multiply",
    "subtract",
    "equal",
    "not_equal",
    "sum",
    "floor_divide",
]
