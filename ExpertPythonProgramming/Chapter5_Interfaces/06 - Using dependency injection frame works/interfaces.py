__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# interfaces.py was created on June 10 2022 @ 10:49 AM
# Project: FluentPython
#

from abc import ABC, abstractmethod
from typing import Dict


class ViewsStorageBackend(ABC):
    @abstractmethod
    def increment(self, key: str):
        ...

    @abstractmethod
    def most_common(self, n: int) -> Dict[str, int]:
        ...