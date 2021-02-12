from typing import Optional


def to_power(x, exp) -> object:
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / to_power(x, -exp)
    elif exp % 2 == 0:
        return to_power(x * x, exp / 2)
    else:
        return to_power(x, exp - 1) * x


if __name__ == '__main__':
    print(to_power(2, 3))
