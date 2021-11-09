import re


# ''.isalnum()
# todo check all string functions


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower().replace(' ', '')
        s1 = re.sub('[^a-zA-Z0-9]', '', s1)

        l = 0
        r = len(s1)-1

        while l < r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1

        return True


so = Solution()
#s = "A man, a plan, a canal: Panama"
#s = "race a car"
s = "ab_a"
res = so.isPalindrome(s)
print(res)
