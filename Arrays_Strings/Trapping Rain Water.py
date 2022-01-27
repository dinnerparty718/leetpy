from typing import List
from unittest import result

# https://leetcode.com/problems/trapping-rain-water/solution/

# find peak
# min(two bar height) * incrase index 0 drop index - values between


# brute force exceed time limit
# time O(n^2)
# space O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        res = 0

        for i in range(1,  n-1):
            # find left max
            # find right max

            l_max = 0
            r_max = 0

            for j in range(i):
                l_max = max(l_max, height[j])
            for k in range(i+1, n):
                r_max = max(r_max, height[k])

            if height[i] < l_max and height[i] < r_max:
                res += min(l_max, r_max) - height[i]

        return res

# approach 2

# avoid finding left_max and right_max over and oever gain
# time O(n)
# space o(n)


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        res = 0

        left_max = [0] * n
        right_max = [0] * n

        l_max = 0
        r_max = 0

        for i in range(n):
            if height[i] > l_max:
                l_max = height[i]
            left_max[i] = l_max

        for i in reversed(range(n)):
            if height[i] > r_max:
                r_max = height[i]
            right_max[i] = r_max

        for i in range(1,  n-1):
            l_max = 0
            r_max = 0
            if height[i] < left_max[i] and height[i] < right_max[i]:
                res += min(left_max[i], right_max[i]) - height[i]

        return res


so = Solution()

#height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]

height = [5, 4, 1, 2]
res = so.trap(height)
print()
print(res)
# class Solution:
#     def trap(self, height: List[int]) -> int:

#         n = len(height)

#         # at least 3 element to trap water
#         if n <= 2:
#             return 0

#         peak = [0] * n

#         for i in range(n):
#             if i == 0 and height[i] > height[i+1]:
#                 peak[i] = 1
#             elif i == n - 1 and height[i] > height[i - 1]:
#                 peak[i] = 1

#             else:
#                 if height[i-1] < height[i] and height[i] > height[i+1]:
#                     peak[i] = 1

#         return 0
