from typing import List


# iterative
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for num in nums:
            size = len(res)
            for i in range(size):
                res.append(res[i] + [num])

        return res


# top down, backtrack
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(index: int, res: List[List[int]], nums: List[int], cur: List[int]):
            if index >= len(nums):
                res.append(cur[:])
                return

            cur.append(nums[index])
            dfs(index+1, res, nums, cur)
            cur.pop()
            dfs(index+1, res, nums, cur)

        dfs(0, res, nums, [])

        return res


so = Solution2()
nums = [1, 2, 3]
res = so.subsets(nums)

print(res)
