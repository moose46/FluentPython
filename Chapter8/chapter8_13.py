__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# chapter8_13.py was created on May 13 2022 @ 1:18 PM
# Project: FluentPython
#
from typing import Sequence

animals = 'drake heron tbex koala lynx tahr xerus yak zapus'.split(' ')


def columize(
    sequence: Sequence[str], num_columns: int = 0
) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)   # Exponentiation sqrt of 9 = 3

    num_rows, remainder = divmod(len(sequence), num_columns)
    num_rows += bool(remainder)

    return [tuple(sequence[t::num_rows]) for t in range(num_rows)]


table = columize(animals)
