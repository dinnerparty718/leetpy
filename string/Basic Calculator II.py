'''
980 · Basic Calculator II

The expression string contains only non-negative integers,
+, -, *, / operators and empty spaces . Division of integers should round off decimals.



stack

preSign

加号：将数字压入栈；
减号：将数字的相反数压入栈；
乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。

python int(-1.5) => towards 0  => -1

Time(n)
space(n)

'''


class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """

    def calculate(self, s: str) -> int:
        # Write your code here
        n = len(s)
        stack = []
        preSign = '+'
        num = 0  # !record current number could be two digit 12

        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():  # ! s[i] in '0123456789'
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':  # ! remeber to handle last number
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                preSign = s[i]
                num = 0
        return sum(stack)


so = Solution()
s = '3+2*2'
# s = ' 3/2 '
res = so.calculate(s)
print(res)
