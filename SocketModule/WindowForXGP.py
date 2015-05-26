# -*- coding: utf8 -*-

from BaseSocketWindow import BaseWindow
from SocketForXGP import UDPService, UDPClient


class WindowForXGP(BaseWindow):
    def __init__(self):
        BaseWindow.__init__(self)

        # UDP Server
        self.xgp_server = UDPService(self.address_receive_XGP)
        self.xgp_server.trigger.connect(self.received)
        self.xgp_server.start()
        # UDP Client
        self.xgp_client = UDPClient(self.address_XGP)
