__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# example2-3.py was created on April 19 2022 @ 10:20 AM
# Project: FluentPython
#


if __name__ == '__main__':
    symbols = '$¢£¥€¤'

    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)

    beyond_ascii = list(filter(lambda c: c > 127, map(ord,symbols)))
    print(beyond_ascii)