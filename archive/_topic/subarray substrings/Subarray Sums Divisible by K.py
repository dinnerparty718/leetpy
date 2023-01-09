from typing import List

'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.


Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

size can be 1


combination of 
    subarray k and        count
    continues sub array      k 



#! number can be negative





'''


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}  # store count here
        cumulative_sum = 0

        res = 0

        for n in nums:
            cumulative_sum += n
            # print(cumulative_sum)
            # remainder = int(math.fmod(cumulative_sum, k))
            remainder = cumulative_sum % k

            if remainder in prefix_sum:
                res += prefix_sum[remainder]

            prefix_sum[remainder] = prefix_sum.get(remainder, 0) + 1

        return res


so = Solution()


nums = [4, 5, 0, -2, -3, 1]
k = 5

nums = [5]
k = 9


nums = [-1, 2, 9]
k = 2

res = so.subarraysDivByK(nums, k)


print(res)
