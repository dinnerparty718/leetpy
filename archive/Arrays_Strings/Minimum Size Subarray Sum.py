from typing import List


# two-pointer own
# Time O(N)
# Space O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_lengh = float('inf')
        start = 0

        cur_sum = 0

        for end in range(len(nums)):
            cur_sum += nums[end]
            if cur_sum < target:
                continue

            while cur_sum - nums[start] >= target:
                cur_sum -= nums[start]
                start += 1

            min_lengh = min(min_lengh, end-start+1)

        return min_lengh if min_lengh != float('inf') else 0


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left = 0

        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            if cur_sum < target:
                continue

            while cur_sum >= target:
                res = min(res, right-left+1)
                cur_sum -= nums[left]
                left += 1
        return res if res != float('inf') else 0


target = 11
nums = [1, 2, 3, 4, 5]

so = Solution2()

res = so.minSubArrayLen(target, nums)


print(res)
