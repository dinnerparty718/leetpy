# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# own yas!!

from typing import Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        
        def dfs(node: TreeNode):
            if not node:
                return (0,0)
            
            
            rob_left,not_rob_left = dfs(node.left)
            rob_right, not_rob_right = dfs(node.right)
            
        
            
            rob = not_rob_left + node.val + not_rob_right
            not_rob = max(rob_left,not_rob_left) + max(rob_right, not_rob_right)

           
            return (rob, not_rob)


        return  max(dfs(root))
    

root_arr = '3,2,3,,3,,1'
root_arr = '3,4,5,1,3,,1'
root_arr = '3,4,5,1,3,,6'
root_arr = '3,2,2'

# root_arr = '4,1,,2,,3'


# root_arr = '5,3,6,1,4,,,,2'

root = build(root_arr)




so = Solution()

res = so.rob(root)


print(res)