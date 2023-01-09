from typing import List


def quick_sort(nums: List[int]):

    def partition(l: int, r: int):
        i = l
        pivot = nums[r]

        for j in range(l, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[r] = nums[r], nums[i]

        return i

    def helper(l, r):

        if l < r:
            p = partition(l, r)
            partition(l, p-1)
            partition(p+1, r)

    helper(0, len(nums)-1)


nums = [2, 5, 8, 3, 9, 4]


quick_sort(nums)

print(nums)
