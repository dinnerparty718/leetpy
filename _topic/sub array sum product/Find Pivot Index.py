from typing import List


# one pass
# calculate sub array sum and total indx

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sub_array_sum = 0

        total_sum = sum(nums)
        for i, num in enumerate(nums):
            left = sub_array_sum
            right = total_sum - left - num
            if left == right:
                return i
            sub_array_sum += num

        return -1
