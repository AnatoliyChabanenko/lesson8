def pre_print(mas):
    print('-'*10)
    for i in mas:
        print(*i)
    print('-' * 10)


def get_number_for_index(i,j):
    return i*4+j+1

def get_empty_list (mas):
    empty = []
    for i in range(4):
        for j in range (4):
            if mas [i] [j] == 0:
                num = get_number_for_index(i,j)
                empty.append(num)
    return empty

def get_index_from_numbers(num):
    num-=1
    x,y = num//4, num%4
    return x,y


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]



mas [1] [2] = 2
mas [3] [0] = 4
print(get_empty_list(mas))
pre_print(mas)


if __name__ == '__main__':
    pass