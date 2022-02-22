from typing import List


'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.







'''
# todo bottom up

# top down
# Time O(T * N ) T -> target value N len(nums)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(target):
            if target < 0:
                return 0
            if target == 0:
                return 1

            if target in memo:
                return memo[target]

            res = 0

            for num in nums:
                res += dfs(target - num)

            memo[target] = res
            return res

        return dfs(target)


so = Solution()


nums = [1, 2, 3]
target = 4

res = so.combinationSum4(nums, target)

print(res)
