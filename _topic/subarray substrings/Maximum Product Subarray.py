from typing import List

'''
simplified DP

min, max = 1,1

when encounter 0, reset back to 1


'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tmp = n * curMax

            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            res = max(res, curMax, curMin)

        return res
