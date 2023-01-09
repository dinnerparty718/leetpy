from typing import List


'''
53. Maximum Subarray


Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



'''

# one pass
# current max either


'''
[-2, 1, -3, 4, -1, 2, 1, -5, 4]


# Kadane's algorithm

remove negative prefix
"sliding window"

'''


# from neetcode
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = curr_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            res = max(curr_sum, res)

        return res


so = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [5, 4, -1, 7, 8]
nums = [1]

res = so.maxSubArray(nums)
print(res)
