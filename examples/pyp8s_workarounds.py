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

from pyp8s import MetricsHandler as meh


if __name__ == "__main__":
    meh.set_metrics_name("pyp8s_eternity")
    meh.serve(listen_address="127.0.0.1", listen_port=8081)

    print('''Can't do that:''')
    print('''>>> meh.inc("catsPaws", 1, from="dog", if="bad_dog")''')
    print('''that would be a syntax error''')

    workaround_dict = {
        "from": "dog",
        "if": "bad_dog",
    }

    meh.inc("catsPaws", 1, **workaround_dict)

    while True:
        meh.inc("seconds", 1)
        time.sleep(1)

