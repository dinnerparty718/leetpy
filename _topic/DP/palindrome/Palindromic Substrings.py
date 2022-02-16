'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


'''

# Time O(n^2)
# Space O(1)
# expand from middle


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        for i in range(n):
            # odd
            l, r = i, i
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1

                l -= 1
                r += 1

            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                count += 1

                l -= 1
                r += 1

        return count


# Time O(n^2)
# Space O(n^2)
# start from left len 1 to len n


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * (n) for _ in range(n)]

        # base case 1 single char

        cnt = 0

        for right in range(n):
            #! base cae len = 1
            dp[right][right] = True
            cnt += 1
            for left in range(right):
                if right - left <= 2:
                    dp[left][right] = s[left] == s[right]
                else:
                    dp[left][right] = (s[left] == s[right] and dp[left+1][right - 1])

                if dp[left][right]:
                    cnt += 1

        return cnt


so = Solution()

s = "aaa"
# s = "babad"


res = so.countSubstrings(s)

print(res)
