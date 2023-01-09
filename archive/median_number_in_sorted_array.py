from typing import List
import statistics

nums = [1]
nums = [1, 2]


def find_median(nums: List[int]):
    return statistics.median(nums)


def find_median2(nums: List[int]):
    n = len(nums)
    l, r = 0, n-1

    #! when even number, mid is shifting to the left
    mid = (l + r) // 2

    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid] + nums[mid+1])/2


res = find_median2(nums)

print(res)
