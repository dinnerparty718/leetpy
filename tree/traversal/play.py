from Tree.TreeNode import TreeNode
from utils.buildTree import build
from collections import deque


def BFS(root: TreeNode) -> list[int]:
    q = deque()
    q.append(root)

    res = []

    while q:
        size = len(q)
        cur = []
        for i in range(size):
            n = q.popleft()
            cur.append(n.val)

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        res.append(cur)

    return res


root = build('1,2,3,4,5,,7')


l = BFS(root)


print(l)
