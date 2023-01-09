from typing import List
import heapq

# Dijkstra

# Time O(m*nlogm*n)  m*n number of nodes
# space O(m*n)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        visited = [[False] * n for i in range(m)]
        differences = [[float('inf')] * n for i in range(m)]

        differences[0][0] = 0

        pq = [(0, 0, 0)]  # efforts, i,j

        def neighbors(i: int, j: int):
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and not visited[I][J]:
                    yield (I, J)

        while pq:
            diff, i, j = heapq.heappop(pq)
            visited[i][j] = True

            for I, J in neighbors(i, j):
                cur_diff = abs(heights[i][j] - heights[I][J])
                # modification of sum path
                max_diff = max(cur_diff, differences[i][j])

                if differences[I][J] > max_diff:
                    differences[I][J] = max_diff
                    heapq.heappush(pq, (max_diff, I, J))

        return differences[m-1][n-1]


so = Solution()

#heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
#heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

res = so.minimumEffortPath(heights)

print(res)
