from typing import List


# top down with memo, slow
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)

        def dfs(i: int, isEven: bool):
            if i == n:
                return 0

            if (i, isEven) in memo:
                return memo[(i, isEven)]

            val = nums[i] if isEven else -nums[i]

            memo[(i, isEven)] = max(val + dfs(i+1, not isEven), dfs(i+1, isEven))

            return memo[(i, isEven)]

        res = dfs(0, True)

        # print(memo)

        return res


# neetcode
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        sumEven, sumOdd = 0, 0

        for i in range(n-1, -1, -1):
            #               taken               skip
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)

            sumEven, sumOdd = tmpEven, tmpOdd

        return sumEven


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        odd = even = 0

        for num in nums:
            odd, even = max(odd, even - num), max(even, odd + num)

        return even


so = Solution()


nums = [4, 2, 5, 3]

res = so.maxAlternatingSum(nums)

print(res)
