"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional

# yass!!! one time pass


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# hash map. create random node when dealing with current node
# using extra space to store old -> new node
# iterative

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        h = {}
        curr = head

        prev = None

        while curr:
            if curr not in h:
                h[curr] = Node(curr.val)
            # previously created

            if curr.random:
                if curr.random not in h:
                    h[curr.random] = Node(curr.random.val)

                h[curr].random = h[curr.random]

            if prev:
                prev.next = h[curr]

            prev = h[curr]

            curr = curr.next

        return h[head]


# recursive!!
# easier to undersday

# Time O(n)
# Space O(n)
class Solution:

    def __init__(self) -> None:
        self.visitedHash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        node = Node(head.val)

        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


# optimzied

# A - A' - B - B'
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pass
