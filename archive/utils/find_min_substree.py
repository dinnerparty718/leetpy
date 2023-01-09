from Tree.TreeNode import TreeNode
from utils.buildTree import build
from Tree.traversal.dfs_recursion import inOrderList


def find_min(node: TreeNode):
    if not node:
        return None

    while node.left:
        node = node.left

    return node


def main():
    root = build('5,3,6,2,4,,7')
    res = find_min(root)

    print(res)


if __name__ == '__main__':
    main()
