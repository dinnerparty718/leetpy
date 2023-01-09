from typing import List


# own solution
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        nums = [num for num in range(1, n+1)]

        def dfs(start: int, nums: List[int], cur: List[int]):
            if len(cur) == k:
                res.append(cur[:])
                return

            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(i+1, nums, cur)
                cur.pop()

        dfs(0, nums, [])

        return res


# leetcode, assgin number base on input
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(start: int, cur: List[int]):
            if len(cur) == k:
                res.append(cur[:])
                return

            for i in range(start, n):
                cur.append(i+1)
                backtrack(i+1, cur)
                cur.pop()

        backtrack(0, [])

        return res


so = Solution2()

n = 4
k = 2

res = so.combine(n, k)


print(res)
