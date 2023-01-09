'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.





'''


from typing import Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build


# important declar self.res or nonlocal res

# time O(n)
# space O(n) implict stack. if balanced O(logn)


'''
res = float('-inf')

heler(node)
    nonlocal res

    base case
        return 0 if not node
        
        
    left = helper(node.left)
    right = helper(node.right)
    
    update global sum
    
    res = max(res, left + right)
    
    
    return max(left, rigtht) +1


'''


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = float('-inf')

        # bottom up
        def helper(node: TreeNode) -> int:

            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            # print(node.val, left, right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1

        helper(root)

        return self.res


so = Solution()

root = build('1,2')


result = so.diameterOfBinaryTree(root)

print(result)
