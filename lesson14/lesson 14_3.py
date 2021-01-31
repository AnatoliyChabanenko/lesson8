'''Напишите декоратор arg_rules, который проверяет аргументы, переданные функции.

Декоратор должен принимать 3 аргумента:

max_length: 15

type_: str

содержит: [] - список символов, которые должен содержать аргумент

Если какая-либо проверка правил возвращает False, функция должна вернуть
 False и вывести причину сбоя; в противном случае вернуть результат.
'''
from functools import wraps


def arg_rules(type_:type, max_length=15, mylist=list):
    def return_fals(func):
        @wraps(func)
        def do_shit(*args, **kwargs):
            if not all(map(lambda x: isinstance(x, type_), args)):
                raise TypeError('неправильный ввод')
            z=[]
            for i in args:
                z.append(len(i))
            if sum(z) > max_length:
                raise  TypeError ('очень много символов')

            a = any(a in mylist for a in args)
            return a
        return do_shit

    return return_fals


@arg_rules(str, 10,['er'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('er' , '43'))
