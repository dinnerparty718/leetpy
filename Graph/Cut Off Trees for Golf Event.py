from typing import List
from collections import deque
import heapq

# https://www.youtube.com/watch?v=OFkLC30OxXM

#  add x -> path shortest path add
# https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/1033258/Python-BFS-and-PriorityQueue-w-comments-and-prints-for-visualization


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])

        min_heap = []

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:  # ! fck only cut tree when height > 1
                    min_heap.append((forest[i][j], i, j))

        heapq.heapify(min_heap)

        res = 0

        def bfs(x0: int, y0: int, x1: int, x2: int) -> int:
            step = 0

            q = deque([(x0, y0)])
            visited = set((x0, y0))

            while q:

                size = len(q)

                for _ in range(size):

                    x, y = q.popleft()
                    if (x, y) == (x1, x2):
                        return step

                    for i, j in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                        if 0 <= i < m and 0 <= j < n and forest[i][j] != 0 and (i, j) not in visited:
                            q.append((i, j))
                            visited.add((i, j))

                step += 1

            return -1

        last_location = 0, 0
        while min_heap:
            h, i, j = heapq.heappop(min_heap)

            val = bfs(last_location[0], last_location[1], i, j)

            if val == -1:
                return -1

            res += val
            last_location = i, j

        return res


so = Solution()

forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
forest = [[4, 2, 3], [0, 0, 1], [7, 6, 5]]
res = so.cutOffTree(forest)

print(res)
