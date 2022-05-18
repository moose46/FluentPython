__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# chapter8_2.py was created on May 11 2022 @ 9:22 AM
# Project: FluentPython
#

from pytest import mark

from chapter8_3 import show_count


@mark.parametrize(
    'qty, expected',
    [
        (1, '1 part'),
        (2, '2 parts'),
    ],
)
def test_show_count(qty, expected):
    got = show_count(qty, 'part')
    assert got == expected


def test_show_count_zero():
    got = show_count(0, 'part')
    assert got == 'no parts'


def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'
