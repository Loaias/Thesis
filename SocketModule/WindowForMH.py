# -*- coding: utf8 -*-

from BaseSocketWindow import BaseWindow
from SocketForMH import Server, Client


class WindowForMH(BaseWindow):
    def __init__(self):
        BaseWindow.__init__(self)

        # TCP Server
        self.hm_server = Server(self.address_receive_MH)
        self.hm_server.trigger.connect(self.received)
        self.hm_server.start()
        # UDP Client
        self.hm_client = Client(self.address_MH)

    # def received(self, json):
    #     command = eval(str(json))
    #     window = None
    #
    #     for attr in self.__dict__:
    #         attr_type = type(self.__dict__[attr])
    #         attr_type = str(attr_type)
    #         if command["Window"] in attr_type:
    #             window = self.__dict__[attr]
    #             break
    #
    #     method = getattr(window, command["CallBack"])
    #     method(json)
