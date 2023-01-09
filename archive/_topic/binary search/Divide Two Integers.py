'''
4 bytes int
# requirement
    return MAX -1
    return MIN

# edge cases



93706 / 157

157
314     2
628     2
1256    2
2512    2
5024    2
10048   2
20096   2
40192   2
80384   2
160768 # Too big


80384 = 157 * 2 ** 9

93706 - 80384 = 13322

157
314
628
1256
2512
5024
10048
20096 # Too big


10048 = 157 * 2 ** 6

13322 - 10048 = 3274


# time O(nlogn)
# space O(nlogn)

'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        # overflow
        if dividend == MIN and divisor == -1:
            return MAX

        # check if result should be negative
        negative = 2
        if dividend > 0:
            negative -= 1
            dividend = -dividend
        if divisor > 0:
            negative -= 1
            divisor = -divisor

        doubles = []
        powersOfTwo = []

        powerOfTwo = 1

        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)

            if divisor < MIN / 2:
                break

            divisor += divisor   # doubling here
            powerOfTwo += powerOfTwo

#        print(doubles)
#       [-157, -314, -628, -1256, -2512, -5024, -10048, -20096, -40192, -80384]

#        print(powersOfTwo)
#       [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        res = 0

        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                res += powersOfTwo[i]
                dividend -= doubles[i]

        return res if negative != 1 else -res


so = Solution()

dividend = 93706
divisor = 157
res = so.divide(dividend, divisor)


print(res)
