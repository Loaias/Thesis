# -*- coding: utf-8 -*-


import os
import numpy as np

from PyQt4 import QtGui
from Received import ReceiveWindow

from Tool.CommandCreator import Command
from Tool.enum import Method, CallBack
from Consts import Parts, KeyPoints


class Window(QtGui.QWidget, ReceiveWindow):
    def __init__(self, parent):
        super(Window, self).__init__()

        self.parent = parent
        self.base_path = os.path.join(os.getcwd(), "ConfigFiles")

        self.init_ui()

    def init_ui(self):
        v_box = QtGui.QVBoxLayout()

        btn = QtGui.QPushButton("Create Parts Files")
        btn.clicked.connect(self.send_request_for_creating_parts_files)
        v_box.addWidget(btn)

        btn = QtGui.QPushButton("Save Indices of Key Point")
        btn.clicked.connect(self.save_indices_of_key_points)
        v_box.addWidget(btn)

        btn = QtGui.QPushButton("Create Mapping Table")
        btn.clicked.connect(self.send_request_for_creating_mapping_tables)
        v_box.addWidget(btn)

        self.setLayout(v_box)

    def closeEvent(self, event):
        self.parent.show()

    def send_request_for_creating_parts_files(self):
        sampling = (-0.1, -0.05, 0, 0.05, 0.1)
        command = {
            "Method": Method.modify_and_get_models,
            "Window": "CreateWindow",
            "CallBack": CallBack.models_received,
            "Short": "",
            "Individuals": []
        }

        for part in Parts.get_all_parts():
            command["Individuals"] = [
                [Command.create_gene(part.long, c)] for c in sampling
            ]
            command["Short"] = part.short

            self.parent.send_to_mh(str(command))

    def save_indices_of_key_points(self):
        from CreatingFiles.Create_Files import save_key_points_indices

        save_key_points_indices(self.base_path, KeyPoints)

    def send_request_for_creating_mapping_tables(self):
        sampling = np.linspace(-1, 1, 20)
        command = {
            "Method": Method.modify_and_get_models,
            "Window": "CreateWindow",
            "CallBack": CallBack.models_received,
            "Short": "",
            "Individuals": []
        }
