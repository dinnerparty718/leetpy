"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# recursion


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node: 'Node'):
            if not node:
                return

            res.append(node.val)

            for child in node.children:
                dfs(child)

        dfs(root)
        return res


# iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []

        s = [root]

        while s:
            root = s.pop()
            res.append(root.val)
            s.extend(root.children)
        return res
