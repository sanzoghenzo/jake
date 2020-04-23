"""pip.py gets installed pip dependencies"""
# pylint: disable=protected-access
# Copyright 2020 Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import pkg_resources

from jake.types.coordinates import Coordinates

class Pip():
  """pip.py gets installed pip dependencies"""
  def __init__(self):
    self._log = logging.getLogger('jake')
    self._format = "pypi"
    self._coords = self.generate_dependencies()

  def generate_dependencies(self, coords=Coordinates()):
    """converts list of pkg_resource.working_set into purl coordinates"""

    for i in iter(pkg_resources.working_set):
      coords.add_coordinate(i.project_name, i._version, self._format)

    if len(coords.get_coordinates()) == 0:
      return None

    self._coords = coords
    return coords

  def get_dependencies(self):
    """ gets the list of dependencies generatated on init
    Returns:
        Coordinates object -- list of coordinates generated by pkg_resources
    """
    return self._coords