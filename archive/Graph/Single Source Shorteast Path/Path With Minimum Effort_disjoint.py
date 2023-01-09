from typing import List

# Union Find
# map 2D array to 1D array for union find
# i,j -> i*n + j
# currentRow * Cols + currentCol


class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        if m == 1 and n == 1:
            return 0

        uf = UnionFind(m*n)

        edges_set = set()

        def getNode(i, j):
            return i*n + j

        def neighbors(i, j):
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < m and 0 <= J < n:
                    yield I, J

        # todo
        for i in range(m):
            for j in range(n):
                for I, J in neighbors(i, j):
                    diff = abs(heights[i][j] - heights[I][J])

                    src = getNode(i, j)
                    des = getNode(I, J)

                    if src > des:
                        src, des = des, src
                    edges_set.add((diff, src, des))

        edges = list(edges_set)
        edges.sort(key=lambda x: x[0])

        for w, s, t in edges:
            uf.union(s, t)
            if uf.connected(0, m*n-1):
                return w


so = Solution()

#heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
#heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

res = so.minimumEffortPath(heights)

print(res)
