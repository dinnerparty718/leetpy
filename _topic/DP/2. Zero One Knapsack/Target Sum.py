from typing import List

# subset sum
# 01 knapsack
# DP

# exceed time limit
# this is brute force


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0

        n = len(nums)

        memo = {}

        def dfs(i: int, currSum: int):
            if i == n:
                if currSum == target:
                    return 1
                else:
                    return 0

            if (i, currSum) in memo:
                return memo[(i, currSum)]

            memo[(i, currSum)] = dfs(i+1, currSum + nums[i]) + dfs(i+1, currSum - nums[i])
            return memo[(i, currSum)]

        return dfs(0, 0)


nums = [1, 1, 1, 1, 1]
target = 3

# nums = [1]
# target = 1

so = Solution()
res = so.findTargetSumWays(nums, target)
print(res)
