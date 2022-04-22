__author__ = 'Robert W. Curtiss'

# https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
# Author: Robert W. Curtiss
# example1-2.py was created on April 18 2022 @ 4:21 PM
# Project: FluentPython
# pp11 Fluent Python

import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x},{self.y})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2,4)
    v2 = Vector(2,1)
    v3 = v1 + v2
    print(f'v1 {v1} + v2 {v2} = {v3}')
    v3 = v1 * 3
    print(v1, v3)

    v = Vector(3,4)
    print(v)
    print(abs(v * 3))

