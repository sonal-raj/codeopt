# -*- coding: UTF-8 -*-
# Copyright (c) 2018 Sonal Raj. This program is open-source software,
# and may be redistributed under the terms of the MIT license. See the
# LICENSE file in this distribution for details.

import os

VERSION_INFO = {
    'major': 1,
    'minor': 0,
    'micro': 0,
}

def get_version(short=False):
    """
    Get a string with app version.
    """
    version = "%(major)i.%(minor)i" % VERSION_INFO
    # append micro version only if not short and micro != 0
    if not short and VERSION_INFO['micro']:
        version = version + (".%(micro)i" % VERSION_INFO)
    return version

__version__ = get_version()
