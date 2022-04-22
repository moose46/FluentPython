__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter2-22.py was created on April 20 2022 @ 10:42 AM
# Project: FluentPython
#
import numpy as np


if __name__ == '__main__':
    a = np.arange(12)
    print(a)
    print(type(a))
    print(a.shape)
    a.shape = 3,4
    print(a)
    print(a[2])
    print(a[2,1])
    print(a[:,1])
    print(a.transpose())
