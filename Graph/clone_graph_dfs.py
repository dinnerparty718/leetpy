"""
# Definition for a Node.

"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # hashmap for old -> new
        visited = {}

        if not node:
            return node

        def dfs(node: 'Node') -> 'Node':

            if not node:
                return node

            if node in visited:
                return visited[node]

            visited[node] = Node(node.val)

            for nei in node.neighbors:
                visited[node].neighbors.append(dfs(nei))

            return visited[node]

        dfs(node)

        return visited[node]

# adjacent list
# [[2,4],[1,3],[2,4],[1,3]]
