from typing import List
from traversal.dfs_recursion import preOrder, postOrder
from tree.TreeNode import TreeNode


class Codec:

    # preorder
    def serialize(self, root):

        res = []

        def helper(node: TreeNode):
            if node:
                res.append(str(node.val))
            else:
                res.append('')
                return

            helper(node.left)
            helper(node.right)

        helper(root)

        return ','.join(res)

    def deserialize(self, data):

        if not data:
            return
        res: List[str] = data.split(',')

        def helper():
            if not res:
                return

            val = res.pop(0)
            if val == '':
                return None
            else:
                node = TreeNode(int(val))

            node.left = helper()
            node.right = helper()
            return node

        return helper()


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

print(str)

preOrder(root)
