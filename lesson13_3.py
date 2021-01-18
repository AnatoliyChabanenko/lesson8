def choose_func(nums: list, func1, func2):
    for i in nums:
        if i >= 0:
            return func2(nums)
        if nums < 0:
            return func1 (nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
nums3 = [ 1, -3 , 2,3  ,1 , 2, - 332]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

def square_nums(nums):
    return [num ** 2 for num in nums]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums3, square_nums, remove_negatives))




# def sqr(nums):
#     return nums ** 2
# print(list(map(sqr,x)))
