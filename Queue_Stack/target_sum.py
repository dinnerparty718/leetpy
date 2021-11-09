from functools import cache
from typing import List
#from functools import cache

# dfs stack or recursive

# https://leetcode.com/problems/target-sum/discuss/1269547/Python-Memoized-Solution-(Most-simple-'Memoized'-template-to-solve-such-questions)


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def helper(i, sum):
            # reference count to ther outer scope
            # but not global scope either

            key = (i, sum)

            if key in memo:
                return memo[key]

            # base case
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            else:

                to_return = helper(
                    i + 1, sum - nums[i]) + helper(i + 1, sum + nums[i])

                memo[key] = to_return
                return to_return

        return helper(0, 0)

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:

        @cache
        def dp(i, sum):
            if i == len(nums):
                if target == sum:
                    return 1
                else:
                    return 0
            else:
                return dp(i+1, sum + nums[i]) + dp(i+1, sum - nums[i])
        return dp(0, 0)


so = Solution()

# nums = [1, 1, 1, 1, 1]
# target = 3

nums = [0, 38, 42, 31, 13, 10, 11, 12, 44,
        16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39]
target = 2

res = so.findTargetSumWays2(nums, target)
print(res)
