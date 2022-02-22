'''

find last peak index idx
if idx == 0 nums sorted in descending order, reverse number using two pointer
else:
    for nums[idx-1], find the next min number grater than nums[idx-1]
    reverse from idx til end using two pointer

#todo

'''

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


nums = [1, 2, 3]
nums = [1, 2, 3, 2, 1]


so = Solution()
res = so.nextPermutation(nums)
