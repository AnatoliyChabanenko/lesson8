import timeit


def sequential_search(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found
def my_binar_search (my_list , iskat):

    if len(my_list) == 0:
        return False
    else:
        mid = len(my_list)//2
        if iskat == my_list[mid]:
            return True
        elif iskat < my_list[mid] :
            return my_binar_search(my_list[:mid], iskat)
        else:
            return my_binar_search(my_list[mid+1:], iskat)



if __name__ == "__main__":
    seq_timer = timeit.timeit(
        stmt="sequential_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100,
        setup="from __main__ import sequential_search"
    )
    print(seq_timer)

    bin_timer = timeit.timeit(
        stmt="binary_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100,
        setup="from __main__ import binary_search"
    )
    print(bin_timer)

    bin_my_bin = timeit.timeit(
        stmt="my_binar_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 5)",
        number=100,
        setup="from __main__ import my_binar_search"
    )
    print(bin_my_bin)
