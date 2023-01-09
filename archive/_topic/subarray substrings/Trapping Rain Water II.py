from typing import List
import heapq

'''
O(mn log(mn))

different from 1d trapping water

heightMap = [
    [12, 13, 1, 12],
    [13, 4, 13, 12],  # 9 +
    [13, 8, 10, 12],  # 4 + 2  4 will leak along with the path 4 -> 8 -> 10 -> 12, so it can not reach to 13, but only 12 and I think that's why it can only store 8 instead of 9.
    [12, 13, 12, 12],  #
    [13, 13, 13, 13]
]

minheap , add 4 neighbors

add row 0, m-1 col 0 ,n-1 to the minheap





'''


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])

        water = 0

        min_heap = []

        for i in range(m):
            # first/last col
            heapq.heappush(min_heap, (heightMap[i][0], i, 0))
            heapq.heappush(min_heap, (heightMap[i][n-1], i, n-1))

        for j in range(n):
            # first/last row
            heapq.heappush(min_heap, (heightMap[0][j], 0, j))
            heapq.heappush(min_heap, (heightMap[m-1][j], m-1, j))

        visited = {(i, j) for _, i, j in min_heap}

        while min_heap:
            h, i, j = heapq.heappop(min_heap)
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and (I, J) not in visited:
                    visited.add((I, J))
                    water += max(0, h - heightMap[I][J])
                    heapq.heappush(min_heap, (max(h, heightMap[I][J]), I, J))

        return water


heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]


heightMap = [
    [3, 3, 3, 3, 3],
    [3, 2, 2, 2, 3],
    [3, 2, 1, 2, 3],
    [3, 2, 2, 2, 3],
    [3, 3, 3, 3, 3]
]


heightMap = [
    [12, 13, 1, 12],
    [13, 4, 13, 12],  # 9 +
    [13, 8, 10, 12],  # 4 + 2  4 will leak along with the path 4 -> 8 -> 10 -> 12, so it can not reach to 13, but only 12 and I think that's why it can only store 8 instead of 9.
    [12, 13, 12, 12],  #
    [13, 13, 13, 13]
]


so = Solution()
res = so.trapRainWater(heightMap)

print(res)
