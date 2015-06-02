# # -*- coding: utf8 -*-
#
# import cPickle as pickle
# import os
# import numpy as np
#
# base_path = os.getcwd()
# base_path = os.path.join(base_path, "ConfigFiles")


# -*- coding: utf-8 -*-

import os
import time
import cPickle
import numpy as np

from tools import search_single_file
from Tool import Consts


def create_parts_files(base_path, json):
    parts = json["ReturnData"]

    for part in parts:
        file_name = os.path.join(base_path, "parts", "%s.npy" % part["Name"])
        np.save(file_name, part["Points"])
        print part["Count"]
        print "%s was saved." % file_name

    # models_list = json["ReturnData"]
    # models = np.array(models_list)
    # file_name = os.path.join(base_path, "parts", "%s.npy" % json["ShortName"])
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


def save_key_points_indices(base_path):
    path = os.path.join(base_path, "parts")
    indices = {}

    for key_point in Consts.KeyPoints.get_all_key_points():
        f = search_single_file(key_point.parts_name, path)
        raw_data = np.load(os.path.join(path, f))
        sorted_data = sorted(raw_data, key=lambda c: (c[key_point.coord] - key_point.coord_value) ** 2)
        indices[key_point.name] = int(sorted_data[0][0])

    with open(os.path.join(path, "indices"), 'w') as f:
        cPickle.dump(indices, f)

    print "key points indices file were created."


def create_mapping_files(base_path, json):
    return_dictionary = eval(str(json))
    feature_name = return_dictionary["ShortName"]

    return_data = return_dictionary["ReturnData"]

    file_name = "%s.npy" % feature_name
    mapping = Consts.Mappings.get_mapping_by_name(feature_name)
    mapping_table = []

    for data in return_data:
        genotype = data["Parameter"]
        key_points = data["KeyPoints"]
        phenotype = mapping.get_value(key_points)

        mapping_table.append((genotype, phenotype))

    np.save(os.path.join(base_path, "mapping", file_name), mapping_table)
    print "Saving complete: %s" % file_name

























#*******************************************************************************************

def create_files():
    import get_indices

    get_indices.init()
    param_coord_mapping_Ver3()

    raw_input("Create File Complete.")
#*******************************************************************************************

#*******************************************************************************************
def param_coord_map(sampling):
    from get_indices import finished_modify
    from tools import get_feature
    from core import G
    import humanmodifier

    with open("/home/loaias/Workspace/Python/MakeHuman/log/parts/indices", 'r') as f:
        indices = pickle.load(f)

    mapping=[
        ("eye-out", "eyes/l-eye-push1-in|out", 0),
        ("eye-in", "eyes/l-eye-push2-in|out", 0),
        ("eye-up", "eyes/l-eye-height2-min|max", 1),
        ("eye-bottom", "eyes/l-eye-height2-min|max", 1),
        ("mouth", "mouth/mouth-trans-up|down", 1),
        ("nose", "nose/nose-scale-vert-incr|decr", 1),
        ("nose-out", "nose/nose-scale-horiz-incr|decr", 0),
        ("forehead", "head/head-scale-vert-more|less", 1),
        ("chin", "head/head-scale-vert-more|less", 1),
        ("cheek", "head/head-scale-horiz-less|more", 0)
    ]

    h = G.app.selectedHuman
    params = np.linspace(-1, 1, sampling)

    for el in mapping:
        coord = []
        for param in params:
            modifier = h.getModifier(el[1])
            humanmodifier.ModifierAction(modifier, 0, param, finished_modify).do()
            mesh = h.mesh.__dict__["coord"]
            index = indices[el[0]]
            coord.append(mesh[index][el[2]])

        result = [params, coord]
        np.save("%s/mapping/%s.npy" % (base_path, el[0]), result)

    raw_input("Parameter-Coordinate Mapping Complete.")

def param_coord_mapping_Ver2(sampling=200):
    from get_indices import finished_modify
    from tools import get_feature
    from core import G
    import humanmodifier

    with open("/home/loaias/Workspace/Python/MakeHuman/log/parts/indices", 'r') as f:
        indices = pickle.load(f)

    mapping=[
        ("eye_width", ["eyes/l-eye-push1-in|out", "eyes/l-eye-push2-in|out"]),
        ("eye_height", "eyes/l-eye-height2-min|max"),
        ("eye_distance", "eyes/l-eye-move-in|out"),
        ("face_width", "head/head-scale-horiz-less|more"),
        ("face_height", "chin/chin-height-min|max"),
        ("nose_width", "nose/nose-scale-horiz-incr|decr"),
        ("forehead_to_nose", "nose/nose-scale-vert-incr|decr"),
        ("nose_to_mouth", "mouth/mouth-trans-up|down")
    ]

    h = G.app.selectedHuman
    params = np.linspace(-1, 1, sampling)

    for el in mapping:
        coord = []
        for param in params:
            if len(el[1]) == 2:
                modifier = h.getModifier(el[1][0])
                humanmodifier.ModifierAction(modifier, 0, param, finished_modify).do()
                modifier = h.getModifier(el[1][1])
                humanmodifier.ModifierAction(modifier, 0, -param, finished_modify).do()
            else:
                modifier = h.getModifier(el[1])
                humanmodifier.ModifierAction(modifier, 0, param, finished_modify).do()
            mesh = h.mesh.__dict__["coord"]
            coord.append(get_feature(el[0], mesh))

        result = [params, coord]
        np.save("%s/mapping_ver2/%s.npy" % (base_path, el[0]), result)

    raw_input("Parameter-Coordinate Mapping Complete.")

def param_coord_mapping_Ver3(sampling=20):
    from get_indices import finished_modify, get_feature
    from core import G
    import humanmodifier

    # with open("/home/loaias/Workspace/Python/MakeHuman/log/parts/indices", 'r') as f:
    #     indices = pickle.load(f)

    mapping = [
        ("eye-out", "eyes/l-eye-push1-in|out"),
        ("eye-in", "eyes/l-eye-push2-in|out"),
        ("eye-height", "eyes/l-eye-height2-min|max"),
        ("eye-distance", "eyes/l-eye-move-in|out"),
        ("face-width", "head/head-scale-horiz-less|more"),
        # ("face_height", "chin/chin-height-min|max"),
        ("face-height", "head/head-scale-vert-more|less"),
        ("nose-width", "nose/nose-scale-horiz-incr|decr"),
        ("nose-apex", "nose/nose-scale-vert-incr|decr"),
        ("mouth-middle", "mouth/mouth-trans-up|down")
    ]

    h = G.app.selectedHuman
    params = np.linspace(-1, 1, sampling)

    for el in mapping:
        parameter_feature_pairs = []
        for param in params:
            modifier = h.getModifier(el[1])
            humanmodifier.ModifierAction(modifier, 0, param, finished_modify).do()

            mesh = h.mesh.__dict__["coord"]
            feature = get_feature(el[0], mesh)
            parameter_feature_pairs.append((param, feature))

        np.save("%s/mapping_ver3/%s.npy" % (base_path, el[0]), parameter_feature_pairs)

    print("Parameter-Coordinate Mapping Complete.")
#*******************************************************************************************
