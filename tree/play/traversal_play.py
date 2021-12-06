from typing import Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build
root = build('1,2,5,3,4,,6')


class Solution:
    def traverse_inorder(self, root: Optional[TreeNode]):

        def visit(node: TreeNode):
            print(node.val)

        if not root:
            return

        stack = []
        cur = root

        while stack or cur:

            while cur:
                stack.append(cur)
                cur = cur.left
            n = stack.pop()
            visit(n)

            if n.right:
                cur = n.right

    def traverse_preorder(self, root: Optional[TreeNode]):

        res = []

        if not root:
            return

        stack = [[root, 0]]

        while stack:

            cur = stack[-1]

            # if visited
            if cur[1]:
                node, _ = stack.pop()
                if node.right:
                    stack.append([node.right, 0])

            else:
                res.append(cur[0].val)

                cur[1] = 1

                if cur[0].left:
                    stack.append([cur[0].left, 0])

        print(res)

    def traverse_postorder(self, root: Optional[TreeNode]):
        res = []

        if not root:
            return

        stack = [[root, 0]]

        while stack:

            cur = stack[-1]

            # if visited
            if cur[1]:
                node, _ = stack.pop()
                if node.left:
                    stack.append([node.left, 0])

            else:
                res.append(cur[0].val)

                cur[1] = 1

                if cur[0].right:
                    stack.append([cur[0].right, 0])

        print(res[::-1])


so = Solution()


so.traverse_postorder(root)
