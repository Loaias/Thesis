# -*- coding: utf8 -*-

from PyQt4 import QtCore
import struct
import socket


class Server(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, address):
        super(Server, self).__init__()

        self.buff_size = 1024
        self.presentation_size = 2

        self.receive_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_Sock.bind(address)

    def start_listen(self):
        self.receive_Sock.listen(True)
        conn, address = self.receive_Sock.accept()
        self.received_data(conn, address)

    def received_data(self, conn, address):
        command_length = struct.unpack('i', conn.recv(struct.calcsize('i')))[0]
        rest_length = command_length
        json = []

        print "正在接收json文件..."

        while True:
            if rest_length > self.buff_size:
                json.append(conn.recv(self.buff_size))
                rest_length -= self.buff_size
            else:
                json.append(conn.recv(rest_length))
                break

        print "json文件接收完毕"
        self.trigger.emit("".join(json))
        print "文件接收完毕,正在关闭连接"
        conn.close()
        # self.receive_Sock.close()
        print "连接已关闭..."

        self.start_listen()

    def run(self):
        self.start_listen()


class Client:
    def __init__(self, address):
        self.address = address
        self.buff_size = 1024

    def send_json(self, json):
        send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_sock.connect(self.address)

        command_length = len(json)
        package_count = (command_length + self.buff_size - 1) / self.buff_size
        data_head = struct.pack("i", command_length)

        print "start sending data:"
        send_sock.send(data_head)
        for i in xrange(package_count):
            index = self.buff_size * i
            send_sock.send(json[index:index + self.buff_size])
        print "Sending completed,closing connecting..."
        send_sock.close()
        print "Connecting closed..."
