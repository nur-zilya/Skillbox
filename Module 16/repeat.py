from typing import Callable, Any

def repeat(n: int):
    def do_twice(func: Callable) -> Callable:
        def wrapped_func(*args, **kwargs) -> Any:
            for _ in range(n):
                func(*args,**kwargs)
            return
        return wrapped_func
    return do_twice


@repeat(3)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))

greeting('Tom')