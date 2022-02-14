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
            # for j in range(2 * total_sum + 1):
            #     # check boundary
            #     if 0 <= j + nums[i] < 2 * total_sum + 1:
            #         dp[i][j] += dp[i-1][j + nums[i]]
            #     if 0 <= j - nums[i] < 2 * total_sum + 1:
            #         dp[i][j] += dp[i-1][j - nums[i]]

            for j in range(-total_sum, total_sum + 1):
                if dp[i-1][j+total_sum] > 0:
                    dp[i][j+total_sum + nums[i]] += dp[i-1][total_sum+j]
                    dp[i][j+total_sum - nums[i]] += dp[i-1][total_sum+j]

        return dp[-1][total_sum + target]


# hua hua
# 2 D
# https://www.youtube.com/watch?v=r6Wz4W1TbuI
# dummy row on top   n + 1 rows
#  dp =  [  [  ] for _ in range(n+1) ]
# much easy to visualize
# Pascal's triangle
# 杨辉三角
#! fastest

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total_sum = sum(nums)

        if total_sum < target:
            return 0

        dp = [[0] * (2 * total_sum + 1) for _ in range(n+1)]

        # none element sum up to 0
        # this is true
        dp[0][total_sum] = 1

        for i in range(0, n):
            # j 的取值范围
            for j in range(nums[i], 2 * total_sum + 1 - nums[i]):
                if dp[i][j] > 0:
                    dp[i+1][j + nums[i]] += dp[i][j]
                    dp[i+1][j - nums[i]] += dp[i][j]

        return dp[-1][total_sum + target]


#! 1d rolling array 滚动数组
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total_sum = sum(nums)

        if total_sum < target:
            return 0

        dp = [0] * (2 * total_sum + 1)
        dp[total_sum] = 1

        for num in nums:
            tmp = [0] * (2 * total_sum + 1)
            for j in range(num, 2 * total_sum + 1 - num):
                if dp[j] > 0:
                    tmp[j + num] += dp[j]
                    tmp[j - num] += dp[j]

            # tmp, dp = dp, tmp
            dp, tmp = tmp, dp

        return dp[target + total_sum]


nums = [1, 1, 1, 1, 1]
target = 3

# nums = [1]
# target = 2

nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
target = 1

so = Solution()
res = so.findTargetSumWays(nums, target)
print(res)
