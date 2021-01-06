lst = ['Alice', 'Bob', 'Carl']


def opps(x):
    return (x[4])


try:
    opps(lst)
except IndexError:
    print(43)
try:
    opps(lst)
except KeyError:
    print(43)
except:
    print('не получилось словить')