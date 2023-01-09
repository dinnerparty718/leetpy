

from typing import List
import heapq


def top_k_th_largest(nums: List[int], k: int):
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]


nums = [2, 1, 3, 4, 0]
k = 2

top2 = top_k_th_largest(nums, 2)

print(top2)
