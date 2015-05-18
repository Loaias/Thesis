__author__ = 'loaias'

import os
import numpy as np
import cPickle as pickle


base_path = os.getcwd().replace("makehuman", "log")


def decode_to_phenotype(feature_name, parameter):
    path = os.path.join(base_path, "mapping_ver3", "%s.npy" % feature_name)
    parameter_feature_pairs = np.load(path)

    feature = sorted(parameter_feature_pairs, key=lambda x:(x[0] - parameter) ** 2)[0][1]
    return feature


def encode_to_genotype(feature_name, feature):
    path = os.path.join(base_path, "mapping_ver3", "%s.npy" % feature_name)
    parameter_feature_pairs = np.load(path)

    sorted_pairs = sorted(parameter_feature_pairs, key=lambda x:(x[1] - feature) ** 2)
    gene = sorted_pairs[0][0]
    return gene


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
    if func_name == "eye-distance":
        return model[indices["eye-in"]][0] * 2
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
