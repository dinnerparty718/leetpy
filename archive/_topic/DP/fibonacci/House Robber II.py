#  All houses at this place are arranged in a circle.

from typing import List


# keep run house robber 1 twice

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(houses: List[int]):
            rob1, rob2 = 0, 0

            for h in houses:
                rob1, rob2 = rob2, max(rob1 + h, rob2)

            return rob2

        #! pattern
        option1 = helper(nums[1:])
        option2 = helper(nums[:-1])

        return max(nums[0], option1, option2)


nums = [2, 3, 2]
nums = [1, 2, 3, 1]
nums = [1, 2, 3]
so = Solution()

res = so.rob(nums)

print(res)
