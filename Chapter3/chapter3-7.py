__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-7.py was created on April 22 2022 @ 9:25 AM
# Project: FluentPython
#
from chapter3_8 import StrKeyDict0

d = StrKeyDict0([('2','two'),('4','four')])
two = d['2']
four = d[4]
d['1']