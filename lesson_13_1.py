def fun():
    a = 1
    str = 'GeeksForGeeks'


def fd(func):
    return print(func.__code__.co_nlocals)
fd(fun)