__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# example2-4.py was created on April 19 2022 @ 10:27 AM
# Project: FluentPython
#


if __name__ == '__main__':
    colors = "black white".split()
    sizes = 's m l'.split()
    tshirts = [(color,size) for color in colors for size in sizes]
    print(tshirts)

    tshirts = [(color,size) for size in sizes for color in colors]
    print(tshirts)