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

        def dfs(node: 'Node', visited: dict) -> 'Node':

            if not node:
                return node

            if visited[node]:
                return visited[node]

            visited[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited[node].neighbors.append(dfs(nei, visited))

            return visited[node]

        dfs(node, visited)

        return visited[node]

# adjacent list
# [[2,4],[1,3],[2,4],[1,3]]
