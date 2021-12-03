from typing import List


# find right most peak

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i: int, j: int, nums: List[int]):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if len(nums) <= 1:
            return

        last_peak_index = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                last_peak_index = i

        # number is in deceding order
        if last_peak_index == 0:
            nums.reverse()
            return

        k = last_peak_index - 1    # find the last "ascending" position
        # find a larger number then k

        j = len(nums) - 1

        while nums[j] <= nums[k]:
            j -= 1

        nums[j], nums[k] = nums[k], nums[j]

        reverse(k+1, len(nums)-1, nums)


so = Solution()
nums = [1, 2, 3]
so.nextPermutation(nums)


print(nums)
