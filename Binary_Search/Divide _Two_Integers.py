

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# hint, mean can use subtraction

# While you might be tempted to use multiplication and division for a few "simple" tasks, this is unnecessary. Here are some alternatives:
# Instead of a = a * -1 for making numbers negative, use a = -a.
# Instead of using a / 2 for dividing by 2, use the right shift operator; a >> 1.
# Instead of using a * 2 for doubling, use a = a + a, a += a, or even the left shift operator; a << 1.

# conver -2147483648 to positive will make input out of bound

#  Time Complexity : O(n)  if divisor = 1.
# excceed time limit
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # this will overflow in some language
        # result is 2**32
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0

        while dividend - divisor <= 0:
            quotient -= 1
            dividend -= divisor

        return -quotient if negatives != 1 else quotient


# better approach Repeated Exponential Searches
# Time O(logn*logn )

class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = MIN_INT/2

        # this will overflow in some language
        # result is 2**32
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0

        # 10  divident
        # 3 divisor
        # ->   -10  -3

        # if it's positive

        # while dividend >= divisor:
        #     powerOfTwo = 1
        #     value = divisor

        #     while value + value < dividend:
        #         value += value
        #         powerOfTwo + 1

        #     quotient += powerOfTwo
        #     dividend -= value

        while divisor >= dividend:
            powerOfTwo = -1
            value = divisor

            # prevent negative overflow
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value  # double every time  value*2
                powerOfTwo += powerOfTwo
                # print(powerOfTwo)
            quotient += powerOfTwo

            dividend -= value

        return -quotient if negatives != 1 else quotient

# memo, store the powerOf2 value
# time O(logN)
# space O(logN)


class Solution2:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = MIN_INT/2

        # this will overflow in some language
        # result is 2**32
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend

        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []  # negative value
        powersOfTwo = []  # positive

        powerOfTwo = 1

        # builid the list
        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor
            powerOfTwo += powerOfTwo

        quotient = 0

        # print(powersOfTwo)
        # print(doubles)

        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:  # reversed logic
                quotient += powersOfTwo[i]
                dividend -= doubles[i]
        return quotient if negatives != 1 else -quotient


so = Solution2()
dividend = 13322
divisor = 157
res = so.divide(dividend, divisor)
print(res)
