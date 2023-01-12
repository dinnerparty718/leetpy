'''
57 · 3Sum

sort then two pointers
tricks to handle duplicate


# Time O(n^2) twoSum O(n) sort O(nlogn)
# space O(n) or O(logn) depends on the sorting implementation

# Sort + (two pointers)

'''


from typing import (
    List,
)


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """

    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        nums = sorted(numbers)

        result = []

        def two_sum(i, nums) -> List[List[int]]:
            left, right = i+1, len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                two_sum(i, nums)
        return result


so = Solution()
numbers = [-1, 0, 1, 2, -1, -4]
numbers = [-1, 1, 0]
numbers = [1, 0, -1, -1, -1, -1, 0, 1, 1, 1]

res = so.three_sum(numbers)
print(res)
