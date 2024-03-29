'''
200 · Longest Palindromic Substring

two pointers middle out
# time O(n^2)
# space O(1) expand from middle

'''


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longest_palindrome(self, s: str) -> str:
        # write your code here
        if not s:
            return ''

        n = len(s)

        res = ''
        maxLen = 0

        def find_palindrome_from(left, right):
            nonlocal res
            nonlocal maxLen
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

        for i in range(n):
            # odd
            left, right = i, i
            find_palindrome_from(left, right)

            # even
            left, right = i, i + 1
            find_palindrome_from(left, right)

        return res


so = Solution()

s = 'abcdzdcab'
res = so.longest_palindrome(s)
print(res)
