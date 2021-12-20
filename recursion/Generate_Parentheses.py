from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        memo = {}

        def dfs(n):
            if n == 0:
                return ['']
            if n in memo:
                return memo[n]

            res = []

            for i in range(1, n+1):
                left_result = dfs(i-1)
                right_result = dfs(n-i)

                for l in left_result:
                    for r in right_result:
                        res.append(l + '(' + r + ')')

            memo[n] = res

            return res

        return dfs(n)


so = Solution()


n = 3


res = so.generateParenthesis(n)


print(res)
