from typing import List
from collections import defaultdict
from collections import deque


# BFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        visited = set()

        q = deque([start])

        while q:
            n = q.popleft()
            if n == end:
                return True

            # if n in visited:
            #     return False

            visited.add(n)

            for nei in graph[n]:
                if nei not in visited:
                    q.append(nei)

        return False

# DFS


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)

        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        visited = set()

        def dfs(index: int):
            if index == end:
                return True

            if index in visited:
                return False

            visited.add(index)

            for nei in graph[index]:
                if dfs(nei):
                    return True

            return False

        return dfs(start)


so = Solution()


n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
start = 0
end = 5


# n = 3
# edges = [[0, 1], [1, 2], [2, 0]]
# start = 0
# end = 2

res = so.validPath(n, edges, start, end)

print(res)
