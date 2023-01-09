from Tree.TreeNode import TreeNode
from utils.buildTree import build

# general
# simply inorder travesal and break early


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:

        self.prev = None
        self.succesor = None

        def inorder(node: TreeNode):
            if not node:
                return

            inorder(node.left)

            if self.prev == p and not self.succesor:
                self.succesor = node
                return
            self.prev = node

            # if answer found stop recursion
            if not self.succesor:
                inorder(node.right)

        inorder(root)

        return self.succesor


# with BST property
# find the node while keep track of the parent whenever cursor go left
# if node found and node has right sub stree, return right subtree's left most node
# else return parent.  parent could be null (the right-most node)
class Solution2:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        parent = None
        cur = root
        while cur:
            if p.val > cur.val:
                cur = cur.right
            elif p.val < cur.val:
                parent = cur
                cur = cur.left
            else:
                if cur.right:
                    p = cur.right
                    while p.left:
                        p = p.left
                    return p
                else:
                    return parent

        return None

# combine p.val >= node.val


class Solution3:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        succ = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                succ = root
                root = root.left

        return succ

    def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        pred = None

        while root:
            if p.val <= root.val:
                root = root.left
            else:
                pred = root
                root = root.right

        return pred


so = Solution3()

# root = build('6,2,8,0,4,7,9,,,3,5')
# p = root.left.right.left  # 3
#p = root.left

root = build('2,,3')


res = so.inorderPredecessor(root, root.right)

print(res.val)
