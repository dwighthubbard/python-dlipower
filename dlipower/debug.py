# Copyright (c) 2015, Yahoo Inc.
# Copyrights licensed under the New BSD License
# See the accompanying LICENSE.txt file for terms.
"""
DLIPower Debug Utilities

This module contains utility functions useful for troubleshooting dlipower.

This module can be run from the command line using the following command::

    python -m dlipower.debug


This will output information like the following::

    $ python -m dlipower.debug

    dlipower debug information:
            Version: 0.7.120
            Module Path: /home/dwight/github/python-dlipower/dlipower

            Source Code Information
                    Git Source URL: https://github.com/dwighthubbard/python-dlipower/tree/9c3bb943124d5d9767403960fdf6a622cbea5128
                    Git Hash: 9c3bb943124d5d9767403960fdf6a622cbea5128
                    Git Version: 0.7.120
                    Git Origin: https://github.com/dwighthubbard/python-dlipower.git
                    Git Branch: master


When run from the command line this will print a dump of information about
the module and it's build information.
"""
from __future__ import print_function
from .__init__ import __version__, __git_version__, __source_url__, \
    __git_hash__, __git_origin__, __git_branch__
import os


def debug_info_list():
    """
    Return a list with the debug information
    :return:
    """
    info = []
    info.append("dlipower debug information:")
    info.append('\tVersion: %s' % __version__)
    info.append('\tModule Path: %s' % os.path.dirname(__file__))
    info.append('')
    info.append('\tSource Code Information')
    if __git_version__:  # pragma: no cover
        info.append('\t\tGit Source URL: %s' % __source_url__)
        info.append('\t\tGit Hash: %s' % __git_hash__)
        info.append('\t\tGit Version: %s' % __git_version__)
        info.append('\t\tGit Origin: %s' % __git_origin__)
        info.append('\t\tGit Branch: %s' % __git_branch__)
    return info


def debug_info():
    """
    Return a multi-line string with the debug information
    :return:
    """
    return os.linesep.join(debug_info_list())


def print_debug_info():
    """
    Display information about the redislite build, and redis-server on stdout.
    :return:
    """
    print(debug_info())


if __name__ == '__main__':  # pragma: no cover
    print_debug_info()
