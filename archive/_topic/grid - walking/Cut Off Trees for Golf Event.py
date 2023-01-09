from typing import List
from sortedcontainers import SortedList
from collections import deque
# loop through array and find all locations >=1
# sort
# from (0,0) to next smallest location. find shortest path


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = SortedList([])

        m = len(forest)
        n = len(forest[0])

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.add((forest[i][j], i, j))

        last_location = (0, 0)

        result = 0

        def bfs(start_i, start_j, I, J):
            step = 0

            q = deque([(start_i, start_j)])

            #! board(forest need re-use, keep track of visited node)
            visited = set([(start_i, start_j)])

            while q:

                size = len(q)

                for _ in range(size):
                    i, j = q.popleft()
                    if (i, j) == (I, J):

                        return step

                    for new_i, new_j in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                        if 0 <= new_i < m and 0 <= new_j < n and forest[new_i][new_j] >= 1 and (new_i, new_j) not in visited:
                            q.append((new_i, new_j))
                            visited.add((new_i, new_j))

                step += 1

            return -1

        while trees:
            h, I, J = trees.pop(0)
            forest[I][J] = 1

            s = bfs(last_location[0], last_location[1], I, J)
            if s == -1:
                return -1
            else:
                result += s
            last_location = (I, J)

        return result


so = Solution()

forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]

forest = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]
forest = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]

res = so.cutOffTree(forest)

print(res)
