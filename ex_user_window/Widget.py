__author__ = 'loaias'

from PyQt4 import QtGui, QtCore
import numpy as np
import os

from core import G
import material
import image
import image_operations as imgop
import projection
import mh

import humanmodifier


class ImageLabel(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QLabel.__init__(self)

        self.setFrameShape(QtGui.QFrame.Box)
        self.widget_index = 0
        self.parent = parent

    def show_image(self):
        # Render Image
        img = my_render()

        # Show Image
        pixel_map = QtGui.QPixmap.fromImage(img.toQImage())
        self.setPixmap(pixel_map)

    def mousePressEvent(self, ev):
        button = ev.buttons()
        print "mouse press event. Index:", self.widget_index
        print "button:", button

        modifier_label = unicode(self.parent.selected_radio)
        ga_helper = self.parent.ga_helpers[modifier_label]

        if button == QtCore.Qt.LeftButton:
            ga_helper.do_evolve(self.widget_index)
            self.parent.image_update()
        elif button == QtCore.Qt.RightButton:
            chromosome = ga_helper.presentation[self.widget_index]
            message_box = QtGui.QMessageBox()
            message_box.setText(str(chromosome))
            message_box.exec_()


def my_render(settings=None):
    if settings is None:
        settings = {'AA': True, 'lightmapSSS': False, 'scene': G.app.scene, 'dimensions': (230, 230)}

    if settings['lightmapSSS']:
        human = G.app.selectedHuman
        material_backup = material.Material(human.material)

        diffuse = imgop.Image(data=human.material.diffuseTexture)
        lmap = projection.mapSceneLighting(settings['scene'], border=human.material.sssRScale)
        lmapG = imgop.blurred(lmap, human.material.sssGScale, 13)
        lmapR = imgop.blurred(lmap, human.material.sssRScale, 13)
        lmap = imgop.compose([lmapR, lmapG, lmap])

        if not diffuse.isEmpty:
            lmap = imgop.resized(lmap, diffuse.width, diffuse.height, filter=image.FILTER_BILINEAR)
            lmap = imgop.multiply(lmap, diffuse)
            lmap.sourcePath = "Internal_Renderer_Lightmap_SSS_Texture"

        human.material.diffuseTexture = lmap
        human.configureShading(diffuse=True)
        human.shadeless = True

    if not mh.hasRenderToRenderbuffer():
        img = mh.grabScreen(0, 0, G.windowWidth, G.windowHeight)
        alphaImg = None
    else:
        width, height = settings['dimensions']
        if settings['AA']:
            width *= 2
            height *= 2

            img = mh.renderToBuffer(width, height)
            alphaImg = mh.renderAlphaMask(width, height)
            img = imgop.addAlpha(img, imgop.getChannel(alphaImg, 0))

        if settings['AA']:
            img = img.resized(width/2, height/2, filter=image.FILTER_BILINEAR)
            img.data[:, :, :] = img.data[:, :, (2, 1, 0, 3)]

    if settings['lightmapSSS']:
        human.material = material_backup

    return img



# def my_render(settings=None):
#     if settings is None:
#         settings = {'AA': True, 'lightmapSSS': False, 'scene': G.app.scene, 'dimensions': (230, 230)}
#
#     if settings['lightmapSSS']:
#         human = G.app.selectedHuman
#         material_backup = material.Material(human.material)
#
#         diffuse = imgop.Image(data=human.material.diffuseTexture)
#         lmap = projection.mapSceneLighting(settings['scene'], border=human.material.sssRScale)
#         lmapG = imgop.blurred(lmap, human.material.sssGScale, 13)
#         lmapR = imgop.blurred(lmap, human.material.sssRScale, 13)
#         lmap = imgop.compose([lmapR, lmapG, lmap])
#
#         if not diffuse.isEmpty:
#             lmap = imgop.resized(lmap, diffuse.width, diffuse.height, filter=image.FILTER_BILINEAR)
#             lmap = imgop.multiply(lmap, diffuse)
#             lmap.sourcePath = "Internal_Renderer_Lightmap_SSS_Texture"
#
#         human.material.diffuseTexture = lmap
#         human.configureShading(diffuse=True)
#         human.shadeless = True
#
#     if not mh.hasRenderToRenderbuffer():
#         img = mh.grabScreen(0, 0, G.windowWidth, G.windowHeight)
#         alphaImg = None
#     else:
#         width, height = settings['dimensions']
#         if settings['AA']:
#             width = width * 2
#             height = height * 2
#
#             img = mh.renderToBuffer(width, height)
#             alphaImg = mh.renderAlphaMask(width, height)
#             img = imgop.addAlpha(img, imgop.getChannel(alphaImg, 0))
#
#         if settings['AA']:
#             img = img.resized(width/2, height/2, filter=image.FILTER_BILINEAR)
#             img.data[:, :, :] = img.data[:, :, (2, 1, 0, 3)]
#
#     if settings['lightmapSSS']:
#         human.material = material_backup
#
#     return img