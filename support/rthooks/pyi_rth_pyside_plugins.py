# PySide plugins are bundled as data files (see hooks/hook-PySide*),
# within a "pyside_plugins" directory.
# We add a runtime hook to tell Qt where to find them.

import os
import sys

d = "pyside_plugins"
d = os.path.join(sys._MEIPASS, d)


# We remove QT_PLUGIN_PATH variable, beasuse we want Qt4 to load
# plugins only from one path.
if 'QT_PLUGIN_PATH' in os.environ:
    del os.environ['QT_PLUGIN_PATH']

# We cannot use QT_PLUGIN_PATH here, because it would not work when
# PyQt4 is compiled with a different CRT from Python (eg: it happens
# with Riverbank's GPL package).
from PySide.QtCore import QCoreApplication
# We set "pyside_plugins" as only one path for Qt4 plugins
QCoreApplication.setLibraryPaths([os.path.abspath(d)])
