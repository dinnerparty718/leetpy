from typing import Optional, List
from Tree.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        result: List[List[int]] = []

        def helper(node: TreeNode, index: int):
            if index == len(result):
                result.append([])

            result[index].append(node.val)

            if node.left:
                helper(node.left, index + 1)
            if node.right:
                helper(node.right, index + 1)

        helper(root, 0)
        return result


solution = Solution()


# root = TreeNode(3)

# root.left = TreeNode(9)
# root.right = TreeNode(20)


# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


root = TreeNode(1)

result = solution.levelOrder(root)

print(result)
