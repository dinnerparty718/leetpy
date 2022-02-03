from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(k: int, numbers: List[int], target: int) -> List[List[int]]:

            res = []

            if not nums:
                return res

            #
            average_value = target // k

            if average_value < numbers[0] or numbers[-1] < average_value:
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
                    hi += 1

                    while lo < hi and nums[lo] != nums[lo-1]:
                        lo += 1
            return res

        nums.sort()
        return kSum(4, nums, target)


so = Solution()


nums = [1, 0, -1, 0, -2, 2]
target = 0

res = so.fourSum()
