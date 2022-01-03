from typing import List
import heapq

# https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3858/

# todo create a class Edege so can be sort by heapq

# Time heapify  O(E) pop  O(logE)  total O(ElogE)
# O(E) heapq to store the edges


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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# 5 points

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # (w,p1,p2)
        minHeap = []

        uf = UnionFind(n)

        print(uf.root)

        for i in range(n):
            for j in range(i+1, n):
                p1 = points[i]
                p2 = points[j]
                w = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                # using heapify at the end
                # heapq.heappush(minHeap, (w, i, j))
                minHeap.append((w, i, j))

        heapq.heapify(minHeap)

        res = 0
        cnt = 0

        while cnt < n-1 and minHeap:
            (w, p1, p2) = heapq.heappop(minHeap)

            if not uf.connected(p1, p2):
                uf.union(p1, p2)
                res += w
                cnt += 1

        if not minHeap:
            return -1

        return res


so = Solution()
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
points = [[3, 12], [-2, 5], [-4, 1]]
res = so.minCostConnectPoints(points)


print(res)
