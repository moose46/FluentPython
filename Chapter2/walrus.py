__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# walrus.py was created on April 19 2022 @ 10:15 AM
# Project: FluentPython
#


if __name__ == '__main__':
    x = 'ABC'
    codes = [ord(x) for x in x]
    print(x)
    print(codes)
    codes = [last := ord(c) for c in x]
    print(codes)
    print(last)
    print(c)