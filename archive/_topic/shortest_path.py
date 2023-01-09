from typing import List
from collections import deque
from collections import defaultdict
# todo


class Solution:
    def shortestPath(self, edges: List[List[str]], source: str, target: str) -> int:
        graph = defaultdict(list)
        visited = set()

        for s, t in edges:
            graph[s].append(t)

        q = deque([[source]])

        while q:

            path = q.popleft()

            if path[-1] == target:
                return path

            visited.add(path[-1])

            for nei in graph[path[-1]]:
                if nei not in visited:
                    q.append(path + [nei])

        return []


edges = [
    ['A', 'C'],
    ['A', 'D'],
    ['A', 'B'],
    ['C', 'E'],
    ['D', 'E'],
    ['E', 'B'],
    ['E', 'F'],
    ['B', 'F']
]

so = Solution()

res = so.shortestPath(edges, 'A', 'F')

print(res)
