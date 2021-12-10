
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


from typing import Optional

from Tree.TreeNode import TreeNode as Node
from utils.buildTree import build
from Tree.traversal.dfs_recursion import inOrder


# visited stack method
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        dummyHead = Node()
        cur = dummyHead

        s = [[root, 0]]

        while s:
            top = s[-1]

            if top[1] == 1:
                node = s.pop()[0]
                cur.right = node
                node.left = cur
                cur = cur.right

                if node.right:
                    s.append([node.right, 0])
            else:
                top[1] = 1

                if top[0].left:
                    s.append([top[0].left, 0])

        head = dummyHead.right
        tail = cur

        head.left = cur
        tail.right = head

        return dummyHead


class Solution2:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        dummyHead = Node()
        cur = dummyHead

        stack = []

        n = root

        while n or stack:
            while n:
                stack.append(n)
                n = n.left

            n = stack.pop()

            cur.right = n
            n.left = cur

            cur = cur.right

            n = n.right

        head = dummyHead.right
        tail = cur

        head.left = cur
        tail.right = head

        return dummyHead.right


# recursive
class Solution3:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        dummyHead = Node(0)

        cur = dummyHead

        def dfs_inorder(node: Node):
            nonlocal cur

            if not node:
                return

            dfs_inorder(node.left)

            # print(node.val)
            cur.right = node
            node.left = cur
            cur = cur.right

            dfs_inorder(node.right)

        dfs_inorder(root)

        head = dummyHead.right

        tail = cur

        head.left = tail
        tail.right = head

        return head


root = build('4, 2, 5, 1, 3')


so = Solution3()
head = so.treeToDoublyList(root)

while head:
    print(head.val)
    head = head.right
