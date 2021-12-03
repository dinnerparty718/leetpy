# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


# first find mid point
# reverse the 2n halp
# insert to the first half, merge
# correct :) https://leetcode.com/problems/reorder-list/solution/

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node: ListNode):
            if node.next == None:
                return node

            n_p = reverse(node.next)

            node.next.next = node
            node.next = None

            return n_p

        last = reverse(slow)
        cur = head

        while last != slow:
            tmp = cur.next
            cur.next = last
            last = last.next
            cur.next.next = tmp
            cur = tmp


head = build_list([1, 2, 3, 4])

# print_list(head)


so = Solution()

so.reorderList(head)

print_list(head)
