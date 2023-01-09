
from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list

# todo
# optimized

# class Node:
#   def __init__(self, x):
#     self.data = x
#     self.next = None

# Add any helper functions you may need here


def reverse_list(node: ListNode):
    prev = None
    curr = node
    while curr:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt

    return prev  # new head


def reverse(head: ListNode):
    # Write your code here
    dummyHead = ListNode()
    dummyHead.next = head

    prev = dummyHead
    curr = head

    last_even_node = None
    last_even_node_prev = None

    while curr:
        if curr.val % 2 == 0 and last_even_node == None:
            last_even_node = curr
            last_even_node_prev = prev

            prev = curr
            curr = curr.next

        elif (curr.val % 2 == 0 and last_even_node != None and curr.next and curr.next.val % 2 == 1) or (curr.val % 2 == 0 and last_even_node != None and not curr.next):
            # reverse
            nxt = curr.next
            curr.next = None  # break the link for reverse

            reverse_list(last_even_node_prev.next)
            prev = last_even_node_prev.next
            last_even_node_prev.next = curr

            curr = nxt
            prev.next = curr

            last_even_node = None
            last_even_node_prev = None
        elif curr.val % 2 == 1 and last_even_node != None:
            last_even_node = None
            last_even_node_prev = None

            prev = curr
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return dummyHead.next


# head = build_list([1, 8, 2, 9, 16, 12])

arr = [2, 18, 24, 3, 5, 7, 9, 6, 1]
# arr = [1, 3, 24]

arr = [1, 2, 1, 4, 2]

head = build_list(arr)
print_list(head)


new_l = reverse(head)

print_list(new_l)
