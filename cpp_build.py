from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension


setup_args = dict(
    name='epos_python',
    version='0.1.1',
    ext_modules=[
        Pybind11Extension(
            'epos_python.EposPy',
            ['epos_python/cpp_wrapper/CHRoco2.cpp'],
            libraries=['EposCmd64'],
            include_dirs=['epos_cmd/include'],
            library_dirs=['epos_cmd/lib'],
            py_limited_api=True,
            language='c++',
            ),
    ]
)

setup(**setup_args)
