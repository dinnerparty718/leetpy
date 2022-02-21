# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from typing import Optional
from LinkedList.ListNode import ListNode

'''
fast, slow pointers

Time O(n)
space O(1)


'''


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        fast = head
        slow = head

        while fast.next and fast.next.next:

            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
