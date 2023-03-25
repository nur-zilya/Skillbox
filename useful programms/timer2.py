import time
from datetime import datetime
import functools
from typing import Callable, Any


def timer(func, *args, **kwargs) -> Any:
    def wrapper(*args, **kwargs):
        start_at = datetime.now()
        time.sleep(1)
        print(start_at)
        # res = func(*args, **kwargs)
        res = func(*args, **kwargs)
        end_time = datetime.now()
        print(end_time)

        return res

    return wrapper


@timer
def say(*args):
    print("Hello", args)


if __name__ == "__main__":
    say(2)