from typing import List


# time O(n2)
# backtracking
# top down level(0)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        # taken first, then remove
        def dfs(index: int, nums: List[int], subset: List[int]):
            if index >= len(nums):
                # !important added a copy of subset
                self.res.append(subset[:])
                return
            subset.append(nums[index])
            dfs(index + 1, nums, subset)
            subset.pop()
            dfs(index + 1, nums, subset)

        dfs(0, nums, [])

        return self.res


# todo
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res


so = Solution2()

nums = [1, 3, 5]

res = so.subsets(nums)

print(res)
