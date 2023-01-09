from typing import List
import heapq
# min spanning tree


class UnionFind:
    def __init__(self, size) -> None:
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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        if not n:
            return 0

        pq = []

        # 0 is virtial node
        for i in range(n):
            pq.append((wells[i], 0, i+1))

        for u, v, w in pipes:
            pq.append((w, u, v))

        heapq.heapify(pq)

        uf = UnionFind(n+1)

        res = 0

        while pq:
            cost, u, v = heapq.heappop(pq)
            if not uf.connected(u, v):
                uf.union(u, v)
                res += cost
                if uf.count == 1:
                    return res


# n = 3
# wells = [1, 2, 2]
# pipes = [[1, 2, 1], [2, 3, 1]]


n = 2
wells = [1, 1]
pipes = [[1, 2, 1]]

so = Solution()

res = so.minCostToSupplyWater(n, wells, pipes)


print(res)
