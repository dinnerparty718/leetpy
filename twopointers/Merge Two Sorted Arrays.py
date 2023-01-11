'''
6 · Merge Two Sorted Arrays
time: O(n)

'''


from typing import (
    List,
)


class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """

    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        p1, p2 = 0, 0

        res = []

        while p1 < len(a) and p2 < len(b):
            if a[p1] < b[p2]:
                res.append(a[p1])
                p1 += 1
            else:
                res.append(b[p2])
                p2 += 1

        while p1 < len(a):
            res.append(a[p1])
            p1 += 1

        while p2 < len(b):
            res.append(b[p2])
            p2 += 1

        return res


so = Solution()
A = [1, 2, 3, 4]
B = [2, 4, 5, 6]

res = so.merge_sorted_array(A, B)

print(res)
