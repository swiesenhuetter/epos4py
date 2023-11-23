from glob import glob
from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "epos_python.epos_py",
        sorted(glob("cpp_wrapper/*.cpp")),  # Sort source files for reproducibility
        libraries=['EposCmd64'],
        include_dirs=[r"epos_python\include"],
        library_dirs=[r'epos_python\lib'],
    ),
]

setup(ext_modules=ext_modules,
      package_data={
          'epos_python': ['lib/*.dll', '*.pyd']
      },
      packages=find_packages(),
    )


