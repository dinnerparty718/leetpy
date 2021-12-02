"""
# Definition for a Node.

"""
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        # hashmap for old -> new
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val, [])

        while q:

            n = q.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    q.append(nei)

                visited[n].neighbors.append(nei)

        return visited[node]

# adjacent list
# [[2,4],[1,3],[2,4],[1,3]]
