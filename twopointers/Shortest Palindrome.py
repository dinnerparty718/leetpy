'''
678 · Shortest Palindrome

O(n^2)
from right to left to see if substr is palindrome

eg.

banana 
    - reversed(banana) + banana
    = ananb banana


reverse s[i + 1 :] plus str
s[i + 1 ][::-1] + str[:]

fing longest prefix



KMP algo O(n) #! todo
1. revesed(str) + str
2. build kmp table
3. remove longtest prefix str

Longest Prefix Suffix

check neetcode
https://www.youtube.com/watch?v=JoF0Z7nVSrA

'''


class Solution:
    """
    @param str: String
    @return: String
    """

    def shortest_palindrome(self, str: str) -> str:
        # Write your code here
        if not str:
            return ''

        n = len(str)
        for i in range(n-1, -1, -1):
            substr = str[:i + 1]
            if self.is_palindrome(substr):
                if i == n - 1:
                    return str
                else:
                    return str[i + 1:][::-1] + str[:]

    def is_palindrome(self, str: str) -> bool:
        left, right = 0, len(str)-1

        while left < right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1
        return True


so = Solution()

str = 'aacecaaa'

res = so.shortest_palindrome()
print(res)
