

# neetcode solution. perfect

# todo check leetcode solution

# https://leetcode.com/problems/palindromic-substrings/solution/
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s)):
            # odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt


so = Solution()

s = "aaa"

s = "aaa"

res = so.countSubstrings(s)


print(res)
