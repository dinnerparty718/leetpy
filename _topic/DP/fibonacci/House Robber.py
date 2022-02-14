from typing import List


# neet code
# better DP without storing the whole array
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1]
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)

        return rob2


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


# top down
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
