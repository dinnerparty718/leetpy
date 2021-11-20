from typing import List
from Tree.TreeNode import TreeNode


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


def preOrderList(node: TreeNode, res: List[int]):
    if not node:
        return
    res.append(node.val)
    preOrderList(node.left, res)
    preOrderList(node.right, res)


def inOrderList(node: TreeNode, res: List[int]):
    if not node:
        return

    inOrderList(node.left, res)
    res.append(node.val)
    inOrderList(node.right, res)


def postOrderList(node: TreeNode, res: List[int]):
    if not node:
        return

    postOrderList(node.left, res)
    postOrderList(node.right, res)
    res.append(node.val)


def main():
    pass
    # postOrder(root)


if __name__ == '__main__':
    main()
