# -*- coding: utf-8 -*-


class Method:
    modify_and_get_images = "modify_and_get_images"
    modify_and_get_points = "modify_and_get_points"
    modify_and_get_models = "modify_and_get_models"
    modify_and_get_mappings = "modify_and_get_mappings"
    modify = "modify"

    def __init__(self):
        pass


class CallBack:
    render_image = "render_image"
    points_received = "points_received"
    models_for_parts_received = "models_for_parts_received"
    models_for_mapping_received = "models_for_mapping_received"

    def __init__(self):
        pass
