
# i != j != k

from typing import List

# sort
# i,j   and  two pointer to find k make sure index are not the same


class Solution:

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i+1, len(nums)-1

        while lo < hi:
            total_sum = nums[i] + nums[lo] + nums[hi]

            if total_sum > 0:
                hi -= 1
            elif total_sum < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []

        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)

        return res


so = Solution()
nums = [-1, 0, 1, 2, -1, -4]
res = so.threeSum(nums)

print(res)
