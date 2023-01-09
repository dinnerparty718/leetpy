from typing import List


# todo check DFS and BFS

# disjoint set to see if two edges are already connected
# check if root count is 1

# Time O(N⋅α(N))
# Space O(n)

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

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

        self.count -= 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for i, j in edges:
            if uf.connected(i, j):
                return False
            else:
                uf.union(i, j)
        return uf.count == 1


n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]


so = Solution()

res = so.validTree(n, edges)
print(res)
