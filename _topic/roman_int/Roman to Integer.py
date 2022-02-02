
class Solution:

    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        for i in range(len(s)-1):

            cur = values[s[i]]
            nxt = values[s[i+1]]
            if cur < nxt:
                result -= cur
            else:
                result += cur

        # remember to add last value
        return result + values[s[-1]]


so = Solution()

res = so.romanToInt('MCMXCIV')


print(res)
