# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.TreeNode import TreeNode
from collections import deque
from utils.buildTree import build

# own solution
# can be optimzied to use index and does not pop item


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = deque()

        def inOrder(node: TreeNode):
            if not node:
                return

            inOrder(node.left)
            self.q.append(node)
            inOrder(node.right)

        if root:
            inOrder(root)
            # print(len(self.q))

    def next(self) -> int:
        if len(self.q) == 0:
            return
        return self.q.popleft().val

    def hasNext(self) -> bool:
        return len(self.q) != 0


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.index = -1

        def inOrder(node: TreeNode):
            if not node:
                return

            inOrder(node.left)
            self.nodes.append(node.val)
            inOrder(node.right)

        if root:
            inOrder(root)
            # print(len(self.q))

    def next(self) -> int:
        if not self.hasNext():
            return
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        if self.index < len(self.nodes) - 1:
            return True
        else:
            return False

        # Your BSTIterator object will be instantiated and called as such:
        # obj = BSTIterator(root)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()


obj = BSTIterator(build('7,3,15,,,9,20'))

print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
