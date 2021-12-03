
# own soluion
# time space O(M^2 + MN)

# todo can be optimized to sum the result one by one

from itertools import zip_longest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        final_res = ''

        for idx, n2 in enumerate(num2):
            cur = '0' * idx
            carry = 0

            for n1 in num1:
                result = (int(n2) * int(n1) + carry) % 10
                cur += str(result)
                carry = (int(n2) * int(n1) + carry) // 10

            if carry != 0:
                cur += str(carry)

            final_res = self.sumResult(final_res, cur)

        return final_res[::-1]

    def sumResult(self, final_res: str, to_be_add: str) -> str:

        if final_res == '':
            return to_be_add

        curry = 0

        tmp = ''

        for digit1, digit2 in zip_longest(final_res, to_be_add, fillvalue='0'):
            d1 = int(digit1)
            d2 = int(digit2)
            sum_result = d1 + d2 + curry
            tmp += str(sum_result % 10)
            curry = sum_result // 10

        if curry != 0:
            tmp += str(curry)

        return tmp

        # maxLen = max([len(c) for c in res])

        # for i, c in enumerate(res):
        #     res[i] += '0' * (maxLen - len(c))

        # result = ''
        # carry = 0
        # for j in range(maxLen):
        #     cur = 0
        #     for i in range(len(res)):
        #         cur += int(res[i][j])

        #     cur += carry

        #     result += str(cur % 10)
        #     carry = cur // 10

        # if carry != 0:
        #     result += str(carry)

        # return result[::-1]


so = Solution()

# num1 = "123456789"
# num2 = "987654321"
num1 = "123"
num2 = "456"

# "121932631112635269"

res = so.multiply(num1, num2)
print(res)
