__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# replacer.py was created on May 16 2022 @ 1:16 PM
# Project: FluentPython
#

from collections.abc import Iterable
from typing import TypeAlias

FromTo: TypeAlias = tuple[str,str]
l33t = [('a','4'),('e','3'),('t', '1'),('o','0')]
text = 'mad skilled moob powned leet'

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_,to in changes:
        text = text.replace(from_,to)

    return text