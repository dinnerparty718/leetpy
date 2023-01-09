
# 123  % 10 ->
# perfect place to use divmod(123, 10)
# (12, 3)

# own Yass !! but slow
import math


class Solution:
    def reverse(self, x: int) -> int:
        # MAX = 2**31 - 1
        MIN = -2**31

        negative = True if x < 0 else False

        x_str = str(abs(x))

        res = 0

        for i in reversed(range(len(x_str))):
            cur_val = int(x_str[i])

            # check overflow

            if negative and (res * 10 - MIN < cur_val):
                return 0

            if not negative and (res * 10 - MIN < cur_val + 1):
                return 0

            res = res * 10 - cur_val

        return res if negative else -res


# leetcode
# https://leetcode.com/problems/reverse-integer/discuss/408697/Two-Python-Solutions-and-Explanation-of-Python-Modulo-and-Int-Division-Differences-From-CJava

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31  # end with 8
        MAX = 2**31 - 1  # end with 7

        res = 0

        while x:

            # (pyton) -1 % 10 = 9
            #        -1 // 10 -1
            # important
            # digit = int(math.fmod(x, 10))  # ! works with negative number

            digit = x % 10 if x >= 0 else (abs(x) % 10) * -1

            # x = int(x / 10)

            x = x // 10 if x >= 0 else math.ceil(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > 7):
                return 0

            if res < math.ceil(MIN) / 10 or (res == math.ceil(MIN) / 10 and digit < -8):
                return 0

            res = res * 10 + digit

        return res


so = Solution()

res = so.reverse(120)


print(res)
