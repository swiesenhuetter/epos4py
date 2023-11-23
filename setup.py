from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
from setuptools.command.install_lib import install_lib as OriginalInstall
from Cython.Build import cythonize
from pathlib import Path
import sysconfig

ext_files = ["epos_python/__main__.py", "epos_python/__init__.py"]

def get_export_symbols_fix(self, ext_module):
    """
    Fix for export symbols for Windows
    Needed to compile __init__.py files
    """
    names = ext_module.name.split('.')
    if names[-1] != "__init__":
        initfunc_name = "PyInit_" + names[-1]
    else:
        # take name of the package if it is an __init__-file
        initfunc_name = "PyInit_" + names[-2]
    if initfunc_name not in ext_module.export_symbols:
        ext_module.export_symbols.append(initfunc_name)
    return ext_module.export_symbols


# replace wrong version with the fixed:
build_ext.get_export_symbols = get_export_symbols_fix


class BinaryOnlyInstall(OriginalInstall):
    def install(self):
        """
        if a pyd file with the same name as a py file in the build folder exists, remove source file
        """
        py_files = Path(self.build_dir).rglob("*.py")
        pyd_files = Path(self.build_dir).rglob("*.pyd")
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        for py_file in py_files:
            pyd_path = Path(str(py_file).replace(".py", ext_suffix))
            if pyd_path in pyd_files:
                print(f"--> compiled version of {py_file} exists, delete source")
                Path.unlink(py_file)
        OriginalInstall.install(self)


setup(
    name='epos_python',
    ext_modules=cythonize(ext_files,
                          build_dir="build",
                          force=True,
                          compiler_directives={'language_level': "3"}),
    cmdclass={'install_lib': BinaryOnlyInstall},
    package_data={
        'epos_python': ['lib/*.dll', '*.pyd']
    },
    packages=find_packages(),
)
