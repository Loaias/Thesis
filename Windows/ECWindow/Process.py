# -*- coding: utf-8 -*-

import numpy as np

from Tool.enum import Windows, Method, CallBack
from Tool.CommandCreator import Command


class ProcessClass:
    def __init__(self):
        self.population = None

    def individuals_received_and_send_for_show(self, tuple_individuals):
        self.population = np.array([tuple_individuals[c*3:c*3+3] for c in xrange(len(tuple_individuals)/3)])

        indices = np.random.choice(len(self.population), self.presentation, replace=False)
        presentation = self.population[indices]

        for index, image in enumerate(self.image_labels):
            image.set_features(presentation[index])

        command = {
            "Method": Method.modify_and_get_images,
            "Window":  Windows.ec_window,
            "CallBack": CallBack.render_image,
            "Individuals": [
                Command.create_modifiers_for_eye_width(individual) for individual in presentation
            ]
        }

        command = str(command)
        print command
        self.parent.send_to_mh(command)



