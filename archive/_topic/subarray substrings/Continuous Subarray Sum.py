from typing import List

'''

https://leetcode.com/problems/continuous-subarray-sum/discuss/1479244/Simple-python-solution-O(n)-time-with-comments

523. Continuous Subarray Sum

similar to Maximum Sum Subarray of Size K
Subarray Sum Equals K

prefix sum

(sum2 - sum1) % k == 0 and idx2 - idx2 >=2



#! all possitive numbers, use % without problem


'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        # e.g nums = [4,2] , k = 3
        sums = {0: -1}  # ! remainder and idx
        cumulative_sum = 0

        for idx, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k

            if remainder in sums and idx - sums[remainder] >= 2:
                return True

            if remainder not in sums:
                sums[remainder] = idx

        return False


nums = [23, 2, 4, 6, 7]
k = 6


so = Solution()

res = so.checkSubarraySum(nums, k)

print(res)
