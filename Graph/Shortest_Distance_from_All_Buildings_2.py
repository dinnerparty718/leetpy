from typing import List, Tuple
from collections import deque
from collections import defaultdict
# 0 empty land
# 1 building
# 2 obstacle

# for each build, visit the empty space

# excee limit most of the time

'''
from all building. BFS to each empty land

for each empty land. sum up the distanc is all reachable


'''


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


class Solution2:

    def __init__(self) -> None:
        self.empty, self.building = 0, 1

    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        candidate_lands = {}  # { position, distance }

        # 1. find all building and candidate empty lands
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == self.building:
                    buildings.append((r, c))
                elif grid[r][c] == self.empty:
                    candidate_lands[(r, c)] = 0

        # 2. compute min distance from each buiding to all cadidate empty lands

        for building_position in buildings:
            self.bfs(candidate_lands, building_position)

        return min(candidate_lands.values()) if buildings and candidate_lands else -1

    def bfs(self, candidate_lands: dict, position):
        distance = 0
        visited = set()
        q = deque([position])

        while q:
            distance += 1
            size = len(q)
            for _i in range(size):
                i, j = q.popleft()
                for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if (I, J) in candidate_lands and (I, J) not in visited:
                        candidate_lands[(I, J)] += distance
                        visited.add((I, J))
                        q.append((I, J))

        # optimized
        if len(visited) != len(candidate_lands):
            for position in set(candidate_lands.keys()).difference(visited):
                candidate_lands.pop(position)


so = Solution()

grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]


res = so.shortestDistance(grid)


print(res)
