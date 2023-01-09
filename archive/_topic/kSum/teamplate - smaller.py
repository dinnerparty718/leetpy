from typing import List

#

# time O(n^2) for loop and two pointer


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)

        res = 0

        def twoSumSmaller(i: int, target: int):
            cnt = 0
            lo = i+1
            hi = n-1

            while lo < hi:

                two_sum = nums[lo] + nums[hi]

                if two_sum < target:
                    cnt += (hi - lo)
                    lo += 1
                else:
                    hi -= 1
            return cnt

        for i in range(n):
            two_sum_target = target - nums[i]
            res += twoSumSmaller(i, two_sum_target)

        return res


so = Solution()
nums = [-2, 0, 1, 3]
target = 2
res = so.threeSumSmaller(nums, target)

print(res)
