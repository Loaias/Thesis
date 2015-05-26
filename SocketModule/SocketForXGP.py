# -*- coding: utf8 -*-

from PyQt4 import QtCore
import socket


class UDPService(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str, str)

    def __init__(self, address):
        super(UDPService, self).__init__()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(address)

    def run(self):
        while True:
            received_message, address = self.socket.recvfrom(1024)
            self.trigger.emit(received_message, address[0])


class UDPClient:
    def __init__(self, address):
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_fitness(self, fitness_value):
        self.socket.sendto(fitness_value, self.address)
