# -*- coding: utf8 -*-

from PyQt4 import QtGui


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        super(BaseWindow, self).__init__()

        self.address_MH = ("127.0.0.1", 6000)
        self.address_receive_MH = ("127.0.0.1", 6001)
        self.address_receive_XGP = ("127.0.0.1", 6002)
        self.address_XGP = ("127.0.0.1", 6003)

    def send(self, command):
        command_string = str(command)
        self.hm_client.send_json(command_string)

    def received(self, json):
        command = eval(str(json))
        window = None

        for attr in self.__dict__:
            attr_type = type(self.__dict__[attr])
            attr_type = str(attr_type)
            if command["Window"] in attr_type:
                window = self.__dict__[attr]
                break

        method = getattr(window, command["CallBack"])
        method(json)
