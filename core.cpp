#include <pybind11/pybind11.h>
using namespace std;

namespace py = pybind11

int heavy_computation(int input) {
    return input * input;
}

PYBIND11_MODULE(cpp_api, m) {
   m.def("compute", &heavy_computation, "A function that computes squares");
}
