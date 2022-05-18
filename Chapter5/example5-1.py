__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# example5-1.py was created on April 29 2022 @ 5:01 PM
# Project: FluentPython
#
from collections import namedtuple
from typing import NamedTuple

Coordinate = namedtuple('Coordinate', 'lat lon')

print(issubclass(Coordinate, tuple))

moscow = Coordinate(55.756, 37.617)
print(moscow)
print(moscow == Coordinate(55.756, 37.617))

Coordinate = NamedTuple('Coordinate', [('lat', float), ('lon', float)])
# print(typing.get_type_hints(Coordinate))

moscow = Coordinate(55.756, 37.617)

Coordinate = NamedTuple('Coordinate', lat=float, lon=float)

from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate():
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}"{ns}, {abs(self.lon):.1f}"{we}'


c = Coordinate(9.55, 2.33)
print(c)
