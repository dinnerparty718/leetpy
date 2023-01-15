'''
55 · Compare Strings
#! consider counts
A = "ABCD"
B = "AABC"
False

Hash or [0] * 26

Time O(m + n)
space O(1)

'''


class Solution:
    """
    @param a: A string
    @param b: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compare_strings(self, a: str, b: str) -> bool:
        # write your code here
        chars = [0] * 26

        for char in a:
            chars[ord(char) - 65] += 1

        for char in b:
            chars[ord(char) - 65] -= 1
            if chars[ord(char) - 65] < 0:
                return False

        return True


so = Solution()

a = 'ABCD'
b = 'ACD'
res = so.compare_strings()
print(res)
