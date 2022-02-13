
# binary search
# not exactly equal

class Solution:
    def mySqrt(self, x: int) -> int:

        if x <= 1:
            return x

        lo = 1
        hi = x

        # stop while lo == hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            s = mid ** 2

            if s == x:
                return mid
            elif s < x:
                lo = mid + 1
            else:
                hi = mid - 1

        print(lo, hi)

        return hi


so = Solution()

x = 4
x = 8
# x = 1

res = so.mySqrt(x)

print(res)
