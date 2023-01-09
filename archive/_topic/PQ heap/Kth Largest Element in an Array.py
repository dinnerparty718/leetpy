from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if k > len(nums):
            return -1

        adjusted = [-num for num in nums]

        heapq.heapify(adjusted)

        val = None

        while k > 0:
            val = heapq.heappop(adjusted)
            k -= 1

        return -val


so = Solution()

nums = [3, 2, 1, 5, 6, 4]
k = 2


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
res = so.findKthLargest(nums, k)

print(res)
