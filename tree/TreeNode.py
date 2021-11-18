# Definition for a binary tree node.
# if run this file __name__ is __main__
# otherwise __name__ is TreeNode
# print(__name__)

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#     def __str__(self) -> str:
#         return f'{self.val}'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
