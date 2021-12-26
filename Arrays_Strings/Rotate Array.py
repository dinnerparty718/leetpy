from typing import List


# own exceed time limit
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)

        if k == 0:
            return

        start_idx = len(nums) - 1

        print(start_idx)

        print(k)

        while k > 1:
            start_idx -= 1
            k -= 1

        print(start_idx)

        reverse(start_idx, len(nums)-1)

        # outer loop
        for i in range(start_idx, len(nums)):
            # inner loop, move item to the left

            j = i

            while j > 0:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # revser whole array

        # reverse first k

        # reverse k+1

        k = k % len(nums)

        if k == 0:
            return

        reverse(0, len(nums)-1)

        reverse(0, k)

        reverse(k+1, len(nums)-1)


so = Solution1()


nums = [1, 2, 3, 4, 5, 6, 7]
nums = [-1, -100, 3, 99]
nums = [1, 2]
k = 3
k = 2

so.rotate(nums, k)


print(nums)
