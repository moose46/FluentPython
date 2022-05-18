__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'
#
# Author: Robert W. Curtiss
# birds.py was created on May 11 2022 @ 1:16 PM
# Project: FluentPython
#


class Bird:
    pass


class Duck(Bird):
    def quack(self):
        print('Quack')


def alert(birdie):
    birdie.quack()


def alert_duck(birdie: Duck) -> None:
    birdie.quack()


def alert_bird(birdie: Bird) -> None:
    birdie.quack()
