__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter3-1.py was created on April 20 2022 @ 12:01 PM
# Project: FluentPython
# Chapter 3

dial_codes = [
    (800,'Bangladesh'),
    (55,'Brazil'),
    (86,'China'),
    (91,'India'),
    (62,'Indonesia'),
    (81,'Japan'),
    (234,'Nigeria'),
    (92,'Pakistan'),
    (7,'Russia'),
    (1,'United States'),
]

def dump(**kwargs):
    return kwargs


if __name__ == '__main__':
    country_dial = {country: code for code, country in dial_codes}
    n = {code: country.upper() for country,code in sorted(country_dial.items()) if code < 90}

    x = dump(**{'x':1},y=2,**{'z': 3})
    x1 = {'a': 0, **{'x' : 1}, 'y': 2, **{'z':3, 'x' : 4, 'yy':42, **{'c': 213, 'd': 128}}}

    # union
    d1 = {'a':1,'b':3}
    d2 = {'a':2,'b':4,'c': 6}
    d3 = d1 | d2

    # stomps on original
    d2 |= d1

