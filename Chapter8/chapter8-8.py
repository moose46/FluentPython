__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter8-8.py was created on May 12 2022 @ 9:02 AM
# Project: FluentPython
#

def tokenize(text: str) -> list[str]:
    return text.upper().split()

print(tokenize('this is poop dog'))
from geolib import geohash as gh
PRECISION = 9
def geohash(lat_lon: tuple[float,float]) -> str:
    return gh.encode(*lat_lon, PRECISION)

shanghai = 31.2304,121.4737
print(shanghai)
print(geohash(shanghai))


