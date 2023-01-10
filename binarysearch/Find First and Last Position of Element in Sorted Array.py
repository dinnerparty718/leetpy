'''
Find First and Last Position of Element in Sorted Array

- find left boundary
- right right boundary

'''


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) >> 1)

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        res[0] = left if nums[left] == target else -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) >> 1) + 1

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = right if nums[right] == target else -1

        return res


nums = [5, 7, 7, 8, 8, 10]
target = 8

so = Solution()
res = so.searchRange(nums, target)

print(res)
