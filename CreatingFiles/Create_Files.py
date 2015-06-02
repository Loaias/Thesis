# -*- coding: utf-8 -*-

import numpy as np
import os

from Tool import search_single_file


def create_parts_files(base_path, json):
    try:
        print "start"
        a = 1/0
        print a
    except:
        print "aaa"

    try:
        return_data = eval(json)
        points = return_data["ReturnData"]
        file_name = os.path.join(base_path, "parts", "%s.npy" % return_data["Short"])
        np.save(file_name, points)
        print "%s was saved." % file_name
    except:
        raw_input()
    # return_data = eval(str(json))
    # models_list = return_data["ReturnData"]
    # models = np.array(models_list)
    # file_name = os.path.join(base_path, "parts", "%s.npy" % return_data["Short"])
    # points = []
    #
    # for index, (x, y, z) in enumerate(models[0]):
    #     diff = True
    #     for (x0, y0, z0) in models[1:, index, :]:
    #         if (x, y, z) == (x0, y0, z0):
    #             diff = False
    #             break
    #     if diff:
    #         points.append([index, x, y, z])
    #
    # np.save(file_name, points)
    # print "%s was saved." % file_name


def save_key_points_indices(base_path, key_points):
    path = os.path.join(base_path, "parts")
    indices = []

    for key_point in key_points.get_all_key_points():
        f = search_single_file(key_point.file_name, path)
        raw_data = np.load(os.path.join(path, f))
        sorted_data = sorted(raw_data, key=lambda c: (c[key_point.coord] - key_point.coord_value) ** 2)
        indices.append([key_point.name, np.int(sorted_data[0][0])])

    nd_indices = np.array(indices)

    file_name = os.path.join(path, "indices.npy")
    np.save(file_name, nd_indices)


def parameter_coord_mapping():
    pass