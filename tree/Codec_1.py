from typing import Deque
from TreeNode import TreeNode
from collections import deque
import json


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return json.dumps([])

        queue = deque()
        myList = []

        # index, level

        level = 0
        queue.append((root, 0))

        while queue:

            l = [None for i in range(2 ** level)]

            size = len(queue)
            for i in range(size):
                (node, index) = queue.popleft()

                l[index] = node.val

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

            level += 1
            myList.extend(l)

        return json.dumps(myList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        str = json.loads(data)

        if str is None:
            return None
        print(str)


root = TreeNode(1)

left, right = TreeNode(2), TreeNode(3)

root.left = left
root.right = right

root.right.left, root.right.right = TreeNode(4), TreeNode(5)


solution = Codec()

str = solution.serialize(root)
root = solution.deserialize(str)


# print(str)


# preOrder(root)
# postOrder(root)
