# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree.TreeNode import TreeNode

from utils.buildTree import build


class Codec:

    def serialize(self, root):

        if not root:
            return ''

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        # pre-order
        def dfs(node: TreeNode):
            if not node:
                res.append('')
                return

            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return None

        nodes = data.split(',')

        def dfs():
            if not nodes:
                return

            val = nodes.pop(0)

            root = TreeNode(int(val)) if val != '' else None

            if root:
                root.left = dfs()
                root.right = dfs()

            return root

        return dfs()


codec = Codec()


root = build('1,2,3,4,5')

#     1
#  2      3
# 4    5

print(codec.serialize(root))
