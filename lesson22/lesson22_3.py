from typing import Optional
def mult(a: int, n: int) -> int:
    if n == 1:
        return  a
    elif n > 1:
        return mult(a +  a , n-1 )
    elif n == 0:
        return 0
    elif n < 0:
        raise ValueError("This function works only with postive integers")


if __name__ == '__main__':
    print(mult(2, 4))