# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
from Tree.TreeNode import TreeNode
from Tree.Codec import Codec


class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generate_trees(start, end):
            if start > end:
                return [None]  # must be a list

            all_trees = []

            for i in range(start, end+1):  # pick a root
                left_trees = generate_trees(start, i-1)
                right_trees = generate_trees(i+1, end)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n) if n else []


so = Solution()


n = 3

res = so.generateTrees(n)


cod = Codec()

for t in res:
    print(cod.serialize2(t))
