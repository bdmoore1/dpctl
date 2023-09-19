//===-- ------------ Implementation of _tensor_impl module  ----*-C++-*-/===//
//
//                      Data Parallel Control (dpctl)
//
// Copyright 2020-2023 Intel Corporation
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
//===--------------------------------------------------------------------===//
///
/// \file
/// This file defines functions of dpctl.tensor._tensor_impl extensions
//===--------------------------------------------------------------------===//

#pragma once
#include <CL/sycl.hpp>
#include <utility>
#include <vector>

#include "dpctl4pybind11.hpp"
#include <pybind11/pybind11.h>

namespace dpctl
{
namespace tensor
{
namespace py_internal
{

extern void init_repeat_dispatch_vectors(void);

extern std::pair<sycl::event, sycl::event>
py_repeat_by_sequence(dpctl::tensor::usm_ndarray src,
                      dpctl::tensor::usm_ndarray dst,
                      dpctl::tensor::usm_ndarray reps,
                      dpctl::tensor::usm_ndarray cumsum,
                      int axis,
                      sycl::queue exec_q,
                      std::vector<sycl::event> const &depends);

extern std::pair<sycl::event, sycl::event>
py_repeat_by_scalar(dpctl::tensor::usm_ndarray src,
                    dpctl::tensor::usm_ndarray dst,
                    const py::ssize_t reps,
                    int axis,
                    sycl::queue exec_q,
                    std::vector<sycl::event> const &depends);

} // namespace py_internal
} // namespace tensor
} // namespace dpctl
