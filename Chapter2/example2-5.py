__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# example2-5.py was created on April 19 2022 @ 10:35 AM
# Project: FluentPython
#

import array
if __name__ == '__main__':
    symbols = '$¢£¥€¤'

    print(tuple(ord(symbol) for symbol in symbols))

    print(array.array('I', (ord(symbol) for symbol in symbols)))


