# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree.TreeNode import TreeNode


'''
bottom up  (isBalanced, height)


isBalance_h(node)
    base case
        1 not node -> True,-1
        
        
        
    # can do early return here
    isLeftBalance, left_height = isBalance_h(node.left)
    isRightBalance, right_height = isBalance_h(node.right)
    
    return (right_height - left_height < 2 , max(right_height, left_height) +1 )
    
    
    
    


return isBalance_h(node)[0]



'''


# own bottom up
# time O(n)
# Space O(n) recursion stack
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node: TreeNode):
            if not node:
                return (1, True)

            left_result = helper(node.left)
            right_result = helper(node.right)

            if left_result[1] == True and right_result[1] == True:
                if abs(left_result[0] - right_result[0]) <= 1:
                    h = max(left_result[0], right_result[0]) + 1
                    return (h, True)

            return (0, False)

        return helper(root)[1]


# leetcode bottom up
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node: TreeNode):
            if not node:
                return True, -1

            # left subtree
            leftIsBalanced, leftHeight = helper(node.left)

            # early determination
            if not leftIsBalanced:
                return False, 0

            rightIsBalanced, rightHeight = help(node.right)
            if not rightIsBalanced:
                return False, 0

            return (abs(leftHeight-rightHeight) < 2, max(leftHeight, rightHeight)+1)

        return helper(root)[0]
