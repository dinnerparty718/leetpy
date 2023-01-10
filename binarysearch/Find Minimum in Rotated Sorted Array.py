from typing import List

'''
Find Minimum in Rotated Sorted Array
non-repeat
binary search, target is right value
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) >> 1)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
