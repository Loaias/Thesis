# -*- coding: utf-8 -*-

############################################################


class Part:
    def __init__(self, long_name, short_name):
        self.long = long_name
        self.short = short_name


class Parts:
    eye_out = Part("eyes/l-eye-push1-in|out", "eye_out")
    eye_in = Part("eyes/l-eye-push2-in|out", "eye_in")
    eye_height = Part("eyes/l-eye-height2-min|max", "eye_height")
    chin = Part("chin/chin-prominent-less|more", "chin")
    forehead = Part("forehead/forehead-trans-depth-forward|backward", "forehead")
    nose = Part("nose/nose-scale-depth-incr|decr", "nose")
    mouth = Part("mouth/mouth-scale-vert-incr|decr", "mouth")
    face = Part("head/head-scale-horiz-less|more", "face")

    def __init__(self):
        pass

    @classmethod
    def get_all_parts(cls):
        for attr in cls.__dict__:
            if isinstance(cls.__dict__[attr], Part):
                yield cls.__dict__[attr]
############################################################


class KeyPoint:
    def __init__(self, name, file_name, coord, coord_value):
        self.name = name
        self.file_name = file_name
        self.coord = coord
        self.coord_value = coord_value


class KeyPoints:
    eye_in = KeyPoint("eye_in", Parts.eye_in.short, 1, 0.4409)
    eye_out = KeyPoint("eye_out", Parts.eye_out.short, 1, 0.4409)
    eye_distance = KeyPoint("eye_distance", Parts.eye_in.short, 1, 0.1624)
    eye_up = KeyPoint("eye_up", Parts.eye_height.short, 2, 7.3794)
    eye_bottom = KeyPoint("eye_bottom", Parts.eye_height.short, 2, 7.3062)
    mouth = KeyPoint("mouth", Parts.mouth.short, 2, 6.6934)
    nose = KeyPoint("nose", Parts.nose.short, 2, 6.8723)
    nose_out = KeyPoint("nose_out", Parts.nose.short, 1, 0.1697)
    face_top = KeyPoint("face_top", Parts.forehead.short, 2, 8.3768)
    face_bottom = KeyPoint("face_bottom", Parts.chin.short, 2, 0.6575)
    face_left = KeyPoint("face_left", Parts.face.short, 1, 0.6983)

    def __init__(self):
        pass

    @classmethod
    def get_all_key_points(cls):
        for attr in cls.__dict__:
            if isinstance(cls.__dict__[attr], KeyPoint):
                yield cls.__dict__[attr]
############################################################


class Pair:
    def __init__(self, phenotype, genotype):
        self.phenotype = phenotype
        self.genotype = genotype


class Mapping:
    eye_out = Pair("eye_out", "eyes/l-eye-push1-in|out")
    eye_in = Pair("eye_in", "eyes/l-eye-push2-in|out")
    eye_height = Pair("eye_height", "eyes/l-eye-height2-min|max")
    eye_distance = Pair("eye_distance", "eyes/l-eye-move-in|out")
    face_width = Pair("face_width", "head/head-scale-horiz-less|more")
    face_height = Pair("face_height", "head/head-scale-vert-more|less")
    nose_width = Pair("nose_width", "nose/nose-scale-horiz-incr|decr")
    nose_apex = Pair("nose_apex", "nose/nose-scale-vert-incr|decr")
    mouth_middle = Pair("mouth_middle", "mouth/mouth-trans-up|down")

    def __init__(self):
        pass


def template(key_point, coord=0):
    return "%s[%s['%s']][%d]" % ("%s", "%s", key_point.name, coord)


class PhenotypeFeatureExpressions:
    eye_in = template(KeyPoints.eye_in)
    eye_out = template(KeyPoints.eye_out)
    eye_width = "%s - %s" % (eye_out, eye_in)
    eye_distance = "%s - %s", (eye_out, eye_in)
    eye_up = template(KeyPoints.eye_up, 1)
    eye_bottom = template(KeyPoints.eye_bottom, 1)
    eye_height = "%s - %s" % (eye_up, eye_bottom)
    face_width = "%s * 2" % template(KeyPoints.face_left)
    face_top = template(KeyPoints.face_top, 1)
    face_bottom = template(KeyPoints.face_bottom, 1)
    face_height = "%s - %s" % (face_top, face_bottom)
    nose_width = "%s * 2" % template(KeyPoints.nose_out)
    nose_apex = template(KeyPoints.nose, 1)
    mouth_middle = template(KeyPoints.mouth, 1)

    def __init__(self):
        pass

    @classmethod
    def get_all_expressions(cls):
        for attr in cls.__dict__:
            if isinstance(cls.__dict__[attr], KeyPoint):
                yield cls.__dict__[attr]