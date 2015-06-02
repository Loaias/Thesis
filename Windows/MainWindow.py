import os

from PyQt4 import QtGui
from SocketModule import WindowForMH, WindowForXGP
from Windows.ECWindow import Window as Evolver
from Windows.CreateWindow import Window as Creator
from Windows.FeatureViewer import Window as Viewer


class Window(WindowForMH, WindowForXGP):
    def __init__(self):
        WindowForMH.__init__(self)
        WindowForXGP.__init__(self)

        self.ec_window = Evolver(self)
        self.create_window = Creator(self)
        self.viewer_window = Viewer(self)

        self.base_path = os.getcwd()
        self.base_path = os.path.join(self.base_path, "ConfigFiles")

        v_box = QtGui.QVBoxLayout()

        # Create Files
        button = QtGui.QPushButton("Create Files")
        button.clicked.connect(self.start_creating_files)
        v_box.addWidget(button)

        # Set and Run EC
        button = QtGui.QPushButton("Start System")
        button.clicked.connect(self.start_system)
        v_box.addWidget(button)

        # Set and Run EC
        button = QtGui.QPushButton("View Features")
        button.clicked.connect(self.start_viewer)
        v_box.addWidget(button)

        self.setLayout(v_box)

    def start_creating_files(self):
        self.create_window.show()
        self.hide()

    def start_system(self):
        self.ec_window.show()
        self.hide()

    def start_viewer(self):
        self.viewer_window.show()
        self.hide()

    def send_to_mh(self, json):
        self.hm_client.send_json(json)

    def send_to_xgp(self, json):
        self.xgp_client.send_fitness(json)
