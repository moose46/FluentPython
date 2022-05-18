__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter6-2.py was created on May 06 2022 @ 11:21 AM
# Project: FluentPython
#
# http://localhost:8889/lab/tree/FluentPython/chapter6.ipynb
import traceback
class Gizmo:
    def __init__(self, def_name=None):
        print(f'Gizmo id:{id(self)}')
        if def_name == None:
            (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
            self.def_name = text[:text.find('=')].strip()

    def __str__(self):
        cls = self.__class__

x = Gizmo()
print(x.def_name)