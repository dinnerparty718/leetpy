

# DP problem
# top down -> in turing planet this would be recursive bottom up, use children result compute current result
class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(i: int, memo: dict) -> int:
            if i <= 2:
                return i

            if i in memo:
                return memo[i]

            res = dp(i-1, memo) + dp(i-2, memo)

            memo[i] = res

            return memo[i]

        return dp(n, {})


so = Solution()

n = 2
res = so.climbStairs(n)


print(res)
