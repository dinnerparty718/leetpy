'''
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

'''


from typing import List
from functools import lru_cache

# time O(m*n)
# space O(m*n)

# exceed memeory
# dit not cache anything


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = sum(nums) // 2

        # n-1 to 0

        @lru_cache(maxsize=None)
        def partition(i: int, target: int):
            if i == 0:
                return target == 0

            if target < 0:
                return False

            #! use one line or for early return
            return partition(i-1, target - nums[i]) or partition(i-1, target)

        res = partition(n-1, target)
        # print(memo)

        return res


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        memo = {}

        total = sum(nums)

        if total % 2 == 1:
            return False

        target = sum(nums) // 2

        def partition(i: int, curr_sum: int):
            if i == n:
                return curr_sum == target

            if curr_sum > target:
                return False

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            option1 = partition(i+1, curr_sum + nums[i])
            option2 = partition(i+1, curr_sum)

            memo[(i, curr_sum)] = option1 or option2

            return memo[(i, curr_sum)]

        res = partition(0, 0)

        return res


# neetcode

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])

            dp = dp.union(nextDP)

        return target in dp


# 2D DP not from leetcode
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2 == 1:
            return False

        target = total // 2

        # dp

        dp = [[None] * (target + 1) for _ in range(n)]

        #! populate 1st col, target 0 True

        for i in range(n):
            dp[i][0] = True

        #! populate 1st row

        for t in range(1, target + 1):
            dp[0][t] = nums[0] == t

        for i in range(1, n):
            for j in range(1, target+1):
                curr = nums[i]

                if j < curr:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - curr]

        return dp[-1][-1]


# nums = [1, 5, 11, 5]
# nums = [1, 2, 3, 5]
nums = [2, 2, 1, 1]
nums = [2, 2, 3, 5]

so = Solution()
res = so.canPartition(nums)

print(res)
