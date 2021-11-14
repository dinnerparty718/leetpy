# will end up with cycle evently for EVERY Number
# either ends with 1 or not 1
# problem becomes detect cycle
# 1. hashset
# 2. fast slow pointer


# time O(log(n))
# space O(log(n))
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        # todo need to optimized

        def nextValue(num: int) -> int:
            num_ls = [int(n) for n in str(num)]
            return sum([n**2 for n in num_ls])

        def get_next(n: int) -> int:
            res = 0

            while n > 0:
                n, digit = divmod(n, 10)
                res += digit ** 2

            return res

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


class Solution2:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def get_next(n: int) -> int:
            res = 0

            while n > 0:
                n, digit = divmod(n, 10)
                res += digit ** 2

            return res

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


so = Solution()


n = 19
print(so.isHappy(n))
