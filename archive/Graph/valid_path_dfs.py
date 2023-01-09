from typing import List, Set
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen = set()

        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(edges: List[List[int]], node: int, end: int,  seen: Set) -> bool:
            if node == end:
                return True
            if node in seen:
                return False

            neighbors = graph[node]

            seen.add(node)
            for nei in neighbors:
                if dfs(edges, nei, end, seen):
                    return True

            return False

        return dfs(edges, start, end, seen)


so = Solution()


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
start = 0
end = 2


res = so.validPath(n, edges, start, end)


print(res)
