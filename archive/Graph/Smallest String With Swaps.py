from typing import List
from collections import defaultdict


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


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))

        for i, j in pairs:
            uf.union(i, j)

        res = []
        m = defaultdict(list)

        for i in range(len(s)):
            m[uf.find(i)].append(s[i])

        for key in m.keys():
            m[key].sort(reverse=True)

        for i in range(len(s)):
            item = m[uf.find(i)].pop()
            res.append(item)

        return ''.join(res)


so = Solution()

s = "dcab"
pairs = [[0, 3], [1, 2]]

res = so.smallestStringWithSwaps(s, pairs)


print(s)
