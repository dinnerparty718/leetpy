from typing import List

# dfs stack or recursive

# https://leetcode.com/problems/target-sum/discuss/1269547/Python-Memoized-Solution-(Most-simple-'Memoized'-template-to-solve-such-questions)


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        count = 0

        def helper(nums, i, sum, target):
            # reference count to ther outer scope
            # but not global scope either
            nonlocal count

            # base case
            if i == len(nums):
                if sum == target:
                    count += 1
            else:
                helper(nums, i + 1, sum + nums[i], target)
                helper(nums, i + 1, sum - nums[i], target)

        helper(nums, 0, 0, target)

        return count


so = Solution()

nums = [1, 1, 1, 1, 1]
target = 3

# nums = [0, 38, 42, 31, 13, 10, 11, 12, 44,
#         16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39]
# target = 2

res = so.findTargetSumWays(nums, target)
print(res)
