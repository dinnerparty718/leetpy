from turtle import right
from typing import List

#   ( +  )

# backtrack


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left: int, right: int, curr: List[str]):
            if len(curr) == 2*n:
                res.append(''.join(curr))
                return

            if left < n:
                curr.append('(')
                backtrack(left+1, right, curr)
                curr.pop()
            if right < left:
                curr.append(')')
                backtrack(left, right+1, curr)
                curr.pop()

        backtrack(0, 0, [])

        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        res = []

        for i in range(1, n+1):
            left_result = self.generateParenthesis(i-1)
            right_result = self.generateParenthesis(n-i)

            for l in left_result:
                for r in right_result:
                    res.append(l + '(' + r + ')')

        return res


so = Solution()
n = 3
res = so.generateParenthesis(n)


print(res)
