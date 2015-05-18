from core import G
human = G.app.selectedHuman
mesh = human.mesh.__dict__["coord"]
# *************************************************************************************


def modify_model(modifiers):
    import humanmodifier

    for index, modifier_name in enumerate(modifiers):
        modifier = human.getModifier(modifier_name)
        m_action = humanmodifier.ModifierAction(modifier, 0, modifiers[modifier_name], finished_modify)
        m_action.do()

def finished_modify():
    pass
# *************************************************************************************
def modify_model_by_chromosome(chromosome):
    pass
# *************************************************************************************
def init_model():
    from const import all_modifiers

    modifiers = all_modifiers["init"]
    modify_model(modifiers)


def modify_eyes(chromosome):
    from const import all_modifiers

    modifiers = all_modifiers["eyes"]
    modifiers["eyes/l-eye-height1-min|max"] = chromosome["l-eye-height1"]
    modifiers["eyes/r-eye-height1-min|max"] = chromosome["l-eye-height1"]
    modifiers["eyes/l-eye-height3-min|max"] = chromosome["l-eye-height3"]
    modifiers["eyes/r-eye-height3-min|max"] = chromosome["l-eye-height3"]
    modifiers["eyes/l-eye-corner1-up|down"] = chromosome["l-eye-corner1"]
    modifiers["eyes/r-eye-corner1-up|down"] = chromosome["l-eye-corner1"]
    modifiers["eyes/l-eye-corner2-up|down"] = chromosome["l-eye-corner2"]
    modifiers["eyes/r-eye-corner2-up|down"] = chromosome["l-eye-corner2"]
    modify_model(modifiers)


def modify_model_by_eye(chromosome):
    from tool import decode_to_phenotype, encode_to_genotype, get_feature
    from const import all_modifiers

    modifiers_1st = all_modifiers["general"]["1st"]
    modifiers_1st["eyes/l-eye-push1-in|out"] = chromosome["eye-out"]
    modifiers_1st["eyes/l-eye-push2-in|out"] = -chromosome["eye-out"]
    modifiers_1st["eyes/l-eye-size-small|big"] = chromosome["eye-size"]
    modify_model(modifiers_1st)

    eye_out = get_feature("eye-out", mesh)
    eye_in = get_feature("eye-in", mesh)
    eye_left = get_feature("eye-distance", mesh)
    eye_min_width = eye_out - eye_in
    eye_width = eye_out - eye_left

    modifiers_2nd = all_modifiers["general"]["2nd"]
    # set eye-height (2~3)
    eye_height = eye_min_width / 3
    eye_height_genotype = encode_to_genotype("eye-height", eye_height)
    modifiers_2nd["eyes/l-eye-height2-min|max"] = eye_height_genotype

    # set eye-distance (1)
    eye_distance = eye_width
    eye_distance_genotype = encode_to_genotype("eye-distance", eye_distance)
    modifiers_2nd["eyes/l-eye-move-in|out"] = eye_distance_genotype

    # set face-width (4~5)
    face_width = 5 * eye_width
    face_width_genotype = encode_to_genotype("face-width", face_width)
    modifiers_2nd["head/head-scale-horiz-less|more"] = face_width_genotype

    # # set nose-width (1)
    nose_width = eye_width
    nose_width_genotype = encode_to_genotype("nose-width", nose_width)
    modifiers_2nd["nose/nose-scale-horiz-incr|decr"] = nose_width_genotype

    # set face-height (2~3)
    face_height = 1.61 * face_width
    face_height_genotype = encode_to_genotype("face-height", face_height)
    # modifiers["chin/chin-height-min|max"] = face_height_genotype
    modifiers_2nd["head/head-scale-vert-more|less"] = face_height_genotype

    # # set forehead_to_nose (1.61)
    # forehead_to_nose = face_height / 2.61 * 1.61
    # modifiers["nose/nose-scale-vert-incr|decr"] = encode_to_genotype("forehead_to_nose", forehead_to_nose)

    # # set nose_to_mouth (1.61)
    # nose_to_mouth = forehead_to_nose / 2.61
    # modifiers["mouth/mouth-trans-up|down"] = get_gene_by_feature("nose_to_mouth", nose_to_mouth)

    # set right eye
    modifiers_2nd["eyes/r-eye-push1-in|out"] = modifiers_1st["eyes/l-eye-push1-in|out"]
    modifiers_2nd["eyes/r-eye-push2-in|out"] = modifiers_1st["eyes/l-eye-push2-in|out"]
    modifiers_2nd["eyes/r-eye-height2-min|max"] = modifiers_2nd["eyes/l-eye-height2-min|max"]
    modifiers_2nd["eyes/r-eye-move-in|out"] = modifiers_2nd["eyes/l-eye-move-in|out"]
    modifiers_2nd["eyes/r-eye-size-small|big"] = modifiers_1st["eyes/l-eye-size-small|big"]

    modify_model(modifiers_2nd)

    # print "check->"
    # print "eye out->", decode_to_phenotype("eye-out", chromosome["eye-out"])
    # print "eye in->", decode_to_phenotype("eye-in", -chromosome["eye-out"])
    # print "eye width->", eye_min_width, "->", eye_width
    # print "eye distance->", decode_to_phenotype("eye-distance", eye_distance_genotype)
    # raw_input()
    # print "******************************************************************"
    # print "eye width:"
    # print eye_width
    # print "eye height:"
    # print "ideal"
    # print eye_height
    # print "real"
    # print decode_to_phenotype("eye-height", eye_height_genotype)
    # print "******************************************************************"
    # print "eye distance:"
    # print "ideal"
    # print eye_distance
    # print "real"
    # print decode_to_phenotype("eye-distance", eye_distance_genotype)
    # print "******************************************************************"
    # print "face width:"
    # print "ideal"
    # print face_width
    # print "real"
    # print decode_to_phenotype("face-width", face_width_genotype)
    # print "******************************************************************"
    # print "nose width:"
    # print "ideal"
    # print nose_width
    # print "real"
    # print decode_to_phenotype("nose-width", nose_width_genotype)
    # print "******************************************************************"
    # print "face height:"
    # print "ideal"
    # print face_height
    # print "real"
    # print decode_to_phenotype("face-height", face_height_genotype)
    # raw_input()
    # import numpy as np
    # import os
    #
    # base_path = "/home/loaias/Workspace/Python/MakeHuman/log"
    # path = os.path.join(base_path, "mapping_ver3", "face-height.npy")
    # parameter_feature_pairs = np.load(path)
    # print parameter_feature_pairs