# -*- coding:utf8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from PyQt4 import QtGui
from Tool.Consts import Parts
from Tool import search_single_file


class Window(QtGui.QWidget):
    def __init__(self, parent):
        super(Window, self).__init__()

        self.parent = parent
        self.base_path = os.path.join(os.getcwd(), "ConfigFiles")

        self.parts_name = QtGui.QComboBox()
        self.coordinate = QtGui.QComboBox()

        self.init_ui()

    def init_ui(self):
        v_box = QtGui.QVBoxLayout()

        # Begin: Show Points of Parts
        h_box = QtGui.QHBoxLayout()
        label = QtGui.QLabel("Parts:")
        h_box.addWidget(label)
        for parts in Parts.get_all_parts():
            self.parts_name.addItem(parts.name)
        h_box.addWidget(self.parts_name)

        label = QtGui.QLabel("Coordinate:")
        h_box.addWidget(label)
        self.coordinate.addItem("xy")
        self.coordinate.addItem("zy")
        self.coordinate.addItem("xz")
        h_box.addWidget(self.coordinate)

        v_box.addLayout(h_box)

        btn = QtGui.QPushButton("Show Points of Parts")
        btn.clicked.connect(self.show_points_of_parts)
        v_box.addWidget(btn)
        # End

        btn = QtGui.QPushButton("Save Indices of Key Point")
        # btn.clicked.connect(self.save_indices_of_key_points)
        v_box.addWidget(btn)

        btn = QtGui.QPushButton("Create Mapping Table")
        # btn.clicked.connect(self.send_request_for_creating_mapping_tables)
        v_box.addWidget(btn)

        self.setLayout(v_box)

    def show_points_of_parts(self):
        path = os.path.join(self.base_path, "Parts")
        name = str(self.parts_name.currentText())
        coordinate = str(self.coordinate.currentText())

        f = search_single_file(name, path)
        raw_data = np.load(os.path.join(path, f))

        x, y, z = raw_data[:, 1], raw_data[:, 2], raw_data[:, 3]

        if coordinate == "xy":
            plt.scatter(x, y, s=5, marker=(5, 3))

            plt.xlim(min(x), max(x))
            plt.ylim(min(y), max(y))
        if coordinate == "zy":
            plt.scatter(z, y, s=5, marker=(5, 3))

            plt.xlim(min(z), max(z))
            plt.ylim(min(y), max(y))

        if coordinate == "xz":
            plt.scatter(x, z, s=5, marker=(5, 3))

            plt.xlim(min(x), max(x))
            plt.ylim(min(z), max(z))

        plt.show()
