from typing import Optional, List
from traverse import inOrder, postOrder
from TreeNode import TreeNode

'''
Note: use inner function for helper function to avoid using self.helper()

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:

#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         self.inorder = inorder[:]
#         self.postorder = postorder[:]
#         self.inorderHash = {val: index for index, val in enumerate(inorder)}
#         self.postOrderIdx = len(postorder)-1

#         return self.helper(0, len(inorder)-1)

#     def helper(self, start: int, end: int) -> Optional[TreeNode]:
#         if start > end:
#             return None

#         rootVal = self.postorder[self.postOrderIdx]

#         self.postOrderIdx -= 1

#         node = TreeNode(rootVal)
#         inOrderIdx = self.inorderHash[rootVal]

#         node.right = self.helper(inOrderIdx + 1, end)
#         node.left = self.helper(start, inOrderIdx - 1)

#         return node


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # inorder = inorder[:]
        # postorder = postorder[:]

        def helper(start: int, end):

            # if there is no elements to construct subtrees
            if(start > end):
                return None

            val = postorder.pop()
            node = TreeNode(val)

            index = idx_map[val]

            node.right = helper(index + 1, end)
            node.left = helper(start, index - 1)
            return node
        # build a hashmap value -> its index

        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper(0, len(inorder)-1)


solution = Solution()

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

result = solution.buildTree(inorder, postorder)


# inOrder()

# inOrder(result)
postOrder(result)

print(postorder)
