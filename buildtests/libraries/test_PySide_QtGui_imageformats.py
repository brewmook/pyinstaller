import os
import sys
from PySide.QtGui import QImageReader

image = 'tinysample.tiff'

if os.path.exists(image):
    reader = QImageReader(image)

    if reader.canRead():
        print "PASS: image format plugin available"
        status = 0
    else:
        print "FAIL: image format plugin NOT available (or file missing)"
        status = 1

else:
    print "ERROR: image file %s missing" % image
    status = 1

sys.exit(status)
