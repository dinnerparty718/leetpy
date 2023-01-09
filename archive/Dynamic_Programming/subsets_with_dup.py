from typing import List

# backtracking


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)

        def dfs(index: int, nums: List[int], res: List[int], cur: List[int]):
            if index >= len(nums):
                if cur not in res:
                    res.append(cur[:])
                return
            cur.append(nums[index])

            dfs(index + 1, nums, res, cur)
            cur.pop()
            dfs(index + 1, nums, res, cur)

        dfs(0, nums, res, [])

        return res


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        nums = sorted(nums)

        for num in nums:
            res += [item + [num] for item in res if item + [num] not in res]

        return res


so = Solution2()


nums = [1, 2, 2]

res = so.subsetsWithDup(nums)

print(res)

# test = [[1, 2]]
# print([2, 1] in test)
