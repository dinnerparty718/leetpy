from typing import List
import statistics

nums = [1]
nums = [1, 2]


def find_median(nums: List[int]):

    return statistics.median(nums)


res = find_median(nums)

print(res)
