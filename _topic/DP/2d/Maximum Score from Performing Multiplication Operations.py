from typing import List
from functools import lru_cache

#! i + right-left + 1 = n
#! right = n - 1 + left - i
#! right = n - 1 - (i - left)

# top down
# time limit or memery limit


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n = len(nums)
        m = len(multipliers)

        # dp return max score after i interation
        # dp(0,0)
        @lru_cache(2000)
        def dp(i: int, left: int) -> int:
            if i == m:
                return 0

            mult = multipliers[i]

            right = n - 1 - (i - left)

            return max(dp(i+1, left+1) + mult * nums[left], dp(i+1, left) + mult * nums[right])

        return dp(0, 0)


# bottom up
# start from base case i == m

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for _ in range(m+1)]

        print(dp)


so = Solution()


nums = [1, 2, 3]
multipliers = [3, 2, 1]

# nums = [-5, -3, -3, -2, 7, 1]
# multipliers = [-10, -5, 3, 4, 6]

res = so.maximumScore(nums, multipliers)

print(res)


#! range(start, stop, step)

l = ['a', 'b', 'c', 'd', 'e']

for i in range(len(l)-1, -1, -1):
    print(l[i])
