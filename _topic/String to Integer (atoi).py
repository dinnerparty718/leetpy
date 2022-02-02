# 8. String to Integer (atoi)


# 32 bit 4 bytes

# min = -2**31
# max = 2*31 -1

# finally own

class Solution:
    def myAtoi(self, s: str) -> int:

        if not s:
            return 0

        MAX = 2**31 - 1
        MIN = - 2**31

        negative = False
        res = 0
        i = 0

        # skip space
        while i < len(s) and s[i] == ' ':
            i += 1

        # check if there is - or +
        if i < len(s):
            if s[i] == '-':
                negative = True
                i += 1
            elif s[i] == '+':
                negative = False
                i += 1
            elif s[i].isalpha():
                # if start with character
                return 0

        while i < len(s) and s[i].isnumeric():
            val = int(s[i])

            if negative:
                if res > MAX // 10 or (res == MAX // 10 and val > 8):
                    return MIN
            else:
                if res > MAX // 10 or (res == MAX // 10 and val > 7):
                    return MAX

            res = res * 10 + val
            i += 1

        return res if not negative else -res


so = Solution()
s = "4193 with words"

s = "words and 987"
s = "   -42"
s = "21474836460"
res = so.myAtoi(s)

print(res)
