from typing import List
from collections import defaultdict
import heapq
# dfs
# use heap to keep lexi order

# todo


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)

        res = []

        for s, t in tickets:
            self.graph[s].append(t)

        # heapify
        for k, v in self.graph.items():
            heapq.heapify(v)
            # print(k, v)

        def dfs(res: List[str], cur: str):
            if cur in self.graph:
                q = self.graph[cur]
                while q:
                    dfs(res, heapq.heappop(self.graph[cur]))
            res.append(cur)

        dfs(res, 'JFK')

        return res[::-1]


so = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
res = so.findItinerary(tickets)
print(res)
