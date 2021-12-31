from typing import List

# dfs all possible path
# this is backtrack technique -> top down, dfs does not return a value, thus no opp for memorization
# ! only mark visited in undirected graph


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(index: int, current: List[int]):
            if index == len(graph)-1:
                res.append(current[:])
                return

            # find neibor graph[index]

            for nei in graph[index]:
                current.append(nei)
                dfs(nei, current)
                current.pop()

        dfs(0, [0])

        return res


graph = [[1, 2], [3], [3], []]

so = Solution()

res = so.allPathsSourceTarget(graph)

print(res)
