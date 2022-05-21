__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# top_test.py was created on May 20 2022 @ 1:35 PM
# Project: FluentPython
#

from collections.abc import Iterator

from typing import TYPE_CHECKING

import pytest

from top import top

def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana'.split()

    series: Iterator[tuple[int,str]] = (
        (len(s), s) for s in fruit
    )
    length = 3
    expected = [(6,'banana'),(5,'mango'),(5,'apple')]
    result = top(series,length)
    if TYPE_CHECKING:
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)
    assert result == expected

# intentional type error
def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)

    with pytest.raises(TypeError) as excinfo:
        top(series,3)

    assert "'<' not supported" in str(excinfo.value)
