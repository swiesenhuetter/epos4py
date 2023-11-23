from os import path, add_dll_directory
import sys
sys.path.append(path.dirname(__file__))
package_path = path.dirname(__file__)
add_dll_directory(path.join(package_path, 'lib'))
print(f"you are here: {__file__}")

import epos_python


v = epos_python.epos_py.version()

print('c++ extension version {} loaded'.format(v))


