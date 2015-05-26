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
