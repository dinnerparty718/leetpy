from typing import List

'''
O(nlogk)
O(k)

#! top k largest, use min_heap


#! top k smallest, use max_heap


'''

import heapq


def top_k_largest_elements(nums: List[int], k: int):

    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap


nums = [2, 1, 3, 4, 0]
k = 2

top2 = top_k_largest_elements(nums, 2)


def top_k_smallest_elements(nums: List[int], k: int):
    max_heap = []

    for num in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -num)
        elif -num > max_heap[0]:
            heapq.heappushpop(max_heap, -num)

    return [-num for num in max_heap]


nums = [2, 1, 3, 4, 0]
k = 2

bottom2 = top_k_smallest_elements(nums, 2)

print(bottom2)
