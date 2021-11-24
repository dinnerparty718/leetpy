from typing import List
from LinkedList.ListNode import DoubleLinkedListNode, ListNode


def build_list(nums: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return head.next


def build_double_linked_list(nums: List[int]) -> DoubleLinkedListNode:
    dummy = DoubleLinkedListNode(0)

    cur = dummy
    prev = None

    for num in nums:
        n = DoubleLinkedListNode(num)
        cur.next = n
        n.prev = prev

        cur = cur.next
        prev = cur

    return dummy.next


def print_list(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print('->'.join([str(val) for val in res]))


def print_double_list(head: DoubleLinkedListNode):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print('->'.join([str(val) for val in res]))

    while head.next:
        head = head.next

    res = []
    while head:
        res.append(head.val)
        head = head.prev

    print('<-'.join([str(val) for val in res[::-1]]))


def main():
    # head = build_list([1, 2, 3, 4, 5])
    # print_list(head)
    head = build_double_linked_list([1, 2, 3, 4, 5])
    print_double_list(head)


if __name__ == '__main__':
    main()
