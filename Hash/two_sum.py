from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for idx, num in enumerate(nums):
            com = target - num

            if com in h:
                return [idx, h[com]]
            else:
                h[num] = idx

        return []


nums = [2, 7, 11, 15]
target = 9

so = Solution()

print(so.twoSum(nums, target))
