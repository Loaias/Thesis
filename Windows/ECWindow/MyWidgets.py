# -*- coding: utf-8 -*-

import numpy as np
from PyQt4 import QtGui, QtCore


class ImageBox(QtGui.QLabel):
    def __init__(self, index):
        super(ImageBox, self).__init__()

        self.index = index
        self.features = None

    def set_features(self, features):
        self.features = features

    def mousePressEvent(self, ev):
        button = ev.buttons()

        if button == QtCore.Qt.LeftButton:
            population = self.parent().population
            best = self.features
            fitness = []

            for individual in population:
                difference = individual - best
                distance = difference.dot(difference) + 10
                fitness.append(str(distance))

            fitness = ",".join(fitness)
            self.parent().parent.send_to_xgp(fitness)
        elif button == QtCore.Qt.RightButton:
            message_box = QtGui.QMessageBox()
            message_box.setText(str(self.features.tolist()))
            message_box.exec_()
