'''
353 · Largest letter
A 65
a 97

Time O(n) build set
Space O(1) 26*2
'''


class Solution:
    """
    @param s: a string
    @return: a string
    """

    def largest_letter(self, s: str) -> str:
        # write your code here
        charSet = set(s)
        for i in range(25, -1, -1):
            if chr(ord('A') + i) in charSet and chr(ord('a') + i) in charSet:
                return chr(ord('A') + i)

        return 'NO'


so = Solution()

s = 'admeDCAB'
res = so.largest_letter(s)
print(res)
