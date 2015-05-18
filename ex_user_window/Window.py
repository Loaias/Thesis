# -*- coding: utf8 -*-

from PyQt4 import QtGui
from Widget import ImageLabel
from const import PRESENTATION_SIZE
from core import G


class Window_Base(QtGui.QWidget):
    def __init__(self):
        super(Window_Base, self).__init__()

        self.setWindowTitle('User Windows')
        self.top_layout = QtGui.QHBoxLayout(self)

        self.images = []
        self.selected_radio = "general"

        self.create_left_frame()
        self.create_right_frame()

        self.setLayout(self.top_layout)

    def create_left_frame(self):
        v_box = QtGui.QVBoxLayout()

        radio = QtGui.QRadioButton("general", self)
        radio.setChecked(True)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        radio = QtGui.QRadioButton("eyes", self)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        radio = QtGui.QRadioButton("nose", self)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        radio = QtGui.QRadioButton("mouth", self)
        radio.clicked.connect(self.radio_click)
        v_box.addWidget(radio)

        v_box.addStretch(-1)

        self.top_layout.addLayout(v_box)

    def create_right_frame(self):
        pass

    def radio_click(self):
        self.selected_radio = self.sender().text()
        print self.selected_radio


class UIF(Window_Base):
    def __init__(self):
        self.app = G.app
        self.app.setFaceCamera()
        self.ga_helpers = {}

        self.ga_init()

        super(UIF, self).__init__()

    def ga_init(self):
        from GA_ver2 import Genetic_Algorithm
        from MyModifier import init_model

        init_model()
        self.ga_helpers["general"] = Genetic_Algorithm("general")
        self.ga_helpers["eyes"] = Genetic_Algorithm("eyes")
        self.ga_helpers["nose"] = Genetic_Algorithm("nose")
        self.ga_helpers["mouth"] = Genetic_Algorithm("mouth")

    def create_right_frame(self):
        grid = QtGui.QGridLayout(self)

        for i in xrange(PRESENTATION_SIZE):
            shower = ImageLabel(self)
            grid.addWidget(shower, i / 2, i % 2)
            # self.connect(shower, QtCore.SIGNAL('clicked()'), shower.image_clicked)

            shower.widget_index = i
            self.images.append(shower)

        self.top_layout.addLayout(grid)

        self.image_update()

    def image_update(self):
        if self.selected_radio == "general":
            from MyModifier import modify_model_by_eye

            ga_helper = self.ga_helpers["general"]

            for i, individual in enumerate(ga_helper.presentation):
                chromosome = individual["chromosome"]
                modify_model_by_eye(chromosome)
                self.app.setFaceCamera()
                self.images[i].show_image()
        elif self.selected_radio == "eyes":
            from MyModifier import modify_eyes

            ga_helper = self.ga_helpers["eyes"]

            for i, individual in enumerate(ga_helper.presentation):
                chromosome = individual["chromosome"]
                modify_eyes(chromosome)
                # self.app.setFaceCamera()
                self.images[i].show_image()
        else:
            from MyModifier import modify_model

            ga_helper = self.ga_helpers[unicode(self.selected_radio)]

            for i, individual in enumerate(ga_helper.presentation):
                chromosome = individual["chromosome"]
                modify_model(chromosome)
                # self.app.setFaceCamera()
                self.images[i].show_image()
            # for i in xrange(PRESENTATION_SIZE):
            #     modify_model_by_eye(eye_outs[i], eye_ins[i])
            #     self.app.setFaceCamera()
            #     self.images[i].show_image()

        # for index, gene in enumerate(self.ga_helper.get_presentation()):

        # for i, el in enumerate(self.ga_helper.get_presentation()):
        #     self.images[i].set_gene(el, self.slice)
        #     self.images[i].modify_model(self.slice)
        #     self.app.setFaceCamera()
        #     self.images[i].show_image()

    # def load_modifiers(self):
    #     self.modifiers = [
    #         "eyes/l-eye-push1-in|out",
    #         "eyes/r-eye-push1-in|out"
    #     ]
    #
    #     GA.GAHelper.set_gene_length(len(self.modifiers))
    #     self.ga_helper = GA.GAHelper()

    def closeEvent(self, ev):
        print "window is closed"
        QtGui.QApplication.quit()



# class UIF(QtGui.QWidget):
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
#
#         self.app = G.app
#         self.setWindowTitle('User Windows')
#
#         self.modifiers = []
#         self.ga_helper = None
#         self.load_modifiers()
#
#         self.app.setFaceCamera()
#
#         self.images = []
#         self.create()
#
#     def create(self):
#         grid = QtGui.QGridLayout(self)
#
#         for i, el in enumerate(self.ga_helper.get_presentation()):
#             shower = ImageLabel(self)
#             grid.addWidget(shower, i / 3, i % 3)
#             self.connect(shower, QtCore.SIGNAL('clicked()'), shower.image_clicked)
#
#             self.images.append(shower)
#
#         self.image_update()
#
#     def image_update(self):
#         for i, el in enumerate(self.ga_helper.get_presentation()):
#             self.images[i].set_gene(el)
#             self.images[i].modify_model()
#             self.images[i].show_image()
#
#     def load_modifiers(self):
#         # with open("./plugins/ex_user_window/modifiers", "r") as f:
#         #     for line in f:
#         #         if line[0] is not "#":
#         #             self.modifiers.append(line.rstrip())
#
#         self.modifiers = [
#             "eyes/l-eye-push1-in|out",
#             "eyes/r-eye-push1-in|out"
#         ]
#
#         GA.GAHelper.set_gene_length(len(self.modifiers))
#         self.ga_helper = GA.GAHelper()
#
#     def closeEvent(self, ev):
#         print "window is closed"
#         QtGui.QApplication.quit()