import bisect


# own

# use bisect_right O(logn)
# could be optimzied not use biset since we can store value largest -> smallest

# todo

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        value_h = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        res = []

        while num > 0:
            idx = bisect.bisect_right(values, num) - 1

            res.append(value_h[values[idx]])
            num -= values[idx]

        return ''.join(res)


# time O(n)
# space O(1)
class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        res = []

        for value, symbol in values:
            if num == 0:
                break

            count, num = divmod(num, value)
            res.append(symbol * count)

        return ''.join(res)


so = Solution()


res = so.intToRoman(3)


print(res)
