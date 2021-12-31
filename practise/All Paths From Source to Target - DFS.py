from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def dfs(start: int, cur: List[int]):
            cur.append(start)
            if start == n - 1:
                res.append(cur[:])
                return

            #! backtracking
            for nei in graph[start]:
                dfs(nei, cur)
                cur.pop()

        if not graph or len(graph) == 0:
            return []
        dfs(0, [])

        return res


so = Solution()

graph = [[1, 2], [3], [3], []]


res = so.allPathsSourceTarget(graph)


print(res)
