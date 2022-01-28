from typing import List


# todo

# https://leetcode.com/problems/sort-colors/solution/

# own
# Time O(n) two passes
# Space O(1) swap in place


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer

        left = 0

        def swap(i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]

        # swap left, right when encounter 0
        for right in range(len(nums)):
            if nums[right] == 0:
                swap(left, right)
                left += 1  # move to next swap position

        # swap left, right when encounter 1

        for right in range(left, len(nums)):
            if nums[right] == 1:
                swap(left, right)
                left += 1


# better
# 3 pointer approach , left, right and cur
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right, i = 0, len(nums) - 1, 0

        # [ 2,0,2,1,1,0]

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1


so = Solution()

nums = [1, 2, 0]
#nums = [2, 0, 1]

so.sortColors(nums)


print(nums)
