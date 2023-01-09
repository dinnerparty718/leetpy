from typing import List


'''
You must write an algorithm that runs in O(log n) time.
binary search on rolated array
nums[mid] > nums[r]
    l = mid +1
else:
    r = mid

'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                #! do not exclude possible val
                l = mid + 1
            else:
                r = mid

        return nums[l]


so = Solution()

nums = [3, 4, 5, 1, 2]
nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [11, 13, 15, 17]
# nums = [3, 1, 2]
# nums = [2, 1]
res = so.findMin(nums)

print(res)
