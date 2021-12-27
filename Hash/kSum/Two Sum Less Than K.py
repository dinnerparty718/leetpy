from typing import List


# return the max sum

# Time O(nlogn)  sort

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums)-1

        res = -1

        while l < r:
            cur_sum = nums[l] + nums[r]

            if cur_sum < k:
                res = max(res, cur_sum)
                l += 1
            else:
                r -= 1

        return res


nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60


so = Solution()

res = so.twoSumLessThanK(nums, k)

print(res)
