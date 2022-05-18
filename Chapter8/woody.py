__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# woody.py was created on May 12 2022 @ 8:18 AM
# Project: FluentPython
#
from typing import Any, Union

from birds import *

woody = Bird()
alert(woody)
alert_duck(woody)
alert_bird(woody)


# subtype-of-versus consistent-with
class T1:
    print('T1')
class T2(T1):
    print('T2')
def f1(p: T1 ) -> None:
    pass

o2 = T2()
f1(o2)
def  f2(p: T2) -> None:
    pass
o1 = T1()
print(f2(o1))
def f3(p: Any) -> None:
    pass
o0 = object()
o1 = T1()
o2 = T2()

f3(o0)
f3(o1)
f3(o2)

def f42(p: str | None): # python > 3.10
   pass

def ord(c: Union[str, bytes]) -> int:
    pass
