# Definition for singly-linked list.
from typing import Optional

from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode()
        dummy.next = head
        s, f = dummy, dummy
        c = 0
        while c < n:
            f = f.next
            c += 1

        while f.next:
            s = s.next
            f = f.next

        s.next = s.next.next

        return dummy.next


so = Solution()


head = build_list([1, 2, 3, 4, 5])


n = so.removeNthFromEnd(head, 2)


print_list(n)
