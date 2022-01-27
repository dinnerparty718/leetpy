# Definition for singly-linked list.
from lib2to3.pytree import Node
from re import L
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode
#  1. reverse input
#  2. construct output and put in the front

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(l: ListNode):
            if not l.next:
                return l

            new_head = reverseList(l.next)

            l.next.next = l
            l.next = None
            return new_head

        list1 = reverseList(l1)
        list2 = reverseList(l2)

        head = Node

        carry = 0

        while list1 or list2:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            val_sum = carry + val1 + val2
            carry = val_sum // 10

            # add to front
            node = ListNode(val_sum % 10)

            node.next = head
            head = node

            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next

        if carry > 0:
            node = ListNode(carry)
            node.next = head
            head = node

        return head
