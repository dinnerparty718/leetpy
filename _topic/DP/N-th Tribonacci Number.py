
'''
Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


'''


class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0

        if n <= 2:
            return 1

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[-1]


so = Solution()

n = 4
n = 25

res = so.tribonacci(n)

print(res)
