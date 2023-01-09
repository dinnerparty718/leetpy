from typing import List


# https://leetcode.com/problems/jump-game/solution/

# dynamic programming

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i = 0
        n = len(nums)

        visited = set()

        while i < n and i not in visited:
            visited.add(i)
            if nums[i] + i >= n - 1:
                return True
            else:
                i = nums[i]

        return False


so = Solution()

nums = [2, 3, 1, 1, 4]

res = so.canJump(nums)


print(res)
