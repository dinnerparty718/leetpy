'''
56 · Two Sum

1. two pointers

sort can store original index


time O(nlog(n))
space O(n)


2. Hashmap




'''

from typing import (
    List,
)


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]

        # transform numbers to a sorted array with index
        nums = [(number, index) for index, number in enumerate(numbers)]

        # write your code here
        nums = sorted(nums)

        left, right = 0, len(numbers) - 1

        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return sorted([nums[left][1], nums[right][1]])
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def two_sum(self, numbers: List[int], target: int) -> List[int]:

        if not numbers:
            return [-1, -1]
        h = {}

        for idx, num in enumerate(numbers):
            if target - num in h:
                return [h[target - num], idx]
            h[num] = idx

        return [-1, -1]


numbers = [2, 7, 11, 15]
target = 9

so = Solution()

res = so.two_sum(numbers, target)

print(res)
