import math
'''
ax^2 + bx + c = 0


(x + 1) * x  / 2 >= n

x^2 +x >= 2n
x^2 + x - 2n > 0


find x that:
x(x + 1) / 2 >= n

1. use formula

time O(1)
space O(1)



'''


class Solution:
    # 直接求解
    def dropEggs(self, n: int) -> int:
        return math.ceil((-1 + math.sqrt(8*n + 1)) / 2)


class Solution:
    # 累加
    def dropEggs(self, n):
        res = 1
        sum = 1
        while sum < n:
            res += 1
            sum += res
        return res


n = 100
so = Solution()

res = so.dropEggs(n)

print(res)
