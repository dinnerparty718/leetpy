

from typing import List


# Given an array nums of integers and integer k
# return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.


def twoSumLessThanK(nums: List[int], k: int) -> int:

    nums.sort()
    lo, hi = 0, len(nums)-1

    res = -1

    while lo < hi:
        two_sum = nums[lo] + nums[hi]

        if two_sum >= k:
            hi -= 1
        else:
            res = max(res, two_sum)
            lo += 1

    return res


nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60


res = twoSumLessThanK(nums, k)
print(res)
