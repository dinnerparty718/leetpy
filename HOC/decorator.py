# decorator add extra features

# keyword args

from time import time


def my_decorator(func):
    def wrap_func():
        print('in the wrapper function')
        func()
        print('***')
    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('see ya later')


def regularHello():
    print('another hello')


# hello()
# bye()


a = my_decorator(regularHello)

a()


def fancy_dec(func):
    def wrapper_func(*args, **kwargs):
        print('in wrapper')
        func(*args, **kwargs)
    return wrapper_func


# @fancy_dec
def hello(x, emoji=":("):
    print(x, emoji)


a = fancy_dec(hello)

a('hi')


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        reuslt = fn(*args, **kwargs)
        t2 = time()

        print(f'it took {t2-t1} ms')
        return reuslt
    return wrapper


@performance
def long_time():
    for i in range(500000):
        i*5


long_time()
