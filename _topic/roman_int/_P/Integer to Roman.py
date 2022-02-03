
# Time O(1)
# space O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I'],
        ]

        res = []

        for val, char in values:

            if num == 0:
                break

            # if val > num:
            #     continue

            # if num > 0:
            quotient, remainder = divmod(num, val)
            num = remainder

            res.append(quotient * char)

        return ''.join(res)


so = Solution()

num = 3
num = 58
num = 1994

res = so.intToRoman(num)
print(res)
