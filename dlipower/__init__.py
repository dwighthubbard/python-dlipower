# Copyright (c) 2009-2015, Dwight Hubbard
# Copyrights licensed under the New BSD License
# See the accompanying LICENSE.txt file for terms.

from .dlipower import Outlet, PowerSwitch
import json
import os


# noinspection PyUnresolvedReferences
_METADATA_FILE = os.path.join(
    os.path.dirname(__file__),
    'package_metadata.json'
)

if os.path.exists(_METADATA_FILE):  # pragma: no cover
    with open(_METADATA_FILE) as fh:
        __version__ = json.load(fh)['version']
else:
    __version__ = '0.0.0'  # pragma: no cover
