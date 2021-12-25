from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        # return i
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb < 0:
                continue
            heapq.heappush(min_heap, climb)
            if len(min_heap) <= ladders:
                continue

            # ladders all used

            bricks -= heapq.heappop(min_heap)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i

        return len(heights) - 1


so = Solution()

# heights = [4, 2, 7, 6, 9, 14, 12]
# bricks = 5
# ladders = 1

heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks = 10
ladders = 2

res = so.furthestBuilding(heights, bricks, ladders)

print(res)
