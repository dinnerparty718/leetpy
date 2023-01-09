"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


# todo

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None

        rootNode = TreeNode(root.val)
        q = deque([(rootNode, root)])  # binary Tree, Nary-Tree

        while q:
            parent, curr = q.popleft()
            prevBNode = None
            headBNode = None

            for child in curr.children:
                newBNode = TreeNode(child.val)
                if prevBNode:
                    prevBNode.right = newBNode
                else:
                    headBNode = newBNode

                prevBNode = newBNode
                q.append((newBNode, child))

            parent.left = headBNode

        return rootNode

        # Decodes your binary tree to an n-ary tree.

    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        rootNode = Node(data.val, [])

        queue = deque([(rootNode, data)])  # NaryTree, Binary Tree

        while queue:
            parent, curr = queue.popleft()

            firstChild = curr.left
            sibling = firstChild

            while sibling:
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                queue.append((newNode, sibling))
                sibling = sibling.right

        return rootNode

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(root))
