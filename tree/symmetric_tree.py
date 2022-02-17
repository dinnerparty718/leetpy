import collections
from Codec import Codec
from typing import Optional
from tree.TreeNode import TreeNode
from tree.traversal.dfs_recursion import preOrder


# time O(n)
# space worst O(n) best case O(logN)


'''

#! similar to "is same tree"

isSymmetric_helper(root, root)

isSymmetric_helper(n1,n2) - recursive
    base case
        1. not n1 and not n2 -> True
        2. not n1 or not n2 -> False
        
    return n1.val == n2.vall and isSymmetric_helper(n1.left, n2.right) and isSymmetric_helper(n1.right, n2.left)


'''


class Solution:

    # recursion
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(n1: TreeNode, n2: TreeNode) -> bool:
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False
            return n1.val == n2.val and helper(n1.left, n2.right) and helper(n1.right, n2.left)

        return helper(root.left, root.right)

    # iterative using dque
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = collections.deque([root.left, root.right])

        while q:
            t1, t2 = q.popleft(), q.popleft()
            if not t1 and not t2:  # empty node
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False

            # add more items in one shot
            q.extend([t1.left, t2.right, t1.right, t2.left])

        return True


codec = Codec()

# symmetric
root = codec.deserialize('1, 2, 2, 3, 4, 4, 3')


so = Solution()
# res = so.isSymmetric(root)
res = so.isSymmetric2(root)


print(res)
