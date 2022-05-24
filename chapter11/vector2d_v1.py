__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# vector2d_v0.py was created on May 24 2022 @ 8:07 AM
# Project: FluentPython
#


from array import array
import math

class Vector2d:

    typecode = 'd'

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def __iter__(self):
        return (t for t in (self.x,self.y))

    def __format__(self, format_spec=''):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(array(self.typecode,self))

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    v1 = Vector2d(3,4)
    print(v1.x, v1.y)

    x,y = v1

    print(v1)

    v1_clone = eval(repr(v1))

    print(v1 == v1_clone)

    octets = bytes(v1)

    print(abs(v1))
    print(bool(v1), bool(Vector2d(0,0)))
    print(format(v1,'.2f'))