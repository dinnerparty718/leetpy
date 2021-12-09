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

        empty_land_dict = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if (i, j) not in empty_land_dict:
                        empty_land_dict[(i, j)] = [-1] * len(buildings)

        mapping = {}

        for i in range(len(buildings)):
            mapping[i] = buildings[i]

        # tuple (bulding index, current location)
        l = [(k, v, 0) for k, v in mapping.items()]

        # change data structure
        visited = {}

        for k in mapping:
            visited[k] = set()

        q = deque(l)

        def getNei(i: int, j: int):
            for I, J in (i + 1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and (I, J) not in visited[idx]:
                    yield I, J

        # bfs
        while q:
            size = len(q)
            for _i in range(size):
                idx, (i, j), step = q.popleft()

                for I, J in getNei(i, j):
                    empty_land_dict[(I, J)][idx] = step + 1
                    visited[idx].add((I, J))
                    q.append((idx, (I, J), step + 1))

        min_step = float('inf')

        # print(empty_land_dict)

        for k, v in empty_land_dict.items():
            print(k, v, sum(v))
            if all(value != -1 for value in v):
                min_step = min(min_step, sum(v))

        return min_step if min_step != float('inf') else -1


so = Solution()

grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]


res = so.shortestDistance(grid)


print(res)
