'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

'''

#! prefix sum { 0 : 1 }


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        prefix_sum = {0: 1}
        cur_sum = 0

        for num in nums:
            cur_sum += num
            if cur_sum - k in prefix_sum:
                res += prefix_sum[cur_sum - k]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return res


so = Solution()

nums = [1, 1, 1]
k = 2


nums = [1, 2, 3]
k = 3

res = so.subarraySum(nums, k)

print(res)
