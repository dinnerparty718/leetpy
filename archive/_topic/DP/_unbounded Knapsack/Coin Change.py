from typing import List

# https://www.youtube.com/watch?v=H9bfqozjoqs

#! 1D min number of coins, dont' need duplicate

# top down
# DFS with memo


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount: int):
            if amount == 0:
                return 0

            if amount < 0:
                return -1

            # 1 means one coin
            if amount-1 in memo:
                return memo[amount-1]

            min_cnt = float('inf')

            for coin in coins:
                res = dfs(amount - coin)

                if res >= 0 and res < min_cnt:
                    min_cnt = 1 + res

            memo[amount-1] = min_cnt if min_cnt != float('inf') else -1

            return memo[amount-1]

        return dfs(amount)


# Time O(n*amoumt)
# Space O(amoumt)
# bottom up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #! becase we wanted to store min value
        dp = [float('inf')] * (amount + 1)  # start from 0

        dp[0] = 0  # ammount zero take 0 coin

        for a in range(1, amount+1):
            for c in coins:
                if a - c < 0:
                    continue

                dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[-1] if dp[-1] != float('inf') else -1


coins = [1, 2, 5]
amount = 11

# coins = [2]
# amount = 3


# coins = [1]
# amount = 0


# coins = [186, 419, 83, 408]
# amount = 6249

so = Solution()
res = so.coinChange(coins, amount)

print(res)
