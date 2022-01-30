# Definition for singly-linked list.
from typing import Optional
from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# own solution!!! hard
#! no additional space
#! reverse function need to be iterative

class Solution:
    def reverse(self, node: ListNode) -> ListNode:
        if not node or not node.next:
            return node

        new_head = self.reverse(node.next)

        node.next.next = node
        node.next = None

        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        cur = head
        cnt = k

        # head.next coule be none
        while cur and cnt > 0:
            if cnt == 1:
                tmp = cur.next
                cur.next = None

                self.reverse(prev.next)

                prev.next.next = tmp

                new_prev = prev.next
                prev.next = cur
                prev = new_prev

                cnt = k
                cur = tmp
            else:
                cnt -= 1

                cur = cur.next

        return dummy_head.next


so = Solution()

head = build_list([1, 2, 3, 4, 5])
# print_list(head)
k = 2
res = so.reverseKGroup(head, k)

print_list(res)
