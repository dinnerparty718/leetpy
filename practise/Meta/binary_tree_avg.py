from typing import List
from collections import deque


class Node():
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


# time O(n)
# space O(n) worse case

def tree_level_avg(root: Node) -> List[int]:
    if not root:
        return None

    res = []

    q = deque([root])

    while q:
        size = len(q)

        running_sum = 0

        for i in range(size):
            cur = q.popleft()
            running_sum += cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res.append(running_sum/size)

    return res
