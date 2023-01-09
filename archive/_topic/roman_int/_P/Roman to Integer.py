

# one pass left to rigth pass.  is less significant number placed before next value. value is negative
# build map


# Time O(1)
# As there is a finite set of roman numerals, the maximum number possible number can be 3999, which in roman numerals is MMMCMXCIX. As such the time complexity is O(1)O(1).
# space O(1)


'''

build hash map with larger number first

One pass left ->right
if m[char] < m[char +1] 
    result is minus

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and m[s[i]] < m[s[i+1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]

        return res


so = Solution()

s = "III"
s = "LVIII"
# s = "MCMXCIV"
res = so.romanToInt(s)


print(res)
