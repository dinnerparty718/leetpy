from typing import List
from collections import deque

# shortest path problem
# own solution
# https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        q = deque()
        visited = set()

        dis = 0

        # start from zeros
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))

        while q:
            n = len(q)

            for _ in range(n):
                i, j = q.popleft()

                if 0 <= i < len(mat) and 0 <= j < len(mat[0]) and (i, j) not in visited:
                    visited.add((i, j))
                    if mat[i][j] == 1:
                        mat[i][j] = dis

                    # todo can speed up by elimiating out of bound cases
                    q.extend([(i + 1, j), (i-1, j), (i, j+1), (i, j-1)])

            dis += 1

            # visited.add((i, j))

        return mat


# optimized
class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        q, m, n = deque(), len(mat), len(mat[0])
        visited = set()

        # start from zeros
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            i, j = q.popleft()

            for I, J in (i + 1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n and (I, J) not in visited:
                    visited.add((I, J))
                    mat[I][J] = mat[i][j] + 1
                    q.append((I, J))

                # visited.add((i, j))

        return mat


so = Solution2()


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

res = so.updateMatrix(mat)

print(res)
