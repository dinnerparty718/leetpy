from typing import List


# one pass hashtable
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for idx, num in enumerate(nums):
            com = target - num

            #! guarantee com and num is different
            if com in h:
                return [idx, h[com]]
            else:
                h[num] = idx

# two pass


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in h and h[complement] != i:
                return [i, h[complement]]


so = Solution()


nums = [2, 7, 11, 15]
target = 9

res = so.twoSum(nums, target)

print(res)
