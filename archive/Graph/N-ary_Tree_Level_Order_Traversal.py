
# Definition for a Node.
from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = deque([root])

        while q:

            size = len(q)
            l = []

            for i in range(size):
                n = q.popleft()
                l.append(n.val)

                for child in n.children:
                    q.append(child)

            res.append(l)

        return res
