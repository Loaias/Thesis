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
        self.hm_client.udp_send(command_string)