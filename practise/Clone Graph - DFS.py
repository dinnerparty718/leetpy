"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         visited = {}

#         s = [node]

#         while s:
#             n = s.pop()

#             if n not in visited:
#                 visited[n] = Node(n.val)

#                 for nei in n.neighbors:
#                     if nei in visited:
#                         visited[n].neighbors.append(visited[nei])
#                     else:


# bfs
# own
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node
        visited = {}

        visited[node] = Node(node.val)

        q = deque([node])

        while q:
            n = q.popleft()

            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)

                visited[n].neighbors.append(visited[nei])

        return visited[node]
