__author__ = 'loaias'

# import numpy as np
#
#
# base_path = "/home/loaias/Workspace/Python/log"
# #*******************************************************************************************
# def get_log(h, gene):
#     import os
#
#     m = h.mesh # r_coord, coord, orig_coord
#     # md = h.meshData # r_coord, coord, orig_coord
#
#     key = "coord" # keys = ["r_coord", "coord", "orig_coord"]
#
#     file_name = '%s/%s_%.1f' % (base_path, key, gene)
#     points = []
#
#     for x, y, z in m.__dict__[key]:
#         points.append([x, y, z])
#         # f.write("(%05d, [%+.2f    %+.2f    %+.2f])\n" % (i, x, y, z))
#     return points
#
#     with open(file_name, "w") as f:
#         for i, (x, y, z) in enumerate(m.__dict__[key]):
#             f.write("(%05d, [%+.2f    %+.2f    %+.2f])\n" % (i, x, y, z))
#         f.close()
#         print 'File output.'
# #*******************************************************************************************
#
#
# #*******************************************************************************************
# import humanmodifier
# from PyQt4 import QtGui
#
# GENE_LENGTH = 6
# modifier_list = [
#     # "eyes/r-eye-height1-min|max",
#     # "eyes/r-eye-height2-min|max",
#     # "eyes/r-eye-height3-min|max",
#     # "eyes/r-eye-push1-in|out",
#     # "eyes/r-eye-push2-in|out"
#     # "eyes/r-eye-move-in|out",
#     # "eyes/r-eye-move-up|down",
#       "eyes/r-eye-size-small|big",
#     # "eyes/r-eye-corner1-up|down",
#     # "eyes/r-eye-corner2-up|down",
#     #
#     # "eyes/l-eye-height1-min|max",
#     # "eyes/l-eye-height2-min|max",
#     # "eyes/l-eye-height3-min|max",
#     # "eyes/l-eye-push1-in|out",
#     # "eyes/l-eye-push2-in|out",
#     # "eyes/l-eye-move-in|out",
#     # "eyes/l-eye-move-up|down",
#     # "eyes/l-eye-size-small|big",
#     # "eyes/l-eye-corner1-up|down",
#     # "eyes/l-eye-corner2-up|down"
# ]
#
# h = G.app.selectedHuman
# models = []
#
# for g in [-1, -0.5, 0, 0.5, 1]:
#     for el in modifier_list:
#         modifier = h.getModifier(el)
#         m_action = humanmodifier.ModifierAction(modifier, 0, g, finished_modify)
#         m_action.do()
#
#     models.append(get_log(h, g)) # ['coord_-1.0', 'coord_0.0', 'coord_0.5', 'coord_1.0', 'coord_-0.5']
#
# #*******************************************************************************************
#
# #*******************************************************************************************
# (a,b,c,d,e) = models
# points_eye = []
# for index, (x,y,z) in enumerate(a):
#     diff = True
#
#     for (xo,yo,zo) in (b[index], c[index], d[index], e[index]):
#         if (x,y,z) == (xo,yo,zo):
#             diff=False
#             continue
#
#     if diff:
#         points_eye.append(index)
#
# np.savetxt(base_path+"/diff_r_eye", points_eye, fmt="%d")
#
# from compare import *
#
# r = get_l_r_eye_width(a)
# print "a->", r
# # print "b->", get_l_r_eye_width(b)
# # print "c->", get_l_r_eye_width(c)
# # print "d->", get_l_r_eye_width(d)
# # print "e->", get_l_r_eye_width(e)
#
# # na = np.array(a)
# # pna = na[points_eye]
# # print pna[:,0]
# # (l,r) = (max(pna[:,0]),(min(pna[:,0])))
# # print "width of a(right eye): %.4f" % (l-r)
# #
# # nb = np.array(b)
# # pnb = nb[points_eye]
# # (l,r) = (max(pnb[:,0]),(min(pnb[:,0])))
# # print "width of b(right eye): %.4f" % (l-r)
# #
# # nc = np.array(c)
# # pnc = nc[points_eye]
# # (l,r) = (max(pnc[:,0]),(min(pnc[:,0])))
# # print "width of c(right eye): %.4f" % (l-r)
# #
# # nd = np.array(d)
# # pnd = nd[points_eye]
# # (l,r) = (max(pnd[:,0]),(min(pnd[:,0])))
# # print "width of d(right eye): %.4f" % (l-r)
# #
# # ne = np.array(e)
# # pne = ne[points_eye]
# # (l,r) = (max(pne[:,0]),(min(pne[:,0])))
# # print "width of e(right eye): %.4f" % (l-r)
#

import cPickle as pickle
import numpy as np

base_path = "/home/loaias/Workspace/Python/MakeHuman/log"

#*******************************************************************************************
def create_files():
    return
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

    mapping=[
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
