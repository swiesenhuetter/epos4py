#include <pybind11/pybind11.h>
#include "Definitions.h"
#include <iostream>
#include <array>


namespace py = pybind11;

namespace epos_py{
    const uint64_t version{ 11 };
}


PYBIND11_MODULE(epos_py, m) {
    m.doc() = "Maxon Epos4 plugin"; // optional module docstring
    m.def("OpenDevice", &VCS_OpenDevice, "Open device");
    m.def("OpenDeviceDlg", &VCS_OpenDeviceDlg, "Service Dialog");
    m.def("CloseAllDevices", &VCS_CloseAllDevices, "Close All Devices");
    m.def("version", []() {return epos_py::version; });
}
