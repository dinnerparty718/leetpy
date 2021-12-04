from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_sum = defaultdict(int)
        sub_sum[0] = 1
        cnt = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in sub_sum:
                #! important

                cnt += sub_sum[current_sum - k]
                # cnt += 1
            sub_sum[current_sum] += 1

        return cnt


# [1,-1,0]
# 0

so = Solution()
nums = [1, 2, 3]
k = 3

res = so.subarraySum(nums, k)

print(res)
