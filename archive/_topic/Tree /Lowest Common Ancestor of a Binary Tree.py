# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from tree.TreeNode import TreeNode

# yass!!
# Time O(n)
# space O(H)  worst case N best case logN

# todo using stack


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result = None

        if not root:
            return None

        def helper(node: TreeNode):
            nonlocal result

            if not node:
                return False, False

            l_p, l_q = helper(node.left)
            r_p, r_q = helper(node.right)

            exist_p = l_p or r_p or node == p
            exist_q = l_q or r_q or node == q

            if not result and exist_p and exist_q:
                result = node

            return exist_p, exist_q

        helper(root)

        return result


class Solution:

    def __init__(self) -> None:
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(node: TreeNode):
            if not node:
                return False

            left = helper(node.left)
            right = helper(node.right)

            mid = node == p or node == q

            if mid + left + right >= 2:
                self.ans = node

            return mid or left or right

        helper(root)

        return self.ans
