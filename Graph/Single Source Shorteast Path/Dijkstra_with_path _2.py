from typing import List
from collections import defaultdict
import heapq


# using dist, inital as empty dict
class Solution:

    # start from A
    def shortest_path(self, edges: List[List[any]], source: str, des: str):
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        dist = {}

        pq = [(0, source)]  # sort by first time cost

        while pq:
            cost, node = heapq.heappop(pq)

            if node == des:
                return cost

            if node in dist:
                continue

            dist[node] = cost

            for new_cost, nei in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (cost + new_cost, nei))

        return -1


class Solution:

    # start from A
    def shortest_path(self, edges: List[List[any]], source: str, des: str):
        graph = defaultdict(list)

        nodes = set()

        for u, v, w in edges:
            nodes.add(u)
            nodes.add(v)
            graph[u].append((w, v))
            graph[v].append((w, u))

        dist = {node: float('inf') for node in nodes}

        pq = [(0, source)]

        while pq:
            cost, cur = heapq.heappop(pq)

            if dist[cur] != float('inf'):
                continue

            dist[cur] = cost

            if cur == des:
                return cost

            for w, nei in graph[cur]:
                if dist[nei] == float('inf'):
                    heapq.heappush(pq, (cost + w, nei))

        for k, v in dist.items():
            print(k, v)

        return -1


edges = [
    ['A', 'C', 2],
    ['A', 'B', 4],
    ['A', 'G', 7],
    ['B', 'D', 2],
    ['D', 'G', 5],
    ['C', 'G', 3],
    ['C', 'F', 8],
    ['F', 'J', 3],
    ['D', 'H', 6],
    ['H', 'J', 2],
    ['G', 'J', 4],
]

so = Solution()

res = so.shortest_path(edges, 'A', 'F')


print(res)
