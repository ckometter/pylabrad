# Copyright (C) 2007  Matthew Neeley
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
labrad.constants

Important constants that show up throughout the code.
"""

import os

def make_bool(value):
    """Convert a string value from env var or cmdline arg to boolean.

    If passed a boolean, we just return the value directly, which is useful
    in handling defaults which we can specify as bools.
    """
    if isinstance(value, bool):
        return value
    if value.lower() in ['true', 't', 'yes', 'y', 'on', '1']:
        return True
    elif value.lower() in ['false', 'f', 'no', 'n', 'off', '0']:
        return False
    else:
        raise ValueError('must be true or false')

# defaults for the labrad manager
MANAGER_ID = 1
MANAGER_PORT = int(os.environ.get('LABRADPORT', 7682))
MANAGER_USE_TLS = make_bool(os.environ.get('LABRAD_TLS', False))
MANAGER_VERIFY_HOST = make_bool(os.environ.get('LABRAD_TLS_VERIFY_HOST', True))
MANAGER_PORT_TLS = int(os.environ.get('LABRAD_TLS_PORT', 7643))
MANAGER_HOST = os.environ.get('LABRADHOST', 'localhost')
PASSWORD = os.environ.get('LABRADPASSWORD', None)

# settings IDs on the LabRAD manager
SERVERS_LIST = 1
SETTINGS_LIST = 2
LOOKUP = 3
HELP = 10
MESSAGE_SUBSCRIBE = 60

# default timeout in seconds
TIMEOUT = 30

# node controller
HTTP_PORT = int(os.environ.get('LABRADHTTPPORT', 7667))
