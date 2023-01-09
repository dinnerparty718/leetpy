from typing import Optional
from tree.TreeNode import TreeNode


# recursive

# boundray float('-inf') , float('inf')

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node: TreeNode, lower: int, uppper: int):
            if not node:
                return True

            valid_node = lower < node.val < uppper

            if not valid_node:
                return False

            return validate(node.left, lower, node.val) and validate(node.right, node.val, uppper)

        return validate(root, float('-inf'), float('inf'))
