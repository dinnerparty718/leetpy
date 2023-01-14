'''
384 · Longest Substring Without Repeating Characters
two pointers



'''


class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def length_of_longest_substring(self, s: str) -> int:
        # write your code here
        h = {}  # store    char:last_index
        left, right = 0, 0
        res = 0

        while right < len(s):
            char = s[right]
            if char not in h or h[char] < left:
                res = max(res, right - left + 1)
            else:
                left = h[char] + 1
            h[char] = right
            right += 1

        return res


so = Solution()

s = "abcabcbb"
s = "bbbbb"
s = 'aab'
s = 'an++--viaj'
res = so.length_of_longest_substring(s)
print(res)
