from typing import List

# could have cycle
# could end up in node that is not the destination
from collections import defaultdict


#! to detect cycle use coloring technique in DFS in [directed] graph
#! white, grey, black None, 1, 2

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        GRAY = 1
        BLACK = 2

        graph = defaultdict(list)

        # one direction
        for s, t in edges:
            graph[s].append(t)

        # list with node and their states
        visited = [None] * n

        def dfs(start: int):
            # base case
            if visited[start] == GRAY:
                return False
            elif visited[start] == BLACK:
                return True

            # if visited[start] != None:
            #     return visited[start] == BLACK

            # if this is a leave node,check if it's the destination
            if start not in graph:
                return start == destination

            visited[start] = GRAY

            for nei in graph[start]:
                if not dfs(nei):
                    return False

            visited[start] = BLACK
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
