from typing import List, Set
from collections import defaultdict
from collections import deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen = set([start])
        q = deque([start])
        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        while q:
            n = q.popleft()
            if n == end:
                return True

            for nei in graph[n]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return False


so = Solution()


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
start = 0
end = 2


res = so.validPath(n, edges, start, end)


print(res)
