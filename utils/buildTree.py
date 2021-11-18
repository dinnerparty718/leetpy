from Tree.TreeNode import TreeNode
from collections import deque
from Tree.traversal.dfs_recursion import inOrder


def build(data: str) -> TreeNode:
    if not data:
        return  # return None by default

    flat_bt = data.split(',')

    ans = TreeNode(int(flat_bt[0]))
    q = deque([ans])

    i = 1
    while q:
        n = q.popleft()
        if i < len(flat_bt) and flat_bt[i]:
            l = TreeNode(int(flat_bt[i]))
            n.left = l
            q.append(l)

        i += 1
        if i < len(flat_bt) and flat_bt[i]:
            r = TreeNode(int(flat_bt[i]))
            n.right = r
            q.append(r)

        i += 1

    return ans


def main():
    data = '1,2,3,,,4,5,6,7,,,,,,'
    res = build(data)
    inOrder(res)


if __name__ == '__main__':
    main()