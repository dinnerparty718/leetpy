from typing import List


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
                res += left * right

            memo[n] = res
            return res

        return dfs(n, memo)


so = Solution()


res = so.numTrees(3)

print(res)
