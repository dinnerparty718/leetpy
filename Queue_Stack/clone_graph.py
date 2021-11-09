"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).


import collections


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def __init__(self) -> None:
        self.visited = {}

    # DFS iteratively
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        stack = [node]
        visited = {node: Node(node.val)}

        while stack:
            n = stack.pop()
            for nei in n.neighbors:
                if nei not in visited:
                    stack.append(nei)
                    visited[nei] = Node(nei.val)
                visited[n].neighbors.append(visited[nei])

        return visited[node]

    # BFS iteratively
    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = collections.deque([node])
        visited = {node: Node(node.val)}

        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    queue.append(nei)
                    visited[nei] = Node(nei.val)
                visited[n].neighbors.append(visited[nei])
        return visited[node]

    # DFS recursively leet code solution
    def cloneGraph3(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        new_node = Node(node.val)
        self.visited[node] = new_node

        new_node.neighbors = [self.cloneGraph3(nei) for nei in node.neighbors]

        return new_node

    # DFS recursively popular python

    def cloneGraph4(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m = {node: Node(node.val)}

        def DFS(n):
            for nei in n.neighbors:
                if nei not in m:
                    m[nei] = Node(nei.val)
                    DFS(nei)
                m[n].neighbors.append(m[nei])
            pass

        DFS(node)

        return m[node]


so = Solution()

n_1 = Node(1)
n_2 = Node(2)
n_3 = Node(3)
n_4 = Node(4)


n_1.neighbors.extend([n_2, n_4])
n_2.neighbors.extend([n_1, n_3])
n_3.neighbors.extend([n_2, n_4])
n_4.neighbors.extend([n_1, n_3])


a = so.cloneGraph3(n_1)

print(a, a.neighbors)
