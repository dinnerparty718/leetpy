
from typing import List

# time O(n^2) Comparision and swaps
# worse case array in descending order


def insertion_sort(nums: List[int]):

    for i in range(1, len(nums)):

        if nums[i] >= nums[i-1]:
            continue

        j = i

        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1


# nums = [2, 8, 5, 3, 9, 4]
nums = [2, 5, 8, 3, 9, 4]

insertion_sort(nums)


print(nums)
