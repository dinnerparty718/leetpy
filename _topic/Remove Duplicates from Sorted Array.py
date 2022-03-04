from typing import List
'''
need to be done in place
array is sorted
two pointer slow and fast


fast start from 1


'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# nums = [1]

so = Solution()
res = so.removeDuplicates(nums)


print(res)
