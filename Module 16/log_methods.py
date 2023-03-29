from _datetime import datetime
import functools


def time(cls, func, date_format):
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
            format = date_format
            for sym in format:
                if sym.isalpha():
                    format = format.replace(sym, '%' + sym)
            print(f'Запускается {cls.__name__}.{func.__name__} Дата и время запуска: {datetime.now().strftime(format)}')
            res = func(*args, **kwargs)
            return res
    return wrapped


def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if method.startswith("__") is False:
                current_method = getattr(cls, method)
                decorated_method = time(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return decorate

@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
