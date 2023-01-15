'''
363 · Trapping Rain Water

left [-1, -1, -1]
right [n, n , n]

O(n)
O(n)

'''


from typing import (
    List,
)


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trap_rain_water(self, heights: List[int]) -> int:
        if not heights:
            return 0

        left_max = []
        right_max = []

        cur_max = float('-inf')

        for height in heights:
            cur_max = max(cur_max, height)
            left_max.append(cur_max)

        cur_max = float('-inf')
        for height in reversed(heights):
            cur_max = max(cur_max, height)
            right_max.append(cur_max)
        right_max = right_max[::-1]  # reverse array

        res = 0
        for i in range(len(heights)):
            res += (min(left_max[i], right_max[i]) - heights[i])
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right_max = [0] * n
        left_max = [0] * n

        l_max = 0
        r_max = 0

        res = 0

        for i in range(n):
            l_max = max(l_max, height[i])
            left_max[i] = l_max

        for i in range(n-1, -1, -1):  # ! right to left
            r_max = max(r_max, height[i])
            right_max[i] = r_max

        for i in range(1, n-1):
            res += min(right_max[i], left_max[i]) - height[i]

        return res


so = Solution()
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = so.trap_rain_water(heights)

print(res)
