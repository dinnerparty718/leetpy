from typing import List


# leetcode
# easy to understand recurrsion relation
# bottom up dp[0] and dp[1] = 0 since it does not cost money
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[-1]

# own


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i: int):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]
        return dp(len(cost))


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        if n == 1:
            return cost[0]

        if n == 2:
            return min(cost[0], cost[1])

        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[-1], dp[-2])


so = Solution()

cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
res = so.minCostClimbingStairs(cost)


print(res)
