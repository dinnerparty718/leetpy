import bisect
from typing import List


# exceed time limit

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/solution/
# todo

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n < 2:
            return [0]

        count = [0] * n

        sorted_nums = sorted(nums)

        for i in range(n):
            sorted_nums.remove(nums[i])
            idx = bisect.bisect_left(sorted_nums, nums[i])

            count[i] = idx

        return count


so = Solution()
nums = [5, 2, 6, 1]
nums = [-1]
nums = [-1, -1]
res = so.countSmaller(nums)

print(res)
