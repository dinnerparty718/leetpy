# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# reverse - two lists
# construct new list with carry
# reverese the new list
# own

# time O((M + N))
# space O(1) without output. with output O(max(M,N))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(list: ListNode):
            if not list.next:
                return list  # new head

            newHead = reverseList(list.next)
            nextNode = list.next

            nextNode.next = list
            list.next = None
            return newHead

        l1_new = reverseList(l1)
        l2_new = reverseList(l2)

        dummyHead = ListNode()
        cur = dummyHead

        carry = 0

        while l1_new and l2_new:
            val = l1_new.val + l2_new.val + carry
            carry = val // 10
            sum_val = val % 10
            cur.next = ListNode(sum_val)
            cur = cur.next
            l1_new = l1_new.next
            l2_new = l2_new.next

        while l1_new or l2_new:
            val = l1_new.val + carry if l1_new else l2_new.val + carry

            carry = val // 10
            sum_val = val % 10
            cur.next = ListNode(sum_val)
            cur = cur.next

            if l1_new:
                l1_new = l1_new.next
            else:
                l2_new = l2_new.next

        if carry != 0:
            cur.next = ListNode(carry)

        return reverseList(dummyHead.next)
