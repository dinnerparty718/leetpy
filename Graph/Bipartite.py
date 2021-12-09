from typing import List

# A bipartile graph can only have even edge length cycle
#

# https://www.youtube.com/watch?v=0ACfAqs8mm0

# https://leetcode.com/problems/is-graph-bipartite/discuss/1544587/Python-simple-dfs-solution-with-coloring


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        pass


so = Solution()

graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]


res = so.isBipartite()

print(res)
