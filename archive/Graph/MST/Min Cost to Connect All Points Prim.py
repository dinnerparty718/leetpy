from typing import List
import heapq
from collections import defaultdict
# https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3858/


class Edge:
    def __init__(self, start: int, end: int, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight

    # less than
    def __lt__(self, other: 'Edge'):
        return self.weight < other.weight

    def __repr__(self) -> str:
        return f'{self.start} -> {self.end}:  {self.weight}'


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if not points or len(points) == 0:
            return 0

        n = len(points)
        count = n-1
        res = 0

        pq = []

        visited = [False] * n

        # Add all edges from points[0] vertexs
        x1, y1 = points[0]

        for j in range(1, n):
            x2, y2 = points[j]
            cost = abs(x1-x2) + abs(y1-y2)
            pq.append(Edge(0, j, cost))

        heapq.heapify(pq)

        visited[0] = True

        while pq and count > 0:
            e: Edge = heapq.heappop(pq)
            if not visited[e.end]:
                res += e.weight
                visited[e.end] = True

                for i in range(n):
                    if not visited[i]:
                        x1, y1 = points[e.end]
                        x2, y2 = points[i]
                        w = abs(x1 - x2) + abs(y1 - y2)
                        heapq.heappush(pq, Edge(e.end, i, w))
                count -= 1
        return res


so = Solution()
#points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
#points = [[3, 12], [-2, 5], [-4, 1]]

points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
res = so.minCostConnectPoints(points)


print(res)


# e1 = Edge(1, 2, 4)
# e2 = Edge(1, 2, 6)
# e3 = Edge(1, 2, 3)
# e4 = Edge(1, 4, 3)


# a = [e1, e2, e3, e4]

# print(sorted(a))
