from tree.TreeNode import TreeNode
from tree.traversal.dfs_recursion import inOrder
from utils.buildTree import build
# DFS

# using preOrder and append ' ', ' '


def serialized(root: TreeNode) -> str:
    res = []

    def dfs(node: TreeNode):
        if not node:
            res.append('')
            return

        res.append(str(node.val))

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ','.join(res)


def deserizlized(data: str) -> TreeNode:

    if not data:
        return None
    vals = data.split(',')

    def dfs():
        if not vals:
            return

        val = vals.pop(0)

        node = TreeNode(int(val)) if val else None

        if node:
            node.left = dfs()
            node.right = dfs()

        return node

    return dfs()


root = build('3,2,5,1,,4,6')


treeStr = serialized(root)


print(treeStr)

newRoot = deserizlized(treeStr)

inOrder(newRoot)
