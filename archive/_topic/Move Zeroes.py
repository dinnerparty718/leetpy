from typing import List


'''

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



todo
loop backwards 
swap zero with end


'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


so = Solution()

nums = [0, 1, 0, 3, 12]
res = so.moveZeroes(nums)

print(res)
