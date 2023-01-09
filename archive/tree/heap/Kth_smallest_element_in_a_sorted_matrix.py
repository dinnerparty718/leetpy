from typing import List
import heapq

# own very slow. probobaly O(n**2)  min() is O(n)


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return -1

        p = [0] * len(matrix)

        counter = 0

        cur = matrix[0][0]

        while counter < k:

            l = [(matrix[row][p[row]] if p[row] < len(matrix)
                  else float('inf'), row) for row in range(len(matrix))]
            min_val, index = min(l)
            cur = min_val
            p[index] += 1
            counter += 1

        return cur


# O(n) + O(klogN)
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        r = []

        for a in matrix:
            r += a
        return heapq.nsmallest(k, r)[-1]


# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1248424/Python-O(klogk)
# push down and right item to min-heap and add them to visited list
class Solution3:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        visited = set([(0, 0)])
        minHeap = []
        minHeap.append((matrix[0][0], 0, 0))
        heapq.heapify(minHeap)

        m = len(matrix)
        n = len(matrix[0])

        res = matrix[0][0]

        while k:
            val, i, j = heapq.heappop(minHeap)

            for I, J in (i + 1, j), (i, j + 1):
                if I < m and J < n and (I, J) not in visited:
                    heapq.heappush(minHeap, (matrix[I][J], I, J))
                    visited.add((I, J))

            res = val
            k -= 1

        return res


so = Solution3()

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

k = 8

# matrix = [
#     [1, 2],
#     [1, 3]
# ]

# k = 3

res = so.kthSmallest(matrix, k)
print(res)
