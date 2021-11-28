# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Tuple
from Tree.TreeNode import TreeNode
from utils.buildTree import build, findNode

# botom up
# base case node is none or common ancester found
# extra step node has both p,q pass from the children
# return that node

# own solution


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.common = None

        def helper(node: TreeNode) -> Tuple:
            if not node or self.common:
                return (False, False)

            is_p = node == p
            is_q = node == q

            l_p, l_q = helper(node.left)
            r_p, r_q = helper(node.right)

            result = (is_p or l_p or r_p,  is_q or l_q or r_q)

            print(result)

            if result == (True, True):
                self.common = node
                return (False, False)
            return result

        helper(root)

        return self.common


# todo
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/1037162/Python-Easy-to-Understand


# root = build('3,5,1,6,2,0,8,,,7,4')
# p = findNode(root, 5)
# q = findNode(root, 1)


root = build('1,2')
p = findNode(root, 1)
q = findNode(root, 2)

so = Solution()

res = so.lowestCommonAncestor(root, p, q)


print(res.val)
