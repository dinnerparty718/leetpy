import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)

        nums = sorted(list(set(nums)))

        e1, e2 = 0, 0

        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]

            if i > 0 and nums[i] == nums[i-1] + 1:
                # temp = e2
                # e2 = max(curEarn + e1, e2)
                # e1 = temp
                #! either take e1 + curr or take e2 only
                e1, e2 = e2, max(curEarn + e1, e2)

            else:
                # temp = e2
                # e2 = curEarn + e2
                # e1 = temp
                e1, e2 = e2, curEarn + e2

        return e2

        #  e1 e2
        # [1, 2, 3]


so = Solution()

nums = [3, 4, 2]
res = so.deleteAndEarn(nums)

print(res)
