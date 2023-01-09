from typing import List

# yass!
# O(n^k-1)


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(k: int, nums: List[int], target: int) -> List[List[int]]:

            res = []

            if not nums:
                return res

            #
            average_value = target // k

            if average_value < nums[0] or nums[-1] < average_value:
                return res

            if k == 2:

                val = twoSum(nums, target)
                return val
            else:

                for i in range(len(nums)):
                    if i == 0 or nums[i] != nums[i-1]:
                        for pair in kSum(k-1, nums[i+1:], target - nums[i]):
                            res.append([nums[i]] + pair)

            return res

        def twoSum(nums: List[int], target: int):
            lo, hi = 0, len(nums)-1

            res = []

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

                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1

            return res

        nums.sort()
        return kSum(4, nums, target)


so = Solution()


# nums = [1, 0, -1, 0, -2, 2]
# target = 0


nums = [-2, -1, -1, 1, 1, 2, 2]
target = 0

res = so.fourSum(nums, target)

print(res)
