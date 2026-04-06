cmake_minimum_required(VERSION 3.12)
project(CppApiFramework)

# 1. Set C++ Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 2. Find dependencies
# This looks for the pybind11 package on the system
find_package(pybind11 REQUIRED)

# 3. Define the Python Module
# 'cpp_api' is the name you use when typing 'import cpp_api' in Python
# 'core.cpp' is your source file containing the C++ logic
pybind11_add_module(cpp_api core.cpp)

# 4. (Optional) Runtime Profiling Optimization
# Ensuring the compiler optimizes for speed so profiling is accurate
target_compile_options(cpp_api PRIVATE -O3)
