from typing import List


# one pass binary search and comparte left and mid values

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid

            #! <=
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return -1


# find rotation point #!  find bottom, loweast point
# search left, search right
# two pass binary search

# Time O(logn)
# sapce O(1)

class Solution1:
    def search(self, nums: List[int], target: int) -> int:

        # def find_peak
        def find_rotate_index(left, right):
            #! no rotation here
            if nums[left] < nums[right]:
                return 0

            while left <= right:

                pivot = left + (right - left) // 2

                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def binary_search(left, right):

            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotated_index = find_rotate_index(0, n-1)

        if nums[rotated_index] == target:
            return rotated_index

        #! standard binary search
        if rotated_index == 0:
            return binary_search(0, n-1)

        if target < nums[0]:
            return binary_search(rotated_index, n-1)
        else:
            return binary_search(0, rotated_index)


so = Solution()

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3


# nums = [1]
# target = 0

res = so.search(nums, target)

print(res)
