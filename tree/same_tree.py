from typing import Optional
from Tree.TreeNode import TreeNode
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        return l and r


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checkValid(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False

            return n1.val == n2.val

        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()
            if not checkValid(n1, n2):
                return False

            if n1:
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))

        return True
