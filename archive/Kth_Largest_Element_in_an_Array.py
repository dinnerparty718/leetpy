import heapq
from typing import List


# max heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        while len(nums) > k:

            heapq.heappop(nums)

        return nums[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2

so = Solution()

res = so.findKthLargest(nums, k)


print(res)
