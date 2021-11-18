from typing import Deque
from Tree.TreeNode import TreeNode
from collections import deque
from traversal.dfs_recursion import preOrder, postOrder


class Codec:

    def serialize(self, root):
        flat_bt = []
        q: Deque[TreeNode] = deque([root])
        while q:
            node = q.popleft()
            if node:
                flat_bt.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                flat_bt.append('')

        # while flat_bt and flat_bt[-1] == '':
        #     flat_bt.pop()

        # time:  O(n)
        # space: O(n)

        return ','.join(flat_bt)

    def deserialize(self, data):
        if not data:
            return  # return None by default
        flat_bt = data.split(',')
        ans = TreeNode(flat_bt[0])
        q: Deque[TreeNode] = deque([ans])  # root
        i = 1
        while q:
            node = q.popleft()
            if i < len(flat_bt) and flat_bt[i]:
                node.left = TreeNode(int(flat_bt[i]))
                q.append(node.left)
            i += 1
            if i < len(flat_bt) and flat_bt[i]:
                node.right = TreeNode(int(flat_bt[i]))
                q.append(node.right)
            i += 1
        return ans

        # time:  O(n)
        # space: O(n)


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

str = solution.serialize(root)
root = solution.deserialize(str)


# postOrder(root)

print(str)
