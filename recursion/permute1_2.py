from typing import List

# top down. when reach leaf. append result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(res: List[List[int]], index: int, nums: List[int]):
            if index >= len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(res, index + 1, nums)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(res, 0, nums)

        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(res: List[List[int]], index: int, nums: List[int]):
            if index >= len(nums):
                res.append(nums[:])
                return

            seen = set()

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                if nums[index] not in seen:
                    dfs(res, index + 1, nums)
                    seen.add(nums[index])
                nums[i], nums[index] = nums[index], nums[i]

        dfs(res, 0, nums)

        return res


so = Solution()


nums = [1, 2, 2]
res = so.permute_dup(nums)


print(res)
