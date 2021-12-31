from typing import List
from collections import defaultdict
from collections import deque


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:

            # add y to x
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                # add x to y
                self.root[rootX] = rootY
            else:
                # equal height
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)

        return uf.connected(start, end)


# DFS find path
# Time O (V + E)
# Space O(V)
class Solution1:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = set()

        graph = defaultdict(list)

        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        def dfs(node: int):

            if node == end:
                return True

            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if dfs(nei):
                    return True

            return False

        return dfs(start)

# DFS using stack


class Solution2:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        s = [start]
        visited = set()

        while s:
            node = s.pop()

            if node == end:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    s.append(nei)

        return False

# BFS


class Solution3:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)

        q = deque([start])

        visited = set()

        while q:
            node = q.popleft()
            if node == end:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    q.append(nei)

        return False


so = Solution3()

# n = 3
# edges = [[0, 1], [1, 2], [2, 0]]
# start = 0
# end = 2

n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
start = 0
end = 5

res = so.validPath(n, edges, start, end)

print(res)
