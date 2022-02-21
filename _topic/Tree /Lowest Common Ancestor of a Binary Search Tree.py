# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree.TreeNode import TreeNode
from utils.buildTree import build

'''
can be solve using stanard LCA of binary, but this does not use BST property


both children
    exist on the left tree. go left
    exist on the right tree. go left
else:
    we found the lowest common accesstor of BST
    
Time O(n)
Space O(n)


'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_value = root.val

        p_val = p.val
        q_val = q.val

        # both are greater tha parent
        if p_val > parent_value and q_val > parent_value:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_value and q_val < parent_value:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # val could be equal to parent_val
            return root


so = Solution()


root = build('6,2,8,0,4,7,9,,,3,5')
p = 2
q = 8

res = so.lowestCommonAncestor(root, p, q)

print(res)
