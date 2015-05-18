# -*- coding: utf8 -*-

from PyQt4 import QtCore
import struct
import socket


class TCPServer(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, address):
        super(TCPServer, self).__init__()

        self.buff_size = 1024
        self.presentation_size = 2

        self.receive_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_Sock.bind(address)

    def start_listen(self):
        self.receive_Sock.listen(True)
        print "等待连接..."

        conn, address = self.receive_Sock.accept()
        print "客户端已连接—> ", address

        self.received_data(conn)

    def received_data(self, conn):
        command_length = struct.unpack('i', conn.recv(struct.calcsize('i')))[0]
        rest_length = command_length
        json = ""

        print "正在接收json文件..."

        while True:
            if rest_length > self.buff_size:
                json += conn.recv(self.buff_size)
                rest_length -= self.buff_size
            else:
                json += conn.recv(rest_length)
                break

        print "json文件接收完毕"
        self.trigger.emit(json)
        print "文件接收完毕,正在关闭连接"
        conn.close()
        # self.receive_Sock.close()
        print "连接已关闭..."

        self.start_listen()

    def run(self):
        self.start_listen()


class UDPClient():
    def __init__(self, address):
        self.address = address
        self.buff_size = 1024

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def udp_send(self, message):
        self.socket.sendto(message, self.address)