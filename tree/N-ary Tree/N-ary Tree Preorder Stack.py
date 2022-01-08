from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# recursion


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        res = []

        stack = [root]

        while stack:
            node = stack.pop()

            res.append(node.val)

            # left-> right
            # so for stack push right first

            stack.extend(node.children[::-1])

        return res


# so = Solution()

# res = so.preorder()
