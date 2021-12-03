# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


# recursion

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists_i(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        while list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next

        while list2:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
        return dummy.next


so = Solution()
l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])
l = so.mergeTwoLists_i(l1, l2)
print_list(l)
