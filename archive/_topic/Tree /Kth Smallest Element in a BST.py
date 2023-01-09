# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from typing import Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build
'''

recursion

in order traversal.
append to res and  return res[k-1]



iterative using stack
more efficient



'''


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1

            if not k:
                return root.val
            root = root.right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node: TreeNode):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return inorder(root)[k-1]


so = Solution()

root = build('3,1,4,, 2')
k = 1

root = build('5,3,6,2,4,,,1')
k = 3
res = so.kthSmallest(root, k)

print(res)
