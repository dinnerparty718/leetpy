from typing import List
from LinkedList.ListNode import ListNode


def build_list(nums: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next

    return head.next


def print_list(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print('->'.join([str(val) for val in res]))


def main():
    head = build_list([1, 2, 3, 4, 5])
    print_list(head)


if __name__ == '__main__':
    main()
