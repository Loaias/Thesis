# -*- coding: utf8 -*-

from PyQt4 import QtGui
from Received import ReceiveWindow
from Tool.enum import Method, CallBack


class Window(QtGui.QWidget, ReceiveWindow):
    def __init__(self, parent):
        super(Window, self).__init__()

        self.parent = parent

        self.image_labels = []
        self.plain_text_edit = None
        self.send_button = None

        self.init_ui()

    def init_ui(self):
        v_box = QtGui.QVBoxLayout(self)

        h_box = QtGui.QHBoxLayout()
        v_box.addLayout(h_box)

        image = QtGui.QLabel(self)
        self.image_labels.append(image)
        h_box.addWidget(image)
        image = QtGui.QLabel(self)
        self.image_labels.append(image)
        h_box.addWidget(image)

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
            "Window": "ECWindow",
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