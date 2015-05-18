__author__ = 'loaias'

import numpy as np
import os
import matplotlib.pyplot as plt

base_path = "/home/loaias/Workspace/Python/MakeHuman/log"

#*******************************************************************************************
def search_single_file(keyword, sub="parts", cond="in"):
    for f in os.listdir(os.path.join(base_path, sub)):
        if cond == "in":
            if keyword in f:
                return f
#*******************************************************************************************

#*******************************************************************************************
def check_ditto():
    path = os.path.join(base_path, "parts")
    points = []

    for f in os.listdir(path):
        file_name = os.path.join(path, f)
        points.append(np.loadtxt(file_name, dtype='i'))

    length = len(points)
    count = 0
    for i in xrange(length - 1):
        for j in xrange(i + 1, length):
            for index in points[i]:
                if index in points[j]:
                    count += 1

    print count
#*******************************************************************************************

#*******************************************************************************************
def show_points(name, coord):
    f = search_single_file(name)
    raw_data = np.load("%s/parts/%s" % (base_path, f))

    x,y,z = raw_data[:,1],raw_data[:,2],raw_data[:,3]

    if coord=="xy":
        plt.scatter(x, y, s=5, marker=(5,3))

        plt.xlim(min(x), max(x))
        plt.ylim(min(y), max(y))
    if coord=="zy":
        plt.scatter(z, y, s=5, marker=(5,3))

        plt.xlim(min(z), max(z))
        plt.ylim(min(y), max(y))

    if coord=="xz":
        plt.scatter(x, z, s=5, marker=(5,3))

        plt.xlim(min(x), max(x))
        plt.ylim(min(z), max(z))

    plt.show()

show_points("eye_in", "xy")
# *******************************************************************************************

#*******************************************************************************************
import cPickle as pickle

def get_feature(func_name, mesh=None):
    model = mesh
    if mesh is None:    # test mesh
        model = np.load(os.path.join(base_path, "parts/test_model.npy"))

    with open(os.path.join(base_path, "parts/indices"), 'r') as f:
        indices = pickle.load(f)

    if func_name == "eye_in":
        return model[indices["eye-in"]][0]
    if func_name == "eye_out":
        return model[indices["eye-out"]][0]
    if func_name == "eye_height":
        return model[indices["eye-up"]][1] - model[indices["eye-bottom"]][1]
    # if func_name == "eye_width":
    #     return model[indices["eye-out"]][0] - model[indices["eye-in"]][0]
    if func_name == "eye_distance":
        return model[indices["eye-in"]][0] * 2
    # if func_name == "face_width":
    #     return model[indices["cheek"]][0] * 2
    if func_name == "face_width":
        return model[indices["face-edge"]][0] * 2
    if func_name == "face_left":
        return model[indices["face-edge"]][0]
    if func_name == "face_height":
        return model[indices["forehead"]][1] - model[indices["chin"]][1]
    if func_name == "nose_width":
        return model[indices["nose-out"]][0] * 2
    if func_name == "forehead_to_nose":
        return model[indices["forehead"]][1] - model[indices["nose"]][1]
    if func_name == "nose_to_chin":
        return model[indices["nose"]][1] - model[indices["chin"]][1]
    if func_name == "nose_to_mouth":
        return model[indices["nose"]][1] - model[indices["mouth"]][1]
    if func_name == "mouth_to_chin":
        return model[indices["mouth"]][1] - model[indices["chin"]][1]

def show_raw_data_figure():
    for index, f in enumerate(os.listdir(os.path.join(base_path, "mapping"))):
        path = os.path.join(base_path, "mapping", f)
        (x, y) = np.load(path)

        plt.subplot(3, 4, index + 1)

        plt.title(f)
        plt.plot(x, y)
        plt.xlim(-1.2, 1.2)
        plt.ylim(min(y), max(y))

    plt.show()

def show_raw_data_figure_ver2():
    for index, f in enumerate(os.listdir(os.path.join(base_path, "mapping_ver2"))):
        path = os.path.join(base_path, "mapping_ver2", f)
        (x, y) = np.load(path)

        plt.subplot(2, 4, index + 1)

        plt.title(f.split(".")[0])
        plt.plot(x, y)
        plt.xlim(-1.2, 1.2)
        plt.ylim(min(y), max(y))

    plt.show()

def show_raw_data_figure_ver3():
    for index, f in enumerate(os.listdir(os.path.join(base_path, "mapping_ver3"))):
        path = os.path.join(base_path, "mapping_ver3", f)
        parameter_feature_pairs = np.load(path)

        parameters = parameter_feature_pairs[:, 0]
        features = parameter_feature_pairs[:, 1]

        plt.subplot(3, 4, index + 1)

        plt.title(f.split(".")[0])
        plt.plot(parameters, features)
        plt.xlim(-1.2, 1.2)
        plt.ylim(min(features), max(features))

    plt.show()

# show_raw_data_figure_ver3()
#*******************************************************************************************