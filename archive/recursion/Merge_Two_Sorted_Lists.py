# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# base case
# if not l1 return l2, if not l2 return l1, if not l1 and l2 return None
#
# recurrence relation
# compare head node, merge(l1.next, l2) or merge(l1, l2.next) return l1 or l2
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def helper(l1, l2):

            if not l1 and not l2:
                return None
            if not l1 and l2:
                return l2
            if l1 and not l2:
                return l1

            if l1.val <= l2.val:
                l1.next = helper(l1.next, l2)

                return l1
            else:
                l2.next = helper(l1, l2.next)

                return l2

        return helper(list1, list2)

# iterative


class Solution1:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1

        if list2:
            cur.next = list2

        return dummy.next
