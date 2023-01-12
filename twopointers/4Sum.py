'''
two loops + two pointers

O(n^)


'''

from typing import (
    List,
)


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """

    def four_sum(self, numbers: List[int], target: int) -> List[List[int]]:
        # write your code here
        numbers.sort()
        n = len(numbers)

        res = []

        def twoSum(i, j):
            left, right = j + 1, len(numbers) - 1

            while left < right:
                fourSum = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                if fourSum < target:
                    left += 1
                elif fourSum > target:
                    right -= 1
                else:
                    res.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1

        for i in range(n):
            if i == 0 or numbers[i] != numbers[i-1]:
                for j in range(i+1, n):
                    #! first j is does not start from 0
                    if j == i + 1 or numbers[j] != numbers[j - 1]:
                        twoSum(i, j)

        return res


so = Solution()
numbers = [1, 0, -1, 0, -2, 2]
target = 0

numbers = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1, 2]
target = 2

res = so.four_sum(numbers, target)
print(res)
