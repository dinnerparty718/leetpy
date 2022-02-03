from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        nums.sort()

        lo, hi = 0, len(nums)-1

        while lo < hi:
            two_sum = nums[lo] + nums[hi]

            if two_sum < target:
                lo += 1
            elif two_sum > target:
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1

                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

        return res


nums = [1, 1, 2, 2]
target = 3

so = Solution()
res = so.twoSum(nums, target)
print(res)
