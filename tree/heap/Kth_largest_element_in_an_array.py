from typing import List


import heapq


# time O(nlogn)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]

# leetcode


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


so = Solution()


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4


res = so.findKthLargest(nums, k)

print(res)
