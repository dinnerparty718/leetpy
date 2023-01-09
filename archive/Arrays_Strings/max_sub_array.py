from typing import List

# maxisum subarray
# Kadane's algorithm
# https://www.youtube.com/watch?v=86CQq3pKSUw


'''
Kadane's algorithm or dp

curMax = globalMax = nums[0]

for i in range(1, len(nums)):
    cur = nums[i]
    curMax = max(curMax + curr)
    
    globalMax = max(globalMax, curMax)

return globalMax

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = maxSub = nums[0]

        for num in nums[1:]:
            # first step compare the current element and current sum

            curSum = max(num, curSum + num)
            maxSub = max(maxSub, curSum)

        return maxSub


so = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1]

res = so.maxSubArray(nums)

print(res)
