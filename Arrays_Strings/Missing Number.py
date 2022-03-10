from typing import List


# array has hashset
# own
# Time O(n)
# space O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            while nums[i] != i and nums[i] != None:

                if nums[i] == n:
                    nums[i] = None
                else:
                    # ! why position matter
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        # print(nums)

        for i in range(len(nums)):
            if nums[i] == None:
                return i

        return n


# leetcode 1 sort
# Time O(nlog(n))
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

# leetcode 2 Hashset
# Time O(n)
# space O(n)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        num_set = set(nums)

        for i in range(len(nums)+1):
            if i not in num_set:
                return i

# leetcode 4 Gauss' Formular
# calculate expetected sum
# expected_sum - actual_sum


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)

        n = len(nums)

        exptected_sum = n * (n+1) // 2

        return exptected_sum - actual_sum


so = Solution()

nums = [1, 2]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
res = so.missingNumber(nums)


print(res)
