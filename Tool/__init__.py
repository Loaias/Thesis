# -*- coding: utf-8 -*-

import os

from enum import *
from Base64 import *
from Consts import *


def search_single_file(keyword, path, cond="in"):
    for f in os.listdir(path):
        if cond == "in":
            if keyword in f:
                return f
