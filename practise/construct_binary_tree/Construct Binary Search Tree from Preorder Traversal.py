from pydoc import Helper
from tree.traversal.dfs_recursion import inOrder, inOrderList
from typing import List, Optional
from tree.TreeNode import TreeNode


# own
# recurive   n * n -> search for value

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        def helper(li: List[int]):
            if not li:
                return None

            val = li.pop(0)
            root = TreeNode(val)

            index = len(li)

            for idx, num in enumerate(li):
                if num > val:
                    index = idx
                    break

            root.left = helper(li[0:index])
            root.right = helper(li[index:])

            return root

        return helper(preorder)


# leet code 1
# time O(nlog(n)) sort nlog(n)
# todo improve use index instead of copy list
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)

        def helper(preorder: List[int], inorder: List[int]):
            if not inorder:
                return None

            root = TreeNode(preorder.pop(0))
            rootIndex = inorder.index(root.val)

            root.left = helper(preorder, inorder[:rootIndex])
            root.right = helper(preorder, inorder[rootIndex+1:])

            return root

        return helper(preorder, inorder)


# leetcode 1
# avoid using list slicing
# build hashmap for storing index
# Time O(nlog(n)) for sort    O(n) to construct the tree
# space O(n) to construct the tree

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)

        def helper(in_left: int, in_right: int):

            nonlocal pre_idx

            #
            if in_left > in_right:
                return None

            root = TreeNode(preorder[pre_idx])
            pre_idx += 1

            rootIndex = in_map[root.val]

            root.left = helper(in_left, rootIndex-1)
            root.right = helper(rootIndex+1, in_right)

            return root

        in_map = {value: idx for idx, value in enumerate(inorder)}

        pre_idx = 0

        return helper(0, len(inorder)-1)


# leetcode 2 use lower and upper limit
# similar to validate BST
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(lower: int, upper: int):
            nonlocal idx

            if idx == len(preorder):
                return None

            if not (lower < preorder[idx] < upper):
                return None

            root = TreeNode(preorder[idx])

            idx += 1

            root.left = helper(lower, root.val)
            root.right = helper(root.val, upper)

            return root

        idx = 0
        return helper(float('-inf'), float('inf'))


so = Solution()


preorder = [8, 5, 1, 7, 10, 12]


root = so.bstFromPreorder(preorder)


res = []

inOrderList(root, res)

print(res)
