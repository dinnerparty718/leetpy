from typing import List

# { 0,1,8 }
# { 6,9 }

# recursive
# base case have two
# recursion relation n and n-2
# top - down


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        def helper(n, og_n):

            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']

            l = []

            middle = helper(n-2, n)

            for m in middle:
                # l.append('0' + m + '0')
                if n != og_n:
                    l.append('0' + m + '0')

                l.append('1' + m + '1')
                l.append('8' + m + '8')
                l.append('6' + m + '9')
                l.append('9' + m + '6')

            return l

        return helper(n, n)


# todo
class Solution2:
    def findStrobogrammatic(self, n: int) -> List[str]:
        l0 = ['']
        l1 = ['0', '1', '8']

        if n == 1:
            return l1

        # for

        return res


so = Solution()

n = 4
res = so.findStrobogrammatic(n)


print(res)


# a = filter(lambda val: val[0] != '0', res)


# print(list(a))
