__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# comparable.py was created on May 20 2022 @ 1:43 PM
# Project: FluentPython
#

from typing import Protocol, Any

class SupportsLessThan(Protocol):
    def __lt__(self, other : Any) -> bool:
        pass
