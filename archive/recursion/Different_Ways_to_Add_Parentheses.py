from typing import List


# modifying input string is better
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        memo = {}

        def dfs(input: str):
            if input in memo:
                return memo[input]

            if input.isnumeric():
                return [int(input)]

            res = []

            for i, c in enumerate(input):
                if c in "+-*":
                    res += [l+r if c == "+" else l-r if c == "-" else l*r for l in dfs(input[:i])
                            for r in dfs(input[i+1:])]

            memo[input] = res
            return res

        return dfs(expression)


class Solution1:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        memo = {}

        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }

        def dfs(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            res = []

            # base case
            if expression[start: end+1].isdigit():
                return [int(expression[start: end+1])]

            for i in range(start, end + 1):
                if expression[i] in ops:
                    left = dfs(start, i-1)
                    right = dfs(i+1, end)

                    for l in left:
                        for r in right:
                            res.append(ops[expression[i]](l, r))

            memo[(start, end)] = res

            return res

        return dfs(0, len(expression) - 1)


so = Solution1()


expression = "2*3-4*5"

expression = '11'

res = so.diffWaysToCompute(expression)

print(res)
