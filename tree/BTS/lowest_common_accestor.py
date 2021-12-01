# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree.TreeNode import TreeNode
from utils.buildTree import build, findNode


# Time O(n)
# Space O(1)

# own solution

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if p.val > q.val:
            p, q = q, p

        cur = root

        while cur:
            if cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val:
                cur = cur.right

            else:
                return cur

        return None


so = Solution()


#root = build('6,2,8,0,4,7,9,,,3,5')
root = build('2,1')

p = findNode(root, 2)
q = findNode(root, 1)


res = so.lowestCommonAncestor(root, p, q)


print(res.val)
