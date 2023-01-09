from typing import List
from collections import defaultdict
from collections import deque
import heapq
# find the shortest path the form k to all other nodes, return the furthest


# best approach Dijkstra
# todo how to restore the path
# need a dict (node, time, prev_node)

# time O(ElogE)
# space E(V + E)

# pq with python
# https://www.youtube.com/watch?v=CerlT7tTZfY

class Solution0:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))   # weight first to facilitate

        pq = [(0, k)]  # min heap
        # n start from 1 in this case
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


# BFS layer by layer

# todo??
# Time O(N^2 + )


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = [0] + [float('inf') for _ in range(n)]

        for u, v, w in times:
            graph[u].append((v, w))

        # (weight, v) # passing current weight to the neibors
        q = deque([(0, k)])

        while q:
            time, node = q.popleft()

            if time < visited[node]:
                visited[node] = time

                for v, w in graph[node]:
                    q.append((w + time, v))

        mx = max(visited)

        return mx if mx != float('inf') else -1


# DFS with sort
# slow
# time O(N^2 + ElogE) for complete graph total deges = N(N-1)/2 -> O(N^2)
# space O(N+E) graph + sort edge in each bucket
class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, n+1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(k, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2  # starting point

so = Solution0()
res = so.networkDelayTime(times, n, k)

print(res)
