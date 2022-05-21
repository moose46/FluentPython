__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
# 
# Author: Robert W. Curtiss
# chapter9-1.py was created on May 20 2022 @ 4:12 PM
# Project: FluentPython
#

def deco(func):
    def inner():
        print('running inner')
    return inner

@deco
def target():
    print("running target")

target()


