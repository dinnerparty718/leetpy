# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev

            prev = cur

            cur = tmp

        return prev


so = Solution()

head = build_list([1, 2, 3, 4, 5])

new_h = so.reverseList(head)

print_list(new_h)
