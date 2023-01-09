
from typing import Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build

# time O(N) N - number of nodes
# space O(H) height of the tree H = log(N)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return -1

        max_val = float('-inf')

        def helper(node: TreeNode):

            nonlocal max_val
            if not node:
                return 0

            #! node value < 0
            left_value = max(helper(node.left), 0)
            right_value = max(helper(node.right), 0)

            result = node.val + left_value + right_value

            max_val = max(result, max_val)

            return node.val + max(left_value, right_value)

        helper(root)

        return max_val


root = build('-10,9,20,,,15,7')
root = build('2,-1')


so = Solution()

res = so.maxPathSum(root)


print(res)
