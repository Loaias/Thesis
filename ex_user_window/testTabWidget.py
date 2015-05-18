__author__ = 'loaias'

from PyQt4 import QtGui
import sys


class Window_Base(QtGui.QWidget):
    def __init__(self):
        super(Window_Base, self).__init__()

        self.setWindowTitle('User Windows')
        self.top_layout = QtGui.QHBoxLayout(self)

        self.images = []

        self.create_left_frame()
        self.create_right_frame()

        self.setLayout(self.top_layout)

    def create_left_frame(self):
        v_box = QtGui.QVBoxLayout()

        radio = QtGui.QRadioButton("aaa", self)
        radio.setChecked(True)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        radio = QtGui.QRadioButton("bbb", self)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        radio = QtGui.QRadioButton("ccc", self)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        radio = QtGui.QRadioButton("ddd", self)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        self.top_layout.addLayout(v_box)

    def create_right_frame(self):
        pass

    def radio_click(self):
        print self.sender().text()


class MainWindow(Window_Base):
    def __init__(self):
        super(MainWindow, self).__init__()

    def create_right_frame(self):
        btn = QtGui.QPushButton("Button created by MainWindow")
        self.top_layout.addWidget(btn)

    def radio_click(self):
        print "Here is MainWindow"
        print self.sender().text()


def main():
    app = QtGui.QApplication(sys.argv)

    win = MainWindow()

    win.show()

    sys.exit(app.exec_())

# def main():
#     app = QtGui.QApplication(sys.argv)
#
#     win = QtGui.QWidget()
#
#     v_box = QtGui.QVBoxLayout(win)
#
#     r = QtGui.QRadioButton("Hello", win)
#     r.setChecked(True)
#     r.clicked.connect(lambda :radio_clicked("r1"))
#     v_box.addWidget(r)
#     r = QtGui.QRadioButton("World", win)
#     r.clicked.connect(lambda :radio_clicked("r2"))
#     v_box.addWidget(r)
#     r = QtGui.QRadioButton("Ciao", win)
#     r.clicked.connect(lambda :radio_clicked("r3"))
#     v_box.addWidget(r)
#
#     win.show()
#
#     sys.exit(app.exec_())

def radio_clicked(self):
    print self

if __name__ == "__main__":
    main()

