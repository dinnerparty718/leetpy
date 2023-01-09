from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# elemenery Math
# M,N

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummyHead = ListNode()
        cur = dummyHead

        while l1 or l2:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            newVal = carry + x + y
            carry = newVal // 10
            cur.next = ListNode(newVal % 10)
            cur = cur.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry > 0:
            cur.next = ListNode(carry)

        return dummyHead.next
