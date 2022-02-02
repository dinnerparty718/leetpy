from typing import List


# brute force
# every pair and compare to the max

# Time O(n^2)
# space O(1)


# two pointer

# Time O(n)
# Space O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        max_area = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


so = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [1, 1]
res = so.maxArea(height)


print(res)
