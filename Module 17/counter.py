global_count = {}


def decorator_counter(func):
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        return func(*args, **kwargs)

    wrapped_func.count = 0
    return wrapped_func


@decorator_counter
def hello():
    print('hello')


@decorator_counter
def hello_2():
    print('hello')


print(global_count, hello.count, hello_2.count)
hello()
print(global_count, hello.count, hello_2.count)
hello_2()
print(global_count, hello.count)

print('*' * 100)
print(dir('.'))