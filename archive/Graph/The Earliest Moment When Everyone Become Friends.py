from typing import List


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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        logs.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        for time, i, j in logs:
            uf.union(i, j)
            if uf.count == 1:
                return time

        # if not possible
        return -1


logs = [
    [20190101, 0, 1],
    [20190104, 3, 4],
    [20190107, 2, 3],
    [20190211, 1, 5],
    [20190224, 2, 4],
    [20190301, 0, 3],
    [20190312, 1, 2],
    [20190322, 4, 5]
]

logs = [[9, 3, 0], [0, 2, 1], [8, 0, 1], [1, 3, 2], [2, 2, 0], [3, 3, 1]]

n = 4

so = Solution()
res = so.earliestAcq(logs, n)


print(res)
