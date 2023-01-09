# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        p1 = list1
        p2 = list2

        dummy = ListNode(0)
        res = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                dummy.next = ListNode(p1.val)
                p1 = p1.next
            else:
                dummy.next = ListNode(p2.val)
                p2 = p2.next

            dummy = dummy.next

        while p1:
            dummy.next = ListNode(p1.val)
            p1 = p1.next
            dummy = dummy.next

        while p2:
            dummy.next = ListNode(p2.val)
            p2 = p2.next
            dummy = dummy.next

        return res.next


so = Solution()


list1 = build_list([])
list2 = build_list([])


new_list = so.mergeTwoLists(list1, list2)


print_list(new_list)
