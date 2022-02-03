# distinct

from typing import List


# yass!!

# O(n^3)  two for loop + two pointer
# space

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)

        if n < 4:
            return []

        res = []
        nums.sort()
        #! yield improve performance

        def twoSum(index: int, target: int):
            lo = index+1
            hi = n-1

            while lo < hi:

                two_sum = nums[lo] + nums[hi]

                if two_sum < target:
                    lo += 1
                elif two_sum > target:
                    hi -= 1
                else:
                    yield nums[lo], nums[hi]

                    lo += 1
                    hi -= 1
                    #! pattern
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
            # return result

        for i in range(n):
            #! avoid duplicate
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, n):
                    #! avoid duplicate
                    if j == i + 1 or nums[j] != nums[j-1]:
                        two_sum_target = target - nums[i] - nums[j]
                        pairs = twoSum(j, two_sum_target)

                        for a, b in pairs:
                            res.append([nums[i], nums[j], a, b])

        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0

# nums = [2, 2, 2, 2, 2]
# target = 8

so = Solution()

res = so.fourSum(nums, target)


print(res)
