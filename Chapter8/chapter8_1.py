__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# chapter8_1.py was created on May 11 2022 @ 9:16 AM
# Project: FluentPython
#
def show_count(count, word) -> str:
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'


show_count(99, 'bird')
