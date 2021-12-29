import heapq
from typing import List


# heapify O(n) -> pop O(nlog(n))

def heap_sort(nums: List[int]):

    heapq.heapify(nums)

    res = []

    for i in range(len(nums)):
        res.append(heapq.heappop(nums))
    return res


nums = [2, 8, 5, 3, 9, 4]

res = heap_sort(nums)

print(res)
