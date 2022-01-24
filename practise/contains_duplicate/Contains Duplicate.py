from typing import List
from collections import Counter

# sort  O(nlogn)
# https://leetcode.com/problems/contains-duplicate/discuss/60852/Three-Python-Solution-for-Contain-Duplicates


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        if all([value == 1 for value in counter.values()]):
            return False
        else:
            return True


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
