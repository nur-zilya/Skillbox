# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
# как с аргументами, так и без них.

from time import sleep


def slow_it_now(_func=None, *, n=1):
    def slowdown_ns(func):
        def wrapper(*args, **kwargs):
            sleep(n)
            result = func(*args, **kwargs)
            return result

        return wrapper

    if _func is None:
        return slowdown_ns
    else:
        return slowdown_ns(_func)


@slow_it_now
def test() -> None:
    print('<Тут что-то происходит...>')


test()