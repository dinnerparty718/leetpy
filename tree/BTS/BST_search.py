from Tree.TreeNode import TreeNode
from typing import Optional
from utils.buildTree import build


# reversive
# time O(h) depends on the heighht of the tree
# space O(h)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return
        if root.val == val:
            return root

        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

# iterative
# space(1)


class Solution2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while root:
            if root.val == val:
                return root

            if root.val < val:
                root = root.right
            else:
                root = root.left

        return None


so = Solution2()


n = so.searchBST(build('4,2,7,1,3'), 5)


print(n)
