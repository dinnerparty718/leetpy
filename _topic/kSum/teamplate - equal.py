
from typing import List

# hashmap, without sort
# 1. Two Sum
# Time O(n)
# space O(n)


#! twoSum return index

#! hash map
def twoSum(nums: List[int], target: int) -> List[int]:
    h = {}

    for idx, num in enumerate(nums):
        complement = target - num

        if complement in h:
            return [h[complement], idx]
        else:
            h[num] = idx

    return []


# nums = [2, 7, 11, 15]
# target = 9
# res = twoSum(nums, target)
# print(res)


# sort()
#! two pointer

def twoSum(nums: List[int], target: int) -> List[int]:
    nums.sort()

    lo, hi = 0, len(nums)-1

    while lo < hi:
        two_sum = nums[lo] + nums[hi]

        if two_sum > target:
            hi -= 1
        elif two_sum < target:
            lo += 1
        else:
            return [lo, hi]


# nums = [2, 7, 11, 15]
# target = 9
# res = twoSum(nums, target)
# print(res)


#! twoSum return [value pairs] without duplicates

def twoSum2(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()

    lo, hi = 0, len(nums) - 1

    res = []

    while lo < hi:
        two_sum = nums[lo] + nums[hi]

        if two_sum < target:
            lo += 1
        elif two_sum > target:
            hi -= 1
        else:
            res.append([nums[lo], nums[hi]])

            lo += 1
            hi -= 1

            # ! skip same values
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1
    return res


# nums = [1, 2, 2, 3, 4, 4, 5]
# res = twoSum2(nums, 6)
# print(res)


#! return values pairs without duplicates

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    res = []

    def twoSum(i: int, nums: List[int], res: List[List[int]]):
        lo, hi = i+1, len(nums)-1

        while lo < hi:
            three_sum = nums[i] + nums[lo] + nums[hi]

            if three_sum > 0:
                hi -= 1
            elif three_sum < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            twoSum(i, nums, res)

    return res


nums = [-1, 0, 1, 2, -1, -4]

res = threeSum(nums)

print(res)
