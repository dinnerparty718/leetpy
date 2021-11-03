from typing import List, Optional
from TreeNode import TreeNode
from traverse import inOrder, preOrder


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(start: int, end: int):
            if(start > end):
                return None

            nodeVal = preorder.pop(0)
            node = TreeNode(nodeVal)
            inOrderIdx = inorderIdx[nodeVal]

            node.left = helper(start, inOrderIdx - 1)
            node.right = helper(inOrderIdx + 1, end)
            return node

        inorderIdx = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]


solution = Solution()

result = solution.buildTree(preorder, inorder)


preOrder(result)
