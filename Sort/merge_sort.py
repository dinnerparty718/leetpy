#divide and conquer


from typing import List


def merge_list(a: List[int], b: List[int]):
    res = []

    p1 = p2 = 0

    while p1 < len(a) and p2 < len(b):
        if a[p1] < b[p2]:
            res.append(a[p1])
            p1 += 1
        else:
            res.append(b[p2])
            p2 += 1

    res.extend(a[p1:])
    res.extend(b[p2:])

    return res


def merge_sort(nums: List[int]):

    if len(nums) <= 1:
        return nums

    # divide

    mid = int(len(nums)/2)

    left_result = merge_sort(nums[0:mid])
    right_result = merge_sort(nums[mid:])

    return merge_list(left_result, right_result)


nums = [2, 5, 8, 3, 9, 4]
res = merge_sort(nums)

print(res)
