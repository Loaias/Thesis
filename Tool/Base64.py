# -*- coding: utf8 -*-

import base64
from cStringIO import StringIO
import zlib


def encode_image(image):
    image_string = image_to_string(image)
    base64_string = base64.b64encode(image_string)
    return base64_string


def image_to_string(image):
    output = StringIO()
    image.save(output, format='JPEG')
    image_data = output.getvalue()

    return image_data


def decode_image(data):
    image = base64.b64decode(data)
    return image
