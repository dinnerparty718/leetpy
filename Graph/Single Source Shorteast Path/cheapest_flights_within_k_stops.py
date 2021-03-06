from typing import List
from collections import defaultdict
import heapq


# modified Dijkstra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))

        # print(graph)
        pq = [(0, src, k+1)]

        # store how many stop to reach each node
        visited = [0] * n
        while pq:
            w, x, stop = heapq.heappop(pq)

            if x == dst:
                return w

            # already visit the node with less stop and cheap path
            # or stop is negative, k stops are exausted, no need to explore next stop
            if visited[x] >= stop:
                continue
            visited[x] = stop

            if x in graph:
                for nei, new_cost in graph[x]:
                    heapq.heappush(pq, (w + new_cost, nei, stop - 1))

        return -1


so = Solution()


flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
n = 4
src = 0
dst = 3
k = 1

# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src = 0
# dst = 2
# k = 1


res = so.findCheapestPrice(n, flights, src, dst, k)
print(res)
