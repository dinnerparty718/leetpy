from typing import List
import bisect


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
