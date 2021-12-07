from typing import List
from collections import deque
from collections import defaultdict
# 0 empty land
# 1 building
# 2 obstacle

# for each build, visit the empty space

# excee limit
# todo


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))

        res = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res[(i, j)] = [-1] * len(buildings)

        def getNei(i: int, j: int, visited):
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and (I, J) not in visited:
                    yield I, J

        def bfs(i: int, j: int, idx: int):
            visited = set()
            q = deque([(i, j, 0)])

            while q:
                i, j, step = q.popleft()

                if (i, j) in visited and grid[i][j] == 0:
                    res[(i, j)][idx] = step

                for I, J in getNei(i, j, visited):
                    visited.add((I, J))
                    q.append((I, J, step+1))

        for idx in range(len(buildings)):
            i, j = buildings[idx]
            bfs(i, j, idx)

        # for k, v in res.items():
        #     print(k, v)

        min_step = float('inf')

        # print(empty_land_dict)

        for k, v in res.items():
            if all(value != -1 for value in v):
                min_step = min(min_step, sum(v))

        # print(visit_count)
        return min_step if min_step != float('inf') else -1


so = Solution()

grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]


res = so.shortestDistance(grid)


print(res)
