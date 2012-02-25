import sys
from PySide.QtCore import QSize
from PySide.QtGui import QApplication, QIcon

app = QApplication([])
icon = QIcon('test_PySide_QtGui_iconengines.svg')
pixmap = icon.pixmap(1,1)
pixel = pixmap.toImage().pixel(0,0)

if pixel != 0xFF0000FF:
    print "FAIL: pixel should be blue"
    status = 1
else:
    print "PASS: pixel was blue"
    status = 0

sys.exit(status)
