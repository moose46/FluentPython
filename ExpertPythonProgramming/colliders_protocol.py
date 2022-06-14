__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# aabb.py was created on June 08 2022 @ 7:11 PM
# Project: Expert Python Programming
#
from dataclasses import dataclass
import itertools
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable, Iterable


@runtime_checkable
class IBox(Protocol):
    x1: float
    x2: float
    y1: float
    y2: float

@runtime_checkable
class ICollider(Protocol):
    @property
    def bounding_box(self) -> IBox:
        pass


class ColliderABC(ABC):
    @property
    @abstractmethod
    def bounding_box(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ColliderABC:
            if any('bounding_box' in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


@dataclass()
class Point:
    x: float
    y: float


@dataclass()
class Box:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Square(ColliderABC):
    x: float
    y: float
    size: float

    @property
    def bounding_box(self):
        return Box(self.x, self.y, self.x + self.size, self.y + self.size)


@dataclass
class Rect(ColliderABC):
    x: float
    y: float
    width: float
    height: float

    @property
    def bounding_box(self):
        return Box(self.x, self.y, self.x + self.width, self.y + self.height)


@dataclass()
class Circle(ColliderABC):
    x: float
    y: float
    radius: float

    @property
    def bounding_box(self):
        return Box(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        )


def rects_collide(rect1: IBox, rect2: IBox):
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
        rect1.x1 < rect2.x2
        and rect1.x2 > rect2.x1
        and rect1.y1 < rect2.y2
        and rect1.y2 > rect2.y1
    )


@dataclass()
class Line:
    p1: Point
    p2: Point

    @property
    def bounding_box(self):
        return Box(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


def find_collisions(objects: Iterable[ICollider]):
    """https://www.geeksforgeeks.org/python-itertools-combinations-function/"""
    # for item in objects:
    #     if not isinstance(item, ColliderABC):
    #         raise TypeError(f'{item} is not a collider')

    return [
        (item1, item2)
        for item1, item2 in itertools.combinations(objects, 2)
        if rects_collide(item1.bounding_box, item2.bounding_box)
    ]


if __name__ == '__main__':
    for collision in find_collisions(
        [
            Square(0, 0, 10),
            Rect(5, 5, 20, 20),
            Square(15, 20, 5),
            Circle(1, 1, 2),
            # Point(1,1)
            Line(Point(0, 0), Point(100, 100)),
        ]
    ):
        print(collision)

class TestMe:
    def __init__(self,booboo: str) -> None:
        pass

t = TestMe("booboo")
