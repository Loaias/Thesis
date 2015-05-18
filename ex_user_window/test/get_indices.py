__author__ = 'Loaias'


# from get_points_index import np, get_indices
import numpy as np
import os
base_path = "/home/loaias/Workspace/Python/MakeHuman/log"


#*******************************************************************************************
# import os
#
# def search_single_file(keyword, sub="parts", cond="in"):
#     for f in os.listdir("%s/%s" % (base_path, sub)):
#         if cond == "in":
#             if keyword in f:
#                 return f
from tools import search_single_file
#*******************************************************************************************

# *******************************************************************************************
import cPickle as pickle

def save_indices():
    points = {
        "eye-out": 0.4409,
        # "eye-in": 0.1881,
        "eye-in": 0.1624,
        # "eye-distance": 0.1424,
        "eye-distance": 0.1624,
        "eye-up": 7.3794,
        "eye-bottom": 7.3062,
        "mouth": 6.6934,
        "nose": 6.8723,
        "nose-out": 0.1697,
        "forehead": 8.3768,
        "chin": 6.2750,
        "cheek": 0.6575,
        "face-left": 0.6983
    }
    indices = {}

    # eye index
    f = search_single_file("eye_in")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[1] - points["eye-in"]) ** 2)
    indices["eye-in"] = np.int(sorted_data[0][0])
    sorted_data = sorted(raw_data, key=lambda c: (c[1] - points["eye-distance"]) ** 2)
    indices["eye-distance"] = np.int(sorted_data[0][0])

    f = search_single_file("eye_out")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[1] - points["eye-out"]) ** 2)
    indices["eye-out"] = np.int(sorted_data[0][0])

    f = search_single_file("eye_height")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[2] - points["eye-up"]) ** 2)
    indices["eye-up"] = np.int(sorted_data[0][0])
    sorted_data = sorted(raw_data, key=lambda c: (c[2] - points["eye-bottom"]) ** 2)
    indices["eye-bottom"] = np.int(sorted_data[0][0])

    # mouse index
    f = search_single_file("mouth")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[2] - points["mouth"]) ** 2)
    indices["mouth-middle"] = np.int(sorted_data[0][0])

    # nose index
    f = search_single_file("nose")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[2] - points["nose"]) ** 2)
    indices["nose-apex"] = np.int(sorted_data[0][0])
    # sorted_data = sorted(raw_data, key=lambda c: c[3])
    # indices["nose"] = np.int(sorted_data[-1][0])
    sorted_data = sorted(raw_data, key=lambda c: (c[1] - points["nose-out"]) ** 2)
    indices["nose-left"] = np.int(sorted_data[0][0])

    # forehead index
    f = search_single_file("forehead")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[2] - points["forehead"]) ** 2)
    indices["face-top"] = np.int(sorted_data[0][0])

    # chin index
    f = search_single_file("chin")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[2] - points["chin"]) ** 2)
    indices["face-bottom"] = np.int(sorted_data[0][0])

    # # cheek index
    # f = search_single_file("cheek")
    # raw_data = np.load("%s/parts/%s" % (base_path, f))
    # sorted_data = sorted(raw_data, key=lambda c: (c[1] - points["cheek"]) ** 2)
    # indices["cheek"] = np.int(sorted_data[0][0])

    # face index
    f = search_single_file("face")
    raw_data = np.load("%s/parts/%s" % (base_path, f))
    sorted_data = sorted(raw_data, key=lambda c: (c[1] - points["face-left"]) ** 2)
    indices["face-left"] = np.int(sorted_data[0][0])

    with open("%s/parts/indices" % base_path, 'w') as f:
        pickle.dump(indices, f)
    raw_input(indices)
    '''
    {
        'eye-up': 14796,
        'eye-bottom': 13368,
        'nose-left': 7053,
        'nose-apex': 343,
        'mouth-middle': 474,
        'eye-in': 7822,
        'eye-distance': 7822,
        'face-bottom': 926,
        'eye-out': 7859,
        'face-left': 12243,
        'face-top': 1025
    }
    '''
#*******************************************************************************************

#*******************************************************************************************
from core import G
import humanmodifier

def finished_modify():
    print "Changed."

def get_parts_models(str_modifier, sampling=(-0.1, -0.05, 0, 0.05, 0.1)):
    h = G.app.selectedHuman

    models = []
    print sampling

    for g in sampling:
        # for el in modifiers:
        #     modifier = h.getModifier(el)
        #     m_action = humanmodifier.ModifierAction(modifier, 0, g, finished_modify)
        #     m_action.do()
        modifier = h.getModifier(str_modifier)
        m_action = humanmodifier.ModifierAction(modifier, 0, g, finished_modify)
        m_action.do()

        m = h.mesh # [r_coord, coord, orig_coord]
        # md = h.meshData # [r_coord, coord, orig_coord]

        key = "coord" # keys = ["r_coord", "coord", "orig_coord"]

        model = []

        for (x,y,z) in m.__dict__[key]:
            model.append((x,y,z))
        models.append(model) # ['coord_-1.0', 'coord_0.0', 'coord_0.5', 'coord_1.0', 'coord_-0.5']
    return np.array(models)

def save_parts_npy(models, file_name):
    points = []

    for index, (x,y,z) in enumerate(models[0]):
        diff=True
        for (x0,y0,z0) in models[1:,index,:]:
            if (x,y,z) == (x0,y0,z0):
                diff=False
                break
        if diff:
            points.append([index, x, y, z])
            # points.append([index, (x,y,z)])

        # if all(models[1:,index,:].all(True)):
        #     points.append(index)
        # a=models[1:,index,:]==[x,y,z]
        # raw_input(all(a.all(True)))

    # np.savetxt("%s/parts/%s_%d" % (base_path, file_name, len(points)), points, fmt="%d,%.4f,%.4f,%.4f")
    np.save(os.path.join(base_path,"parts", "%s.npy" % file_name), points)
#*******************************************************************************************

#*******************************************************************************************
def get_feature(func_name, mesh=None):
    model = mesh
    if mesh is None:    # test mesh
        model = np.load(os.path.join(base_path, "parts/test_model.npy"))

    with open(os.path.join(base_path, "parts/indices"), 'r') as f:
        indices = pickle.load(f)

    if func_name == "eye-in":
        return model[indices["eye-in"]][0]
    if func_name == "eye-out":
        return model[indices["eye-out"]][0]
    if func_name == "eye-width":
        return model[indices["eye-out"]][0] - model[indices["eye-in"]][0]
    if func_name == "eye-distance":
        return model[indices["eye-distance"]][0] * 2
    if func_name == "eye-up":
        return model[indices["eye-up"]][1]
    if func_name == "eye-bottom":
        return model[indices["eye-bottom"]][1]
    if func_name == "eye-height":
        return model[indices["eye-up"]][1] - model[indices["eye-bottom"]][1]
    if func_name == "eye-bottom":
        return model[indices["eye-bottom"]][1]
    if func_name == "face-width":
        return model[indices["face-left"]][0] * 2
    if func_name == "face-top":
        return model[indices["face-top"]][1]
    if func_name == "face-bottom":
        return model[indices["face-bottom"]][1]
    if func_name == "face-height":
        return model[indices["face-top"]][1] - model[indices["face-bottom"]][1]
    if func_name == "nose-width":
        return model[indices["nose-left"]][0] * 2
    if func_name == "nose-apex":
        return model[indices["nose-apex"]][1]
    if func_name == "mouth-middle":
        return model[indices["mouth-middle"]][1]
#*******************************************************************************************

#*******************************************************************************************
def init():
    # Save Test Mesh
    mesh = G.app.selectedHuman.mesh.__dict__["coord"]
    np.save("%s/parts/test_model.npy" % base_path, mesh)

    # Save Parts {
    models = get_parts_models("eyes/l-eye-push1-in|out")
    save_parts_npy(models, "eye_out")
    models = get_parts_models("eyes/l-eye-push2-in|out")
    save_parts_npy(models, "eye_in")
    models = get_parts_models("eyes/l-eye-height2-min|max")
    save_parts_npy(models, "eye_height")

    models = get_parts_models("chin/chin-prominent-less|more")
    save_parts_npy(models, "chin")

    models = get_parts_models("forehead/forehead-trans-depth-forward|backward")
    save_parts_npy(models, "forehead")

    models = get_parts_models("nose/nose-scale-depth-incr|decr")
    save_parts_npy(models, "nose")

    models = get_parts_models("mouth/mouth-scale-vert-incr|decr")
    save_parts_npy(models, "mouth")

    # models = get_parts_models("cheek/l-cheek-bones-in|out")
    # save_parts_npy(models, "cheek")
    models = get_parts_models("head/head-scale-horiz-less|more")
    save_parts_npy(models, "face")
    # }

    save_indices()
#*******************************************************************************************