#!/usr/bin/env python3
# pylint: disable=line-too-long, missing-function-docstring, logging-fstring-interpolation
# pylint: disable=too-many-locals, broad-except, too-many-arguments, raise-missing-from
# pylint: disable=import-error
"""

  Prometheus metrics server and collector example
  ===============================================

  Collection of workarounds.

  GitHub repository:
  https://github.com/pyp8s/pyp8s

  Community support:
  https://github.com/pyp8s/pyp8s/issues

  Copyright © 2022, Pavel Kim

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


import time
import socket

from pyp8s import MetricsHandler as meh


LISTEN_ADDRESS = "127.0.0.1"
LISTEN_PORT = 8081
FQDN = socket.getfqdn()


if __name__ == "__main__":

    meh.init("pyp8s_tricky_bits", "counter", "A dummy metric just to show up a few tricks")
    meh.init("pyp8s_ticker", "counter", "Reflects the number of seconds passed after the startup")

    meh.serve(listen_address=LISTEN_ADDRESS, listen_port=LISTEN_PORT)

    print(f"""""")
    print(f"""Metrics server started on {LISTEN_ADDRESS}:{LISTEN_PORT}""")
    print(f"""URL: http://{LISTEN_ADDRESS}:{LISTEN_PORT}/metrics""")
    print(f"""Run in console: curl {LISTEN_ADDRESS}:{LISTEN_PORT}/metrics""")
    print(f"""""")
    print(f"""Stop with Ctrl+C""")

    '''
    Can't do that:
    >>> meh.inc("pyp8s_tricky_bits", 1, from="dog", if="bad_dog")
    that would be a syntax error
    '''

    workaround_dict = {
        "from": "dog",
        "if": "bad_dog",
    }

    meh.inc("pyp8s_tricky_bits", 1, **workaround_dict)

    while True:
        meh.inc("pyp8s_ticker", 1, hostname=FQDN)
        time.sleep(1)

