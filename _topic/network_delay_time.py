from typing import List
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = {}  # v, cost
        pq = [(0, k)]
        for u, v, w in times:
            graph[u].append((v, w))

        while pq:
            cost, cur = heapq.heappop(pq)

            if cur in visited:
                continue
            visited[cur] = cost

            for nei, new_cost in graph[cur]:
                if nei not in visited:
                    heapq.heappush(pq, (cost+new_cost, nei))

        return max(visited.values()) if len(visited) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2


so = Solution()

res = so.networkDelayTime(times, n, k)

print(res)
