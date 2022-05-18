__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter5-4.py was created on May 01 2022 @ 12:06 PM
# Project: FluentPython
#

from collections import namedtuple
import json
if __name__ == '__main__':
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
    tokyo_data = ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    x =City._make(tokyo_data)
    print(x._fields)
    print(json.dumps(x._asdict()))
    print(tokyo)