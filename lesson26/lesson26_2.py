def _merge_sort(indices, the_list):
    start = indices[0] #аргументы
    end = indices[1]
    mid = (end - start) // 2 + start
    if start < mid:
        _merge_sort((start, mid), the_list)
    if mid + 1 <= end and end - start != 1:
        _merge_sort((mid + 1, end), the_list)
    sort_sub_list(the_list, indices[0], indices[1])


def sort_sub_list(the_list, start, end):
    orig_start = start
    initial_start_second_list = (end - start) // 2 + start + 1
    list2_first_index = initial_start_second_list
    new_list = []
    while start < initial_start_second_list and list2_first_index <= end:
        first1 = the_list[start]
        first2 = the_list[list2_first_index]
        if first1 > first2:
            new_list.append(first2)
            list2_first_index += 1
        else:
            new_list.append(first1)
            start += 1

    while start < initial_start_second_list:
        new_list.append(the_list[start])
        start += 1

    while list2_first_index <= end:
        new_list.append(the_list[list2_first_index])
        list2_first_index += 1

    for i in new_list:
        the_list[orig_start] = i
        orig_start += 1


def merge_sort(the_list):
    return _merge_sort((0, len(the_list) - 1), the_list)


if __name__ == '__main__':
    d = [32, 1, 2, 34, 4, 43]
    merge_sort(d)
    print(d)
