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
    def create_gene(name, value):
        return {"Modifier": name, "Value": value}

    def set_method(self, method):
        self.cmd["Method"] = method

    def set_parameters(self, parameters):
        self.cmd["Parameters"] = parameters

    def set_individuals(self, individuals):
        self.cmd["Individuals"] = individuals

    def get_command(self):
        return str(self.cmd)