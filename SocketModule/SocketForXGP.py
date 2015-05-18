# -*- coding: utf8 -*-

from PyQt4 import QtCore
import socket


class UDPService(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, address):
        super(UDPService, self).__init__()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(address)

    def run(self):
        while True:
            received_message, address = self.socket.recvfrom(1024)
            print "received_message->   ", received_message
            print "address->    ", address

            self.trigger.emit(received_message)


class UDPClient():
    def __init__(self, address):
        self.address = address
        self.buff_size = 1024

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def udp_send(self, fitness_value):
        self.socket.sendto(fitness_value, self.address)