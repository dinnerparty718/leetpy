
from typing import List
'''


left_max, right_max
    for each i , find max on the left, find max on the right

for loop, 1- n-2   skip first and last index

    res += min(r_max[i], l_max[i]) - height[i]


'''


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

        for i in range(n-1, -1, -1):
            r_max = max(r_max, height[i])
            right_max[i] = r_max

        for i in range(1, n-1):
            res += min(right_max[i], left_max[i]) - height[i]

        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

height = [4, 2, 0, 3, 2, 5]

so = Solution()

res = so.trap(height)

print(res)
