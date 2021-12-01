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
                # res += [res[i] + [n]]
        return res


# call cascading
# O(n * 2^n)

class Solution4:
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            # [1] + [2] = [1,2]
            res += [item + [num] for item in res]
        return res

# []
# [][1]
# [][1][2][1,2]
# [][1][2][1,2][3][1,3][2,3][1,2,3]    2^n = 2^3 = 8

# tree by substring length 0,1,2,3   for l in range(n+1) #! important to include n


class Solution3(object):
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    # nums is the remaining subset

    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path+[nums[i]], res)


so = Solution3()

nums = [1, 2, 3]

res = so.subsets(nums)

print(res)
