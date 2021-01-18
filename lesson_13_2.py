'''Write a Python program to access a function inside a function
 (Tips: use function, which returns another function)'''
def outer(num1):
    def inner_increment(num2):
        nonlocal num1
        num1 += 2
        return num1 + num2
    return inner_increment
func = outer(2)
print(func(4))