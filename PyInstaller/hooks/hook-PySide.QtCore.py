import os
import platform
import sys

from PyInstaller.hooks.pyside_utils import pyside_plugins_binaries

def add_pyside_to_path():
    path_separator = ';'
    python_home= os.path.dirname(sys.executable)
    pyside_home= os.path.join(python_home, 'lib', 'site-packages', 'PySide')
    os.environ['PATH']= path_separator.join([pyside_home, os.environ['PATH']])

def hook(mod):
    if platform.system() == 'Windows':
        add_pyside_to_path()
    mod.binaries.extend(pyside_plugins_binaries('codecs'))
    return mod
