from typing import Optional, Union  # either some type or None
from typing import List
from TreeNode import TreeNode

T = Union[int, float]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return None


solution = Solution()

result = solution.buildTree([1, 2, 3], [2, 3, 3])

print(result)


if(not result):
    print('reuls is null')
