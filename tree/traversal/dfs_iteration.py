from typing import Optional
from typing import List
from Tree.TreeNode import TreeNode
from utils.buildTree import build
# Definition for a binary tree node.


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

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return

        res = []
        stack = [root]

        while stack:
            cur = stack.pop()

            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return res

# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45785/Share-my-two-Python-iterative-solutions-post-order-and-modified-preorder-then-reverse

    # two stack vs one stack (one stack must have a flag)
    # two stack method is modified preorder travasal

    # one stack  by setting a flag

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]

        cur = root

        while stack:
            pass

            # return res


def main():
    root = build('1,,2,3')
    so = Solution()
    res = so.preorderTraversal(root)
    print(res)


if __name__ == '__main__':
    main()
