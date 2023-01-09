from typing import List, Optional
from Tree.TreeNode import TreeNode
from utils.buildTree import build
from Tree.traversal.dfs_recursion import inOrderList

# case 1 leaf node, cut the link
# case 2, 3 only one child, replace deleted nod with that child
# case 4 two child, replace val with its inorder next val and recursively delete


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # find the node

            # case 1
            if not root.left and not root.right:
                return None

            # case 2, only right child
            if not root.left:
                return root.right

            # case 3, only left child
            if not root.right:
                return root.left

            # case 4 has two child
            root.val = self.find_min(root.right)
            root.right = self.deleteNode(root.right, root.val)

        return root

    # has right tree
    def find_min(self, root: TreeNode) -> int:
        while root.left:
            root = root.left
        return root.val


so = Solution()

# root = so.deleteNode(build('5,3,6,2,4,,7'), 3)
root = build('12,5,15,3,7,13,17,1,,,9')
result = so.deleteNode(root, 15)


res = []

inOrderList(result, res)
print(res)
