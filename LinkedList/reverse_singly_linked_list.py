# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list

# first attemp, each time return next node which is unnessary since we can get it from n.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def helper(n: ListNode) -> ListNode:
            # find tail
            if not n.next:
                self.h = n
                return n

            next_node = helper(n.next)
            next_node.next = n
            n.next = None
            return n

        helper(head)

        return self.h


class Solution2:

    # not head only applies to when input is None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        reversed_node = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return reversed_node


class Solution:

    def reverseList(self, node: ListNode) -> ListNode:
        if not node or not node.next:
            return node

        new_head = self.reverseList(node.next)

        node.next.next = node
        node.next = None

        return new_head


so = Solution()


head = build_list([1, 2, 3, 4, 5])

new_list = so.reverseList(head)


print_list(new_list)
