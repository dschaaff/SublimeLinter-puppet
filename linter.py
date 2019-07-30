#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Andrew Grim
# Copyright (c) 2014 Andrew Grim
#
# License: MIT
#

"""This module exports the Puppet plugin class."""

from SublimeLinter.lint import Linter, util


class Puppet(Linter):

    """Provides an interface to puppet."""

    defaults = {
        'selector': 'source.puppet'
    }
    cmd = ('puppet', 'parser', 'validate', '--color=false')
    regex = r'^Error:.+?(?P<message>Syntax error at \'(?P<near>.+?)\'?(?P<line>\d+):?(?P<col>\d+))'
    error_stream = util.STREAM_STDERR
