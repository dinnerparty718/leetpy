from typing import Optional


from Tree.TreeNode import TreeNode


# bottom up
# when return value and problem is not the same, use a global variable
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float('-inf')

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            l = 0 if l < 0 else l
            r = 0 if r < 0 else r

            self.global_max = max(self.global_max, l + r + node.val)

            return max(l, r) + node.val

        helper(root)

        return self.global_max
