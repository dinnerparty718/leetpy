"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# todo use stack
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/solution/

from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# own Yass!  pre-order DFS, a disguised binary tree
# make use of doulbly linklist property, dont' need return value
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(node: Node):
            if not node:
                return

            dfs(node.child)
            dfs(node.next)

            if node.child and node.next:
                nxt = node.next
                node.next = node.child
                node.child.prev = node

                tail = node.child

                while tail.next:
                    tail = tail.next

                tail.next = nxt
                nxt.prev = tail

                node.child = None

            elif node.child:
                node.next = node.child
                node.child.prev = node
                node.child = None

        dfs(head)
        return head


# leet code bottom up, use child return result build current solution

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # special cases
        if not head:
            return head

        dummyHead = Node(None, None, head, None)

        self.faltten_dfs(dummyHead, head)

        dummyHead.next.prev = None
        return dummyHead.next

    def faltten_dfs(self, prev: Node, cur: Node):
        # return the tail of the faltten list

        if not cur:
            return prev

        # make connection in the begining
        cur.prev = prev
        prev.next = cur

        tempNext = cur.next

        tail = self.faltten_dfs(cur, cur.child)

        cur.child = None

        return self.faltten_dfs(tail, tempNext)
