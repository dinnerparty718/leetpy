# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Optional
from tree.TreeNode import TreeNode
from tree.traversal.dfs_recursion import inOrderList, preOrderList
from utils.buildTree import build


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def preOrder(node: TreeNode):

            if not node:
                res.append('')
                return
            else:
                res.append(str(node.val))
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if not data:
            return None

        vals = data.split(',')

        i = 0

        def preOrder():
            nonlocal i
            if i == len(vals):
                return

            val = vals[i]
            i += 1

            node = TreeNode(int(val)) if val else None

            if not node:
                return None

            node.left = preOrder()
            node.right = preOrder()

            return node

        return preOrder()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
ser = Codec()

root = build('3,2,5,1,,4,6')


treeStr = ser.serialize(root)

print(treeStr)


newRoot = ser.deserialize(treeStr)


res = []
preOrderList(newRoot, res)

print(res)
