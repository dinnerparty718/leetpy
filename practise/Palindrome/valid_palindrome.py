#import re


# ''.isalnum()
# todo check all string functions

# time O(n)
# space O(1)
# do not take extra space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s1 = s.lower().replace(' ', '')
        # s1 = re.sub('[^a-zA-Z0-9]', '', s1)

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
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
