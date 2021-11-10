from typing import Optional
from typing import List


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# need to keep track of the current node

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        curr = root
        stack = []
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


root = TreeNode(0)
left, right = TreeNode(1), TreeNode(2)

root.left = left
root.right = right

l, r = TreeNode(3), TreeNode(4)
left.left = l
left.right = r


left.right.left = TreeNode(5)
left.right.right = TreeNode(6)


so = Solution()
res = so.inorderTraversal(root)

print(res)
