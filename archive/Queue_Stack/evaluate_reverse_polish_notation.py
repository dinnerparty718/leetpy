from typing import List
from collections import deque

# own solution
# optimized using lambda function
# time space O(n)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])

        stack = deque()

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                tmp = 0
                if token == '+':
                    tmp = v1 + v2
                elif token == '-':
                    tmp = v1 - v2
                elif token == '*':
                    tmp = v1 * v2
                else:
                    tmp = v1 / v2

                stack.append(int(tmp))
        return stack[-1]

    def evalRPN2(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = deque()

        for token in tokens:
            if token in operations:
                n_2 = stack.pop()
                n_1 = stack.pop()
                op = operations[token]
                stack.append(op(n_1, n_2))
            else:
                stack.append(int(token))

        return stack.pop()


so = Solution()

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

res = so.evalRPN2(tokens)


print(res)
