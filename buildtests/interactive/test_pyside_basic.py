#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PySide import QtCore, QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    formats = [unicode(format).lower() for format in QtGui.QImageReader.supportedImageFormats()]

    print "Qt plugin paths: " + unicode(list(app.libraryPaths()))
    print "Qt image read support: " + ', '.join(formats)
    print 'Qt Libraries path: ' + unicode(QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibrariesPath))
    label = QtGui.QLabel("Hello World from PySide", None)
    label.setWindowTitle("Hello World from PySide")
    label.resize(300, 300)
    label.show()
    app.exec_()

if __name__ == "__main__":
    main()
