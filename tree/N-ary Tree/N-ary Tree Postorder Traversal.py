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


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []

        def dfs(node: 'Node'):
            if not node:
                return node

            for child in node.children:
                dfs(child)

            res.append(node.val)

        dfs(root)

        return root


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        res = []

        stack = [root]

        while stack:
            node = stack.pop()

            res.append(node.val)

            # left-> right
            # so for stack push right first

            stack.extend(node.children)

        return res[::-1]
