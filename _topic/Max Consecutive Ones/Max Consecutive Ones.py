'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


'''


# one pass count
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        curr_sum = 0

        for num in nums:
            if num == 1:
                curr_sum += 1
            else:
                res = max(res, curr_sum)
                curr_sum = 0

        return max(curr_sum, res)


# stack find next 0

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        next_zero = [n]*n

        for i, num in enumerate(nums):
            while stack and num == 0:
                idx = stack.pop()
                next_zero[idx] = i

            if num == 1:
                stack.append(i)

        stack = []

        res = 0

        for i in range(n):
            if nums[i] == 0:
                continue

            res = max(res, next_zero[i] - i)

        return res
