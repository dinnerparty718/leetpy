from collections import defaultdict
import collections
import heapq
from typing import DefaultDict, List


# Dijkstra with  Dijkstra's Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        if not times:
            return -1

        self.graph = self.build_dict(times)
        self.cost = defaultdict(int)

        h = []

        self.cost[k] = 0

        if self.graph[k]:
            for pair in self.graph[k]:
                heapq.heappush(h, pair)

        if not h:
            return -1

        while h:
            cost, dest = heapq.heappop(h)
            if dest not in self.cost:
                self.cost[dest] = cost

            if self.graph[dest]:
                for c, d in self.graph[dest]:
                    if d not in self.cost:
                        heapq.heappush(h, [c + cost, d])

        if len(self.cost) < n:
            return -1

        return max(self.cost.values())

    def build_dict(self, times: List[List[int]]) -> dict:
        d = DefaultDict(list)
        for src, dest, cost in times:
            d[src].append([cost, dest])

        return d

# leetcode


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        dist = {}

        while pq:
            d, node = heapq.heappop(pq)

            if node in dist:
                continue

            dist[node] = d

            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == n else -1


so = Solution2()

times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
n = 3
k = 1


res = so.networkDelayTime(times, n, k)

print(res)
