'''
539 · Move Zeroes

two pointers
1. swap

time: O(n)
space: O(1)

2. better without swap, overwrite and pad 0 at the end 

'''


from typing import (
    List,
)


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def move_zeroes(self, nums: List[int]):
        # write your code here
        l, r = 0, 0

        def swap(idx1: int, idx2: int, nums: List[int]):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        while r < len(nums):
            if nums[r] != 0:
                swap(l, r, nums)
                l += 1
            r += 1


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def move_zeroes(self, nums: List[int]):
        # 将两个指针先指向数组头部
        left, right = 0, 0

        while right < len(nums):
            # 遇到非0数赋值给新数组指针指向的位置
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                # 将left向后移动一位
                left += 1
            right += 1

        # 若新数组指针还未指向尾部,将剩余数组赋值为0
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1


nums = [0, 1, 0, 3, 12]
nums = [0, 0, 0, 3, 1]

so = Solution()
res = so.move_zeroes(nums)


print(nums)
