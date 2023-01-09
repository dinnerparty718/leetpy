from typing import List


import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks:
            return 0

        heapq.heapify(sticks)

        total = 0

        while len(sticks) > 1:
            first, second = heapq.heappop(sticks), heapq.heappop(sticks)

            total += first + second

            heapq.heappush(sticks, first + second)

        return total


so = Solution()

sticks = [5]
res = so.connectSticks(sticks)

print(res)
