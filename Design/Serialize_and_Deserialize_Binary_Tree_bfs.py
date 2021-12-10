# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree.TreeNode import TreeNode
from utils.buildTree import build
from collections import deque
from Tree.traversal.bfs_iteration import levelOrder


class Codec:

    # level order
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []

        q = deque([root])

        while q:
            n = q.popleft()
            if n:
                ans.append(str(n.val))

                q.append(n.left)
                q.append(n.right)
            else:
                ans.append('')

        return (',').join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        nodes = data.split(',')

        root = TreeNode(int(nodes[0]))

        q = deque([root])

        i = 1

        while q:
            node = q.popleft()

            if i < len(nodes) and nodes[i] != '':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)

            i += 1

            if i < len(nodes) and nodes[i] != '':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1

        return root


root = build('4,-7,-3,,,-9,-3,9,-7,-4,,6,,-6,-6,,,0,6,5,,9,,,-1,-4,,,,-2')

ser = Codec()


ans = ser.serialize(root)

# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# print(ans)


deser = Codec()


newroot = deser.deserialize(ans)


res = levelOrder(newroot)
print(res)
