import bisect
from typing import List


'''

bisect_right_implementation

[5, 7, 7, 8, 8, 10]

implement python bisect_left and bisect_right

#! insertion point
#! right boundary need to be len(nums) biset_right index could be out of bound

lo, hi = 0, len(nums)





'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = self.bisect_left(nums, target)
        end = self.bisect_right(nums, target) - 1

        if 0 <= start < len(nums) and start <= end and nums[start] == target:
            return [start, end]

        else:
            return [-1, -1]

    def bisect_left(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def bisect_right(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1  # ! insertion point

        return lo


nums = [5, 7, 7, 8, 8, 10]

nums = [0]


so = Solution()

target = 0
res = so.searchRange(nums, target)
