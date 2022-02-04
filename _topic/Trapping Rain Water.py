from typing import List


# two pass l -> r r->l

# cur value = min(l_max, r_max) - value

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max = [0] * n
        right_max = [0] * n

        l_max = 0

        r_max = 0

        res = 0

        for i in range(n):
            l_max = max(l_max, height[i])
            left_max[i] = l_max

        for i in reversed(range(n)):
            r_max = max(r_max, height[i])
            right_max[i] = r_max

        for i in range(1, n-1):
            res += min(left_max[i], right_max[i]) - height[i]

        return res


so = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

height = [4, 2, 0, 3, 2, 5]
res = so.trap(height)

print(res)
