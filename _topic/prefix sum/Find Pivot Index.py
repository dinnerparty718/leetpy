from typing import List

# O(n)
# O(1)


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == (total_sum - leftsum - num):
                return i
            leftsum += num

        return -1


so = Solution()

nums = [1, 7, 3, 6, 5, 6]

res = so.pivotIndex(nums)

print(res)
