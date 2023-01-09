
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # operations = '+-*/'
        # ops = {
        #     '+': lambda a, b: a + b,
        #     '-': lambda a, b: a - b,
        #     '*': lambda a, b: a * b,
        #     '/': lambda a, b: a * 10 + b,
        # }

        res = []

        n = len(num)

        # [1,]

        def dfs(i: int, prev_operand: int, current_operand: int, value,  output: List[str]):

            if i == n:
                if value == target and current_operand == 0:
                    res.append(''.join(output[1:]))
                return

            # extending the current operand by one diget
            current_operand = current_operand*10 + int(num[i])
            str_op = str(current_operand)

            if current_operand > 0:

                # print(current_operand)
                dfs(i+1, prev_operand, current_operand, value, output)

            # addition, can be in the beginnin

            output.append('+')
            output.append(str_op)
            dfs(i+1, current_operand, 0, value + current_operand, output)
            output.pop()
            output.pop()

            if output:
                # subtraction
                output.append('-')
                output.append(str_op)
                dfs(i+1, -current_operand, 0, value-current_operand, output)
                output.pop()
                output.pop()

                # multipication

                output.append('*')
                output.append(str_op)
                dfs(i+1, current_operand * prev_operand, 0, value -
                    prev_operand + (current_operand * prev_operand), output)

                output.pop()
                output.pop()

        # dfs(1, int(num[0]), [num[0]])

        dfs(0, 0, 0, 0, [])

        return res


so = Solution()


num = "232"
target = 8


res = so.addOperators(num, target)

print(res)
