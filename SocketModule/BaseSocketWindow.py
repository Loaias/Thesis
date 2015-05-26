# -*- coding: utf8 -*-

from PyQt4 import QtGui
from Tool.enum import Windows, CallBack


class BaseWindow(QtGui.QWidget):
    def __init__(self):
        super(BaseWindow, self).__init__()

        self.address_MH = ("127.0.0.1", 6000)
        self.address_receive_MH = ("127.0.0.1", 6001)
        self.address_receive_XGP = ("172.20.71.28", 6002)
        self.address_XGP = ("172.20.71.39", 6003)

    def received(self, message, address):
        json = eval(str(message))
        window = None
        window_type = Windows.ec_window
        window_method = CallBack.individuals_received_from_xgp

        if "127.0.0.1" == address:
            window_type = json["Window"]
            window_method = json["CallBack"]

        for attr in self.__dict__:
            attr_type = type(self.__dict__[attr])
            attr_type = str(attr_type)
            if window_type in attr_type:
                window = self.__dict__[attr]
                break

        method = getattr(window, window_method)
        method(json)
