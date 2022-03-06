'''
plus operation for a and b
    a XOR b
+   (a & b)<<1     -> carry, keep doing this until carry = 0






while b != 0

a, b = a^b, (a&b)<< 1




max_int = 2**31 -1

'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a < max_int else ~(a ^ mask)


so = Solution()
a = 1
b = 2
res = so.getSum(a, b)

print(res)
