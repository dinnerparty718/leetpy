# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time O(nlogk)
# Space O (n)new linked list O(k) is far less than O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        min_heap = []
        counter = 0

        for l in lists:
            if not l:
                continue
            min_heap.append((l.val, counter, l))
            counter += 1

        # O(n)
        heapq.heapify(min_heap)

        dummyHead = ListNode()
        cur = dummyHead

        # O(logk)
        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            cur.next = node

            cur = cur.next
            if node.next:
                newHead = node.next
                heapq.heappush(min_heap, (newHead.val, counter, newHead))
                counter += 1

        return dummyHead.next


# todo Merge list one by one
# base case merge 2 list
# recursive or iterative
# Time O(kN)
# space O(1)
