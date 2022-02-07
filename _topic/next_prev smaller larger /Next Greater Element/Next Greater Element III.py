

# same as next permutation
# find last peak


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        MAX = 2**31 - 1

        digits = []

        #! skill
        while n > 0:
            n, remainder = divmod(n, 10)
            digits.append(remainder)

        digits.reverse()

        next_greater_el = [-1] * len(digits)

        stack = []

        for idx, num in enumerate(digits):
            while stack and digits[stack[-1]] < num:
                i = stack.pop()
                next_greater_el[i] = idx
            stack.append(idx)

        if all(val == -1 for val in next_greater_el):
            return -1

        print(next_greater_el)

        # next permutation
        # find last peak, swap previous and last number greater than previous

        peak_idx = 0

        for i in range(1, len(digits)):
            if next_greater_el[i] == -1 and next_greater_el[i-1] != -1:
                peak_idx = i

        target = digits[peak_idx-1]

        max_val = float('inf')

        j = None

        for i in range(peak_idx, len(digits)):

            if digits[i] > target and digits[i] < max_val:
                max_val = digits[i]
                j = i

        digits[peak_idx - 1], digits[j] = digits[j], digits[peak_idx - 1]

        last = digits[peak_idx:]
        #! 12222333
        last.sort()  # instead of reverse
        digits = digits[:peak_idx] + last

        res = 0

        for d in digits:
            if res > MAX // 10 or res == MAX // 10 and d > MAX % 10:
                return -1
            res = res * 10 + d

        return res


so = Solution()


n = 321
n = 123
n = 1232  # 1322
n = 1324  # 1342
n = 12
n = 21

n = 230241  # 230412
n = 2147483486


n = 2147483476    # 2147483647  674 -> 647
n = 12222333


res = so.nextGreaterElement(n)


print(res)
