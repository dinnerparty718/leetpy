from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # append backwards
        res = []

        carry = 0

        for i in reversed(range(len(digits))):

            curr = 0

            if i == len(digits) - 1:
                curr = digits[i] + carry + 1
            else:
                curr = digits[i] + carry

            carry = curr // 10

            res.append(curr % 10)

        if carry > 0:
            res.append(1)

        res.reverse()

        return res
