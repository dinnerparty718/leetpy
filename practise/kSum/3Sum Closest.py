# not exact value can't use hash
from typing import List
import bisect


# O(1) sorting selection sort

# two pointer

# time O(n**2)   O(nlogn + n**2) -> O(n**2)

# space two pointer O(logn) to O(n) depend on sorting


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        diff = float('inf')

        n = len(nums)

        if n < 3:
            return -1

        nums.sort()

        for i in range(n):
            lo, hi = i+1, n - 1

            while lo < hi:
                Sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - Sum) < abs(diff):
                    diff = target - Sum

                if Sum < target:
                    lo += 1
                else:
                    hi -= 1

                if diff == 0:
                    break
        return target - diff


# binary search

# O(n**2 logn) binary search O(logn)
# space two pointer O(logn) to O(n) depend on sorting


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums = nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                complement = target - nums[i] - nums[j]

                # built-in function
                hi = bisect.bisect_right(nums, complement, j+1)
                lo = hi - 1

                if hi < len(nums) and abs(complement - nums[hi] < abs(diff)):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break

        return target - diff


so = Solution()

nums = [-1, 2, 1, -4]
target = 1

res = so.threeSumClosest(nums, target)


print(res)
