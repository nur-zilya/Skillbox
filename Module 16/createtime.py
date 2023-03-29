from contextlib import contextmanager

import math
import datetime

def createtime(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print("Created at: ", datetime.datetime.now())
        print("Methods: ", end=' ')
        for i_method in dir(cls):
            if i_method.startswith("__") is True:
                continue
            else:
                print(i_method, end=' ')
        print()
        return instance
    return wrapper



@createtime
class MyMath():

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


    def circle_len(cls, r):
        c = 2 * math.pi * r
        return c


    def circle_square(cls, r):
        a = math.pi * r ** 2
        return a


    def cube_vol(cls, a):
        vol = a ** 3
        return vol


    def sphere_sq(cls, r):
        s = 4 * math.pi * r ** 2
        return s


MyMath()
MyMath()