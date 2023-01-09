# 8. String to Integer (atoi)


# 32 bit 4 bytes

# min = -2**31
# max = 2*31 -1

#


'''algorithm

1. skip any white spaces
2. check next i '+' or '-' and change the sign accordingly
3  construct positive number until reaching non-numeric
4  before * 10 check overflow and underflow

 min = -2**31
 max = 2*31 -1
   0-7
'''


class Solution:
    def myAtoi(self, s: str) -> int:

        if not s:
            return 0

        MAX = 2**31 - 1  # pow(2,31) -1
        MIN = - 2**31   # -pow(2,31)

        negative = False
        res = 0
        i = 0

        # skip space
        while i < len(s) and s[i] == ' ':
            i += 1

        # check if there is - or +
        if i < len(s) and s[i] == '+':
            i += 1
        elif i < len(s) and s[i] == '-':
            negative = True
            i += 1

        while i < len(s) and s[i].isdigit():
            val = int(s[i])

            # check overflow and underflow

            #! Note: We do not need to handle 0-7 for positive and 0-8 for negative integers separately.
            #! If the sign is negative and the current number is 214748364,
            #! then appending the digit 8, which is more than 7, will also lead to the same result, i.e., INT_MIN.
            if res > MAX // 10 or (res == MAX // 10 and val > MAX % 10):
                if negative:
                    return MIN
                else:
                    return MAX

            res = res * 10 + val
            i += 1

        return res if not negative else -res


so = Solution()
s = "4193 with words"

s = "words and 987"
s = "   -42"
# s = "21474836460"
res = so.myAtoi(s)

print(res)
