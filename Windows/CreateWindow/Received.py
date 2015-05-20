# -*- coding: utf-8 -*-


class ReceiveWindow:
    def __init__(self):
        pass

    def models_for_parts_received(self, json):
        from CreatingFiles import create_parts_files

        create_parts_files(self.base_path, json)

    def models_for_mapping_received(self, json):
        from CreatingFiles import create_mapping_files

        create_mapping_files(self.base_path, json)
