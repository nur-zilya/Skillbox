from contextlib import contextmanager
from collections.abc import Iterator
import time

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    finally:
        print(time.time() - start)

with timer() as t1:
    def hard_func():
        return [x ** 2 ** x for x in range(22)]


