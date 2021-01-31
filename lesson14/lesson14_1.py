from functools import wraps
def decorator (func):
    @wraps(func)
    def print_func(*args ,**kwargs ):
        func(*args, **kwargs)
        print(f'{func.__name__}   called with {args}, {kwargs}')
    return print_func

@decorator
def add(x, y):

    return print(x + y)

add(4,5)

@decorator
def square_all(*args):

    return print([arg ** 2 for arg in args])
square_all(4 , 3 ,2 , 1 , 1)