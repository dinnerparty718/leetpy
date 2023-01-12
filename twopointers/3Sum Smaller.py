'''
918 · 3Sum Smaller

sort then 2 poiner

'''

from typing import (
    List,
)


class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """

    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        # Write your code here
        res = 0
        nums.sort()

        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res


nums = [-2, 0, 1, 3]
target = 2


so = Solution()

res = so.three_sum_smaller(nums, target)
print(res)
