from typing import List

# practice
# recursive with memo


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        memo = [None] * (n+1)

        def dfs(n: int, s: str, memo: List):

            if n == 1 and s[0] == '0':
                return 0

            if n <= 1:
                return 1

            if memo[n] != None:
                return memo[n]

            x = s[n-1]
            y = s[n-2]

            res = 0

            if x != '0':
                res += dfs(n-1, s, memo)

            last_two = int(y)*10 + int(x)
            if 10 <= last_two <= 26:
                res += dfs(n-2, s, memo)

            memo[n] = res

            return res

        return dfs(n, s, memo)


# DP  bottom up, pattern
class Solution1:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        dp[1] = 1

        for i in range(2, len(dp)):
            prev = s[i-2]
            cur = s[i-1]

            if cur != '0':
                # there is one way till here
                dp[i] = dp[i-1]

            two_digits = int(prev) * 10 + int(cur)

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

            # print(s[i-2], dp[i])

        return dp[-1]  # or dp[n]

# dp  looping throught original string, not throught DP array


class Solution2:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        dp[1] = 1

        for i in range(1, n):
            if s[i] != '0':
                dp[i+1] = dp[i]

            twoDigits = int(s[i-1]) * 10 + int(s[i])

            if 10 <= twoDigits <= 26:
                dp[i+1] += dp[i-1]
        return dp[-1]  # or dp[n]

# dp only memorize last two result

# best DP
# time O(n)
# space O(n1)


class Solution3:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        n = len(s)
        twoBack = 1
        oneBack = 1

        for i in range(1, n):

            res = 0

            if s[i] != '0':
                res = oneBack

            twoDigits = int(s[i-1]) * 10 + int(s[i])

            if 10 <= twoDigits <= 26:
                res += twoBack

            twoBack = oneBack
            oneBack = res

        return oneBack  # or dp[n]


so = Solution3()


s = '11106'
# s = '0'


res = so.numDecodings(s)


print(res)
