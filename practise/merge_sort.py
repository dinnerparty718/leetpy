from typing import List


def mergeList(l1: List[int], l2: List[int]):
    res = []

    p1 = 0
    p2 = 0
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            p2 += 1

    res.extend(l1[p1:])
    res.extend(l2[p2:])

    return res


def mergeSort(nums: List[int]):

    if len(nums) == 1:
        return nums

    mid = len(nums) // 2

    left_result = mergeSort(nums[:mid])

    right_result = mergeSort(nums[mid:])

    return mergeList(left_result, right_result)


nums = [4, 3, 1, 2, 0]


print(mergeSort(nums))

# l1 = [1, 3, 5]
# l2 = [2, 4, 6, 8]
