from typing import List

'''
DP O(n^2)
dp[2] = False

Greedy, going backward
Time O(n)
space O(1)

'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
