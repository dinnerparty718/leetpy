# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
from LinkedList.ListNode import ListNode
from utils.buildLinkedList import build_list, print_list
import heapq

# python 3 priority queue issue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        h = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))

        res = ListNode(0)
        cur = res

        while h:
            _val, _i, node = heapq.heappop(h)
            cur.next = node
            cur = cur.next

            if node.next:
                i += 1
                heapq.heappush(h, (node.next.val, i, node.next))

        return res.next


class Wrapper:
    def __init__(self, ln):
        self.ln = ln

    def __lt__(self, other):
        return self.ln.val < other.ln.val

# todo use wrapper class


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


so = Solution()

l = [[1, 4, 5], [1, 3, 4], [2, 6]]

list_input = []

for i in l:
    list_input.append(build_list(i))


res = so.mergeKLists(list_input)


print_list(res)
