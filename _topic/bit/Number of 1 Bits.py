'''
check each bit   => 32 times
mask 0001
    1011
    0001
    
mask 0010
     1011
     
mask 0100
     1011

mask 1000
     1011
     
cnt = 4


'''


class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                cnt += 1

            mask <<= 1

        return cnt
