
# own solution
# todo https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/289/discuss/107718/Easy-to-Understand-Python-Solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        diff = 0

        skipLeft = True
        skipRight = True

        while l < r:
            if s[l] != s[r]:
                diff += 1
                l += 1
                if diff > 1:
                    skipLeft = False
                    break
            else:
                l += 1
                r -= 1

        l, r = 0, len(s)-1
        diff = 0

        if skipLeft:
            return True

        while l < r:
            if s[l] != s[r]:
                diff += 1
                r -= 1
                if diff > 1:
                    skipRight = False
                    break
            else:
                l += 1
                r -= 1

        return skipRight


so = Solution()

s = 'abca'

res = so.validPalindrome(s)

print(res)
