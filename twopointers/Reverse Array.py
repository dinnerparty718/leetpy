'''
767 · Reverse Array

'''

from typing import (
    List,
)


class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """

    def reverse_array(self, nums: List[int]):
        # write your code here
        left, right = 0, len(nums)-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


nums = [1, 2, 5]


so = Solution()

res = so.reverse_array(nums)
print(nums)
