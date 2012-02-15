import sys
from PySide.QtCore import QTextCodec

if QTextCodec.codecForName("SHIFT_JIS") is None:
    print 'FAIL'
    exitcode = 1
else:
    print 'PASS'
    exitcode = 0

sys.exit(exitcode)
