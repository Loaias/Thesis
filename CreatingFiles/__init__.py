# -*- coding: utf8 -*-

import cPickle as pickle
import os
import numpy as np

base_path = os.getcwd()
base_path = os.path.join(base_path, "ConfigFiles")


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
