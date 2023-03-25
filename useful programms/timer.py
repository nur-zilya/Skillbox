# import time
# from datetime import datetime
# import functools
# from typing import Callable, Any
#
#
# def timer(func, *args, **kwargs) -> Any:
#     def wrapper(*args, **kwargs):
#         start_at = datetime.now()
#         time.sleep(1)
#         print(start_at)
#         # res = func(*args, **kwargs)
#         res = func(*args, **kwargs)
#         end_time = datetime.now()
#         print(end_time)
#
#         return res
#
#     return wrapper
#
#
# @timer
# def say(*args):
#     print("Hello", args)
#
#
# if __name__ == "__main__":
#     say(2)


import time


def timer(func):
    start = time.time()
    func()
    end = time.time()
    return end - start


def hard_func():
    return [x ** 2 ** x for x in range(22)]


print(timer(hard_func))