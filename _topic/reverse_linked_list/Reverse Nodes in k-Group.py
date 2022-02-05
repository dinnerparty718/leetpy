from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# own one time yeass! but slow
# interative O(n)
# space O(1)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseList(l: ListNode) -> ListNode:
            prev = None
            curr = l

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        n = k
        dummyHead = ListNode(0)
        dummyHead.next = head

        curr = head
        prev = dummyHead

        while curr:
            if n == 1:
                tmp = curr.next
                curr.next = None

                head = prev.next

                prev.next = reverseList(head)

                head.next = tmp
                curr = tmp
                prev = head

                n = k
            else:
                curr = curr.next
                n -= 1

        return dummyHead.next
