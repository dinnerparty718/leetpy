from typing import List
import heapq
#from heapq import nsmallest

# todo add use binarysearch to calculate the strenth

# own
# nsmallest or nlargest
# time complexity O(n + k*logn) , first it heapify the list(length = n)


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        my_dict = {}

        for row in range(len(mat)):
            my_dict[row] = sum(mat[row])

        print(my_dict)

        return heapq.nsmallest(k, my_dict.keys(), key=my_dict.get)


class Solution2:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [x[1] for x in heapq.nsmallest(k, ((sum(s), i) for i, s in enumerate(mat)))]


# using sort
# time 1. count   O(m*n)
# time 2  sort    O(mlogm)
# add time O(m(n+ logm))
# space o(m)
class Solution3:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = [(sum(s), i) for i, s in enumerate(mat)]
        res.sort()

        return [row for _, row in res[:k]]


so = Solution3()

mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2

res = so.kWeakestRows(mat, k)
print(res)
