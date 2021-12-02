from typing import List

# dfs all possible path
# this is backtrack technique -> top down, dfs does not return a value, thus no opp for memorization
# ! only mark visited in undirected graph


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(graph: List[List[int]], index: int, current: List[int], res: List[List[int]]):
            if index == len(graph)-1:
                res.append(current[:])
                return

            # find neibor graph[index]

            for nei in graph[index]:
                current.append(nei)
                dfs(graph, nei, current, res)
                current.pop()

        dfs(graph, 0, [0], res)

        return res


graph = [[1, 2], [3], [3], []]

so = Solution()

res = so.allPathsSourceTarget(graph)

print(res)
