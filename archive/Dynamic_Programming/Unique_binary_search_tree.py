from typing import List
import math

# from Turing planet
# dfs with memo

# https://www.youtube.com/watch?v=GgP75HAvrlY

# good for generate the subtree


class Solution:
    def numTrees(self, n: int) -> int:

        memo = [None] * (n+1)

        def dfs(n: int, memo: List[int]):
            if n <= 1:
                return 1

            if memo[n] != None:
                return memo[n]
            res = 0

            for i in range(1, n+1):
                left = dfs(i-1, memo)
                right = dfs(n-i, memo)
                res += left * right  # cartesian product

            memo[n] = res
            return res

        return dfs(n, memo)


# time O(n^2)
class Solution1:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        # complexity
        for i in range(2, n+1):
            for j in range(1, i+1):
                # when pick j as root
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]


#   c(2) = C(0)C(1) + C(1,0) = 1 + 1 = 2
#   c(3) = C(0)C(2) + C(1)C(1) + C(2)C(0) = 2 + 1 + 2 = 5
class Solution2:
    def numTrees(self, n: int) -> int:
        C = [0] * (n+1)

        C[0] = 1
        C[1] = 1

        for i in range(2, n+1):
            for j in range(0, i):
                C[i] += C[j]*C[i-j-1]

        return C[n]


so = Solution2()


res = so.numTrees(3)

print(res)


# time O(n)


def catalan_number(n):
    val = math.factorial(2*n) / (math.factorial(n) * math.factorial(n+1))
    return int(val)


print(catalan_number(4))
