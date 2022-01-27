from typing import Optional

from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list

# recursion


def reverseList(head: ListNode) -> ListNode:

    cur = head
    prev = None

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev


head = build_list([1, 2, 3, 4, 5])

new_head = reverseList(head)


print_list(new_head)
