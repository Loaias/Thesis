# -*- coding: utf-8 -*-


class ReceiveWindow():
    def __init__(self):
        pass

    def models_received(self, json):
        from CreatingFiles.Create_Files import create_parts_files

        create_parts_files(self.base_path, json)
