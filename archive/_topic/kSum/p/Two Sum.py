# 1. Two Sum
from typing import List


#! return one result and return

# todo multiple pairs

# Time O(n) one pass
# Space O(n) for hash table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in h:
                return [h[complement], idx]

            h[num] = idx
        return []


# two pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            h[num] = idx

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in h and h[complement] != idx:
                return [h[complement], idx]

        return []
