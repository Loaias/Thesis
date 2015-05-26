# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from Tool import decode_image


class ReceivedClass:
    def __init__(self):
        pass

    def render_image(self, json):
        command = eval(str(json))
        for lt, image_data in enumerate(command["ReturnData"]):
            image = decode_image(image_data)

            pix = QtGui.QPixmap()
            pix.loadFromData(image)
            self.image_labels[lt].setPixmap(pix)

    def points_received(self, json):
        self.plain_text_edit.setPlainText(json)

    def individuals_received_from_xgp(self, tuple_individuals):
        self.individuals_received_and_send_for_show(tuple_individuals)
