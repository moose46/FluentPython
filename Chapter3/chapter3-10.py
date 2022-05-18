__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-10.py was created on April 27 2022 @ 9:12 AM
# Project: FluentPython
#


if __name__ == '__main__':
    l = ['spam','spam','eggs','spam','eggs','bacon', 'eggs']
    ls = set(l)
    l1 = list(ls)
    d1 = dict.fromkeys(l).keys()