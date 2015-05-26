# -*- coding: utf-8 -*-


class Windows:
    create_window = "CreateWindow"
    ec_window = "ECWindow"

    def __init__(self):
        pass

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

    individuals_received_from_xgp = "individuals_received_from_xgp"

    def __init__(self):
        pass
