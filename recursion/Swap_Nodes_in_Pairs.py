# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# own solution
# recursive
# time O(n)
# space O(n) recursive stack
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        if head and head.next:

            firstNode = head
            secondNode = head.next

            secondNode.next = firstNode

            firstNode.next = self.swapPairs(secondNode.next)

            return secondNode

# iterative


class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            prev_node = first_node
            head = first_node.next

        return dummy.next


#head = [1, 2, 3, 4]
#result = [1,2,4,3]
