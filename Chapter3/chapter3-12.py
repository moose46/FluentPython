__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-12.py was created on April 27 2022 @ 9:20 AM
# Project: FluentPython
#

found = 0
needles = [1,3,5,6,7,9,20]
haystack = range(1,30)
if __name__ == '__main__':
    for n in needles:
        if n in haystack:
            found += 1

    found1 = len(set(needles) & set(haystack))

    found2 = len(set(needles).intersection(haystack))
