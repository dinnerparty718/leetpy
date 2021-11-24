from typing import Optional

from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list

# recursion


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # tail, this is the new head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

# iteration


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # tail, this is the new head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head


so = Solution()

head = build_list([1, 2, 3, 4, 5])

new_head = so.reverseList(head)


print_list(new_head)
