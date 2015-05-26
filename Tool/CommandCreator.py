# -*- coding: utf-8 -*-


class Command:
    def __init__(self, method=None, parameters=None):
        self.cmd = {
            "Method": None,
            "Parameters": None,
            "Individuals": []
        }

        self.set_method(method)
        self.set_parameters(parameters)

    @staticmethod
    def create_modifier(name, value):
        return {"Modifier": name, "Value": value}

    @staticmethod
    def create_modifiers_for_eye_width(values):
        return [
            {"Modifier": "eyes/l-eye-push1-in|out", "Value": values[0]},
            {"Modifier": "eyes/r-eye-push1-in|out", "Value": values[0]},
            {"Modifier": "eyes/l-eye-push2-in|out", "Value": values[1]},
            {"Modifier": "eyes/r-eye-push2-in|out", "Value": values[1]},
            {"Modifier": "eyes/l-eye-size-small|big", "Value": values[2]},
            {"Modifier": "eyes/r-eye-size-small|big", "Value": values[2]}
        ]

    def set_method(self, method):
        self.cmd["Method"] = method

    def set_parameters(self, parameters):
        self.cmd["Parameters"] = parameters

    def set_individuals(self, individuals):
        self.cmd["Individuals"] = individuals

    def get_command(self):
        return str(self.cmd)