# Copyright (c) 2009-2015, Dwight Hubbard
# Copyrights licensed under the New BSD License
# See the accompanying LICENSE.txt file for terms.

from .dlipower import Outlet, PowerSwitch, DLIPowerException

try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution("dlipower").version
except ImportError:
    __version__ = str('0.0.0')

__all__ = ['dlipower']
