

from typing import List


# time O(n^2)
# space O(1)

def bubble_sort(nums: List[int]):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


nums = [2, 8, 5, 3, 9, 4]


bubble_sort(nums)

print(nums)
