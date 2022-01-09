"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# bottom up
# own

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        maxChild = float('-inf')

        for child in root.children:
            maxChild = max(maxChild, self.maxDepth(child))

        return maxChild + 1


# bottom up
# leetcode

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1

        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1


# bfs, level

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1

        level = 0

        q = deque([root])

        while q:
            level += 1
            size = len(q)

            for i in range(size):
                node = q.popleft()
                q.extend(node.children)

        return level
