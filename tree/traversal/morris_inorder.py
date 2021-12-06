

from typing import Optional

from Tree.TreeNode import TreeNode
from utils.buildTree import build


# morris traversal
# https://www.youtube.com/watch?v=wGXB9OWhPTg
# if node.left is not None, find predecessor, set predecessor.right = node
# if node.left is None or visited, cur = cur.right

class Solution:
    def traverse_inorder(self, root: Optional[TreeNode]):
        if not root:
            return []

        res = []

        cur = root

        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right

            else:
                pred = cur.left

                while pred.right != cur and pred.right:
                    pred = pred.right

                if pred.right == None:
                    pred.right = cur
                    cur = cur.left
                else:
                    # linked established before
                    pred.right = None
                    res.append(cur.val)
                    cur = cur.right

        print(res)


so = Solution()


root = build('1,2,5,3,4,,6')


so.traverse_inorder(root)
