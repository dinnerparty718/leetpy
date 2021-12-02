

from typing import List
from collections import defaultdict
from collections import deque

# return the steps
# todo return the path


class Solution:
    def shortestPath(self, edges: List[List[str]], source: str, target: str) -> int:
        graph = defaultdict(list)
        q = deque([source])
        visited = set()

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        level = 0

        while q:
            size = len(q)
            level += 1

            for i in range(size):
                n = q.popleft()
                if n == target:
                    return level
                if source not in visited:
                    visited.add(source)

                    for nei in graph[source]:
                        if nei not in visited:
                            q.append(nei)

        return level

    def shortestPath_path(self, edges: List[List[str]], source: str, target: str) -> List[str]:
        graph = defaultdict(list)
        q = deque([[source]])
        visited = set()

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        while q:
            path = q.popleft()
            if path[-1] == target:
                return path

            for nei in graph[path[-1]]:
                if nei not in visited:
                    new_path = path[:]
                    new_path.append(nei)
                    q.append(new_path)

            visited.add(path[-1])

        return []

        # if n not in visited:


so = Solution()


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

res = so.shortestPath_path(edges, 'A', 'F')


print(res)
