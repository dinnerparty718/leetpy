'''
460 · Find K Closest Elements
O(logn + k) time

binary search + two pointers

1. find the closet index
#! specail case
 all elements > target
 all elements > target

2. left, right

'''


from typing import (
    List,
)


class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:

        def firstIndex(a: List[int], target: int):
            # write your code here
            left, right = 0, len(a) - 1
            while left + 1 < right:
                mid = left + ((right - left) >> 1)
                if a[mid] <= target:
                    left = mid
                else:
                    right = mid

            if a[left] >= target:
                return left

            if a[right] >= target:
                return right

            return len(a)   # [1,2,5,6]  target 11

        index = firstIndex(a, target)
        left, right = index - 1, index

        res = []

        for _ in range(k):
            if left < 0:
                res.append(a[right])
                right += 1
            elif right == len(a):
                res.append(a[left])
                left -= 1
            else:
                if target - a[left] <= a[right] - target:
                    res.append(a[left])
                    left -= 1
                else:
                    res.append(a[right])
                    right += 1

        return res


so = Solution()

A = [1, 4, 6, 8]
target = 3
k = 3

res = so.k_closest_numbers(A, target, k)
print(res)
