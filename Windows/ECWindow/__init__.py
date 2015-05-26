# -*- coding: utf8 -*-

from PyQt4 import QtGui
from Received import ReceivedClass
from Process import ProcessClass
from MyWidgets import ImageBox
from Tool.enum import Windows, Method, CallBack


class Window(QtGui.QWidget, ReceivedClass, ProcessClass):
    def __init__(self, parent):
        super(Window, self).__init__()

        self.parent = parent

        self.presentation = 4
        self.image_labels = [ImageBox(c) for c in xrange(self.presentation)]
        self.plain_text_edit = None
        self.send_button = None

        self.init_ui()

    def init_ui(self):
        v_box = QtGui.QVBoxLayout(self)

        grid = QtGui.QGridLayout()
        v_box.addLayout(grid)

        for index, image in enumerate(self.image_labels):
            grid.addWidget(image, index / (self.presentation / 2), index % (self.presentation / 2))

        self.plain_text_edit = QtGui.QPlainTextEdit()
        v_box.addWidget(self.plain_text_edit)

        self.send_button = QtGui.QPushButton(u"送信")
        self.send_button.clicked.connect(self.send_button_click)
        v_box.addWidget(self.send_button)
        button = QtGui.QPushButton("Clear")
        button.clicked.connect(self.clear)
        v_box.addWidget(button)

        self.setLayout(v_box)

    def closeEvent(self, event):
        self.parent.show()

    def send_button_click(self):
        btn = self.sender()
        btn.setEnabled(False)

        command = {
            "Method": Method.modify_and_get_images,
            "Window":  Windows.ec_window,
            "CallBack": CallBack.render_image,
            "Parameters": (10, 20, 30),
            "Individuals": [
                [
                    {
                        "Modifier": "eyes/l-eye-height2-min|max",
                        "Value": 1
                    },
                    {
                        "Modifier": "eyes/l-eye-move-in|out",
                        "Value": 1
                    }
                ],
                [
                    {
                        "Modifier": "eyes/l-eye-height2-min|max",
                        "Value": -1
                    },
                    {
                        "Modifier": "eyes/l-eye-move-in|out",
                        "Value": -1
                    }
                ],
            ]
        }

        command_string = str(command)
        self.parent.send_to_mh(command_string)

    def clear(self):
        # pass
        self.send_button.setEnabled(True)

        for el in self.image_labels:
            el.clear()
