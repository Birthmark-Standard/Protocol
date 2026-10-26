# Copyright (C) 2024-2026 The Birthmark Standard Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

# Builds sha256_zk_bench against a Longfellow-zk clone.
#   cmake -S . -B <build> -D LONGFELLOW_SRC=<clone> -D CMAKE_BUILD_TYPE=Release
# Longfellow's own targets are excluded from the default build; only the
# libraries the driver links are compiled.

cmake_minimum_required(VERSION 3.13)
project(birthmark_partB_longfellow CXX)
set(CMAKE_CXX_STANDARD 17)

if(NOT LONGFELLOW_SRC)
  message(FATAL_ERROR "set LONGFELLOW_SRC to the Longfellow-zk clone")
endif()

add_subdirectory(${LONGFELLOW_SRC}/lib longfellow EXCLUDE_FROM_ALL)

add_executable(sha256_zk_bench sha256_zk_bench.cc)
target_include_directories(sha256_zk_bench PRIVATE ${LONGFELLOW_SRC}/lib)
# Same architecture flags as the Longfellow libraries (ARCH_FLAGS is set in
# Longfellow's lib/CMakeLists.txt, after any change fetch_and_build.sh makes).
get_directory_property(LF_ARCH_FLAGS DIRECTORY ${LONGFELLOW_SRC}/lib DEFINITION ARCH_FLAGS)
target_compile_options(sha256_zk_bench PRIVATE ${LF_ARCH_FLAGS})
target_link_libraries(sha256_zk_bench PRIVATE flatsha ec algebra util crypto)
