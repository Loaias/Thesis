# -*- coding: utf-8 -*-

############################################################


class Part:
    def __init__(self, modifier, name):
        self.modifier = modifier
        self.name = name


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


class Coordinate:
    X, Y, Z = 1, 2, 3

    def __init__(self):
        pass


class KeyPoint:
    def __init__(self, name, parts_name, coord, coord_value):
        self.name = name
        self.parts_name = parts_name
        self.coord = coord
        self.coord_value = coord_value


class KeyPoints:
    eye_in = KeyPoint("eye_in", Parts.eye_in.name, Coordinate.X, 0.4409)
    eye_out = KeyPoint("eye_out", Parts.eye_out.name, Coordinate.X, 0.4409)
    eye_distance = KeyPoint("eye_distance", Parts.eye_in.name, Coordinate.X, 0.1624)
    eye_up = KeyPoint("eye_up", Parts.eye_height.name, Coordinate.Y, 7.3794)
    eye_bottom = KeyPoint("eye_bottom", Parts.eye_height.name, Coordinate.Y, 7.3062)
    mouth_middle = KeyPoint("mouth_middle", Parts.mouth.name, Coordinate.Y, 6.6934)
    nose_apex = KeyPoint("nose_apex", Parts.nose.name, Coordinate.Y, 6.8723)
    nose_out = KeyPoint("nose_out", Parts.nose.name, Coordinate.X, 0.1697)
    face_top = KeyPoint("face_top", Parts.forehead.name, Coordinate.Y, 8.3768)
    face_bottom = KeyPoint("face_bottom", Parts.chin.name, Coordinate.Y, 0.6575)
    face_left = KeyPoint("face_left", Parts.face.name, Coordinate.X, 0.6983)

    def __init__(self):
        pass

    @classmethod
    def get_all_key_points(cls):
        for attr in cls.__dict__:
            if isinstance(cls.__dict__[attr], KeyPoint):
                yield cls.__dict__[attr]

    @classmethod
    def get_key_point_by_name(cls, name):
        return cls.__dict__[name]

############################################################


class Pair:
    def __init__(self, name, modifier, key_points, expression=""):
        self.name = name
        self.modifier = modifier
        self.key_points = key_points
        self.operator = expression

    def get_value(self, json):
        key_points = [(KeyPoints.get_key_point_by_name(c['name']), c['value']) for c in json]

        if self.operator is "-":
            return self.subtraction(key_points)
        elif self.operator is "*":
            return self.multiplication(key_points)
        else:
            return self.default(key_points)

    def subtraction(self, key_points):
        value = key_points[0][1][key_points[0][0].coord - 1] - key_points[1][1][key_points[1][0].coord - 1]
        return abs(value)

    def multiplication(self, key_points):
        value = key_points[0][1][key_points[0][0].coord - 1] * 2
        return abs(value)

    def default(self, key_points):
        value = key_points[0][1][key_points[0][0].coord - 1]
        return abs(value)


class Mappings:
    eye_out = Pair("eye_out", "eyes/l-eye-push1-in|out", (KeyPoints.eye_out,))
    eye_in = Pair("eye_in", "eyes/l-eye-push2-in|out", (KeyPoints.eye_in,))
    eye_height = Pair("eye_height", "eyes/l-eye-height2-min|max", (KeyPoints.eye_up, KeyPoints.eye_bottom), "-")
    eye_distance = Pair("eye_distance", "eyes/l-eye-move-in|out", (KeyPoints.eye_in,), "*")
    face_width = Pair("face_width", "head/head-scale-horiz-less|more", (KeyPoints.eye_in,), "2")
    face_height = Pair("face_height", "head/head-scale-vert-more|less", (KeyPoints.face_top, KeyPoints.face_bottom), "-")
    nose_width = Pair("nose_width", "nose/nose-scale-horiz-incr|decr", (KeyPoints.nose_out,), "*")
    nose_apex = Pair("nose_apex", "nose/nose-scale-vert-incr|decr", (KeyPoints.nose_apex,))
    mouth_middle = Pair("mouth_middle", "mouth/mouth-trans-up|down", (KeyPoints.mouth_middle,))

    def __init__(self):
        pass

    @classmethod
    def get_all_mapping_pair(cls):
        for attr in cls.__dict__:
            if isinstance(cls.__dict__[attr], Pair):
                yield cls.__dict__[attr]

    @classmethod
    def get_mapping_by_name(cls, name):
        return cls.__dict__[name]
