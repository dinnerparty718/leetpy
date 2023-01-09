# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree.TreeNode import TreeNode
from utils.buildTree import build

# own does not use the BST property, val is not used
# but this is a general approach for binary tree


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        found = False
        res = None

        def inOrder(node: TreeNode, target: TreeNode):
            nonlocal found
            nonlocal res
            if not node:
                return

            inOrder(node.left, target)

            print(node.val)

            if found:
                res = node
                found = False

            if node == p:
                found = True

            if not res:
                inOrder(node.right, target)

        inOrder(root, p)
        return res

# better than own solution using inorder travesal and use the next val

# https://leetcode.com/problems/inorder-successor-in-bst/discuss/696555/Python-Simple-Inorder-traversal


class Solution2:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ## RC ##
        ## APPROACH : RECURSION ##
        ## LOGIC : IN AN INORDER TRAVERSAL, SUCCESOR IS ALWAYS THE VERY NEXT ELEMENT ##

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        def helper(node: TreeNode):

            if not node or self.res:
                return
            helper(node.left)

            if node.val > p.val and not self.res:
                self.res = node
                return
            helper(node.right)

        self.res = None
        helper(root)

        return self.res


# todo using BST value


class Solution3:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        succersor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                succersor = root
                root = root.left

        return succersor

    def inorderPredecessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        predecessor = None

        while root:
            if p.val <= root.val:
                root = root.left
            else:
                predecessor = root
                root = root.right

        return predecessor


so = Solution()


root = build('6,3,7,1,5')
p = root.left
res = so.inorderSuccessor(root, p)


print(res)
