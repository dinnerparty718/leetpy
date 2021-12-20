
# n row has 2^(n-1) elements
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1 and k == 1:
            return 0

        total_num = 2**(n-1)
        first_half = k <= total_num / 2

        if first_half:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k - total_num / 2)


so = Solution()

n = 3
k = 1

res = so.kthGrammar(2, 2)


print(res)
