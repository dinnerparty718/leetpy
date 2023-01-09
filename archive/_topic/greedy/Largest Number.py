from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1  # ! put in front
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        # [0，0，0]

        return str(int(''.join(nums)))
