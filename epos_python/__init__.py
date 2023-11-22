import os
import sys
package_path = os.path.dirname(__file__)
sys.path.append(os.path.join(package_path))
os.add_dll_directory(os.path.join(package_path, 'lib'))

from .EposPy import *
