import heapq
from typing import List

'''
greedy, use ladders first and store the height diff in heap


N = number of heights
L = number of ladders

Time: O(NlogN)
Space: O(N)


'''


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        min_heap = []

        # compare current to next
        for i in range(n-1):
            h = heights[i+1] - heights[i]
            if h <= 0:
                continue
            heapq.heappush(min_heap, h)

            if len(min_heap) <= ladders:
                continue

            bricks -= heapq.heappop(min_heap)
            if bricks < 0:
                return i

        return n-1
