
# naive recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x

        def helper(x, n):
            if n == 0:
                return 1

            if n == 1:
                return x

            return x * helper(x, n-1)

        return helper(x, n)

# naive iterative


class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x

        res = 1

        for _i in range(n):

            res *= x

        return res


# better approach log?
# fast pow
# time O(logn)
# space O(logn)
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x

        if n == 0:
            return 1

        def fastPow(x, n):
            if n == 0:
                return 1

            half = fastPow(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        return fastPow(x, n)


class Solution3:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = abs(n)
            x = 1 / x

        if n == 0:
            return 1

        res = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                res = res * current_product
                print(n)
            current_product = current_product * current_product

            print(res, n, current_product)

            n = n // 2

        return res


so = Solution3()


x = 2.00000
n = 10

res = so.myPow(x, n)

print(res)
