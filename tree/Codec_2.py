from typing import Deque, List
from TreeNode import TreeNode
from collections import deque
import json
from traversal.dfs_recursion import preOrder, postOrder


'''
own solution
leetcode format
'''


class Codec:
    def serialize(self, root):
        res_list = []
        if root is None:
            return json.dumps(res_list)

        q: Deque[TreeNode] = deque()
        q.append(root)
        while q:
            size = len(q)
            l = []
            for i in range(size):
                n = q.popleft()

                if n is None:
                    l.append(None)
                    continue

                q.append(n.left)
                q.append(n.right)

                l.append(n.val)

            res_list.extend(l)

        while res_list and res_list[-1] is None:
            res_list.pop()

        return json.dumps(res_list)

    def deserialize(self, data):
        obj = json.loads(data)
        print(obj)
        if not obj:
            return None

        n_list: List[TreeNode] = []

        for val in obj:
            if val is None:
                n_list.append(None)
            else:
                n_list.append(TreeNode(val))

        idx = 1

        for node in n_list:
            if idx > len(n_list) - 1:
                break

            if node:
                node.left = n_list[idx]
                idx += 1
                if idx > len(n_list) - 1:
                    break
                node.right = n_list[idx]
                idx += 1

        return n_list[0]


root = TreeNode(1)

left, right = TreeNode(2), TreeNode(3)

root.left = left
root.right = right

root.right.left, root.right.right = TreeNode(4), TreeNode(5)


root.right.left.left, root.right.left.right = TreeNode(6), TreeNode(7)

# root.right.left.left.left = TreeNode(8)

# root.right.left.left.left.left = TreeNode(10)

# root.right.left.right.right = TreeNode(9)

solution = Codec()

str = solution.serialize(None)
root = solution.deserialize(str)


# print(str)

# print(root)

# preOrder(root)
postOrder(root)
