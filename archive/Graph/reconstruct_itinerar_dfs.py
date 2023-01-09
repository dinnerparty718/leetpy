from typing import List
from collections import defaultdict
import heapq

# buiild graph, if a key does not exist in graph, that key is the destination
# we stop at the vertex where we do not have any unvisited edges.


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        res = []
        for s, e in tickets:
            graph[s].append(e)

        for k in graph.keys():
            heapq.heapify(graph[k])

        def dfs(start: str, res: List[int], graph: dict):
            # base case
            # since using default dict, not need to check exist
            q = graph[start]
            while q:
                dfs(heapq.heappop(q), res, graph)

            res.append(start)

        dfs('JFK', res, graph)

        # at this point there is no edges left
        # print(graph)

        return res[::-1]


so = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
res = so.findItinerary(tickets)
print(res)
