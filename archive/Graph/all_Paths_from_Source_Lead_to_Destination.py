from typing import List
from collections import defaultdict


# ! how to detect a cycle in the graph, visited list not enough, need to record the vertex

class Solution:

    GRAY = 1
    BLACK = 2

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            if n1 == n2:
                return False  # self loop detected
            graph[n1].append(n2)

        # for k, v in graph.items():
        #     print(k, v)

        def dfs(source: int, destination: int, graph: dict, states: List):

            # detect loop, if source is beiing proccess 'GRAY'
            if states[source] != None:
                print('loop detected')
                return states[source] == Solution.BLACK

            # leaf node
            if not graph[source]:
                return source != destination

            states[source] = Solution.GRAY

            for nei in graph[source]:
                if not dfs(nei, destination, graph, states):
                    return False

            # while graph[source]:
            #     nei = graph[source].pop()

            #     if not dfs(nei, destination, graph, visited):
            #         return False

            states[source] = Solution.BLACK

            return True

        return dfs(source, destination, graph, [None] * (n+1))


so = Solution()

edges = [[0, 1], [0, 2], [0, 3], [0, 3], [1, 2],
         [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
n = 5

source = 0
destination = 4


res = so.leadsToDestination(n, edges, source, destination)

print(res)
