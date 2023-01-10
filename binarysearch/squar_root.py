'''
left two values and compare

'''


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x: int) -> int:
        # write your code here

        l, r = 0, x

        while l + 1 < r:
            mid = (l + r) // 2
            if mid < x // mid:  # ! mid * mid might out of bound
                l = mid
            else:
                r = mid

        # end condition l + 1 == r
        if r * r <= x:
            return r
        else:
            return l


so = Solution()

res = so.sqrt(65536)

print(res)
