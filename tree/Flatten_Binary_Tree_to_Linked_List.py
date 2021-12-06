# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import List, Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build
from Tree.traversal.dfs_recursion import preOrderList

# todo morris traversal

# own use additional space


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def dfs(n: TreeNode, nodes: List[TreeNode]):
            if not n:
                return

            nodes.append(n)
            dfs(n.left, nodes)
            dfs(n.right, nodes)

        dfs(root, nodes)

        for i, n in enumerate(nodes):
            n.left = None
            if i != len(nodes)-1:
                n.right = nodes[i+1]


# own
# time space O(n) implicit stack
# kinda slow
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # if right child, return root
        # if left child return

        def helper(node: TreeNode) -> TreeNode:
            if not node:
                return None

            if not node.left and not node.right:
                return node

            # can be optimzied
            if not node.left and node.right:
                return helper(node.right)

            if node.left and not node.right:
                left = helper(node.left)
                node.right = node.left
                node.left = None
                return left

            if node.left and node.right:
                og_right = node.right
                right = helper(node.right)
                left = helper(node.left)

                node.right = node.left

                if left:
                    left.right = og_right
                else:
                    node.right.right = og_right

                node.left = None

                return right

        helper(root)


class Solution3:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.flattenTree(root)

    def flattenTree(self, node: TreeNode):
        if not node:
            return None

        # if a leaf node, simple return itself
        if not node.left and not node.right:
            return node

        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)

        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        #! important
        return rightTail if rightTail else leftTail


so = Solution3()

root = build('1,2,5,3,4,,6')


so.flatten(root)


res = []
preOrderList(root, res)

print(res)


while root:
    print(root.val)
    root = root.right
