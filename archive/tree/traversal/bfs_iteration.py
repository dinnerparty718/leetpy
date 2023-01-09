from typing import Optional, List, Deque
from Tree.TreeNode import TreeNode
from collections import deque


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []

    queue: Deque[TreeNode] = deque()
    queue.append(root)
    level = 0

    while queue:
        size = len(queue)
        result.append([])

        for i in range(size):
            node = queue.popleft()
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
            result[level].append(node.val)

        level += 1
    return result


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        queue: Deque[TreeNode] = deque()
        queue.append(root)
        level = 0

        while queue:
            size = len(queue)
            result.append([])

            for i in range(size):
                node = queue.popleft()
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                result[level].append(node.val)

            level += 1
        return result


def main():
    solution = Solution()

    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = solution.levelOrder(root)

    print(result)


if __name__ == '__main__':
    main()
