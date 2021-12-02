from typing import List
from collections import defaultdict


# ! how to detect a cycle in the graph, visited list not enough, need to record the vertex

class Solution:

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            if n1 == n2:
                return False  # self loop detected
            graph[n1].append(n2)

        visited = [None] * n

        def dfs(source: int, destination: int, graph: dict, visited: List):
            if visited[source] != None:
                return visited[source] == False
            if source not in graph:
                return source == destination

            visited[source] = False

            for nei in graph[source]:
                if not dfs(nei, destination, graph, visited):
                    return False

            visited[source] = True
            return True

        return dfs(source, destination, graph, visited)


so = Solution()

edges = [[0, 1], [0, 2], [0, 3], [0, 3], [1, 2],
         [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
n = 5

source = 0
destination = 4


res = so.leadsToDestination(n, edges, source, destination)

print(res)
