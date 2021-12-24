
from typing import List


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

    return l


# bottom up
def merge_sort(nums: List[int]):
    l = [[num] for num in nums]

    while len(l) > 1:
        tmp = []

        for i in range(0, len(l), 2):
            if i + 1 < len(l):
                tmp.append(merge_list(l[i], l[i+1]))
            else:
                tmp.append(l[i])

        l = tmp

    return l[0]


nums = [4, 3, 1, 2, 0]
res = merge_sort(nums)


print(res)
