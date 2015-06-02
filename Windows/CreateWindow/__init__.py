# -*- coding: utf-8 -*-


import os
import numpy as np
from PyQt4 import QtGui

from Tool import Consts
from Received import ReceiveWindow
from Tool.CommandCreator import Command
from Tool.enum import Windows, Method, CallBack


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
            "Window": Windows.create_window,
            "CallBack": CallBack.models_for_parts_received,
            "Parts": []
        }

        for part in Consts.Parts.get_all_parts():
            command["Parts"].append(
                {
                    "Individuals": [
                        [Command.create_modifier(part.modifier, c)] for c in sampling
                    ],
                    "ShortName": part.name
                }
            )

        self.parent.send_to_mh(str(command))

    def save_indices_of_key_points(self):
        from CreatingFiles import save_key_points_indices

        save_key_points_indices(self.base_path)

    def send_request_for_creating_mapping_tables(self):
        import cPickle

        samplings = np.linspace(-1, 1, 200)
        with open(os.path.join(self.base_path, "parts/indices"), 'r') as f:
            indices = cPickle.load(f)

        command = {
            "Method": Method.modify_and_get_mappings,
            "Window": "CreateWindow",
            "CallBack": CallBack.models_for_mapping_received,
        }
        self.parent.send_to_mh(str(command))

        for mapping in Consts.Mappings.get_all_mapping_pair():
            command["Parameter"] = [{"name": k.name, "index": indices[k.name]} for k in mapping.key_points]
            command["Individuals"] = [
                [Command.create_modifier(mapping.modifier, round(c, 2))] for c in samplings
            ]
            command["ShortName"] = mapping.name

            self.parent.send_to_mh(str(command))



