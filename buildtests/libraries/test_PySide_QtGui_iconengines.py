import sys
from PySide.QtGui import QApplication, QIcon

app = QApplication([])
icon = QIcon('test_PySide_QtGui_iconengines.svg')

if icon.pixmap(1,1).toImage().pixel(0,0) == 0xFF0000FF:
    print "PASS: pixel was blue"
    status = 0
else:
    print "FAIL: pixel was not blue"
    status = 1

sys.exit(status)
