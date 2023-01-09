from typing import List
from collections import deque

# bfs
# ! only mark visited in undirected graph
# ! garantee no cycle in the description

# todo can push tuple to the queue (current_node, path)


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        q = deque([[0]])

        target = len(graph) - 1

        # only append to the res list if the last item is the target

        while q:
            path = q.popleft()

            if path[-1] == target:
                res.append(path)

            for nei in graph[path[-1]]:
                new_path = path[:]
                new_path.append(nei)
                q.append(new_path)

        return res


graph = [[1, 3], [2], [3], []]

so = Solution()

res = so.allPathsSourceTarget(graph)

print(res)
