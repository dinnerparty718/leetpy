'''
Fenwick Tree or Binary Index Tree

solve the problem of range queries

construction O(n)
point update O(log(n))
Range sum O(log(n))
range update O(log(n))

Least significant bit (LSB)


5
4
3
2  
1 00001

#! todo construct use n

'''


class BIT:
    def __init__(self, n) -> None:
        self.sums = [0] * (n+1)

    # nlog(n)

    def update(self, i, v):  # v is delta
        while i < len(self.sums):
            self.sums[i] += v
            i += (i & -i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= (i & -1)

        return res
