"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


'''
in order traversal

find the first node and keep updating the last

dfs(node.left)

work on current node

dfs(node.right)


'''




from distutils.command.build_scripts import first_line_re
from typing import Optional
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        last, first = None, None

        if not root:
            return None

        def helper(node: Node):
            nonlocal last, first

            if not node:
                return None

            # left
            helper(node.left)

            # node

            if last:
                # link the previous node (last)
                # with the current one (node)
                last.right = node
                node.left = last
            else:
                # kee the smallest node
                # for later
                first = node
            last = node

            # right
            helper(node.right)

        helper(root)
        # close the loop
        last.right = first
        first.left = last

        return first
