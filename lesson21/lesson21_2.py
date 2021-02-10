from typing import List


def question3(first_list: List[int], second_list: List[int]) -> List[int]:  # O(1)
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


print(question3([321, 66, 87, 67, 77], [86, 43, 43, 77, 2, 21, 88, 543]))
