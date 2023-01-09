
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from typing import List, Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build
from tree.traversal.dfs_recursion import preOrderList

# todo morris traversal
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/solution/


'''
recursive

bottom up -> return tail of the left- subtree

helper(node)
    base case
    return None if leaf node
    
    left_tail = helper(node.left)
    right_tail = helper(ndoe.right)
    
    
    if left_tail:
        left_tail.right = node.right
        node.right = node.left
        node.left = None
    
    return right_tail if right_tail else left_tail




'''


class Solution:
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


# yass!!
# Time O(n)
# Space O(1)

class Solution0:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        cur = root

        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pred = cur.left

                while pred.right:
                    pred = pred.right

                pred.right = cur.right
                cur.right = cur.left
                cur.left = None


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


so = Solution0()

root = build('1,2,5,3,4,,6')


so.flatten(root)


res = []
preOrderList(root, res)

print(res)


while root:
    print(root.val)
    root = root.right
