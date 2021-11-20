# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build


# own
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        n = TreeNode(val)
        if not root:
            return n

        parent = None
        cur = root

        while cur:
            parent = cur
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right

        if val < parent.val:
            parent.left = n
        else:
            parent.right = n

        return root


# own
class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        self.n = TreeNode(val)

        if not root:
            return self.n

        def helper(n: TreeNode, parent: TreeNode):
            if not n:
                if val < parent.val:
                    parent.left = self.n
                else:
                    parent.right = self.n
                return

            parent = n
            if n.val > val:
                helper(n.left, parent)
            else:
                helper(n.right, parent)

        helper(root, None)

        return root

# https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/1365503/Python-recursive-solution-beats-85-time-96-space


class Solution3:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


so = Solution2()

root = so.insertIntoBST(build('40,20,60,10,30,50,70'), 25)

# print(root)


res = []


def inorder(root: TreeNode, res: List[int]):
    if not root:
        return

    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)


inorder(root, res)
print(res)
