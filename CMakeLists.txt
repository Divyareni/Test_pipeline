cmake_minimum_required(VERSION 3.12)
project(CppApiFramework LANGUAGES CXX)

# 1. Force C++17 for modern features and pybind11 compatibility
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 2. Find Python first (Required to find pybind11)
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# 3. Dynamically locate pybind11 using the Python interpreter
# This solves the "Could not find a package configuration file" error
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmake
    OUTPUT_VARIABLE pybind11_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    RESULT_VARIABLE pybind11_FOUND_RESULT
)

# Error handling if pybind11 isn't installed in the environment
if(NOT pybind11_FOUND_RESULT EQUAL 0)
    message(FATAL_ERROR "pybind11 not found. Please run: pip install pybind11")
endif()

# 4. Add the discovered path to CMake's search list
list(APPEND CMAKE_PREFIX_PATH "${pybind11_DIR}")
find_package(pybind11 REQUIRED)

# 5. Define the Python module
# 'cpp_api' is the name you will use in: import cpp_api
# 'core.cpp' is your C++ source file
pybind11_add_module(cpp_api core.cpp)

# 6. Optimization for Performance Profiling
# In an interview, mention that you use -O3 so your runtime 
# benchmarks reflect production speeds, not debug speeds.
if(MSVC)
    target_compile_options(cpp_api PRIVATE /O2)
else()
    target_compile_options(cpp_api PRIVATE -O3)
endif()
