# -*- coding: utf8 -*-

import sys
from Windows import Window
from PyQt4 import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()