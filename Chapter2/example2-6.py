__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# example2-6.py was created on April 19 2022 @ 10:41 AM
# Project: FluentPython
#
# cartesian product in a generator expression


if __name__ == '__main__':
    colors = 'black white'.split()
    sizes = 's m l'.split()

    for tshirt in (f'{c} {s}' for c in colors for s in sizes):
        print(tshirt)
