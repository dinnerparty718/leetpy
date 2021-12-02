from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [None] * (n+1)

        def dfs(n: int, s: str, memo: List[int]):

            if n == 1 and s[0] == '0':
                return 0

            if n <= 1:
                return 1

            if memo[n] is not None:
                return memo[n]

            #! last item have to take n into consideration
            x = s[n-1]  # last item
            y = s[n-2]  # second to the left

            res = 0

            if x != '0':
                res += dfs(n-1, s, memo)

            # last_two = 0

            last_two = int(y) * 10 + int(x)

            if 10 <= last_two <= 26:
                res += dfs(n-2, s, memo)

            memo[n] = res
            return memo[n]

        return dfs(n, s, memo)


so = Solution()

s = '1201234'
res = so.numDecodings(s)

print(res)
