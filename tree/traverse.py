from TreeNode import TreeNode


def preOrder(node: TreeNode):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node: TreeNode):
    if not node:
        return
    inOrder(node.left)
    print(node.val)
    inOrder(node.right)


def postOrder(node: TreeNode):
    if not node:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.val)


root = TreeNode(0)
left, right = TreeNode(1), TreeNode(2)

root.left = left
root.right = right

l, r = TreeNode(3), TreeNode(4)
left.left = l
left.right = r


right.left = TreeNode(5)

# preOrder(root)
# inOrder(root)
# postOrder(root)
