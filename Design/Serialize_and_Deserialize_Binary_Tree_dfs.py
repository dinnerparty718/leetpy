# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree.TreeNode import TreeNode
from utils.buildTree import build
from Tree.traversal.dfs_recursion import preOrder
from collections import deque


class Codec:

    # level order
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = []

        # pre order
        def dfs(node: TreeNode):
            if not node:
                res.append('')
                return

            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return (',').join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        nodes = deque(data.split(','))

        # preorder
        def dfs():
            if not nodes:
                return

            if nodes[0] == '':
                nodes.popleft()
                return None

            root = TreeNode(int(nodes.popleft()))

            root.left = dfs()
            root.right = dfs()
            return root

        root = dfs()

        # print(nodes)

        return root


root = build('1,2,3,,,4,5')

ser = Codec()


ans = ser.serialize(root)

print(ans)


# print(ans)


deser = Codec()


newroot = deser.deserialize(ans)


preOrder(newroot)
