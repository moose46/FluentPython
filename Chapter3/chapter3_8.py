__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'


#
# Author: Robert W. Curtiss
# chapter3_8.py was created on April 22 2022 @ 9:28 AM
# Project: FluentPython
#

class StrKeyDict0(dict):
    """
    a better way to create user defined mapping type is to subclass
    collections.UserDict

    """

    def __missing__(self, key):
        if isinstance(key, str):  # key is missing and it is already a string
            raise KeyError(key)  # blow up
        return self[str(key)]  # build string key and look it up

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default  # the get method delegates to __getitem__ by using self[key] notation

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
