from typing import List


# own
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


# leetcode
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return ['']
        ans = []

        for i in range(1, n+1):
            for left in self.generateParenthesis(i-1):
                for right in self.generateParenthesis(n-i):
                    ans.append(left + '(' + right + ')')

        return ans

# place left firt, try to match right


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2*n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:  # valid
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


so = Solution2()


n = 3


res = so.generateParenthesis(n)


print(res)
