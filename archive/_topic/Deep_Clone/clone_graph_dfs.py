"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        visited = {}

        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]

            visited[node] = Node(node.val)

            for nei in node.neighbors:
                visited[node].neighbors.append(dfs(nei))
            return visited[node]

        dfs(node)

        return visited[node]
