# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build


# using BST tree recursion

# time O(H) height of the tree
# space O(1)


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            #! remember pattern
            closest = min(root.val, closest, key=lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest


# own
# recursive inorder + binary search

# Time O(N) + O(logN) = O(N)
# space O(N) build the array


class Solution2:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res = []

        def dfs(node: TreeNode):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)

        l, r = 0, len(res)-1

        while l + 1 < r:
            mid = l + (r-l) // 2

            if target == res[mid]:
                return res[mid]
            elif target > res[mid]:
                l = mid
            else:
                r = mid

        if target < res[l]:
            return res[l]

        if target > res[r]:
            return res[r]

        return res[l] if (target - res[l]) < (res[r] - target) else res[r]


# leetcode interative traverse tree and find result
# ! memorize inorder tree traversal iterative method
class Solution3:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        pred = float('-inf')

        s = []

        while s or root:
            while root:
                s.append(root)
                root = root.left

            root = s.pop()

            if pred <= target and target < root.val:
                return root.val if root.val - target < target - pred else pred

            pred = root.val
            root = root.right

        return pred


so = Solution()

root = build('4,2,5,1,3')
target = 3.714286

res = so.closestValue(root, target)

print(res)
