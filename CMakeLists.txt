cmake_minimum_required(VERSION 3.12)
project(CppApiFramework LANGUAGES CXX)

# 1. Force C++17 for modern features and pybind11 compatibility
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 2. Find Python first (Required to find pybind11)
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# 3. Dynamically locate pybind11 using the Python interpreter
# Try the modern flag first, then fallback to the legacy flag
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
    OUTPUT_VARIABLE pybind11_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
    ERROR_QUIET
)

if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmake
        OUTPUT_VARIABLE pybind11_DIR
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
endif()

# 4. Check if we actually found a path
if(NOT pybind11_DIR)
    message(FATAL_ERROR "pybind11 not found in Python environment. Run: pip install pybind11")
endif()

# Debug: Print the path in the logs so you can verify it in GitHub Actions
message(STATUS "Found pybind11 at: ${pybind11_DIR}")

# 5. Add the discovered path to CMake's search list
list(APPEND CMAKE_PREFIX_PATH "${pybind11_DIR}")
find_package(pybind11 REQUIRED)

# 6. Define the Python module
# 'cpp_api' is the name you will use in: import cpp_api
# 'core.cpp' is your C++ source file
pybind11_add_module(cpp_api core.cpp)

# 7. Optimization for Performance Profiling
# We use -O3 so your runtime benchmarks reflect production speeds
if(MSVC)
    target_compile_options(cpp_api PRIVATE /O2)
else()
    target_compile_options(cpp_api PRIVATE -O3)
endif()
