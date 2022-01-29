
from typing import List, Optional
from tree.traversal.dfs_recursion import inOrder
from utils.buildTree import build


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# preorder traversal without extra empty place holder
# use lower upper limit to construct the tree

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        if not root:
            return ''

        res = []

        def helper(node: TreeNode):
            if not node:
                return

            res.append(str(node.val))

            helper(node.left)
            helper(node.right)

        helper(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if not data:
            return None

        nodes = data.split(',')

        node_idx = 0

        def helper(lower: int, upper: int):
            nonlocal node_idx

            if node_idx == len(nodes):
                return None

            if not (lower < int(nodes[node_idx]) < upper):
                return None

            root = TreeNode(int(nodes[node_idx]))
            node_idx += 1

            root.left = helper(lower, root.val)
            root.right = helper(root.val, upper)
            return root

        return helper(float('-inf'), float('inf'))


# using postOrder instead of preorder
# seems faster
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def helper(node: TreeNode):
            return helper(node.left) + helper(node.right) + [str(node.val)] if node else []

        return ','.join(helper(root))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if not data:
            return None

        values = data.split(',')

        def helper(lower: int, upper: int):
            if not values:
                return None

            if not (lower < int(values[-1]) < upper):
                return None

            root = TreeNode(int(values.pop()))

            #! pop right first
            root.right = helper(root.val, upper)
            root.left = helper(lower, root.val)

            return root

        return helper(float('-inf'), float('inf'))


class Codec:

    def postorder(self, root) -> List[int]:
        return self.postorder(root.left) + self.postorder(root.right) + [root.val] if root else []

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """


codec = Codec()

root = build('3,2,5,1,,4,6')


treeStr = codec.serialize(root)


# newRoot = codec.deserialize(treeStr)


# inOrder(newRoot)
