from Tree.TreeNode import TreeNode
from utils.buildTree import build
from Tree.traversal.dfs_recursion import inOrderList


def find_min_subtree(node: TreeNode):
    res = []
    inOrderList(node, res)

    print(res)


def main():
    root = build('5,3,6,2,4,,7')
    res = find_min_subtree(root)


if __name__ == '__main__':
    main()
