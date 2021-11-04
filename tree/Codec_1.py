from typing import Deque
from TreeNode import TreeNode
from collections import deque
import json


class Codec:

    def serialize(self, root):

        if root is None:
            return json.dumps([])

        queue = deque()
        myList = []

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
            # myList.extend(l)
            myList.append(l)

        return json.dumps(myList)

    def deserialize(self, data):

        l = json.loads(data)

        if l is None:
            return None

        n_list = l

        # index = 0

        # while index <= len(l) - 1:
        #     size = 2 ** index
        #     n_list.append(l[index:index + size])
        #     index = index + size

        def helper(level, index):
            if level == len(n_list):
                return None

            val = n_list[level][index]
            # print('val ' + val)

            if val is None:
                return None

            node = TreeNode(val)

            l_idx = 2 * index
            r_idx = 2 * index + 1
            node.left = helper(level+1, l_idx)
            node.right = helper(level+1, r_idx)
            return node

        return helper(0, 0)


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
