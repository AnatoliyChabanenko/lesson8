'''Create your own implementation of a built-in function enumerate,
named `with_index`, which takes two parameters: `iterable` and `start`,
 default is 0. Tips: see the documentation for the enumerate function'''

def enumerate(iterable, start=0):
    count = start
    for elem in iterable:
        yield count, elem
        count += 1


a= [ 'apple', 'vodila ', 'champ ']
b = enumerate(a)

print(next(b))
print(next(b))
print(next(b))
