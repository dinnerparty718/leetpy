
# time O(n) with memo
# time O(2^n) without memo
class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if n in self.cache:
            return self.cache[n]

        res = self.fib(n-1) + self.fib(n-2)

        self.cache[n] = res

        return res


so = Solution()


n = 4

res = so.fib(n)


print(res)

print(so.cache)
