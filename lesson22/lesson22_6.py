def sumall(inval: int ,d :int = 0 ) -> int :

    if inval == 0:
        return  d
    else:
        return sumall(inval//10, d + inval % 10 )



if __name__ == '__main__':
    print(sumall(432432))
