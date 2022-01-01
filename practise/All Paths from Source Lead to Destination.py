from typing import List

# could have cycle
# could end up in node that is not the destination
from collections import defaultdict


# !important, to detect cycle use coloring technique

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for s, t in edges:
            graph[s].append(t)

        def dfs(node: int):
            if node == destination:
                return True

            if node != destination and node not in graph:
                return False

            visited = set()

            visited.add(node)

            for nei in graph[node]:
                visited.add(nei)
                result = dfs(nei)
                if result:
                    visited.remove(nei)
                else:
                    return False

            return True

        return dfs(source)


so = Solution()

n = 4
edges = [[0, 1], [0, 3], [1, 2], [2, 1]]
source = 0
destination = 3

# n = 4
# edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
# source = 0
# destination = 3

res = so.leadsToDestination(n, edges, source, destination)

print(res)
