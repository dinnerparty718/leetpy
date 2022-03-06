'''
check nth bit & 1


1011
   1


use OR for result

res = res | bit << (31 - i)



'''

#! neet code


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = n >> i & 1
            res = res | (bit << (31 - i))
        return res


'''
31 -> 0

mask = 1
keep shifting left bit by bit


'''

#! not efficent


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(31, -1, -1):
            if n & mask != 0:
                res += 2 ** i
            mask = mask << 1

        return res
