__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'


#
# Author: Robert W. Curtiss
# chapter8_3.py was created on May 11 2022 @ 10:00 AM
# Project: FluentPython
#
from typing import Optional

def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'


show_count(99, 'bird')
