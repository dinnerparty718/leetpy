from typing import List


# bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[len(nums)-1]


# top up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i: int):
            if i == 0:
                return nums[0]

            if i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i-1), dp(i-2) + nums[i])

            return memo[i]

        return dp(n-1)


nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
nums = [1]
so = Solution()

res = so.rob(nums)

print(res)
