'''
https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
'''

from typing import Optional
from tree.TreeNode import TreeNode
from utils.buildTree import build
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
own solution
use queue to add possible root to array
def isSameTree recursion


from leetcode disussion
recursion of recursion using isSameTree



from leetcode disussion
Advanced approach, O(|s| + |t|) (Merkle hashing):
compare s.merkle == t.merkle



'''

# faster but more memoery usage


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from hashlib import sha256

        def hash_(x):
            S = sha256()
            S.update(x.encode('utf-8'))
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(root)
        merkle(subRoot)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == subRoot.merkle or
                    dfs(node.left) or dfs(node.right))

        return dfs(root)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not q or not p:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# own
# using stack to find all possible root


class Solution1:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if not subRoot:
            return True

        possibleNodes = []

        q = collections.deque([root])

        while q:
            n = q.popleft()

            if n.val == subRoot.val:
                possibleNodes.append(n)

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        # compare
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not q or not p:
                return False

            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        for n in possibleNodes:
            if isSameTree(n, subRoot):
                return True

        return False


root = build('3,4,5,1,2')
subRoot = build('4,1,2')


so = Solution()
res = so.isSubtree(root, subRoot)

print(res)
