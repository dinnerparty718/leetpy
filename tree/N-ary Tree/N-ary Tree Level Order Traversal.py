"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


from typing import List
from collections import deque
from naryTree import sample_NaryTree


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# time O(n)
# space O(n)

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []

        q = deque([root])

        while q:
            size = len(q)
            cur = []

            for i in range(size):
                node = q.popleft()
                cur.append(node.val)

                if node.children:
                    q.extend(node.children)

            res.append(cur)

        return res


root = sample_NaryTree()


so = Solution()

res = so.levelOrder(root)

# print(res)
