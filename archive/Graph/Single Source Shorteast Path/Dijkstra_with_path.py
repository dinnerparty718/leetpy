from typing import List
from collections import defaultdict
import heapq


class Solution:

    # start from A
    def shortest_path(self, edges: List[List[any]], source: str, des: str):
        graph = defaultdict(list)
        v = set()

        for v1, v2, cost in edges:
            v.add(v1)
            v.add(v2)
            graph[v1].append((cost, v2))
            graph[v2].append((cost, v1))

        dist = {}  # (path,cost)

        pq = [(0, source, None)]  # prev

        while pq and len(dist) != len(v):
            (cost, cur, prev) = heapq.heappop(pq)

            if cur in dist:
                continue

            dist[cur] = (cost, prev)

            if cur == des:
                break

            for new_cost, nei in graph[cur]:
                if nei not in dist:
                    heapq.heappush(pq, (cost+new_cost, nei, cur))

        path = [des]

        cur = des

        while cur != source:
            cost, prev = dist[cur]
            path.append(prev)
            cur = prev

        print(path[::-1])

        # for k, v in dist.items():
        #     print(k, v)


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

so.shortest_path(edges, 'A', 'F')
