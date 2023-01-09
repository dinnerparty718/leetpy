from typing import List

# todo

# https://www.youtube.com/watch?v=86GHTcY0K4I&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=2

# own


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        p1 = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[p1] = nums[i]
                p1 += 1

        return p1


# better i is the first available slot
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1

        return i

# pointer start from 0, handle all situcation
# i is available spot, anything < i is proccessed


class Solution3:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0

        while j < len(nums):
            if i == 0 or nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1

        return i


so = Solution3()

nums = [0]

res = so.removeDuplicates(nums)

print(res)

print(nums)
