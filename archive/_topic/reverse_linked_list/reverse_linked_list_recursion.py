from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list


def reverseList(list: ListNode) -> ListNode:

    if not list.next:
        return list
    newNode = reverseList(list.next)
    list.next.next = list
    list.next = None

    return newNode


def reverseList_i(list: ListNode) -> ListNode:

    prev = None
    curr = list

    while curr:

        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


l = build_list([1, 2, 3, 4, 5])


reversed_l = reverseList_i(l)


print_list(reversed_l)
