from typing import List
from collections import deque
from collections import defaultdict
# A bipartile graph can only have even edge length cycle
# A bipartile graph can be colored by two color

# https://www.youtube.com/watch?v=0ACfAqs8mm0

# https://leetcode.com/problems/is-graph-bipartite/discuss/1544587/Python-simple-dfs-solution-with-coloring


# dfs
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True

        adj_list = defaultdict(list)

        n = len(graph)

        for i in range(n):
            for num in graph[i]:
                adj_list[i].append(num)

        NOT_COLOR, BLUE, GREEN = 0, 1, -1

        color_table = [NOT_COLOR] * n

        def dfs(node: int, color: int):
            color_table[node] = color

            if node in adj_list:
                for nei in adj_list[node]:
                    if color_table[nei] == NOT_COLOR and (not dfs(nei, -color)):
                        return False
                    else:
                        if color_table[nei] == color:
                            return False

            return True

        for i in range(n):
            if color_table[i] == NOT_COLOR and (not dfs(i, BLUE)):
                return False

        return True


so = Solution()

graph = [[1, 3], [0, 2], [1, 3], [0, 2]]


res = so.isBipartite(graph)

print(res)
