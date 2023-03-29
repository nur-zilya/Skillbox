from abc import ABC, abstractmethod
import math


class MyMath(ABC):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @classtmethod
    def circle_len(cls, r):
        c = 2 * math.pi * r
        return c

    @classtmethod
    def circle_square(cls, r):
        a = math.pi * r ** 2
        return a

    @classtmethod
    def cube_vol(cls, a):
        vol = a ** 3
        return vol

    @classtmethod
    def sphere_sq(cls, r):
        s = 4 * math.pi * r ** 2
        return s
