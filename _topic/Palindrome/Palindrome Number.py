# 9. Palindrome Number


# convert to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        l, r = 0, len(x_str)-1

        while l < r:
            if x_str[l] != x_str[r]:
                return False
            l += 1
            r -= 1

        return True


# without converted to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revertedNumber = 0

        # reverted half
        # 12 21    12  vs 12
        # 12 321   12 vs 123
        while x > revertedNumber:
            quotient, remainder = divmod(x, 10)

            x = quotient

            revertedNumber = revertedNumber*10 + remainder

        return x == revertedNumber or x == revertedNumber // 10


so = Solution()

x = 12321

res = so.isPalindrome(x)

print(res)
