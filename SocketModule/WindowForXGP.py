# -*- coding: utf8 -*-

from BaseSocketWindow import BaseWindow
from SocketForXGP import UDPService, UDPClient


class WindowForXGP(BaseWindow):
    def __init__(self):
        BaseWindow.__init__(self)

        # TCP Server
        self.xgp_server = UDPService(self.address_receive_XGP)
        self.xgp_server.trigger.connect(self.received)
        self.xgp_server.start()
        # UDP Client
        self.xgp_client = UDPClient(self.address_XGP)

    def received(self, data):
        print data
        self.plain_text_edit.setPlainText(data)
