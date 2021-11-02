from TreeNode import TreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


root = TreeNode(0)

left, right = TreeNode(1), TreeNode(2)

root.left = left
root.right = right


print(root)
solution = Codec()
