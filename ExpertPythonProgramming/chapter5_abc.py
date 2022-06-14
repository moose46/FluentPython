__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter5_abc.py was created on June 09 2022 @ 9:13 AM
# Project: FluentPython
#

from abc import ABC, abstractmethod

class DummyInterface(ABC):
    @abstractmethod
    def dummy_interface(self):
        pass

    @property
    @abstractmethod
    def dummy_method(self):
        pass


if __name__ == '__main__':
    pass
