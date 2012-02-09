#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PySide.QtGui import QApplication, QLabel

def main():
    app = QApplication(sys.argv)
    label = QLabel("Hello World from PySide", None)
    label.setWindowTitle("Hello World from PySide")
    label.resize(300, 300)
    label.show()
    app.exec_()

if __name__ == "__main__":
    main()
