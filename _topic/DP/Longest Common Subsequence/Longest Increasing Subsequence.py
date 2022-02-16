from typing import List


# brute force

# O(2^n)

# own yass with logic from neetcode

# O(n^2)
# two for loop


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        LIS = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


so = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]
# nums = [0, 1, 0, 3, 2, 3]

# nums = [7, 7, 7, 7, 7, 7, 7]

res = so.lengthOfLIS(nums)


print(res)
