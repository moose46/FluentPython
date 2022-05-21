__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# variance.py was created on May 20 2022 @ 3:28 PM
# Project: FluentPython
#

from collections.abc import Callable

def update(probe: Callable[[], float], display: Callable[[float], None]) -> None:
    temperature = probe()
    # imagine lots of code here
    display(temperature)

def probe_ok() -> int:
    return 42

def display_wrong(temperature: int) -> None:
    print(hex(temperature))

update(probe_ok, display_wrong)  # type errors

def display_ok(temperature: complex) -> None:
    print(temperature)

update(probe_ok, display_ok) # ok
