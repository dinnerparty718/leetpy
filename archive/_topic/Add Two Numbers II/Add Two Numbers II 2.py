# Definition for singly-linked list.
from typing import List, Optional
from utils.buildLinkedList import build_list, print_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode method 2
#  1. reverse input
#  2. construct output and put in the front


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = n2 = 0
        p1, p2 = l1, l2

        while p1:
            p1 = p1.next
            n1 += 1

        while p2:
            p2 = p2.next
            n2 += 1

        p1, p2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0

            if n1 >= n2:
                val += p1.val
                p1 = p1.next
                n1 -= 1
            if n1 < n2:
                val += p2.val
                p2 = p2.next
                n2 -= 1

            # update the result: add to front
            cur = ListNode(val)
            cur.next = head
            head = cur

        # step = abs(n1-n2)

        # if step > 0 and n1 < n2:
        #     l1, l2 = l2, l1

        # # l1 is longer

        # head = None

        # list1 = l1
        # list2 = l2

        # while step > 0:
        #     node = ListNode(list1.val)
        #     node.next = head
        #     head = node
        #     step -= 1
        #     list1 = list1.next

        # while list1 and list2:
        #     node = ListNode(list1.val + list2.val)
        #     node.next = head
        #     head = node
        #     list1 = list1.next
        #     list2 = list2.next

        # iterative

        prev = None

        carry = 0
        while head:
            new_sum = carry + head.val
            head.val = new_sum % 10
            carry = new_sum // 10

            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        if carry > 0:
            node = ListNode(carry)
            node.next = prev

            prev = node

        return prev


l1 = build_list([7, 2, 4, 3])
l2 = build_list([5, 6, 4])


so = Solution()


res = so.addTwoNumbers(l1, l2)

print_list(res)
