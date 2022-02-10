# https://leetcode.com/problems/sum-of-subarray-ranges/


'''
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

'''


#! subarray sum(max) -  sum(min)

#! brute force generate subarray O(n^2)
#! better stack
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        next_smaller = [n] * n
        prev_smaller = [-1] * n  # or equal

        next_larger = [n] * n
        prev_larger = [-1] * n  # or equal

        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                idx = stack.pop()
                next_smaller[idx] = i
            stack.append(i)

        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                next_larger[idx] = i
            stack.append(i)

        stack = []

        for i in reversed(range(n)):
            num = nums[i]
            while stack and nums[stack[-1]] >= num:
                idx = stack.pop()
                prev_smaller[idx] = i
            stack.append(i)

        stack = []

        for i in reversed(range(n)):
            num = nums[i]
            while stack and nums[stack[-1]] <= num:
                idx = stack.pop()
                prev_larger[idx] = i
            stack.append(i)

        res = 0

        for i in range(n):
            l_smaller, right_smaller = prev_smaller[i], next_smaller[i]
            l_larger, right_larger = prev_larger[i], next_larger[i]

            res += nums[i]*(i-l_larger) * (right_larger - i) - \
                nums[i]*(i-l_smaller) * (right_smaller - i)

        return res


so = Solution()


nums = [1, 2, 3]

nums = [1, 3, 3]


nums = [4, -2, -3, 4, 1]
res = so.subArrayRanges(nums)

print(res)
