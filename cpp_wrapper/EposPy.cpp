#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "Definitions.h"
#include <iostream>
#include <array>

namespace py = pybind11;

namespace epos_py{
    const uint64_t version{ 1 };
}

PYBIND11_MODULE(EposPy, m) {
    m.doc() = "Maxon Epos4 plugin"; // optional module docstring
    m.def("OpenDevice", &VCS_OpenDevice, "Open device");
    m.def("CloseAllDevices", &VCS_CloseAllDevices, "Close All Devices");

    py::register_exception<Chr2Exception>(m, "Chr2Exception");
}
