import os

from PyQt4 import QtGui
from SocketModule import WindowForMH, WindowForXGP
from Windows.ECWindow import Window as Evolver
from Windows.CreateWindow import Window as Creator


class Window(WindowForMH, WindowForXGP):
    def __init__(self):
        WindowForMH.__init__(self)
        WindowForXGP.__init__(self)

        self.ec_window = Evolver(self)
        self.create_window = Creator(self)

        self.base_path = os.getcwd()
        self.base_path = os.path.join(self.base_path, "ConfigFiles")

        v_box = QtGui.QVBoxLayout()

        # Create Files
        btn_create_files = QtGui.QPushButton("Create Files")
        btn_create_files.clicked.connect(self.start_creating_files)
        v_box.addWidget(btn_create_files)

        # Set and Run EC
        btn_create_files = QtGui.QPushButton("Start System")
        btn_create_files.clicked.connect(self.start_system)
        v_box.addWidget(btn_create_files)

        self.setLayout(v_box)

    def start_creating_files(self):
        self.create_window.show()
        self.hide()

    def start_system(self):
        self.ec_window.show()
        self.hide()

    def send_to_mh(self, json):
        self.hm_client.send_json(json)

    def send_to_xgp(self, json):
        pass
