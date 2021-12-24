from typing import List


def quicksort(lst: List[int]):

    # two pointer inplace

    def partition(lst, l, r):
        pivot = lst[r]

        i = l

        for j in range(l, r):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1

        # move the pivot point its place
        lst[i], lst[r] = lst[r], lst[i]

        return i

    def helper(lst, l, r):
        if l < r:
            p = partition(lst, l, r)
            helper(lst, l, p-1)
            helper(lst, p+1, r)

        return l

    return helper(lst, 0, len(lst)-1)


nums = [1, 5, 3, 2, 8, 7, 6, 4]

quicksort(nums)

# [1, 5, 3, 2, 8, 7, 6, 4]


print(nums)
