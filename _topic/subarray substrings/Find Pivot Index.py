from typing import List


'''
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11


calculate total_sum
loop through nums and calculate
    sub_array_sum
    
    left = sub_array_sum
    right = total_sum - sub_array_sum - num
    
    return i if left == right


'''

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
