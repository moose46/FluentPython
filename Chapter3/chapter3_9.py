__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3_9.py was created on April 22 2022 @ 11:14 AM
# Project: FluentPython
#
import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):  # key is missing and it is already a string
            raise KeyError(key)  # blow up
        return self[str(key)]  # build string key and look it up

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value

