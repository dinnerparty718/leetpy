from typing import List

# top down


def merge_sort(nums: List[int]):

    if len(nums) <= 1:
        return nums

    mid = int(len(nums)/2)
    left_list = merge_sort(nums[0: mid])
    right_list = merge_sort(nums[mid:])
    return merge_list(left_list, right_list)


# merge 2 two sorted list
def merge_list(l1: List[int], l2: List[int]):
    p1 = 0
    p2 = 0

    l = []

    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] <= l2[p2]:
            l.append(l1[p1])
            p1 += 1
        else:
            l.append(l2[p2])
            p2 += 1

    # append what is remained in either of the lists
    l.extend(l1[p1:])
    l.extend(l2[p2:])

    # if p1 < len(l1):
    #     l.extend(l1[p1:])
    # else:
    #     l.extend(l2[p2:])

    return l


l1 = [1, 2, 5, 7, 23, 45]
l2 = [4, 6, 9, 10, ]


res = merge_list(l1, l2)

print(res)
