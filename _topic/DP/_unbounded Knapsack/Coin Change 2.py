from typing import List
#! how many ways, need to avoid duplicate

# top down with memo
# m*n 2D

# https://www.youtube.com/watch?v=Mjy4hd2xgrs


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def dfs(i: int, amount: int):

            if amount == 0:
                return 1

            if amount < 0:
                return 0

            if i == len(coins):
                return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            #! taken or skip
            memo[(i, amount)] = dfs(i, amount - coins[i]) + dfs(i+1, amount)

            return memo[(i, amount)]

        res = dfs(0, amount)

        return res


# random guy on youtube
class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        #! problem has duplicate
        for coin in coins:

            for a in range(amount + 1):
                if a >= coin:
                    dp[a] += dp[a-coin]

        return dp[-1]

# leetcode


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        #! similar to generate subset
        for coin in coins:
            for a in range(coin,  amount + 1):
                dp[a] += dp[a-coin]

        return dp[-1]


so = Solution()

amount = 5
coins = [1, 2, 5]
res = so.change(amount, coins)

print(res)
