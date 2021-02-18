
a = [ [ [ 38.123318, 47.049666 ], [ 38.123284, 47.049521 ], [ 38.123074, 47.049478 ], [ 38.122915, 47.049408 ], [ 38.122835, 47.049367 ]]]


def recursive(obj):
    for item in obj:
        if isinstance(item[0] , float):
            return recursive(item[::-1])
        else:
            return obj

if __name__ == '__main__':
    print(recursive(a))