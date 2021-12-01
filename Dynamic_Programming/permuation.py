from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(nums: List[int], index: int, res: List[List[int]]):

            # add a copy of current state to the result set

            if index >= len(nums):
                res.append(nums[:])
                return

            num_set = set()

            for i in range(index, len(nums)):
                nums[i],  nums[index] = nums[index], nums[i]
                if nums[index] not in num_set:
                    dfs(nums, index+1, res)
                    num_set.add(nums[index])
                nums[i],  nums[index] = nums[index], nums[i]

        dfs(nums, 0, res)

        return res


so = Solution()

nums = [1, 2, 2]
res = so.permute(nums)


for i in res:
    print(i)
