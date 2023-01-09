'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


'''


from typing import List


#! two pointers

# todo more efficient two pointers
# https://leetcode.com/problems/max-consecutive-ones-iii/solution/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = right = 0

        res = 0

        cnt_of_zeros = 0

        while right < n:
            if nums[right] == 0:
                cnt_of_zeros += 1

            while cnt_of_zeros > k:
                if nums[left] == 0:
                    cnt_of_zeros -= 1

                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res


so = Solution()

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

res = so.longestOnes(nums, k)

print(res)
