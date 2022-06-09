__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# aabb.py was created on June 08 2022 @ 7:11 PM
# Project: Expert Python Programming
#
from dataclasses import dataclass
import itertools


@dataclass()
class Box:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Square:
    x: float
    y: float
    size: float

    @property
    def bounding_box(self):
        return Box(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size
        )


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def bounding_box(self):
        return Box(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height
        )


@dataclass()
class Circle:
    x: float
    y: float
    radius: float

    @property
    def bounding_box(self):
        return Box(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius
        )


def rects_collide(rect1: Box, rect2: Box):
    """Check collision between rectangles
        rectangle coordinates
        ------(x2,y2)
        |           |
        (x1,y1)------
    :param rect1:
    :param rect2:
    :return:
    """
    return (
            rect1.x1 < rect2.x2 and
            rect1.x2 > rect2.x1 and
            rect1.y1 < rect2.y2 and
            rect1.y2 > rect2.y1
    )


def find_collisions(objects):
    return [
        (item1, item2) for item1, item2 in itertools.combinations(objects, 2)
        if rects_collide(
            item1.bounding_box,
            item2.bounding_box
        )
    ]


if __name__ == '__main__':
    for collision in find_collisions(
            [
                Square(0, 0, 10),
                Rect(5, 5, 20, 20),
                Square(15, 20, 5),
                Circle(1, 1, 2)
            ]
    ):
        print(collision)
