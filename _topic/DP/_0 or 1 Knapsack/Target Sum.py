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

 # 2-D DP


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total_sum = sum(nums)

        if total_sum < target:
            return 0

        dp = [[0] * (2 * total_sum + 1) for _ in range(n)]

        #! populate first row

        dp[0][nums[0] + total_sum] += 1
        #! if [nums[0] == 0 , two possible ways
        dp[0][-nums[0] + total_sum] += 1

        for i in range(1, n):
            # loop
            for j in range(2 * total_sum + 1):
                # check boundary
                if 0 <= j + nums[i] < 2 * total_sum + 1:
                    dp[i][j] += dp[i-1][j + nums[i]]
                if 0 <= j - nums[i] < 2 * total_sum + 1:
                    dp[i][j] += dp[i-1][j - nums[i]]

        return dp[-1][total_sum + target]


nums = [1, 1, 1, 1, 1]
target = 3

# nums = [1]
# target = 2

nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
target = 1

so = Solution()
res = so.findTargetSumWays(nums, target)
print(res)
