# Copyright 2017 Chi-kwan Chan
# Copyright 2017 Harvard-Smithsonian Center for Astrophysics
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

from abc  import ABCMeta
from lict import Lict

class Metainer(metaclass=ABCMeta):
    """Metainer

    `Metainer` provides a metadata-based mixin for building
    interpolatable python classes.

    """
    __slots__ = ('_metainer')

    def set(self, name, value, **kwargs):
        l = Lict(value, name=name, **kwargs)
        try:
            self._metainer.append(l)
        except AttributeError:
            self._metainer = Lict(l)
        self.name = value
