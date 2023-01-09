from collections import defaultdict, deque

import heapq
from typing import List

# https://leetcode.com/problems/network-delay-time/discuss/471164/Python-DFS-BFS-Dijkstra-Bellman-Ford-SPFA-Floyd-Warshall
#
# Dijkstra's Algorithm using heap


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

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

# using queue


# todo BFS update shortest path layer by layer
# 1 <= k <= n <= 100

class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # tricks to store distance in a list
        t = [0] + [float("inf")] * n

        q = deque([(0, k)])

        for u, v, w in times:
            graph[u].append((v, w))

        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time  # store the shortest path
                for v, w in graph[node]:
                    q.append((time+w, v))

        mx = max(t)
        return mx if mx < float('inf') else -1


so = Solution2()

times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
n = 3
k = 1


res = so.networkDelayTime(times, n, k)

print(res)
