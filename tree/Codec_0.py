from typing import Deque, List, Tuple
from TreeNode import TreeNode
from collections import deque
from Tree.traversal.dfs_recursion import inOrder, postOrder, preOrder

import json

# level |
# node  ,
#       -


class Codec:
    def serialize(self, root) -> str:

        if not root:
            return json.dumps(None)

        result = []

        level = 0
        myList: List[List[List[int]]] = []

        queue: Deque[TreeNode] = deque()
        queue.append(root)

        while queue:

            myList.append([])
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                result = [node.val]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                result.append(node.left.val if node.left else None)
                result.append(node.right.val if node.right else None)

                myList[level].append(result)

            level += 1

        # print(myList)

        return json.dumps(myList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        levels = json.loads(data)

        if not levels:
            return None
        # helper(levels[0][0]0)

        # for level, nodes in enumerate(levels):
        #     for node in nodes:
        #         print(level, node)

        def helper(val, level: int):
            if val is not None:
                return None
            node = TreeNode(val)

            # find that element

            levelList = levels[level]
            leftVal: int
            rightVal: int

            for [nodeVal, left, right] in levelList:
                if nodeVal == val:
                    leftVal = left
                    rightVal = right

            node.left = helper(leftVal, level + 1)
            node.right = helper(rightVal, level + 1)

            return node

        return helper(levels[0][0][0], 0)

        # print(result)


root = TreeNode(1)

left, right = TreeNode(2), TreeNode(3)

root.left = left
root.right = right

root.right.left, root.right.right = TreeNode(4), TreeNode(5)


solution = Codec()

str = solution.serialize(root)
root = solution.deserialize(str)


# preOrder(root)
postOrder(root)
