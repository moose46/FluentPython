__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter8_12.py was created on May 12 2022 @ 3:49 PM
# Project: FluentPython
#

from typing import NamedTuple

from geolib import geohash as gh # type: ignore

x = tuple[int,...]
PRECISION = 9

class Coordinate(NamedTuple):
    lat: float
    lon: float

def geohash(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PRECISION)

def display(lat_lon: tuple[float,float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    return f'{abs(lat):0.1f}"{ns} {abs(lon):0.1f}"{ew}'

shanghai = 31.2304,121.4737
print(shanghai)
print(geohash(shanghai))
print(display(shanghai))