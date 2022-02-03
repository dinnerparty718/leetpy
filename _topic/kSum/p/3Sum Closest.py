from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')  # store the difference

        n = len(nums)

        if n < 3:
            return -1

        for i in range(n):
            lo, hi = i+1, n-1

            while lo < hi:
                Sum = nums[i] + nums[lo] + nums[hi]

                if abs(target - Sum) < abs(diff):
                    diff = target - Sum

                if Sum < target:
                    lo += 1
                elif Sum > target:
                    hi -= 1
                else:

                    break
        return target - diff


so = Solution()

nums = [-1, 2, 1, -4]
target = 1

res = so.threeSumClosest(nums, target)
print(res)
